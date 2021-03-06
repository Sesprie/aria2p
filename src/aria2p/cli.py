"""
Module that contains the command line application.

Why does this file exist, and why not put this in __main__?

You might be tempted to import things from __main__ later,
but that will cause problems: the code will get executed twice:

- When you run `python -m aria2p` python will execute
  ``__main__.py`` as a script. That means there won't be any
  ``aria2p.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``aria2p.__main__`` in ``sys.modules``.

Also see http://click.pocoo.org/5/setuptools/#setuptools-integration.
"""

import argparse
import json
import sys

import requests

from aria2p import Download

from .api import API
from .client import DEFAULT_HOST, DEFAULT_PORT, Client, ClientException


# ============ MAIN FUNCTION ============ #
def main(args=None):
    """The main function, which is executed when you type ``aria2p`` or ``python -m aria2p``."""

    parser = get_parser()
    args = parser.parse_args(args=args)
    check_args(parser, args)
    kwargs = args.__dict__

    api = API(Client(host=kwargs.pop("host"), port=kwargs.pop("port"), secret=kwargs.pop("secret")))

    # Warn if no aria2 daemon process seems to be running
    try:
        api.client.get_version()
    except requests.ConnectionError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        print(file=sys.stderr)
        print("Please make sure that an instance of aria2c is running with RPC mode enabled,", file=sys.stderr)
        print("and that you have provided the right host, port and secret token.", file=sys.stderr)
        print("More information at https://aria2p.readthedocs.io/en/latest.", file=sys.stderr)
        return 2

    subcommands = {
        None: subcommand_show,
        "show": subcommand_show,
        "call": subcommand_call,
        "add-magnet": subcommand_add_magnet,
        "add-torrent": subcommand_add_torrent,
        "add-metalink": subcommand_add_metalink,
        "pause": subcommand_pause,
        "resume": subcommand_resume,
        "remove": subcommand_remove,
        "purge": subcommand_purge,
        "autopurge": subcommand_autopurge,
    }

    subcommand = kwargs.pop("subcommand")

    try:
        return subcommands.get(subcommand)(api, **kwargs)
    except ClientException as e:
        print(e.message, file=sys.stderr)
        return e.code


def check_args(parser, args):
    """Additional checks for command line arguments."""
    subparser = [action for action in parser._actions if isinstance(action, argparse._SubParsersAction)][0].choices

    if args.subcommand in ("pause", "remove", "resume", "purge"):
        if not args.do_all and not args.gids:
            subparser[args.subcommand].error("the following arguments are required: gids or --all")
        elif args.do_all and args.gids:
            subparser[args.subcommand].error("argument -a/--all: not allowed with arguments gids")


def get_parser():
    """Return a parser for the command-line options and arguments."""
    usage = "%(prog)s [GLOBAL_OPTS...] COMMAND [COMMAND_OPTS...]"
    description = "Command-line tool and Python library to interact with an `aria2c` daemon process through JSON-RPC."
    parser = argparse.ArgumentParser(add_help=False, usage=usage, description=description, prog="aria2p")

    main_help = "Show this help message and exit. Commands also accept the -h/--help option."
    subcommand_help = "Show this help message and exit."

    global_options = parser.add_argument_group(title="Global options")
    global_options.add_argument("-h", "--help", action="help", help=main_help)

    global_options.add_argument(
        "-p", "--port", dest="port", default=DEFAULT_PORT, type=int, help="Port to use to connect to the remote server."
    )
    global_options.add_argument(
        "-H", "--host", dest="host", default=DEFAULT_HOST, help="Host address for the remote server."
    )
    global_options.add_argument(
        "-s", "--secret", dest="secret", default="", help="Secret token to use to connect to the remote server."
    )

    # ========= SUBPARSERS ========= #
    subparsers = parser.add_subparsers(dest="subcommand", title="Commands", metavar="", prog="aria2p")

    def subparser(command, text, **kwargs):
        p = subparsers.add_parser(command, add_help=False, help=text, description=text, **kwargs)
        p.add_argument("-h", "--help", action="help", help=subcommand_help)
        return p

    add_magnet_parser = subparser("add-magnet", "Add a download with a Magnet URI.")
    add_metalink_parser = subparser("add-metalink", "Add a download with a Metalink file.")
    add_torrent_parser = subparser("add-torrent", "Add a download with a torrent file.")
    subparser("autopurge", "Automatically purge completed/removed/failed downloads.", aliases=["autoclear"])
    call_parser = subparser("call", "Call a remote method through the JSON-RPC client.")
    pause_parser = subparser("pause", "Pause downloads.")
    purge_parser = subparser("purge", "Purge downloads.", aliases=["clear"])
    remove_parser = subparser("remove", "Remove downloads.", aliases=["rm"])
    resume_parser = subparser("resume", "Resume downloads.")
    subparser("show", "Show the download progression.")

    # ========= CALL PARSER ========= #
    call_parser.add_argument(
        "method",
        help=(
            "The method to call (case insensitive). "
            "Dashes and underscores will be removed so you can use as many as you want, or none. "
            "Prefixes like 'aria2.' or 'system.' are also optional."
        ),
    )
    call_parser_mxg = call_parser.add_mutually_exclusive_group()
    call_parser_mxg.add_argument(
        "-P", "--params-list", dest="params", nargs="+", help="Parameters as a list of strings."
    )
    call_parser_mxg.add_argument(
        "-J",
        "--json-params",
        dest="params",
        help="Parameters as a JSON string. You should always wrap it at least once in an array '[]'.",
    )

    # ========= ADD MAGNET PARSER ========= #
    add_magnet_parser.add_argument("uri", help="The magnet URI to use.")

    # ========= ADD TORRENT PARSER ========= #
    add_torrent_parser.add_argument("torrent_file", help="The path to the torrent file.")

    # ========= ADD METALINK PARSER ========= #
    add_metalink_parser.add_argument("metalink_file", help="The path to the metalink file.")

    # ========= PAUSE PARSER ========= #
    pause_parser.add_argument("gids", nargs="*", help="The GIDs of the downloads to pause.")
    pause_parser.add_argument("-a", "--all", action="store_true", dest="do_all", help="Pause all the downloads.")
    pause_parser.add_argument(
        "-f", "--force", dest="force", action="store_true", help="Pause without contacting servers first."
    )

    # ========= RESUME PARSER ========= #
    resume_parser.add_argument("gids", nargs="*", help="The GIDs of the downloads to resume.")
    resume_parser.add_argument("-a", "--all", action="store_true", dest="do_all", help="Resume all the downloads.")

    # ========= REMOVE PARSER ========= #
    remove_parser.add_argument("gids", nargs="*", help="The GIDs of the downloads to remove.")
    remove_parser.add_argument("-a", "--all", action="store_true", dest="do_all", help="Remove all the downloads.")
    remove_parser.add_argument(
        "-f", "--force", dest="force", action="store_true", help="Remove without contacting servers first."
    )

    # ========= PURGE PARSER ========= #
    purge_parser.add_argument("gids", nargs="*", help="The GIDs of the downloads to purge.")
    purge_parser.add_argument("-a", "--all", action="store_true", dest="do_all", help="Purge all the downloads.")

    # TODO: when API is ready
    # info_parser = subparsers.add_parser("info", help="Show information about downloads.")
    # info_parser_mxg = info_parser.add_mutually_exclusive_group()
    # info_parser_mxg.add_argument("gids", nargs="+")
    # info_parser_mxg.add_argument("-a", "--all", dest="select_all", action="store_true")
    # TODO: add --format, --fields

    # TODO: when API is ready
    # list_parser = subparsers.add_parser("list", help="List downloads.", aliases=["ls"])
    # list_parser.add_argument("-f", "--format", dest="format")
    # list_parser.add_argument("-s", "--sort", dest="sort")
    # TODO: add --hide-metadata

    # TODO: when API is ready
    # search_parser = subparsers.add_parser("search", help="Search downloads using patterns or regular expressions.")
    # search_parser.add_argument("-L", "--literal", dest="literal", action="store_true")

    # TODO: add options (--set), stats, move-files, save-session, shutdown

    # "show" to show progress.
    # Will evolve into a top-like interface with its own alternate buffer.
    # Many display options, stored in a configuration file.

    # "list" to list current downloads. Alias "ls".
    # By default only outputs downloads names.
    # Option -l, --long for additional information (--format=long).
    # Option -f, --format with choices and custom string.
    # Option -a, --all to list all downloads.
    # Option -m, --metadata to show metadata downloads (default false).
    # Option -s, --sort with choices and custom sort.
    # Option -H, --human-readable.

    # "options" to manipulate options. Alias "opt".
    # Option -s, --set to set an option to a given value.
    # Option -g, --get to get the value of an option.
    # Option -u, --unset to unset an option (reset to default value).
    # Option -i, --increase to increase an integer/float option value.
    # Option -d, --decrease to decrease an integer/float option value.
    # Example: aria2p opts -i max-concurrent-downloads:2 -d timeout:30

    return parser


# ============ SHOW SUBCOMMAND ============ #
def subcommand_show(api):
    """
    Show subcommand.

    Args:
        api (API): the API instance to use.

    Returns:
        int: always 0.
    """
    downloads = api.get_downloads()

    print(
        f"{'GID':<17} "
        f"{'STATUS':<9} "
        f"{'PROGRESS':>8} "
        f"{'DOWN_SPEED':>12} "
        f"{'UP_SPEED':>12} "
        f"{'ETA':>8}  "
        f"NAME"
    )

    for download in downloads:
        print(
            f"{download.gid:<17} "
            f"{download.status:<9} "
            f"{download.progress_string():>8} "
            f"{download.download_speed_string():>12} "
            f"{download.upload_speed_string():>12} "
            f"{download.eta_string():>8}  "
            f"{download.name}"
        )

    return 0


# ============ CALL SUBCOMMAND ============ #
def subcommand_call(api, method, params):
    """
    Call subcommand.

    Args:
        api (API): the API instance to use.
        method (str): name of the method to call.
        params (str / list of str): parameters to use when calling method.

    Returns:
        int: always 0.
    """
    real_method = get_method(method)
    if real_method is None:
        print(f"[ERROR] call: Unknown method {method}.", file=sys.stderr)
        print(file=sys.stderr)
        print(f"Run 'aria2p call listmethods' to list the available methods.", file=sys.stderr)
        return 1

    if isinstance(params, str):
        params = json.loads(params)
    elif params is None:
        params = []

    response = api.client.call(real_method, params)
    print(json.dumps(response))

    return 0


def get_method(name, default=None):
    """Return the actual aria2 method name from a differently formatted name."""
    methods = {}
    for method in Client.METHODS:
        methods[method.lower()] = method
        methods[method.split(".")[1].lower()] = method
    name = name.lower()
    name = name.replace("-", "")
    name = name.replace("_", "")
    return methods.get(name, default)


# ============ ADD MAGNET SUBCOMMAND ============ #
def subcommand_add_magnet(api, uri):
    """
    Add magnet subcommand.

    Args:
        api (API): the API instance to use.
        uri (str): the URI of the magnet.

    Returns:
        int: always 0.
    """
    new_download = api.add_magnet(uri)
    print(f"Created download {new_download.gid}")
    return 0


# ============ ADD TORRENT SUBCOMMAND ============ #
def subcommand_add_torrent(api, torrent_file):
    """
    Add torrent subcommand.

    Args:
        api (API): the API instance to use.
        torrent_file (str): the path to the torrent file.

    Returns:
        int: always 0.
    """
    new_download = api.add_torrent(torrent_file)
    print(f"Created download {new_download.gid}")
    return 0


# ============ ADD METALINK SUBCOMMAND ============ #
def subcommand_add_metalink(api: API, metalink_file):
    """
    Add metalink subcommand.

    Args:
        api (API): the API instance to use.
        metalink_file (str): the path to the metalink file.

    Returns:
        int: always 0.
    """
    new_downloads = api.add_metalink(metalink_file)
    for download in new_downloads:
        print(f"Created download {download.gid}")
    return 0


# ============ PAUSE SUBCOMMAND ============ #
def subcommand_pause(api: API, gids=None, do_all=False, force=False):
    """
    Pause subcommand.

    Args:
        api (API): the API instance to use.
        gids (list of str): the GIDs of the downloads to pause.
        do_all (bool): pause all downloads if True.
        force (bool): force pause or not (see API.pause).

    Returns:
        int: 0 if all success, 1 if one failure.
    """
    if do_all:
        if api.pause_all(force=force):
            return 0
        return 1

    downloads = [Download(api, {"gid": gid}) for gid in gids]
    result = api.pause(downloads, force=force)
    if all(result):
        return 0
    for item in result:
        if isinstance(item, ClientException):
            print(item, file=sys.stderr)
    return 1


# ============ RESUME SUBCOMMAND ============ #
def subcommand_resume(api: API, gids=None, do_all=False):
    """
    Resume subcommand.

    Args:
        api (API): the API instance to use.
        gids (list of str): the GIDs of the downloads to resume.
        do_all (bool): pause all downloads if True.

    Returns:
        int: 0 if all success, 1 if one failure.
    """
    if do_all:
        if api.resume_all():
            return 0
        return 1

    downloads = [Download(api, {"gid": gid}) for gid in gids]
    result = api.resume(downloads)
    if all(result):
        return 0
    for item in result:
        if isinstance(item, ClientException):
            print(item, file=sys.stderr)
    return 1


# ============ REMOVE SUBCOMMAND ============ #
def subcommand_remove(api: API, gids=None, do_all=False, force=False):
    """
    Remove subcommand.

    Args:
        api (API): the API instance to use.
        gids (list of str): the GIDs of the downloads to remove.
        do_all (bool): pause all downloads if True.
        force (bool): force pause or not (see API.remove).

    Returns:
        int: 0 if all success, 1 if one failure.
    """
    if do_all:
        if api.remove_all():
            return 0
        return 1

    downloads = [Download(api, {"gid": gid}) for gid in gids]
    result = api.remove(downloads, force=force)
    if all(result):
        return 0
    for item in result:
        if isinstance(item, ClientException):
            print(item, file=sys.stderr)
    return 1


# ============ PURGE SUBCOMMAND ============ #
def subcommand_purge(api: API, gids=None, do_all=False):
    """
    Purge subcommand.

    Args:
        api (API): the API instance to use.
        gids (list of str): the GIDs of the downloads to purge.
        do_all (bool): pause all downloads if True.

    Returns:
        int: 0 if all success, 1 if one failure.
    """
    if do_all:
        if api.purge_all():
            return 0
        return 1

    downloads = [Download(api, {"gid": gid}) for gid in gids]
    result = api.purge(downloads)
    if all(result):
        return 0
    for item in result:
        if isinstance(item, ClientException):
            print(item, file=sys.stderr)
    return 1


# ============ AUTOPURGE SUBCOMMAND ============ #
def subcommand_autopurge(api: API):
    """
    Autopurge subcommand.

    Args:
        api (API): the API instance to use.

    Returns:
        int: 0 if all success, 1 if one failure.
    """
    if api.autopurge():
        return 0
    return 1


# ============ INFO SUBCOMMAND ============ #
# def subcommand_info(api: API, gids, select_all=False):
#     if select_all:
#         downloads = api.get_downloads()
#     else:
#         downloads = api.get_downloads(gids)
#
#     api.info(downloads)
#     return 0


# ============ LIST SUBCOMMAND ============ #
# def subcommand_list(api: API, list_format=None, sort=None):
#     api.list(list_format=list_format, sort=sort)
#     return 0


# ============ SEARCH SUBCOMMAND ============ #
# def subcommand_search(api: API, ):
#     api.search()
#     return 0
