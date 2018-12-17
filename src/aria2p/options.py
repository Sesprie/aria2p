class Options:
    def __init__(self, api, struct, gid=None):
        self.api = api
        self._gids = [gid] if gid else []
        self._struct = struct

    # Basic Options
    @property
    def dir(self):
        return self._struct.get("dir")

    @dir.setter
    def dir(self, value):
        if self.api.change_option({"dir": value}, self.gid):
            self._struct["dir"] = value

        # =<DIR>
        #
        # The directory to store the downloaded file.

    @property
    def input_file(self):
        return self._struct.get("input-file")

    @input_file.setter
    def input_file(self, value):
        if self.api.change_option({"input-file": value}, self.gid):
            self._struct["input-file"] = value

        # =<FILE>
        #
        # Downloads the URIs listed in FILE. You can specify multiple sources for a single entity by putting
        # multiple URIs on a single line separated by the TAB character. Additionally, options can be specified
        # after each URI line. Option lines must start with one or more white space characters (SPACE or TAB) and
        # must only contain one option per line. Input files can use gzip compression. When FILE is specified as -,
        # aria2 will read the input from stdin. See the Input File subsection for details. See also the
        # --deferred-input option. See also the --save-session option.

    @property
    def log(self):
        return self._struct.get("log")

    @log.setter
    def log(self, value):
        if self.api.change_option({"log": value}, self.gid):
            self._struct["log"] = value

        # =<LOG>
        #
        # The file name of the log file. If - is specified, log is written to stdout. If empty string("") is
        # specified, or this option is omitted, no log is written to disk at all.

    @property
    def max_concurrent_downloads(self):
        return self._struct.get("max-concurrent-downloads")

    @max_concurrent_downloads.setter
    def max_concurrent_downloads(self, value):
        if self.api.change_option({"max-concurrent-downloads": value}, self.gid):
            self._struct["max-concurrent-downloads"] = value

        # =<N>
        #
        # Set the maximum number of parallel downloads for every queue item. See also the --split option. Default: 5

    @property
    def check_integrity(self):
        return self._struct.get("check-integrity")

    @check_integrity.setter
    def check_integrity(self, value):
        if self.api.change_option({"check-integrity": value}, self.gid):
            self._struct["check-integrity"] = value

        # [=true|false]
        #
        # Check file integrity by validating piece hashes or a hash of entire file. This option has effect only in
        # BitTorrent, Metalink downloads with checksums or HTTP(S)/FTP downloads with --checksum option. If piece
        # hashes are provided, this option can detect damaged portions of a file and re-download them. If a hash of
        # entire file is provided, hash check is only done when file has been already download. This is determined by
        # file length. If hash check fails, file is re-downloaded from scratch. If both piece hashes and a hash of
        # entire file are provided, only piece hashes are used. Default: false

    @property
    def continue_(self):
        return self._struct.get("continue")

    @continue_.setter
    def continue_(self, value):
        if self.api.change_option({"continue": value}, self.gid):
            self._struct["continue"] = value

        # [=true|false]
        #
        # Continue downloading a partially downloaded file. Use this option to resume a download started by a web
        # browser or another program which downloads files sequentially from the beginning. Currently this option is
        # only applicable to HTTP(S)/FTP downloads.

    @property
    def help(self):
        return self._struct.get("help")

    @help.setter
    def help(self, value):
        if self.api.change_option({"help": value}, self.gid):
            self._struct["help"] = value

        # [=<TAG>|<KEYWORD>]
        #
        # The help messages are classified with tags. A tag starts with #. For example, type --help=#http to get the
        # usage for the options tagged with #http. If non-tag word is given, print the usage for the options whose
        # name includes that word. Available Values: #basic, #advanced, #http, #https, #ftp, #metalink,
        # #bittorrent, #cookie, #hook, #file, #rpc, #checksum, #experimental, #deprecated, #help, #all Default: #basic

        # HTTP/FTP/SFTP Options

    @property
    def all_proxy(self):
        return self._struct.get("all-proxy")

    @all_proxy.setter
    def all_proxy(self, value):
        if self.api.change_option({"all-proxy": value}, self.gid):
            self._struct["all-proxy"] = value

        # =<PROXY>
        #
        # Use a proxy server for all protocols. To override a previously defined proxy, use "". You also can override
        # this setting and specify a proxy server for a particular protocol using --http-proxy, --https-proxy
        # and --ftp-proxy options. This affects all downloads. The format of PROXY is [http://][
        # USER:PASSWORD@]HOST[:PORT]. See also ENVIRONMENT section.
        #
        # NOTE:
        #     If user and password are embedded in proxy URI and they are also specified by --{http,https,ftp,
        #     all}-proxy-{user,passwd}  options, those specified later override prior options. For example,
        #     if you specified http-proxy-user=myname, http-proxy-passwd=mypass in aria2.conf and you specified
        #     --http-proxy="http://proxy" on the command-line, then you'd get HTTP proxy http://proxy with user myname
        #     and password mypass.
        #
        #     Another example: if you specified on the command-line --http-proxy="http://user:pass@proxy"
        #     --http-proxy-user="myname" --http-proxy-passwd="mypass", then you'd get HTTP proxy http://proxy with user
        #     myname and password mypass.
        #
        #     One more example:  if you specified in command-line --http-proxy-user="myname"
        #     --http-proxy-passwd="mypass" --http-proxy="http://user:pass@proxy", then you'd get HTTP proxy http://proxy
        #     with user user and password pass.

    @property
    def all_proxy_passwd(self):
        return self._struct.get("all-proxy-passwd")

    @all_proxy_passwd.setter
    def all_proxy_passwd(self, value):
        if self.api.change_option({"all-proxy-passwd": value}, self.gid):
            self._struct["all-proxy-passwd"] = value

        # =<PASSWD>
        #
        # Set password for --all-proxy option.

    @property
    def all_proxy_user(self):
        return self._struct.get("all-proxy-user")

    @all_proxy_user.setter
    def all_proxy_user(self, value):
        if self.api.change_option({"all-proxy-user": value}, self.gid):
            self._struct["all-proxy-user"] = value

        # =<USER>
        #
        # Set user for --all-proxy option.

    @property
    def checksum(self):
        return self._struct.get("checksum")

    @checksum.setter
    def checksum(self, value):
        if self.api.change_option({"checksum": value}, self.gid):
            self._struct["checksum"] = value

        # =<TYPE>=<DIGEST>
        #
        # Set checksum. TYPE is hash type. The supported hash type is listed in Hash Algorithms in aria2c -v. DIGEST
        # is hex digest. For example, setting sha-1 digest looks like this:
        # sha-1=0192ba11326fe2298c8cb4de616f4d4140213838 This option applies only to HTTP(S)/FTP downloads.

    @property
    def connect_timeout(self):
        return self._struct.get("connect-timeout")

    @connect_timeout.setter
    def connect_timeout(self, value):
        if self.api.change_option({"connect-timeout": value}, self.gid):
            self._struct["connect-timeout"] = value

        # =<SEC>
        #
        # Set the connect timeout in seconds to establish connection to HTTP/FTP/proxy server. After the connection
        # is established, this option makes no effect and --timeout option is used instead. Default: 60

    @property
    def dry_run(self):
        return self._struct.get("dry-run")

    @dry_run.setter
    def dry_run(self, value):
        if self.api.change_option({"dry-run": value}, self.gid):
            self._struct["dry-run"] = value

        # [=true|false]
        #
        # If true is given, aria2 just checks whether the remote file is available and doesn't download data. This
        # option has effect on HTTP/FTP download. BitTorrent downloads are canceled if true is specified. Default:
        # false

    @property
    def lowest_speed_limit(self):
        return self._struct.get("lowest-speed-limit")

    @lowest_speed_limit.setter
    def lowest_speed_limit(self, value):
        if self.api.change_option({"lowest-speed-limit": value}, self.gid):
            self._struct["lowest-speed-limit"] = value

        # =<SPEED>
        #
        # Close connection if download speed is lower than or equal to this value(bytes per sec). 0 means aria2
        # does not have a lowest speed limit. You can append K or M (1K = 1024, 1M = 1024K). This option does not
        # affect BitTorrent downloads. Default: 0

    @property
    def max_connection_per_server(self):
        return self._struct.get("max-connection-per-server")

    @max_connection_per_server.setter
    def max_connection_per_server(self, value):
        if self.api.change_option({"max-connection-per-server": value}, self.gid):
            self._struct["max-connection-per-server"] = value

        # =<NUM>
        #
        # The maximum number of connections to one server for each download. Default: 1

    @property
    def max_file_not_found(self):
        return self._struct.get("max-file-not-found")

    @max_file_not_found.setter
    def max_file_not_found(self, value):
        if self.api.change_option({"max-file-not-found": value}, self.gid):
            self._struct["max-file-not-found"] = value

        # =<NUM>
        #
        # If aria2 receives "file not found" status from the remote HTTP/FTP servers NUM times without getting a
        # single byte, then force the download to fail. Specify 0 to disable this option. This options is
        # effective only when using HTTP/FTP servers. The number of retry attempt is counted toward --max-tries,
        # so it should be configured too.
        #
        # Default: 0

    @property
    def max_tries(self):
        return self._struct.get("max-tries")

    @max_tries.setter
    def max_tries(self, value):
        if self.api.change_option({"max-tries": value}, self.gid):
            self._struct["max-tries"] = value

        # =<N>
        #
        # Set number of tries. 0 means unlimited. See also --retry-wait. Default: 5

    @property
    def min_split_size(self):
        return self._struct.get("min-split-size")

    @min_split_size.setter
    def min_split_size(self, value):
        if self.api.change_option({"min-split-size": value}, self.gid):
            self._struct["min-split-size"] = value

        # =<SIZE>
        #
        # aria2 does not split less than 2*SIZE byte range. For example, let's consider downloading 20MiB file. If
        # SIZE is 10M, aria2 can split file into 2 range [0-10MiB)  and [10MiB-20MiB)  and download it using 2
        # sources(if --split >= 2, of course). If SIZE is 15M, since 2*15M > 20MiB, aria2 does not split file and
        # download it using 1 source. You can append K or M (1K = 1024, 1M = 1024K). Possible Values: 1M -1024M
        # Default: 20M

    @property
    def netrc_path(self):
        return self._struct.get("netrc-path")

    @netrc_path.setter
    def netrc_path(self, value):
        if self.api.change_option({"netrc-path": value}, self.gid):
            self._struct["netrc-path"] = value

        # =<FILE>
        #
        # Specify the path to the netrc file. Default: $(HOME)/.netrc
        #
        # NOTE:
        #    Permission of the .netrc file must be 600. Otherwise, the file will be ignored.

    @property
    def no_netrc(self):
        return self._struct.get("no-netrc")

    @no_netrc.setter
    def no_netrc(self, value):
        if self.api.change_option({"no-netrc": value}, self.gid):
            self._struct["no-netrc"] = value

        # [=true|false]
        #
        # Disables netrc support. netrc support is enabled by default.
        #
        # NOTE:
        #     netrc file is only read at the startup if --no-netrc is false. So if --no-netrc is true at the startup,
        #     no netrc is available throughout the session. You cannot get netrc enabled even if you send
        #     --no-netrc=false using aria2.changeGlobalOption().

    @property
    def no_proxy(self):
        return self._struct.get("no-proxy")

    @no_proxy.setter
    def no_proxy(self, value):
        if self.api.change_option({"no-proxy": value}, self.gid):
            self._struct["no-proxy"] = value

        # =<DOMAINS>
        #
        # Specify a comma separated list of host names, domains and network addresses with or without a subnet mask
        # where no proxy should be used.
        #
        # NOTE:
        #     For network addresses with a subnet mask, both IPv4 and IPv6 addresses work. The current
        #     implementation does not resolve the host name in an URI to compare network addresses specified in
        #     --no-proxy. So it is only effective if URI has numeric IP addresses.

    @property
    def out(self):
        return self._struct.get("out")

    @out.setter
    def out(self, value):
        if self.api.change_option({"out": value}, self.gid):
            self._struct["out"] = value

        # =<FILE>
        #
        # The file name of the downloaded file. It is always relative to the directory given in --dir option. When
        # the --force-sequential option is used, this option is ignored.
        #
        # NOTE:
        #
        # You cannot specify a file name for Metalink or BitTorrent downloads. The file name specified here is only
        # used when the URIs fed to aria2 are given on the command line directly, but not when using --input-file,
        # --force-sequential option.
        #
        #    Example:
        #
        #        $ aria2c -o myfile.zip "http://mirror1/file.zip" "http://mirror2/file.zip"

    @property
    def proxy_method(self):
        return self._struct.get("proxy-method")

    @proxy_method.setter
    def proxy_method(self, value):
        if self.api.change_option({"proxy-method": value}, self.gid):
            self._struct["proxy-method"] = value

        # =<METHOD>
        #
        # Set the method to use in proxy request. METHOD is either get or tunnel. HTTPS downloads always use tunnel
        # regardless of this option. Default: get

    @property
    def remote_time(self):
        return self._struct.get("remote-time")

    @remote_time.setter
    def remote_time(self, value):
        if self.api.change_option({"remote-time": value}, self.gid):
            self._struct["remote-time"] = value

        # [=true|false]
        #
        # Retrieve timestamp of the remote file from the remote HTTP/FTP server and if it is available, apply it to
        # the local file. Default: false

    @property
    def reuse_uri(self):
        return self._struct.get("reuse-uri")

    @reuse_uri.setter
    def reuse_uri(self, value):
        if self.api.change_option({"reuse-uri": value}, self.gid):
            self._struct["reuse-uri"] = value

        # [=true|false]
        #
        # Reuse already used URIs if no unused URIs are left. Default: true

    @property
    def retry_wait(self):
        return self._struct.get("retry-wait")

    @retry_wait.setter
    def retry_wait(self, value):
        if self.api.change_option({"retry-wait": value}, self.gid):
            self._struct["retry-wait"] = value

        # =<SEC>
        #
        # Set the seconds to wait between retries. When SEC > 0, aria2 will retry downloads when the HTTP server
        # returns a 503 response. Default: 0

    @property
    def server_stat_of(self):
        return self._struct.get("server-stat-of")

    @server_stat_of.setter
    def server_stat_of(self, value):
        if self.api.change_option({"server-stat-of": value}, self.gid):
            self._struct["server-stat-of"] = value

        # =<FILE>
        #
        # Specify the file name to which performance profile of the servers is saved. You can load saved data using
        # --server-stat-if option. See Server Performance Profile subsection below for file format.

    @property
    def server_stat_if(self):
        return self._struct.get("server-stat-if")

    @server_stat_if.setter
    def server_stat_if(self, value):
        if self.api.change_option({"server-stat-if": value}, self.gid):
            self._struct["server-stat-if"] = value

        # =<FILE>
        #
        # Specify the file name to load performance profile of the servers. The loaded data will be used in
        # some URI selector such as feedback. See also --uri-selector option. See Server Performance Profile
        # subsection below for file format.

    @property
    def server_stat_timeout(self):
        return self._struct.get("server-stat-timeout")

    @server_stat_timeout.setter
    def server_stat_timeout(self, value):
        if self.api.change_option({"server-stat-timeout": value}, self.gid):
            self._struct["server-stat-timeout"] = value

        # =<SEC>
        #
        # Specifies timeout in seconds to invalidate performance profile of the servers since the last contact to
        # them. Default: 86400 (24hours)

    @property
    def split(self):
        return self._struct.get("split")

    @split.setter
    def split(self, value):
        if self.api.change_option({"split": value}, self.gid):
            self._struct["split"] = value

        # =<N>
        #
        # Download a file using N connections. If more than N URIs are given, first N URIs are used and remaining
        # URIs are used for backup. If less than N URIs are given, those URIs are used more than once so that N
        # connections total are made simultaneously. The number of connections to the same host is restricted by the
        # --max-connection-per-server option. See also the --min-split-size option. Default: 5
        #
        # NOTE:
        #     Some Metalinks regulate the number of servers to connect. aria2 strictly respects them. This means that if
        #     Metalink defines the maxconnections attribute lower than N, then aria2 uses the value of this lower
        #     value instead of N.

    @property
    def stream_piece_selector(self):
        return self._struct.get("stream-piece-selector")

    @stream_piece_selector.setter
    def stream_piece_selector(self, value):
        if self.api.change_option({"stream-piece-selector": value}, self.gid):
            self._struct["stream-piece-selector"] = value

        # =<SELECTOR>
        #
        # Specify piece selection algorithm used in HTTP/FTP download. Piece means fixed length segment which is
        # downloaded in parallel in segmented download. If default is given, aria2 selects piece so that it reduces
        # the number of establishing connection. This is reasonable default behavior because establishing
        # connection is an expensive operation. If inorder is given, aria2 selects piece which has minimum index.
        # Index=0 means first of the file. This will be useful to view movie while downloading it.
        # --enable-http-pipelining option may be useful to reduce re-connection overhead. Please note that aria2
        # honors --min-split-size option, so it will be necessary to specify a reasonable value to
        # --min-split-size option. If random is given, aria2 selects piece randomly. Like inorder, --min-split-size
        # option is honored. If geom is given, at the beginning aria2 selects piece which has minimum index like
        # inorder, but it exponentially increasingly keeps space from previously selected piece. This will reduce
        # the number of establishing connection and at the same time it will download the beginning part of the file
        # first. This will be useful to view movie while downloading it. Default: default

    @property
    def timeout(self):
        return self._struct.get("timeout")

    @timeout.setter
    def timeout(self, value):
        if self.api.change_option({"timeout": value}, self.gid):
            self._struct["timeout"] = value

        # =<SEC>
        #
        # Set timeout in seconds. Default: 60

    @property
    def uri_selector(self):
        return self._struct.get("uri-selector")

    @uri_selector.setter
    def uri_selector(self, value):
        if self.api.change_option({"uri-selector": value}, self.gid):
            self._struct["uri-selector"] = value

        # =<SELECTOR>
        #
        # Specify URI selection algorithm. The possible values are inorder, feedback and adaptive. If inorder is
        # given, URI is tried in the order appeared in the URI list. If feedback is given, aria2 uses download
        # speed observed in the previous downloads and choose fastest server in the URI list. This also effectively
        # skips dead mirrors. The observed download speed is a part of performance profile of servers
        # mentioned in --server-stat-of and --server-stat-if options. If adaptive is given, selects one of the
        # best mirrors for the first and reserved connections. For supplementary ones, it returns mirrors which has
        # not been tested yet, and if each of them has already been tested, returns mirrors which has to be tested
        # again. Otherwise, it doesn't select anymore mirrors. Like feedback, it uses a performance profile of
        # servers. Default: feedback

        # HTTP Specific Options

    @property
    def ca_certificate(self):
        return self._struct.get("ca-certificate")

    @ca_certificate.setter
    def ca_certificate(self, value):
        if self.api.change_option({"ca-certificate": value}, self.gid):
            self._struct["ca-certificate"] = value

        # =<FILE>
        #
        # Use the certificate authorities in FILE to verify the peers. The certificate file must be in PEM format and
        # can contain multiple CA certificates. Use --check-certificate option to enable verification.
        #
        # NOTE:
        #     If you build with OpenSSL or the recent version of GnuTLS which has
        #     gnutls_certificate_set_x509_system_trust() function and the library is properly configured to locate the
        #     system-wide CA certificates store, aria2 will automatically load those certificates at the startup.
        #
        # NOTE:
        #     WinTLS and AppleTLS do not support this option. Instead you will have to import the certificate into the
        #     OS trust store.

    @property
    def certificate(self):
        return self._struct.get("certificate")

    @certificate.setter
    def certificate(self, value):
        if self.api.change_option({"certificate": value}, self.gid):
            self._struct["certificate"] = value

        # =<FILE>
        #
        # Use the client certificate in FILE. The certificate must be either in PKCS12 (.p12, .pfx) or in PEM format.
        #
        # PKCS12 files must contain the certificate, a key and optionally a chain of additional certificates. Only
        # PKCS12 files with a blank import password can be opened!
        #
        # When using PEM, you have to specify the private key via --private-key as well.
        #
        # NOTE:
        #    WinTLS does not support PEM files at the moment. Users have to use PKCS12 files.
        #
        # NOTE:
        #     AppleTLS users should use the KeyChain Access utility to import the client certificate and get the SHA-1
        #     fingerprint from the Information dialog corresponding to that certificate. To start aria2c use
        #     --certificate=<SHA-1>. Alternatively PKCS12 files are also supported. PEM files, however, are not
        #     supported.

    @property
    def check_certificate(self):
        return self._struct.get("check-certificate")

    @check_certificate.setter
    def check_certificate(self, value):
        if self.api.change_option({"check-certificate": value}, self.gid):
            self._struct["check-certificate"] = value

        # [=true|false]
        #
        # Verify the peer using certificates specified in --ca-certificate option. Default: true

    @property
    def http_accept_gzip(self):
        return self._struct.get("http-accept-gzip")

    @http_accept_gzip.setter
    def http_accept_gzip(self, value):
        if self.api.change_option({"http-accept-gzip": value}, self.gid):
            self._struct["http-accept-gzip"] = value

        # [=true|false]
        #
        # Send Accept: deflate, gzip request header and inflate response if remote server responds with
        # Content-Encoding:  gzip or Content-Encoding:  deflate. Default: false
        #
        # NOTE:
        #     Some server responds with Content-Encoding: gzip for files which itself is gzipped file. aria2 inflates
        #     them anyway because of the response header.

    @property
    def http_auth_challenge(self):
        return self._struct.get("http-auth-challenge")

    @http_auth_challenge.setter
    def http_auth_challenge(self, value):
        if self.api.change_option({"http-auth-challenge": value}, self.gid):
            self._struct["http-auth-challenge"] = value

        # [=true|false]
        #
        # Send HTTP authorization header only when it is requested by the server. If false is set, then authorization
        # header is always sent to the server. There is an exception: if user name and password are embedded in URI,
        # authorization header is always sent to the server regardless of this option. Default: false

    @property
    def http_no_cache(self):
        return self._struct.get("http-no-cache")

    @http_no_cache.setter
    def http_no_cache(self, value):
        if self.api.change_option({"http-no-cache": value}, self.gid):
            self._struct["http-no-cache"] = value

        # [=true|false]
        #
        # Send Cache-Control:  no-cache and Pragma:  no-cache header to avoid cached content. If false is given,
        # these headers are not sent and you can add Cache-Control header with a directive you like using --header
        # option. Default: false

    @property
    def http_user(self):
        return self._struct.get("http-user")

    @http_user.setter
    def http_user(self, value):
        if self.api.change_option({"http-user": value}, self.gid):
            self._struct["http-user"] = value

        # =<USER>
        #
        # Set HTTP user. This affects all URIs.

    @property
    def http_passwd(self):
        return self._struct.get("http-passwd")

    @http_passwd.setter
    def http_passwd(self, value):
        if self.api.change_option({"http-passwd": value}, self.gid):
            self._struct["http-passwd"] = value

        # =<PASSWD>
        #
        # Set HTTP password. This affects all URIs.

    @property
    def http_proxy(self):
        return self._struct.get("http-proxy")

    @http_proxy.setter
    def http_proxy(self, value):
        if self.api.change_option({"http-proxy": value}, self.gid):
            self._struct["http-proxy"] = value

        # =<PROXY>
        #
        # Use a proxy server for HTTP. To override a previously defined proxy, use "". See also the --all-proxy
        # option. This affects all http downloads. The format of PROXY is [http://][USER:PASSWORD@]HOST[:PORT]

    @property
    def http_proxy_passwd(self):
        return self._struct.get("http-proxy-passwd")

    @http_proxy_passwd.setter
    def http_proxy_passwd(self, value):
        if self.api.change_option({"http-proxy-passwd": value}, self.gid):
            self._struct["http-proxy-passwd"] = value

        # =<PASSWD>
        #
        # Set password for --http-proxy.

    @property
    def http_proxy_user(self):
        return self._struct.get("http-proxy-user")

    @http_proxy_user.setter
    def http_proxy_user(self, value):
        if self.api.change_option({"http-proxy-user": value}, self.gid):
            self._struct["http-proxy-user"] = value

        # =<USER>
        #
        # Set user for --http-proxy.

    @property
    def https_proxy(self):
        return self._struct.get("https-proxy")

    @https_proxy.setter
    def https_proxy(self, value):
        if self.api.change_option({"https-proxy": value}, self.gid):
            self._struct["https-proxy"] = value

        # =<PROXY>
        #
        # Use a proxy server for HTTPS. To override a previously defined proxy, use "". See also the --all-proxy
        # option. This affects all https download. The format of PROXY is [http://][USER:PASSWORD@]HOST[:PORT]

    @property
    def https_proxy_passwd(self):
        return self._struct.get("https-proxy-passwd")

    @https_proxy_passwd.setter
    def https_proxy_passwd(self, value):
        if self.api.change_option({"https-proxy-passwd": value}, self.gid):
            self._struct["https-proxy-passwd"] = value

        # =<PASSWD>
        #
        # Set password for --https-proxy.

    @property
    def https_proxy_user(self):
        return self._struct.get("https-proxy-user")

    @https_proxy_user.setter
    def https_proxy_user(self, value):
        if self.api.change_option({"https-proxy-user": value}, self.gid):
            self._struct["https-proxy-user"] = value

        # =<USER>
        #
        # Set user for --https-proxy.

    @property
    def private_key(self):
        return self._struct.get("private-key")

    @private_key.setter
    def private_key(self, value):
        if self.api.change_option({"private-key": value}, self.gid):
            self._struct["private-key"] = value

        # =<FILE>
        #
        # Use the private key in FILE. The private key must be decrypted and in PEM format. The behavior when
        # encrypted one is given is undefined. See also --certificate option.

    @property
    def referer(self):
        return self._struct.get("referer")

    @referer.setter
    def referer(self, value):
        if self.api.change_option({"referer": value}, self.gid):
            self._struct["referer"] = value

        # =<REFERER>
        #
        # Set an http referrer (Referer). This affects all http/https downloads. If * is given, the download URI is
        # also used as the referrer. This may be useful when used together with the --parameterized-uri option.

    @property
    def enable_http_keep_alive(self):
        return self._struct.get("enable-http-keep-alive")

    @enable_http_keep_alive.setter
    def enable_http_keep_alive(self, value):
        if self.api.change_option({"enable-http-keep-alive": value}, self.gid):
            self._struct["enable-http-keep-alive"] = value

        # [=true|false]
        #
        # Enable HTTP/1.1 persistent connection. Default: true

    @property
    def enable_http_pipelining(self):
        return self._struct.get("enable-http-pipelining")

    @enable_http_pipelining.setter
    def enable_http_pipelining(self, value):
        if self.api.change_option({"enable-http-pipelining": value}, self.gid):
            self._struct["enable-http-pipelining"] = value

        # [=true|false]
        #
        # Enable HTTP/1.1 pipelining. Default: false
        #
        # NOTE:
        #    In performance perspective, there is usually no advantage to enable this option.

    @property
    def header(self):
        return self._struct.get("header")

    @header.setter
    def header(self, value):
        if self.api.change_option({"header": value}, self.gid):
            self._struct["header"] = value

        # =<HEADER>
        #
        # Append HEADER to HTTP request header. You can use this option repeatedly to specify more than one header:
        #
        #    $ aria2c --header="X-A: b78" --header="X-B: 9J1" "http://host/file"

    @property
    def load_cookies(self):
        return self._struct.get("load-cookies")

    @load_cookies.setter
    def load_cookies(self, value):
        if self.api.change_option({"load-cookies": value}, self.gid):
            self._struct["load-cookies"] = value

        # =<FILE>
        #
        # Load Cookies from FILE using the Firefox3 format (SQLite3), Chromium/Google Chrome (SQLite3) and the
        # Mozilla/Firefox(1.x/2.x)/Netscape format.
        #
        # NOTE:
        #     If aria2 is built without libsqlite3, then it doesn't support Firefox3 and Chromium/Google Chrome cookie
        #     format.

    @property
    def save_cookies(self):
        return self._struct.get("save-cookies")

    @save_cookies.setter
    def save_cookies(self, value):
        if self.api.change_option({"save-cookies": value}, self.gid):
            self._struct["save-cookies"] = value

        # =<FILE>
        #
        # Save Cookies to FILE in Mozilla/Firefox(1.x/2.x)/ Netscape format. If FILE already exists,
        # it is overwritten. Session Cookies are also saved and their expiry values are treated as 0. Possible
        # Values: /path/to/file

    @property
    def use_head(self):
        return self._struct.get("use-head")

    @use_head.setter
    def use_head(self, value):
        if self.api.change_option({"use-head": value}, self.gid):
            self._struct["use-head"] = value

        # [=true|false]
        #
        # Use HEAD method for the first request to the HTTP server. Default: false

    @property
    def user_agent(self):
        return self._struct.get("user-agent")

    @user_agent.setter
    def user_agent(self, value):
        if self.api.change_option({"user-agent": value}, self.gid):
            self._struct["user-agent"] = value

        # =<USER_AGENT>
        #
        # Set user agent for HTTP(S) downloads. Default: aria2/$VERSION, $VERSION is replaced by package version.

        # FTP/SFTP Specific Options

    @property
    def ftp_user(self):
        return self._struct.get("ftp-user")

    @ftp_user.setter
    def ftp_user(self, value):
        if self.api.change_option({"ftp-user": value}, self.gid):
            self._struct["ftp-user"] = value

        # =<USER>
        #
        # Set FTP user. This affects all URIs. Default: anonymous

    @property
    def ftp_passwd(self):
        return self._struct.get("ftp-passwd")

    @ftp_passwd.setter
    def ftp_passwd(self, value):
        if self.api.change_option({"ftp-passwd": value}, self.gid):
            self._struct["ftp-passwd"] = value

        # =<PASSWD>
        #
        # Set FTP password. This affects all URIs. If user name is embedded but password is missing in URI,
        # aria2 tries to resolve password using .netrc. If password is found in .netrc, then use it as password. If
        # not, use the password specified in this option. Default: ARIA2USER@

    @property
    def ftp_pasv(self):
        return self._struct.get("ftp-pasv")

    @ftp_pasv.setter
    def ftp_pasv(self, value):
        if self.api.change_option({"ftp-pasv": value}, self.gid):
            self._struct["ftp-pasv"] = value

        # [=true|false]
        #
        # Use the passive mode in FTP. If false is given, the active mode will be used. Default: true
        #
        # NOTE:
        #    This option is ignored for SFTP transfer.

    @property
    def ftp_proxy(self):
        return self._struct.get("ftp-proxy")

    @ftp_proxy.setter
    def ftp_proxy(self, value):
        if self.api.change_option({"ftp-proxy": value}, self.gid):
            self._struct["ftp-proxy"] = value

        # =<PROXY>
        #
        # Use a proxy server for FTP. To override a previously defined proxy, use "". See also the --all-proxy
        # option. This affects all ftp downloads. The format of PROXY is [http://][USER:PASSWORD@]HOST[:PORT]

    @property
    def ftp_proxy_passwd(self):
        return self._struct.get("ftp-proxy-passwd")

    @ftp_proxy_passwd.setter
    def ftp_proxy_passwd(self, value):
        if self.api.change_option({"ftp-proxy-passwd": value}, self.gid):
            self._struct["ftp-proxy-passwd"] = value

        # =<PASSWD>
        #
        # Set password for --ftp-proxy option.

    @property
    def ftp_proxy_user(self):
        return self._struct.get("ftp-proxy-user")

    @ftp_proxy_user.setter
    def ftp_proxy_user(self, value):
        if self.api.change_option({"ftp-proxy-user": value}, self.gid):
            self._struct["ftp-proxy-user"] = value

        # =<USER>
        #
        # Set user for --ftp-proxy option.

    @property
    def ftp_type(self):
        return self._struct.get("ftp-type")

    @ftp_type.setter
    def ftp_type(self, value):
        if self.api.change_option({"ftp-type": value}, self.gid):
            self._struct["ftp-type"] = value

        # =<TYPE>
        #
        # Set FTP transfer type. TYPE is either binary or ascii. Default: binary
        #
        # NOTE:
        #    This option is ignored for SFTP transfer.

    @property
    def ftp_reuse_connection(self):
        return self._struct.get("ftp-reuse-connection")

    @ftp_reuse_connection.setter
    def ftp_reuse_connection(self, value):
        if self.api.change_option({"ftp-reuse-connection": value}, self.gid):
            self._struct["ftp-reuse-connection"] = value

        # [=true|false]
        #
        # Reuse connection in FTP. Default: true

    @property
    def ssh_host_key_md(self):
        return self._struct.get("ssh-host-key-md")

    @ssh_host_key_md.setter
    def ssh_host_key_md(self, value):
        if self.api.change_option({"ssh-host-key-md": value}, self.gid):
            self._struct["ssh-host-key-md"] = value

        # =<TYPE>=<DIGEST>
        #
        # Set checksum for SSH host public key. TYPE is hash type. The supported hash type is sha-1 or
        # md5. DIGEST is hex digest. For example: sha-1=b030503d4de4539dc7885e6f0f5e256704edf4c3. This option can be
        # used to validate server's public key when SFTP is used. If this option is not set, which is default,
        # no validation takes place.

        # BitTorrent/Metalink Options

    @property
    def select_file(self):
        return self._struct.get("select-file")

    @select_file.setter
    def select_file(self, value):
        if self.api.change_option({"select-file": value}, self.gid):
            self._struct["select-file"] = value

        # =<INDEX>...
        #
        # Set file to download by specifying its index. You can find the file index using the --show-files option.
        # Multiple indexes can be specified by using ,, for example: 3,6. You can also use - to specify a range: 1-5.
        # , and - can be used together: 1-5,8,9. When used with the -M option, index may vary depending on the query
        # (see --metalink-* options).
        #
        # NOTE:
        #     In multi file torrent, the adjacent files specified by this option may also be downloaded. This is by
        #     design, not a bug. A single piece may include several files or part of files, and aria2 writes the piece
        #     to the appropriate files.

    @property
    def show_files(self):
        return self._struct.get("show-files")

    @show_files.setter
    def show_files(self, value):
        if self.api.change_option({"show-files": value}, self.gid):
            self._struct["show-files"] = value

        # [=true|false]
        #
        # Print file listing of ".torrent", ".meta4" and ".metalink" file and exit. In case of ".torrent" file,
        # additional information (infohash, piece length, etc) is also printed.

        # BitTorrent Specific Options

    @property
    def bt_detach_seed_only(self):
        return self._struct.get("bt-detach-seed-only")

    @bt_detach_seed_only.setter
    def bt_detach_seed_only(self, value):
        if self.api.change_option({"bt-detach-seed-only": value}, self.gid):
            self._struct["bt-detach-seed-only"] = value

        # [=true|false]
        #
        # Exclude seed only downloads when counting concurrent active downloads (See -j option). This means that
        # if -j3 is given and this option is turned on and 3 downloads are active and one of those enters seed mode,
        # then it is excluded from active download count (thus it becomes 2), and the next download waiting in queue
        # gets started. But be aware that seeding item is still recognized as active download in RPC method. Default:
        # false

    @property
    def bt_enable_hook_after_hash_check(self):
        return self._struct.get("bt_enable_hook_after_hash_check")

    @bt_enable_hook_after_hash_check.setter
    def bt_enable_hook_after_hash_check(self, value):
        if self.api.change_option({"bt_enable_hook_after_hash_check": value}, self.gid):
            self._struct["bt_enable_hook_after_hash_check"] = value

        # [=true|false]
        #
        # Allow hook command invocation after hash check (see -V option) in BitTorrent download. By default,
        # when hash check succeeds, the command given by --on-bt-download-complete is executed. To disable this
        # action, give false to this option. Default: true

    @property
    def bt_enable_lpd(self):
        return self._struct.get("bt-enable-lpd")

    @bt_enable_lpd.setter
    def bt_enable_lpd(self, value):
        if self.api.change_option({"bt-enable-lpd": value}, self.gid):
            self._struct["bt-enable-lpd"] = value

        # [=true|false]
        #
        # Enable Local Peer Discovery. If a private flag is set in a torrent, aria2 doesn't use this feature for that
        # download even if true is given. Default: false

    @property
    def bt_exclude_tracker(self):
        return self._struct.get("bt-exclude-tracker")

    @bt_exclude_tracker.setter
    def bt_exclude_tracker(self, value):
        if self.api.change_option({"bt-exclude-tracker": value}, self.gid):
            self._struct["bt-exclude-tracker"] = value

        # =<URI>[,...]
        #
        # Comma separated list of BitTorrent tracker's announce URI to remove. You can use special value * which
        # matches all URIs, thus removes all announce URIs. When specifying * in shell command-line, don't forget to
        # escape or quote it. See also --bt-tracker option.

    @property
    def bt_external_ip(self):
        return self._struct.get("bt-external-ip")

    @bt_external_ip.setter
    def bt_external_ip(self, value):
        if self.api.change_option({"bt-external-ip": value}, self.gid):
            self._struct["bt-external-ip"] = value

        # =<IPADDRESS>
        #
        # Specify the external IP address to use in BitTorrent download and DHT. It may be sent to BitTorrent
        # tracker. For DHT, this option should be set to report that local node is downloading a particular
        # torrent. This is critical to use DHT in a private network. Although this function is named external,
        # it can accept any kind of IP addresses.

    @property
    def bt_force_encryption(self):
        return self._struct.get("bt-force-encryption")

    @bt_force_encryption.setter
    def bt_force_encryption(self, value):
        if self.api.change_option({"bt-force-encryption": value}, self.gid):
            self._struct["bt-force-encryption"] = value

        # [=true|false]
        #
        # Requires BitTorrent message payload encryption with arc4. This is a shorthand of --bt-require-crypto
        # --bt-min-crypto-level=arc4. This option does not change the option value of those options. If true is
        # given, deny legacy BitTorrent handshake and only use Obfuscation handshake and always encrypt message
        # payload. Default: false

    @property
    def bt_hash_check_seed(self):
        return self._struct.get("bt-hash-check-seed")

    @bt_hash_check_seed.setter
    def bt_hash_check_seed(self, value):
        if self.api.change_option({"bt-hash-check-seed": value}, self.gid):
            self._struct["bt-hash-check-seed"] = value

        # [=true|false]
        #
        # If true is given, after hash check using --check-integrity option and file is complete, continue to seed
        # file. If you want to check file and download it only when it is damaged or incomplete, set this option to
        # false. This option has effect only on BitTorrent download. Default: true

    @property
    def bt_lpd_interface(self):
        return self._struct.get("bt-lpd-interface")

    @bt_lpd_interface.setter
    def bt_lpd_interface(self, value):
        if self.api.change_option({"bt-lpd-interface": value}, self.gid):
            self._struct["bt-lpd-interface"] = value

        # =<INTERFACE>
        #
        # Use given interface for Local Peer Discovery. If this option is not specified, the default interface is
        # chosen. You can specify interface name and IP address. Possible Values: interface, IP address

    @property
    def bt_max_open_files(self):
        return self._struct.get("bt-max-open-files")

    @bt_max_open_files.setter
    def bt_max_open_files(self, value):
        if self.api.change_option({"bt-max-open-files": value}, self.gid):
            self._struct["bt-max-open-files"] = value

        # =<NUM>
        #
        # Specify maximum number of files to open in multi-file BitTorrent/Metalink download globally. Default: 100

    @property
    def bt_max_peers(self):
        return self._struct.get("bt-max-peers")

    @bt_max_peers.setter
    def bt_max_peers(self, value):
        if self.api.change_option({"bt-max-peers": value}, self.gid):
            self._struct["bt-max-peers"] = value

        # =<NUM>
        #
        # Specify the maximum number of peers per torrent. 0 means unlimited. See also --bt-request-peer-speed-limit
        # option. Default: 55

    @property
    def bt_metadata_only(self):
        return self._struct.get("bt-metadata-only")

    @bt_metadata_only.setter
    def bt_metadata_only(self, value):
        if self.api.change_option({"bt-metadata-only": value}, self.gid):
            self._struct["bt-metadata-only"] = value

        # [=true|false]
        #
        # Download meta data only. The file(s) described in meta data will not be downloaded. This option has effect
        # only when BitTorrent Magnet URI is used. See also --bt-save-metadata option. Default: false

    @property
    def bt_min_crypto_level(self):
        return self._struct.get("bt-min-crypto-level")

    @bt_min_crypto_level.setter
    def bt_min_crypto_level(self, value):
        if self.api.change_option({"bt-min-crypto-level": value}, self.gid):
            self._struct["bt-min-crypto-level"] = value

        # =plain|arc4
        #
        # Set minimum level of encryption method. If several encryption methods are provided by a peer,
        # aria2 chooses the lowest one which satisfies the given level. Default: plain

    @property
    def bt_prioritize_piece(self):
        return self._struct.get("bt-prioritize-piece")

    @bt_prioritize_piece.setter
    def bt_prioritize_piece(self, value):
        if self.api.change_option({"bt-prioritize-piece": value}, self.gid):
            self._struct["bt-prioritize-piece"] = value

        # =head[=<SIZE>],tail[=<SIZE>]
        #
        # Try to download first and last pieces of each file first. This is useful for previewing files. The argument
        # can contain 2 keywords: head and tail. To include both keywords, they must be separated by comma. These
        # keywords can take one parameter, SIZE. For example, if head=<SIZE> is specified, pieces in the range of
        # first SIZE bytes of each file get higher priority. tail=<SIZE> means the range of last SIZE bytes of each
        # file. SIZE can include K or M (1K = 1024, 1M = 1024K). If SIZE is omitted, SIZE=1M is used.

    @property
    def bt_remove_unselected_file(self):
        return self._struct.get("bt-remove-unselected-file")

    @bt_remove_unselected_file.setter
    def bt_remove_unselected_file(self, value):
        if self.api.change_option({"bt-remove-unselected-file": value}, self.gid):
            self._struct["bt-remove-unselected-file"] = value

        # [=true|false]
        #
        # Removes the unselected files when download is completed in BitTorrent. To select files,
        # use --select-file option. If it is not used, all files are assumed to be selected. Please use this option
        # with care because it will actually remove files from your disk. Default: false

    @property
    def bt_require_crypto(self):
        return self._struct.get("bt-require-crypto")

    @bt_require_crypto.setter
    def bt_require_crypto(self, value):
        if self.api.change_option({"bt-require-crypto": value}, self.gid):
            self._struct["bt-require-crypto"] = value

        # [=true|false]
        #
        # If true is given, aria2 doesn't accept and establish connection with legacy BitTorrent handshake(
        # \19BitTorrent protocol). Thus aria2 always uses Obfuscation handshake. Default: false

    @property
    def bt_request_peer_speed_limit(self):
        return self._struct.get("bt-request-peer-speed-limit")

    @bt_request_peer_speed_limit.setter
    def bt_request_peer_speed_limit(self, value):
        if self.api.change_option({"bt-request-peer-speed-limit": value}, self.gid):
            self._struct["bt-request-peer-speed-limit"] = value

        # =<SPEED>
        #
        # If the whole download speed of every torrent is lower than SPEED, aria2 temporarily increases the number
        # of peers to try for more download speed. Configuring this option with your preferred download speed can
        # increase your download speed in some cases. You can append K or M (1K = 1024, 1M = 1024K). Default: 50K

    @property
    def bt_save_metadata(self):
        return self._struct.get("bt-save-metadata")

    @bt_save_metadata.setter
    def bt_save_metadata(self, value):
        if self.api.change_option({"bt-save-metadata": value}, self.gid):
            self._struct["bt-save-metadata"] = value

        # [=true|false]
        #
        # Save meta data as ".torrent" file. This option has effect only when BitTorrent Magnet URI is used. The
        # file name is hex encoded info hash with suffix ".torrent". The directory to be saved is the same directory
        # where download file is saved. If the same file already exists, meta data is not saved. See also
        # --bt-metadata-only option. Default: false

    @property
    def bt_seed_unverified(self):
        return self._struct.get("bt-seed-unverified")

    @bt_seed_unverified.setter
    def bt_seed_unverified(self, value):
        if self.api.change_option({"bt-seed-unverified": value}, self.gid):
            self._struct["bt-seed-unverified"] = value

        # [=true|false]
        #
        # Seed previously downloaded files without verifying piece hashes. Default: false

    @property
    def bt_stop_timeout(self):
        return self._struct.get("bt-stop-timeout")

    @bt_stop_timeout.setter
    def bt_stop_timeout(self, value):
        if self.api.change_option({"bt-stop-timeout": value}, self.gid):
            self._struct["bt-stop-timeout"] = value

        # =<SEC>
        #
        # Stop BitTorrent download if download speed is 0 in consecutive SEC seconds. If 0 is given, this feature is
        # disabled. Default: 0

    @property
    def bt_tracker(self):
        return self._struct.get("bt-tracker")

    @bt_tracker.setter
    def bt_tracker(self, value):
        if self.api.change_option({"bt-tracker": value}, self.gid):
            self._struct["bt-tracker"] = value

        # =<URI>[,...]
        #
        # Comma separated list of additional BitTorrent tracker's announce URI. These URIs are not affected by
        # --bt-exclude-tracker option because they are added after URIs in --bt-exclude-tracker option are removed.

    @property
    def bt_tracker_connect_timeout(self):
        return self._struct.get("bt-tracker-connect-timeout")

    @bt_tracker_connect_timeout.setter
    def bt_tracker_connect_timeout(self, value):
        if self.api.change_option({"bt-tracker-connect-timeout": value}, self.gid):
            self._struct["bt-tracker-connect-timeout"] = value

        # =<SEC>
        #
        # Set the connect timeout in seconds to establish connection to tracker. After the connection is
        # established, this option makes no effect and --bt-tracker-timeout option is used instead. Default: 60

    @property
    def bt_tracker_interval(self):
        return self._struct.get("bt-tracker-interval")

    @bt_tracker_interval.setter
    def bt_tracker_interval(self, value):
        if self.api.change_option({"bt-tracker-interval": value}, self.gid):
            self._struct["bt-tracker-interval"] = value

        # =<SEC>
        #
        # Set the interval in seconds between tracker requests. This completely overrides interval value and
        # aria2 just uses this value and ignores the min interval and interval value in the response of tracker. If 0
        # is set, aria2 determines interval based on the response of tracker and the download progress.
        # Default: 0

    @property
    def bt_tracker_timeout(self):
        return self._struct.get("bt-tracker-timeout")

    @bt_tracker_timeout.setter
    def bt_tracker_timeout(self, value):
        if self.api.change_option({"bt-tracker-timeout": value}, self.gid):
            self._struct["bt-tracker-timeout"] = value

        # =<SEC>
        #
        # Set timeout in seconds. Default: 60

    @property
    def dht_entry_point(self):
        return self._struct.get("dht-entry-point")

    @dht_entry_point.setter
    def dht_entry_point(self, value):
        if self.api.change_option({"dht-entry-point": value}, self.gid):
            self._struct["dht-entry-point"] = value

        # =<HOST>:<PORT>
        #
        # Set host and port as an entry point to IPv4 DHT network.

    @property
    def dht_entry_point6(self):
        return self._struct.get("dht-entry-point6")

    @dht_entry_point6.setter
    def dht_entry_point6(self, value):
        if self.api.change_option({"dht-entry-point6": value}, self.gid):
            self._struct["dht-entry-point6"] = value

        # =<HOST>:<PORT>
        #
        # Set host and port as an entry point to IPv6 DHT network.

    @property
    def dht_file_path(self):
        return self._struct.get("dht-file-path")

    @dht_file_path.setter
    def dht_file_path(self, value):
        if self.api.change_option({"dht-file-path": value}, self.gid):
            self._struct["dht-file-path"] = value

        # =<PATH>
        #
        # Change the IPv4 DHT routing table file to PATH. Default: $HOME/.aria2/dht.dat if present, otherwise
        # $XDG_CACHE_HOME/aria2/dht.dat.

    @property
    def dht_file_path6(self):
        return self._struct.get("dht-file-path6")

    @dht_file_path6.setter
    def dht_file_path6(self, value):
        if self.api.change_option({"dht-file-path6": value}, self.gid):
            self._struct["dht-file-path6"] = value

        # =<PATH>
        #
        # Change the IPv6 DHT routing table file to PATH. Default: $HOME/.aria2/dht6.dat if present, otherwise
        # $XDG_CACHE_HOME/aria2/dht6.dat.

    @property
    def dht_listen_addr6(self):
        return self._struct.get("dht-listen-addr6")

    @dht_listen_addr6.setter
    def dht_listen_addr6(self, value):
        if self.api.change_option({"dht-listen-addr6": value}, self.gid):
            self._struct["dht-listen-addr6"] = value

        # =<ADDR>
        #
        # Specify address to bind socket for IPv6 DHT. It should be a global unicast IPv6 address of the host.

    @property
    def dht_listen_port(self):
        return self._struct.get("dht-listen-port")

    @dht_listen_port.setter
    def dht_listen_port(self, value):
        if self.api.change_option({"dht-listen-port": value}, self.gid):
            self._struct["dht-listen-port"] = value

        # =<PORT>...
        #
        # Set UDP listening port used by DHT(IPv4, IPv6) and UDP tracker. Multiple ports can be specified by using ,
        # , for example: 6881,6885. You can also use - to specify a range: 6881-6999. , and - can be used together.
        # Default: 6881-6999
        #
        # NOTE:
        #    Make sure that the specified ports are open for incoming UDP traffic.

    @property
    def dht_message_timeout(self):
        return self._struct.get("dht-message-timeout")

    @dht_message_timeout.setter
    def dht_message_timeout(self, value):
        if self.api.change_option({"dht-message-timeout": value}, self.gid):
            self._struct["dht-message-timeout"] = value

        # =<SEC>
        #
        # Set timeout in seconds. Default: 10

    @property
    def enable_dht(self):
        return self._struct.get("enable-dht")

    @enable_dht.setter
    def enable_dht(self, value):
        if self.api.change_option({"enable-dht": value}, self.gid):
            self._struct["enable-dht"] = value

        # [=true|false]
        #
        # Enable IPv4 DHT functionality. It also enables UDP tracker support. If a private flag is set in a torrent,
        # aria2 doesn't use DHT for that download even if true is given. Default: true

    @property
    def enable_dht6(self):
        return self._struct.get("enable-dht6")

    @enable_dht6.setter
    def enable_dht6(self, value):
        if self.api.change_option({"enable-dht6": value}, self.gid):
            self._struct["enable-dht6"] = value

        # [=true|false]
        #
        # Enable IPv6 DHT functionality. If a private flag is set in a torrent, aria2 doesn't use DHT
        # for that download even if true is given. Use --dht-listen-port option to specify port number to listen on.
        # See also --dht-listen-addr6 option.

    @property
    def enable_peer_exchange(self):
        return self._struct.get("enable-peer-exchange")

    @enable_peer_exchange.setter
    def enable_peer_exchange(self, value):
        if self.api.change_option({"enable-peer-exchange": value}, self.gid):
            self._struct["enable-peer-exchange"] = value

        # [=true|false]
        #
        # Enable Peer Exchange extension. If a private flag is set in a torrent, this feature is disabled for that
        # download even if true is given. Default: true

    @property
    def follow_torrent(self):
        return self._struct.get("follow-torrent")

    @follow_torrent.setter
    def follow_torrent(self, value):
        if self.api.change_option({"follow-torrent": value}, self.gid):
            self._struct["follow-torrent"] = value

        # =true|false|mem
        #
        # If true or mem is specified, when a file whose suffix is .torrent or content type is
        # application/x-bittorrent is downloaded, aria2 parses it as a torrent file and downloads files
        # mentioned in it. If mem is specified, a torrent file is not written to the disk, but is just kept in
        # memory. If false is specified, the .torrent file is downloaded to the disk, but is not parsed as a torrent
        # and its contents are not downloaded. Default: true

    @property
    def index_out(self):
        return self._struct.get("index-out")

    @index_out.setter
    def index_out(self, value):
        if self.api.change_option({"index-out": value}, self.gid):
            self._struct["index-out"] = value

        # =<INDEX>=<PATH>
        #
        # Set file path for file with index=INDEX. You can find the file index using the --show-files option. PATH is
        # a relative path to the path specified in --dir option. You can use this option multiple times. Using this
        # option, you can specify the output file names of BitTorrent downloads.

    @property
    def listen_port(self):
        return self._struct.get("listen-port")

    @listen_port.setter
    def listen_port(self, value):
        if self.api.change_option({"listen-port": value}, self.gid):
            self._struct["listen-port"] = value

        # =<PORT>...
        #
        # Set TCP port number for BitTorrent downloads. Multiple ports can be specified by using, for example:
        # 6881,6885. You can also use - to specify a range: 6881-6999. , and - can be used together: 6881-6889,
        # 6999. Default: 6881-6999
        #
        # NOTE:
        #    Make sure that the specified ports are open for incoming TCP traffic.

    @property
    def max_overall_upload_limit(self):
        return self._struct.get("max-overall-upload-limit")

    @max_overall_upload_limit.setter
    def max_overall_upload_limit(self, value):
        if self.api.change_option({"max-overall-upload-limit": value}, self.gid):
            self._struct["max-overall-upload-limit"] = value

        # =<SPEED>
        #
        # Set max overall upload speed in bytes/sec. 0 means unrestricted. You can append K or M (1K = 1024,
        # 1M = 1024K). To limit the upload speed per torrent, use --max-upload-limit option. Default: 0

    @property
    def max_upload_limit(self):
        return self._struct.get("max-upload-limit")

    @max_upload_limit.setter
    def max_upload_limit(self, value):
        if self.api.change_option({"max-upload-limit": value}, self.gid):
            self._struct["max-upload-limit"] = value

        # =<SPEED>
        #
        # Set max upload speed per each torrent in bytes/sec. 0 means unrestricted. You can append K or M (1K = 1024,
        # 1M = 1024K). To limit the overall upload speed, use --max-overall-upload-limit option. Default: 0

    @property
    def peer_id_prefix(self):
        return self._struct.get("peer-id-prefix")

    @peer_id_prefix.setter
    def peer_id_prefix(self, value):
        if self.api.change_option({"peer-id-prefix": value}, self.gid):
            self._struct["peer-id-prefix"] = value

        # =<PEER_ID_PREFIX>
        #
        # Specify the prefix of peer ID. The peer ID in BitTorrent is 20 byte length. If more than 20 bytes are
        # specified, only first 20 bytes are used. If less than 20 bytes are specified, random byte data are added
        # to make its length 20 bytes.
        #
        # Default:  A2-$MAJOR-$MINOR-$PATCH-, $MAJOR, $MINOR and $PATCH are replaced by major, minor and patch
        # version number respectively. For instance, aria2 version 1.18.8 has prefix ID A2-1-18-8-.

    @property
    def seed_ratio(self):
        return self._struct.get("seed-ratio")

    @seed_ratio.setter
    def seed_ratio(self, value):
        if self.api.change_option({"seed-ratio": value}, self.gid):
            self._struct["seed-ratio"] = value

        # =<RATIO>
        #
        # Specify share ratio. Seed completed torrents until share ratio reaches RATIO. You are strongly encouraged
        # to specify equals or more than 1.0 here. Specify 0.0 if you intend to do seeding regardless of
        # share ratio. If --seed-time option is specified along with this option, seeding ends when at least one of
        # the conditions is satisfied. Default: 1.0

    @property
    def seed_time(self):
        return self._struct.get("seed-time")

    @seed_time.setter
    def seed_time(self, value):
        if self.api.change_option({"seed-time": value}, self.gid):
            self._struct["seed-time"] = value

        # =<MINUTES>
        #
        # Specify seeding time in (fractional) minutes. Also see the --seed-ratio option.
        #
        # NOTE:
        #    Specifying --seed-time=0 disables seeding after download completed.

    @property
    def torrent_file(self):
        return self._struct.get("torrent-file")

    @torrent_file.setter
    def torrent_file(self, value):
        if self.api.change_option({"torrent-file": value}, self.gid):
            self._struct["torrent-file"] = value

        # =<TORRENT_FILE>
        #
        # The path to the ".torrent" file. You are not required to use this option because you can specify ".torrent"
        # files without --torrent-file.

        # Metalink Specific Options

    @property
    def follow_metalink(self):
        return self._struct.get("follow-metalink")

    @follow_metalink.setter
    def follow_metalink(self, value):
        if self.api.change_option({"follow-metalink": value}, self.gid):
            self._struct["follow-metalink"] = value

        # =true|false|mem
        #
        # If true or mem is specified, when a file whose suffix is .meta4 or .metalink or content type of
        # application/metalink4+xml or application/metalink+xml is downloaded, aria2 parses it as a metalink
        # file and downloads files mentioned in it. If mem is specified, a metalink file is not written to the disk,
        # but is just kept in memory. If false is specified, the .metalink file is downloaded to the disk,
        # but is not parsed as a metalink file and its contents are not downloaded. Default: true

    @property
    def metalink_base_uri(self):
        return self._struct.get("metalink-base-uri")

    @metalink_base_uri.setter
    def metalink_base_uri(self, value):
        if self.api.change_option({"metalink-base-uri": value}, self.gid):
            self._struct["metalink-base-uri"] = value

        # =<URI>
        #
        # Specify base URI to resolve relative URI in metalink:url and metalink:metaurl element in a metalink
        # file stored in local disk. If URI points to a directory, URI must end with /.

    @property
    def metalink_file(self):
        return self._struct.get("metalink-file")

    @metalink_file.setter
    def metalink_file(self, value):
        if self.api.change_option({"metalink-file": value}, self.gid):
            self._struct["metalink-file"] = value

        # =<METALINK_FILE>
        #
        # The file path to ".meta4" and ".metalink" file. Reads input from stdin when - is specified. You are not
        # required to use this option because you can specify ".metalink" files without --metalink-file.

    @property
    def metalink_language(self):
        return self._struct.get("metalink-language")

    @metalink_language.setter
    def metalink_language(self, value):
        if self.api.change_option({"metalink-language": value}, self.gid):
            self._struct["metalink-language"] = value

        # =<LANGUAGE>
        #
        # The language of the file to download.

    @property
    def metalink_location(self):
        return self._struct.get("metalink-location")

    @metalink_location.setter
    def metalink_location(self, value):
        if self.api.change_option({"metalink-location": value}, self.gid):
            self._struct["metalink-location"] = value

        # =<LOCATION>[,...]
        #
        # The location of the preferred server. A comma-delimited list of locations is acceptable, for example, jp,us.

    @property
    def metalink_os(self):
        return self._struct.get("metalink-os")

    @metalink_os.setter
    def metalink_os(self, value):
        if self.api.change_option({"metalink-os": value}, self.gid):
            self._struct["metalink-os"] = value

        # =<OS>
        #
        # The operating system of the file to download.

    @property
    def metalink_version(self):
        return self._struct.get("metalink-version")

    @metalink_version.setter
    def metalink_version(self, value):
        if self.api.change_option({"metalink-version": value}, self.gid):
            self._struct["metalink-version"] = value

        # =<VERSION>
        #
        # The version of the file to download.

    @property
    def metalink_preferred_protocol(self):
        return self._struct.get("metalink-preferred-protocol")

    @metalink_preferred_protocol.setter
    def metalink_preferred_protocol(self, value):
        if self.api.change_option({"metalink-preferred-protocol": value}, self.gid):
            self._struct["metalink-preferred-protocol"] = value

        # =<PROTO>
        #
        # Specify preferred protocol. The possible values are http, https, ftp and none. Specify none to disable this
        # feature. Default: none

    @property
    def metalink_enable_unique_protocol(self):
        return self._struct.get("metalink_enable_unique_protocol")

    @metalink_enable_unique_protocol.setter
    def metalink_enable_unique_protocol(self, value):
        if self.api.change_option({"metalink_enable_unique_protocol": value}, self.gid):
            self._struct["metalink_enable_unique_protocol"] = value

        # [=true|false]
        #
        # If true is given and several protocols are available for a mirror in a metalink file, aria2 uses one of
        # them. Use --metalink-preferred-protocol option to specify the preference of protocol. Default: true

        # RPC Options

    @property
    def enable_rpc(self):
        return self._struct.get("enable-rpc")

    @enable_rpc.setter
    def enable_rpc(self, value):
        if self.api.change_option({"enable-rpc": value}, self.gid):
            self._struct["enable-rpc"] = value

        # [=true|false]
        #
        # Enable JSON-RPC/XML-RPC server. It is strongly recommended to set secret authorization token using
        # --rpc-secret option. See also --rpc-listen-port option. Default: false

    @property
    def pause(self):
        return self._struct.get("pause")

    @pause.setter
    def pause(self, value):
        if self.api.change_option({"pause": value}, self.gid):
            self._struct["pause"] = value

        # [=true|false]
        #
        # Pause download after added. This option is effective only when --enable-rpc=true is given. Default: false

    @property
    def pause_metadata(self):
        return self._struct.get("pause-metadata")

    @pause_metadata.setter
    def pause_metadata(self, value):
        if self.api.change_option({"pause-metadata": value}, self.gid):
            self._struct["pause-metadata"] = value

        # [=true|false]
        #
        # Pause downloads created as a result of metadata download. There are 3 types of metadata downloads in
        # aria2: (1) downloading .torrent file. (2) downloading torrent metadata using magnet link. (3) downloading
        # metalink file. These metadata downloads will generate downloads using their metadata. This option pauses
        # these subsequent downloads. This option is effective only when --enable-rpc=true is given. Default: false

    @property
    def rpc_allow_origin_all(self):
        return self._struct.get("rpc-allow-origin-all")

    @rpc_allow_origin_all.setter
    def rpc_allow_origin_all(self, value):
        if self.api.change_option({"rpc-allow-origin-all": value}, self.gid):
            self._struct["rpc-allow-origin-all"] = value

        # [=true|false]
        #
        # Add Access-Control-Allow-Origin header field with value * to the RPC response. Default: false

    @property
    def rpc_certificate(self):
        return self._struct.get("rpc-certificate")

    @rpc_certificate.setter
    def rpc_certificate(self, value):
        if self.api.change_option({"rpc-certificate": value}, self.gid):
            self._struct["rpc-certificate"] = value

        # =<FILE>
        #
        # Use the certificate in FILE for RPC server. The certificate must be either in PKCS12 (.p12, .pfx) or in PEM
        # format.
        #
        # PKCS12 files must contain the certificate, a key and optionally a chain of additional certificates. Only
        # PKCS12 files with a blank import password can be opened!
        #
        # When using PEM, you have to specify the private key via --rpc-private-key as well. Use --rpc-secure option
        # to enable encryption.
        #
        # NOTE:
        #    WinTLS does not support PEM files at the moment. Users have to use PKCS12 files.
        #
        # NOTE:

        #     AppleTLS users should use the KeyChain Access utility to first generate a self-signed SSL-Server
        #     certificate, e.g. using the wizard, and get the SHA-1 fingerprint from the Information dialog
        #     corresponding to that new certificate. To start aria2c with --rpc-secure use --rpc-certifi‐
        #     cate=<SHA-1>. Alternatively PKCS12 files are also supported. PEM files, however, are not supported.

    @property
    def rpc_listen_all(self):
        return self._struct.get("rpc-listen-all")

    @rpc_listen_all.setter
    def rpc_listen_all(self, value):
        if self.api.change_option({"rpc-listen-all": value}, self.gid):
            self._struct["rpc-listen-all"] = value

        # [=true|false]
        #
        # Listen incoming JSON-RPC/XML-RPC requests on all network interfaces. If false is given, listen only on
        # local loopback interface. Default: false

    @property
    def rpc_listen_port(self):
        return self._struct.get("rpc-listen-port")

    @rpc_listen_port.setter
    def rpc_listen_port(self, value):
        if self.api.change_option({"rpc-listen-port": value}, self.gid):
            self._struct["rpc-listen-port"] = value

        # =<PORT>
        #
        # Specify a port number for JSON-RPC/XML-RPC server to listen to. Possible Values: 1024 -65535 Default: 6800

    @property
    def rpc_max_request_size(self):
        return self._struct.get("rpc-max-request-size")

    @rpc_max_request_size.setter
    def rpc_max_request_size(self, value):
        if self.api.change_option({"rpc-max-request-size": value}, self.gid):
            self._struct["rpc-max-request-size"] = value

        # =<SIZE>
        #
        # Set max size of JSON-RPC/XML-RPC request. If aria2 detects the request is more than SIZE bytes,
        # it drops connection. Default: 2M

    @property
    def rpc_passwd(self):
        return self._struct.get("rpc-passwd")

    @rpc_passwd.setter
    def rpc_passwd(self, value):
        if self.api.change_option({"rpc-passwd": value}, self.gid):
            self._struct["rpc-passwd"] = value

        # =<PASSWD>
        #
        # Set JSON-RPC/XML-RPC password.
        #
        # WARNING:
        #     --rpc-passwd option will be deprecated in the future release. Migrate to --rpc-secret option as soon as
        #     possible.

    @property
    def rpc_private_key(self):
        return self._struct.get("rpc-private-key")

    @rpc_private_key.setter
    def rpc_private_key(self, value):
        if self.api.change_option({"rpc-private-key": value}, self.gid):
            self._struct["rpc-private-key"] = value

        # =<FILE>
        #
        # Use the private key in FILE for RPC server. The private key must be decrypted and in PEM format. Use
        # --rpc-secure option to enable encryption. See also --rpc-certificate option.

    @property
    def rpc_save_upload_metadata(self):
        return self._struct.get("rpc-save-upload-metadata")

    @rpc_save_upload_metadata.setter
    def rpc_save_upload_metadata(self, value):
        if self.api.change_option({"rpc-save-upload-metadata": value}, self.gid):
            self._struct["rpc-save-upload-metadata"] = value

        # [=true|false]
        #
        # Save the uploaded torrent or metalink meta data in the directory specified by --dir option. The file
        # name consists of SHA-1 hash hex string of meta data plus extension. For torrent, the extension is
        # '.torrent'. For metalink, it is '.meta4'. If false is given to this option, the downloads added by
        # aria2.addTorrent() or aria2.addMetalink() will not be saved by --save-session option. Default: true

    @property
    def rpc_secret(self):
        return self._struct.get("rpc-secret")

    @rpc_secret.setter
    def rpc_secret(self, value):
        if self.api.change_option({"rpc-secret": value}, self.gid):
            self._struct["rpc-secret"] = value

        # =<TOKEN>
        #
        # Set RPC secret authorization token. Read RPC authorization secret token to know how this option value is used.

    @property
    def rpc_secure(self):
        return self._struct.get("rpc-secure")

    @rpc_secure.setter
    def rpc_secure(self, value):
        if self.api.change_option({"rpc-secure": value}, self.gid):
            self._struct["rpc-secure"] = value

        # [=true|false]
        #
        # RPC transport will be encrypted by SSL/TLS. The RPC clients must use https scheme to access the
        # server. For WebSocket client, use wss scheme. Use --rpc-certificate and --rpc-private-key options to
        # specify the server certificate and private key.

    @property
    def rpc_user(self):
        return self._struct.get("rpc-user")

    @rpc_user.setter
    def rpc_user(self, value):
        if self.api.change_option({"rpc-user": value}, self.gid):
            self._struct["rpc-user"] = value

        # =<USER>
        #
        # Set JSON-RPC/XML-RPC user.
        #
        # WARNING:
        #     --rpc-user option will be deprecated in the future release. Migrate to --rpc-secret option as soon as
        #     possible.

        # Advanced Options

    @property
    def allow_overwrite(self):
        return self._struct.get("allow-overwrite")

    @allow_overwrite.setter
    def allow_overwrite(self, value):
        if self.api.change_option({"allow-overwrite": value}, self.gid):
            self._struct["allow-overwrite"] = value

        # [=true|false]
        #
        # Restart download from scratch if the corresponding control file doesn't exist. See also
        # --auto-file-renaming option. Default: false

    @property
    def allow_piece_length_change(self):
        return self._struct.get("allow-piece-length-change")

    @allow_piece_length_change.setter
    def allow_piece_length_change(self, value):
        if self.api.change_option({"allow-piece-length-change": value}, self.gid):
            self._struct["allow-piece-length-change"] = value

        # [=true|false]
        #
        # If false is given, aria2 aborts download when a piece length is different from one in a control file. If
        # true is given, you can proceed but some download progress will be lost. Default: false

    @property
    def always_resume(self):
        return self._struct.get("always-resume")

    @always_resume.setter
    def always_resume(self, value):
        if self.api.change_option({"always-resume": value}, self.gid):
            self._struct["always-resume"] = value

        # [=true|false]
        #
        # Always resume download. If true is given, aria2 always tries to resume download and if resume is not
        # possible, aborts download. If false is given, when all given URIs do not support resume or aria2
        # encounters N URIs which does not support resume (N is the value specified using
        # --max-resume-failure-tries option), aria2 downloads file from scratch. See --max-resume-failure-tries
        # option. Default: true

    @property
    def async_dns(self):
        return self._struct.get("async-dns")

    @async_dns.setter
    def async_dns(self, value):
        if self.api.change_option({"async-dns": value}, self.gid):
            self._struct["async-dns"] = value

        # [=true|false]
        #
        # Enable asynchronous DNS. Default: true

    @property
    def async_dns_server(self):
        return self._struct.get("async-dns-server")

    @async_dns_server.setter
    def async_dns_server(self, value):
        if self.api.change_option({"async-dns-server": value}, self.gid):
            self._struct["async-dns-server"] = value

        # =<IPADDRESS>[,...]
        #
        # Comma separated list of DNS server address used in asynchronous DNS resolver. Usually asynchronous
        # DNS resolver reads DNS server addresses from /etc/resolv.conf. When this option is used, it uses DNS
        # servers specified in this option instead of ones in /etc/resolv.conf. You can specify both IPv4 and IPv6
        # address. This option is useful when the system does not have /etc/resolv.conf and user does not have the
        # permission to create it.

    @property
    def auto_file_renaming(self):
        return self._struct.get("auto-file-renaming")

    @auto_file_renaming.setter
    def auto_file_renaming(self, value):
        if self.api.change_option({"auto-file-renaming": value}, self.gid):
            self._struct["auto-file-renaming"] = value

        # [=true|false]
        #
        # Rename file name if the same file already exists. This option works only in HTTP(S)/FTP download. The new
        # file name has a dot and a number(1..9999) appended after the name, but before the file extension,
        # if any. Default: true

    @property
    def auto_save_interval(self):
        return self._struct.get("auto-save-interval")

    @auto_save_interval.setter
    def auto_save_interval(self, value):
        if self.api.change_option({"auto-save-interval": value}, self.gid):
            self._struct["auto-save-interval"] = value

        # =<SEC>
        #
        # Save a control file(*.aria2) every SEC seconds. If 0 is given, a control file is not saved during download.
        # aria2 saves a control file when it stops regardless of the value. The possible values are between 0 to
        # 600. Default: 60

    @property
    def conditional_get(self):
        return self._struct.get("conditional-get")

    @conditional_get.setter
    def conditional_get(self, value):
        if self.api.change_option({"conditional-get": value}, self.gid):
            self._struct["conditional-get"] = value

        # [=true|false]
        #
        # Download file only when the local file is older than remote file. This function only works with HTTP(S)
        # downloads only. It does not work if file size is specified in Metalink. It also ignores Content-Disposition
        # header. If a control file exists, this option will be ignored. This function uses If-Modified-Since
        # header to get only newer file conditionally. When getting modification time of local file, it uses user
        # supplied file name (see --out option) or file name part in URI if --out is not specified. To overwrite
        # existing file, --allow-overwrite is required. Default: false

    @property
    def conf_path(self):
        return self._struct.get("conf-path")

    @conf_path.setter
    def conf_path(self, value):
        if self.api.change_option({"conf-path": value}, self.gid):
            self._struct["conf-path"] = value

        # =<PATH>
        #
        # Change the configuration file path to PATH. Default: $HOME/.aria2/aria2.conf if present, otherwise
        # $XDG_CONFIG_HOME/aria2/aria2.conf.

    @property
    def console_log_level(self):
        return self._struct.get("console-log-level")

    @console_log_level.setter
    def console_log_level(self, value):
        if self.api.change_option({"console-log-level": value}, self.gid):
            self._struct["console-log-level"] = value

        # =<LEVEL>
        #
        # Set log level to output to console. LEVEL is either debug, info, notice, warn or error. Default: notice

    @property
    def daemon(self):
        return self._struct.get("daemon")

    @daemon.setter
    def daemon(self, value):
        if self.api.change_option({"daemon": value}, self.gid):
            self._struct["daemon"] = value

        # [=true|false]
        #
        # Run as daemon. The current working directory will be changed to / and standard input, standard output
        # and standard error will be redirected to /dev/null. Default: false

    @property
    def deferred_input(self):
        return self._struct.get("deferred-input")

    @deferred_input.setter
    def deferred_input(self, value):
        if self.api.change_option({"deferred-input": value}, self.gid):
            self._struct["deferred-input"] = value

        # [=true|false]
        #
        # If true is given, aria2 does not read all URIs and options from file specified by --input-file option at
        # startup, but it reads one by one when it needs later. This may reduce memory usage if input file contains a
        # lot of URIs to download. If false is given, aria2 reads all URIs and options at startup. Default: false
        #
        # WARNING:
        #    --deferred-input option will be disabled when --save-session is used together.

    @property
    def disable_ipv6(self):
        return self._struct.get("disable-ipv6")

    @disable_ipv6.setter
    def disable_ipv6(self, value):
        if self.api.change_option({"disable-ipv6": value}, self.gid):
            self._struct["disable-ipv6"] = value

        # [=true|false]
        #
        # Disable IPv6. This is useful if you have to use broken DNS and want to avoid terribly slow AAAA record
        # lookup. Default: false

    @property
    def disk_cache(self):
        return self._struct.get("disk-cache")

    @disk_cache.setter
    def disk_cache(self, value):
        if self.api.change_option({"disk-cache": value}, self.gid):
            self._struct["disk-cache"] = value

        # =<SIZE>
        #
        # Enable disk cache. If SIZE is 0, the disk cache is disabled. This feature caches the downloaded data in
        # memory, which grows to at most SIZE bytes. The cache storage is created for aria2 instance and shared by
        # all downloads. The one advantage of the disk cache is reduce the disk I/O because the data are written
        # in larger unit and it is reordered by the offset of the file. If hash checking is involved and the data
        # are cached in memory, we don't need to read them from the disk. SIZE can include K or M (1K = 1024,
        # 1M = 1024K). Default: 16M

    @property
    def download_result(self):
        return self._struct.get("download-result")

    @download_result.setter
    def download_result(self, value):
        if self.api.change_option({"download-result": value}, self.gid):
            self._struct["download-result"] = value

        # =<OPT>
        #
        # This option changes the way Download Results is formatted. If OPT is default, print GID, status,
        # average download speed and path/URI. If multiple files are involved, path/URI of first requested file is
        # printed and remaining ones are omitted. If OPT is full, print GID, status, average download speed,
        # percentage of progress and path/URI. The percentage of progress and path/URI are printed for each requested
        # file in each row. If OPT is hide, Download Results is hidden. Default: default

    @property
    def dscp(self):
        return self._struct.get("dscp")

    @dscp.setter
    def dscp(self, value):
        if self.api.change_option({"dscp": value}, self.gid):
            self._struct["dscp"] = value

        # =<DSCP>
        #
        # Set DSCP value in outgoing IP packets of BitTorrent traffic for QoS. This parameter sets only DSCP
        # bits in TOS field of IP packets, not the whole field. If you take values from /usr/include/netinet/ip.h
        # divide them by 4 (otherwise values would be incorrect, e.g. your CS1 class would turn into CS4). If you
        # take commonly used values from RFC, network vendors' documentation, Wikipedia or any other source,
        # use them as they are.

    @property
    def rlimit_nofile(self):
        return self._struct.get("rlimit-nofile")

    @rlimit_nofile.setter
    def rlimit_nofile(self, value):
        if self.api.change_option({"rlimit-nofile": value}, self.gid):
            self._struct["rlimit-nofile"] = value

        # =<NUM>
        #
        # Set the soft limit of open file descriptors. This open will only have effect when:
        #
        #    a. The system supports it (posix)
        #
        #    b. The limit does not exceed the hard limit.
        #
        #    c. The specified limit is larger than the current soft limit.
        #
        # This is equivalent to setting nofile via ulimit, except that it will never decrease the limit.
        #
        # This option is only available on systems supporting the rlimit API.

    @property
    def enable_color(self):
        return self._struct.get("enable-color")

    @enable_color.setter
    def enable_color(self, value):
        if self.api.change_option({"enable-color": value}, self.gid):
            self._struct["enable-color"] = value

        # [=true|false]
        #
        # Enable color output for a terminal. Default: true

    @property
    def enable_mmap(self):
        return self._struct.get("enable-mmap")

    @enable_mmap.setter
    def enable_mmap(self, value):
        if self.api.change_option({"enable-mmap": value}, self.gid):
            self._struct["enable-mmap"] = value

        # [=true|false]
        #
        # Map files into memory. This option may not work if the file space is not pre-allocated. See --file-allocation.
        #
        # Default: false

    @property
    def event_poll(self):
        return self._struct.get("event-poll")

    @event_poll.setter
    def event_poll(self, value):
        if self.api.change_option({"event-poll": value}, self.gid):
            self._struct["event-poll"] = value

        # =<POLL>
        #
        # Specify the method for polling events. The possible values are epoll, kqueue, port, poll and select.
        # For each epoll, kqueue, port and poll, it is available if system supports it. epoll is available on recent
        # Linux. kqueue is available on various *BSD systems including Mac OS X. port is available on Open Solaris.
        # The default value may vary depending on the system you use.

    @property
    def file_allocation(self):
        return self._struct.get("file-allocation")

    @file_allocation.setter
    def file_allocation(self, value):
        if self.api.change_option({"file-allocation": value}, self.gid):
            self._struct["file-allocation"] = value

        # =<METHOD>
        #
        # Specify file allocation method. none doesn't pre-allocate file space. prealloc pre-allocates file space
        # before download begins. This may take some time depending on the size of the file. If you are using newer
        # file systems such as ext4 (with extents support), btrfs, xfs or NTFS(MinGW build only), falloc is your
        # best choice. It allocates large(few GiB) files almost instantly. Don't use falloc with legacy file
        # systems such as ext3 and FAT32 because it takes almost same time as prealloc and it blocks aria2 entirely
        # until allocation finishes. falloc may not be available if your system doesn't have
        # posix_fallocate(3)  function. trunc uses ftruncate(2) system call or platform-specific counterpart to
        # truncate a file to a specified length.
        #
        # Possible Values: none, prealloc, trunc, falloc Default: prealloc
        #
        # WARNING:
        #     Using trunc seemingly allocates disk space very quickly, but what it actually does is that it sets file
        #     length metadata in file system, and does not allocate disk space at all. This means that it does not help
        #     avoiding fragmentation.
        #
        # NOTE:
        #     In multi file torrent downloads, the files adjacent forward to the specified files are also allocated if
        #     they share the same piece.

    @property
    def force_save(self):
        return self._struct.get("force-save")

    @force_save.setter
    def force_save(self, value):
        if self.api.change_option({"force-save": value}, self.gid):
            self._struct["force-save"] = value

        # [=true|false]
        #
        # Save download with --save-session option even if the download is completed or removed. This option also
        # saves control file in that situations. This may be useful to save BitTorrent seeding which is recognized as
        # completed state. Default: false

    @property
    def save_not_found(self):
        return self._struct.get("save-not-found")

    @save_not_found.setter
    def save_not_found(self, value):
        if self.api.change_option({"save-not-found": value}, self.gid):
            self._struct["save-not-found"] = value

        # [=true|false]
        #
        # Save download with --save-session option even if the file was not found on the server. This option also
        # saves control file in that situations. Default: true

    @property
    def gid(self):
        return self._struct.get("gid")

    @gid.setter
    def gid(self, value):
        if self.api.change_option({"gid": value}, self.gid):
            self._struct["gid"] = value

        # =<GID>
        #
        # Set GID manually. aria2 identifies each download by the ID called GID. The GID must be hex string of 16
        # characters, thus [0-9a-zA-Z] are allowed and leading zeros must not be stripped. The GID all 0 is reserved
        # and must not be used. The GID must be unique, otherwise error is reported and the download is not
        # added. This option is useful when restoring the sessions saved using --save-session option. If this option
        # is not used, new GID is generated by aria2.

    @property
    def hash_check_only(self):
        return self._struct.get("hash-check-only")

    @hash_check_only.setter
    def hash_check_only(self, value):
        if self.api.change_option({"hash-check-only": value}, self.gid):
            self._struct["hash-check-only"] = value

        # [=true|false]
        #
        # If true is given, after hash check using --check-integrity option, abort download whether or not download
        # is complete. Default: false

    @property
    def human_readable(self):
        return self._struct.get("human-readable")

    @human_readable.setter
    def human_readable(self, value):
        if self.api.change_option({"human-readable": value}, self.gid):
            self._struct["human-readable"] = value

        # [=true|false]
        #
        # Print sizes and speed in human readable format (e.g., 1.2Ki, 3.4Mi) in the console readout. Default: true

    @property
    def interface(self):
        return self._struct.get("interface")

    @interface.setter
    def interface(self, value):
        if self.api.change_option({"interface": value}, self.gid):
            self._struct["interface"] = value

        # =<INTERFACE>
        #
        # Bind sockets to given interface. You can specify interface name, IP address and host name. Possible Values:
        # interface, IP address, host name
        #
        # NOTE:
        #     If an interface has multiple addresses, it is highly recommended to specify IP address explicitly. See
        #     also --disable-ipv6. If your system doesn't have getifaddrs(3), this option doesn't accept interface
        #     name.

    @property
    def keep_unfinished_download_result(self):
        return self._struct.get("keep_unfinished_download_result")

    @keep_unfinished_download_result.setter
    def keep_unfinished_download_result(self, value):
        if self.api.change_option({"keep_unfinished_download_result": value}, self.gid):
            self._struct["keep_unfinished_download_result"] = value

        # [=true|false]
        #
        # Keep unfinished download results even if doing so exceeds --max-download-result. This is useful if all
        # unfinished downloads must be saved in session file (see --save-session option). Please keep in mind that
        # there is no upper bound to the number of unfinished download result to keep. If that is undesirable,
        # turn this option off. Default: true

    @property
    def max_download_result(self):
        return self._struct.get("max-download-result")

    @max_download_result.setter
    def max_download_result(self, value):
        if self.api.change_option({"max-download-result": value}, self.gid):
            self._struct["max-download-result"] = value

        # =<NUM>
        #
        # Set maximum number of download result kept in memory. The download results are completed/error/removed
        # downloads. The download results are stored in FIFO queue and it can store at most NUM download results.
        # When queue is full and new download result is created, oldest download result is removed from the front of
        # the queue and new one is pushed to the back. Setting big number in this option may result high memory
        # consumption after thousands of downloads. Specifying 0 means no download result is kept. Note that
        # unfinished downloads are kept in memory regardless of this option value. See
        # --keep-unfinished-download-result option. Default: 1000

    @property
    def max_mmap_limit(self):
        return self._struct.get("max-mmap-limit")

    @max_mmap_limit.setter
    def max_mmap_limit(self, value):
        if self.api.change_option({"max-mmap-limit": value}, self.gid):
            self._struct["max-mmap-limit"] = value

        # =<SIZE>
        #
        # Set the maximum file size to enable mmap (see --enable-mmap option). The file size is determined by the sum
        # of all files contained in one download. For example, if a download contains 5 files, then file size is the
        # total size of those files. If file size is strictly greater than the size specified in this option,
        # mmap will be disabled. Default: 9223372036854775807

    @property
    def max_resume_failure_tries(self):
        return self._struct.get("max-resume-failure-tries")

    @max_resume_failure_tries.setter
    def max_resume_failure_tries(self, value):
        if self.api.change_option({"max-resume-failure-tries": value}, self.gid):
            self._struct["max-resume-failure-tries"] = value

        # =<N>
        #
        # When used with --always-resume=false, aria2 downloads file from scratch when aria2 detects N number of
        # URIs that does not support resume. If N is 0, aria2 downloads file from scratch when all given URIs do not
        # support resume. See --always-resume option. Default: 0

    @property
    def min_tls_version(self):
        return self._struct.get("min-tls-version")

    @min_tls_version.setter
    def min_tls_version(self, value):
        if self.api.change_option({"min-tls-version": value}, self.gid):
            self._struct["min-tls-version"] = value

        # =<VERSION>
        #
        # Specify minimum SSL/TLS version to enable. Possible Values: SSLv3, TLSv1, TLSv1.1, TLSv1.2 Default: TLSv1

    @property
    def multiple_interface(self):
        return self._struct.get("multiple-interface")

    @multiple_interface.setter
    def multiple_interface(self, value):
        if self.api.change_option({"multiple-interface": value}, self.gid):
            self._struct["multiple-interface"] = value

        # =<INTERFACES>
        #
        # Comma separated list of interfaces to bind sockets to. Requests will be splited among the interfaces to
        # achieve link aggregation. You can specify interface name, IP address and hostname. If --interface is
        # used, this option will be ignored. Possible Values: interface, IP address, hostname

    @property
    def log_level(self):
        return self._struct.get("log-level")

    @log_level.setter
    def log_level(self, value):
        if self.api.change_option({"log-level": value}, self.gid):
            self._struct["log-level"] = value

        # =<LEVEL>
        #
        # Set log level to output. LEVEL is either debug, info, notice, warn or error. Default: debug

    @property
    def on_bt_download_complete(self):
        return self._struct.get("on-bt-download-complete")

    @on_bt_download_complete.setter
    def on_bt_download_complete(self, value):
        if self.api.change_option({"on-bt-download-complete": value}, self.gid):
            self._struct["on-bt-download-complete"] = value

        # =<COMMAND>
        #
        # For BitTorrent, a command specified in --on-download-complete is called after download completed and
        # seeding is over. On the other hand, this option set the command to be executed after download completed but
        # before seeding. See Event Hook for more details about COMMAND. Possible Values: /path/to/command

    @property
    def on_download_complete(self):
        return self._struct.get("on-download-complete")

    @on_download_complete.setter
    def on_download_complete(self, value):
        if self.api.change_option({"on-download-complete": value}, self.gid):
            self._struct["on-download-complete"] = value

        # =<COMMAND>
        #
        # Set the command to be executed after download completed. See See Event Hook for more details about COMMAND.
        # See also --on-download-stop option. Possible Values: /path/to/command

    @property
    def on_download_error(self):
        return self._struct.get("on-download-error")

    @on_download_error.setter
    def on_download_error(self, value):
        if self.api.change_option({"on-download-error": value}, self.gid):
            self._struct["on-download-error"] = value

        # =<COMMAND>
        #
        # Set the command to be executed after download aborted due to error. See Event Hook for more details
        # about COMMAND. See also --on-download-stop option. Possible Values: /path/to/command

    @property
    def on_download_pause(self):
        return self._struct.get("on-download-pause")

    @on_download_pause.setter
    def on_download_pause(self, value):
        if self.api.change_option({"on-download-pause": value}, self.gid):
            self._struct["on-download-pause"] = value

        # =<COMMAND>
        #
        # Set the command to be executed after download was paused. See Event Hook for more details about COMMAND.
        # Possible Values: /path/to/command

    @property
    def on_download_start(self):
        return self._struct.get("on-download-start")

    @on_download_start.setter
    def on_download_start(self, value):
        if self.api.change_option({"on-download-start": value}, self.gid):
            self._struct["on-download-start"] = value

        # =<COMMAND>
        #
        # Set the command to be executed after download got started. See Event Hook for more details about COMMAND.
        # Possible Values: /path/to/command

    @property
    def on_download_stop(self):
        return self._struct.get("on-download-stop")

    @on_download_stop.setter
    def on_download_stop(self, value):
        if self.api.change_option({"on-download-stop": value}, self.gid):
            self._struct["on-download-stop"] = value

        # =<COMMAND>
        #
        # Set the command to be executed after download stopped. You can override the command to be
        # executed for particular download result using --on-download-complete and --on-download-error. If they are
        # specified, command specified in this option is not executed. See Event Hook for more details about
        # COMMAND. Possible Values: /path/to/command

    @property
    def optimize_concurrent_downloads(self):
        return self._struct.get("optimize-concurrent-downloads")

    @optimize_concurrent_downloads.setter
    def optimize_concurrent_downloads(self, value):
        if self.api.change_option({"optimize-concurrent-downloads": value}, self.gid):
            self._struct["optimize-concurrent-downloads"] = value

        # [=true|false|<A>:<B>]
        #
        # Optimizes the number of concurrent downloads according to the bandwidth available. aria2 uses the download
        # speed observed in the previous downloads to adapt the number of downloads launched in parallel according to
        # the rule N = A + B Log10(speed in Mbps). The coefficients A and B can be customized in the option
        # arguments with A and B separated by a colon. The default values (A=5, B=25) lead to using typically 5
        # parallel downloads on 1Mbps networks and above 50 on 100Mbps networks. The number of parallel downloads
        # remains constrained under the maximum defined by the --max-concurrent-downloads parameter. Default:
        # false

    @property
    def piece_length(self):
        return self._struct.get("piece-length")

    @piece_length.setter
    def piece_length(self, value):
        if self.api.change_option({"piece-length": value}, self.gid):
            self._struct["piece-length"] = value

        # =<LENGTH>
        #
        # Set a piece length for HTTP/FTP downloads. This is the boundary when aria2 splits a file. All splits occur
        # at multiple of this length. This option will be ignored in BitTorrent downloads. It will be also ignored if
        # Metalink file contains piece hashes. Default: 1M
        #
        # NOTE:
        #     The possible use case of --piece-length option is change the request range in one HTTP pipelined
        #     request. To enable HTTP pipelining use --enable-http-pipelining.

    @property
    def show_console_readout(self):
        return self._struct.get("show-console-readout")

    @show_console_readout.setter
    def show_console_readout(self, value):
        if self.api.change_option({"show-console-readout": value}, self.gid):
            self._struct["show-console-readout"] = value

        # [=true|false]
        #
        # Show console readout. Default: true

    @property
    def stderr(self):
        return self._struct.get("stderr")

    @stderr.setter
    def stderr(self, value):
        if self.api.change_option({"stderr": value}, self.gid):
            self._struct["stderr"] = value

        # [=true|false]
        #
        # Redirect all console output that would be otherwise printed in stdout to stderr. Default: false

    @property
    def summary_interval(self):
        return self._struct.get("summary-interval")

    @summary_interval.setter
    def summary_interval(self, value):
        if self.api.change_option({"summary-interval": value}, self.gid):
            self._struct["summary-interval"] = value

        # =<SEC>
        #
        # Set interval in seconds to output download progress summary. Setting 0 suppresses the output. Default: 60

    @property
    def force_sequential(self):
        return self._struct.get("force-sequential")

    @force_sequential.setter
    def force_sequential(self, value):
        if self.api.change_option({"force-sequential": value}, self.gid):
            self._struct["force-sequential"] = value

        # [=true|false]
        #
        # Fetch URIs in the command-line sequentially and download each URI in a separate session,
        # like the usual command-line download utilities. Default: false

    @property
    def max_overall_download_limit(self):
        return self._struct.get("max-overall-download-limit")

    @max_overall_download_limit.setter
    def max_overall_download_limit(self, value):
        if self.api.change_option({"max-overall-download-limit": value}, self.gid):
            self._struct["max-overall-download-limit"] = value

        # =<SPEED>
        #
        # Set max overall download speed in bytes/sec. 0 means unrestricted. You can append K or M (1K = 1024,
        # 1M = 1024K). To limit the download speed per download, use --max-download-limit option. Default: 0

    @property
    def max_download_limit(self):
        return self._struct.get("max-download-limit")

    @max_download_limit.setter
    def max_download_limit(self, value):
        if self.api.change_option({"max-download-limit": value}, self.gid):
            self._struct["max-download-limit"] = value

        # =<SPEED>
        #
        # Set max download speed per each download in bytes/sec. 0 means unrestricted. You can append K or M (1K
        # = 1024, 1M = 1024K). To limit the overall download speed, use --max-overall-download-limit option. Default: 0

    @property
    def no_conf(self):
        return self._struct.get("no-conf")

    @no_conf.setter
    def no_conf(self, value):
        if self.api.change_option({"no-conf": value}, self.gid):
            self._struct["no-conf"] = value

        # [=true|false]
        #
        # Disable loading aria2.conf file.

    @property
    def no_file_allocation_limit(self):
        return self._struct.get("no-file-allocation-limit")

    @no_file_allocation_limit.setter
    def no_file_allocation_limit(self, value):
        if self.api.change_option({"no-file-allocation-limit": value}, self.gid):
            self._struct["no-file-allocation-limit"] = value

        # =<SIZE>
        #
        # No file allocation is made for files whose size is smaller than SIZE. You can append K or M (1K = 1024,
        # 1M = 1024K). Default: 5M

    @property
    def parameterized_uri(self):
        return self._struct.get("parameterized-uri")

    @parameterized_uri.setter
    def parameterized_uri(self, value):
        if self.api.change_option({"parameterized-uri": value}, self.gid):
            self._struct["parameterized-uri"] = value

        # [=true|false]
        #
        # Enable parameterized URI support. You can specify set of parts: http://{sv1,sv2,sv3}/foo.iso. Also you
        # can specify numeric sequences with step counter:  http://host/image[000-100:2].img. A step counter
        # can be omitted. If all URIs do not point to the same file, such as the second example above, -Z option is
        # required. Default: false

    @property
    def quiet(self):
        return self._struct.get("quiet")

    @quiet.setter
    def quiet(self, value):
        if self.api.change_option({"quiet": value}, self.gid):
            self._struct["quiet"] = value

        # [=true|false]
        #
        # Make aria2 quiet (no console output). Default: false

    @property
    def realtime_chunk_checksum(self):
        return self._struct.get("realtime-chunk-checksum")

    @realtime_chunk_checksum.setter
    def realtime_chunk_checksum(self, value):
        if self.api.change_option({"realtime-chunk-checksum": value}, self.gid):
            self._struct["realtime-chunk-checksum"] = value

        # [=true|false]
        #
        # Validate chunk of data by calculating checksum while downloading a file if chunk checksums are provided.
        # Default: true

    @property
    def remove_control_file(self):
        return self._struct.get("remove-control-file")

    @remove_control_file.setter
    def remove_control_file(self, value):
        if self.api.change_option({"remove-control-file": value}, self.gid):
            self._struct["remove-control-file"] = value

        # [=true|false]
        #
        # Remove control file before download. Using with --allow-overwrite=true, download always starts from
        # scratch. This will be useful for users behind proxy server which disables resume.

    @property
    def save_session(self):
        return self._struct.get("save-session")

    @save_session.setter
    def save_session(self, value):
        if self.api.change_option({"save-session": value}, self.gid):
            self._struct["save-session"] = value

        # =<FILE>
        #
        # Save error/unfinished downloads to FILE on exit. You can pass this output file to aria2c with
        # --input-file option on restart. If you like the output to be gzipped append a .gz extension to the file
        # name. Please note that downloads added by aria2.addTorrent() and aria2.addMetalink() RPC method and whose
        # meta data could not be saved as a file are not saved. Downloads removed using aria2.remove() and
        # aria2.forceRemove() will not be saved. GID is also saved with gid, but there are some restrictions,
        # see below.
        #
        # NOTE:
        #     Normally, GID of the download itself is saved. But some downloads use meta data (e.g., BitTorrent and
        #     Metalink). In this case, there are some restrictions.
        #
        #    magnet URI, and followed by torrent download
        #           GID of BitTorrent meta data download is saved.
        #
        #    URI to torrent file, and followed by torrent download
        #           GID of torrent file download is saved.
        #
        #    URI to metalink file, and followed by file downloads described in metalink file
        #           GID of metalink file download is saved.
        #
        #    local torrent file
        #           GID of torrent download is saved.
        #
        #    local metalink file
        #           Any meaningful GID is not saved.

    @property
    def save_session_interval(self):
        return self._struct.get("save-session-interval")

    @save_session_interval.setter
    def save_session_interval(self, value):
        if self.api.change_option({"save-session-interval": value}, self.gid):
            self._struct["save-session-interval"] = value

        # =<SEC>
        #
        # Save error/unfinished downloads to a file specified by --save-session option every SEC seconds. If 0
        # is given, file will be saved only when aria2 exits. Default: 0

    @property
    def socket_recv_buffer_size(self):
        return self._struct.get("socket-recv-buffer-size")

    @socket_recv_buffer_size.setter
    def socket_recv_buffer_size(self, value):
        if self.api.change_option({"socket-recv-buffer-size": value}, self.gid):
            self._struct["socket-recv-buffer-size"] = value

        # =<SIZE>
        #
        # Set the maximum socket receive buffer in bytes. Specifying 0 will disable this option. This value will
        # be set to socket file descriptor using SO_RCVBUF socket option with setsockopt() call. Default: 0

    @property
    def stop(self):
        return self._struct.get("stop")

    @stop.setter
    def stop(self, value):
        if self.api.change_option({"stop": value}, self.gid):
            self._struct["stop"] = value

        # =<SEC>
        #
        # Stop application after SEC seconds has passed. If 0 is given, this feature is disabled. Default: 0

    @property
    def stop_with_process(self):
        return self._struct.get("stop-with-process")

    @stop_with_process.setter
    def stop_with_process(self, value):
        if self.api.change_option({"stop-with-process": value}, self.gid):
            self._struct["stop-with-process"] = value

        # =<PID>
        #
        # Stop application when process PID is not running. This is useful if aria2 process is forked from a parent
        # process. The parent process can fork aria2 with its own pid and when parent process exits for some reason,
        # aria2 can detect it and shutdown itself.

    @property
    def truncate_console_readout(self):
        return self._struct.get("truncate-console-readout")

    @truncate_console_readout.setter
    def truncate_console_readout(self, value):
        if self.api.change_option({"truncate-console-readout": value}, self.gid):
            self._struct["truncate-console-readout"] = value

        # [=true|false]
        #
        # Truncate console readout to fit in a single line. Default: true