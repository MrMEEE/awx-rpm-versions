%global python3_pkgversion 3.11

%define  debug_package %{nil}
%define _prefix /opt/awx-rpm
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/tower
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX-RPM Web UI
Name: awx-ui
Version: 30.0.0
Release: 1%{dist}
Source0: awx-30.0.0.tar.gz
Source1: settings.py-%{version}
Source2: awx-receiver.service-%{version}
Source3: awx-dispatcher.service-%{version}
Source4: awx-wsrelay.service-%{version}
Source5: awx-ws-heartbeat.service-%{version}
Source6: awx-daphne.service-%{version}
Source7: awx-web.service-%{version}
Source20: awx-receptor.service-%{version}
Source21: awx-receptor-hop.service-%{version}
Source22: awx-receptor-worker.service-%{version}
Source23: awx.target-%{version}
Source30: receptor.conf-%{version}
Source31: receptor-hop.conf-%{version}
Source32: receptor-worker.conf-%{version}
Source40: awx-rpm-logo.svg-%{version}
Source8: awx-rpm-nginx.conf-%{version}
License: GPLv3
Group: AWX
URL: https://awx.wiki
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: make python%{python3_pkgversion} python%{python3_pkgversion}-devel nodejs npm gettext git python%{python3_pkgversion}-build rsync libpq libpq-devel 
BuildRequires: python3.11-adal = 1.2.7
BuildRequires: python3.11-aiodns = 3.2.0
BuildRequires: python3.11-aiohappyeyeballs = 2.4.4
BuildRequires: python3.11-aiohttp = 3.11.11
BuildRequires: python3.11-aiohttp-retry = 2.8.3
BuildRequires: python3.11-aiohttp+speedups = 3.11.11
BuildRequires: python3.11-aiosignal = 1.3.2
BuildRequires: python3.11-ansi2html = 1.9.2
BuildRequires: python3.11-ansible-builder = 3.1.0
BuildRequires: python3.11-anyio = 4.8.0
BuildRequires: python3.11-argon2-cffi = 23.1.0
BuildRequires: python3.11-argon2-cffi-bindings = 21.2.0
BuildRequires: python3.11-asciichartpy = 1.5.25
BuildRequires: python3.11-asgiref = 3.8.1
BuildRequires: python3.11-asn1 = 2.7.1
BuildRequires: python3.11-async-timeout = 5.0.1
BuildRequires: python3.11-attrs = 24.3.0
BuildRequires: python3.11-autobahn = 24.4.2
BuildRequires: python3.11-autocommand = 2.2.2
BuildRequires: python3.11-automat = 24.8.1
BuildRequires: python3.11-awscrt = 0.22.4
BuildRequires: python3.11-azure-core = 1.32.0
BuildRequires: python3.11-azure-core+aio = 1.32.0
BuildRequires: python3.11-azure-identity = 1.19.0
BuildRequires: python3.11-azure-keyvault = 4.2.0
BuildRequires: python3.11-azure-keyvault-certificates = 4.9.0
BuildRequires: python3.11-azure-keyvault-keys = 4.10.0
BuildRequires: python3.11-azure-keyvault-secrets = 4.9.0
BuildRequires: python3.11-babel = 2.17.0
BuildRequires: python3.11-backports-tarfile = 1.2.0
BuildRequires: python3.11-bcrypt = 4.2.1
BuildRequires: python3.11-bcrypt+tests = 4.2.1
BuildRequires: python3.11-bcrypt+typecheck = 4.2.1
BuildRequires: python3.11-bindep = 2.12.0
BuildRequires: python3.11-blinker = 1.9.0
BuildRequires: python3.11-boto3 = 1.35.96
BuildRequires: python3.11-boto3+crt = 1.35.96
BuildRequires: python3.11-botocore = 1.35.96
BuildRequires: python3.11-botocore+crt = 1.35.96
BuildRequires: python3.11-brotli = 1.1.0
BuildRequires: python3.11-build = 1.2.2^post1
BuildRequires: python3.11-cachecontrol = 0.14.2
BuildRequires: python3.11-cachecontrol+filecache = 0.14.2
BuildRequires: python3.11-cachetools = 5.5.0
BuildRequires: python3.11-calver = 2022.6.26
BuildRequires: python3.11-certifi = 2025.1.31
BuildRequires: python3.11-cffi = 1.17.1
BuildRequires: python3.11-changelog-chug = 0.0.3
BuildRequires: python3.11-channels = 4.2.0
BuildRequires: python3.11-channels-redis = 4.2.1
BuildRequires: python3.11-chardet = 5.2.0
BuildRequires: python3.11-charset-normalizer = 3.4.1
BuildRequires: python3.11-cleo = 2.1.0
BuildRequires: python3.11-click = 8.1.8
BuildRequires: python3.11-constantly = 23.10.4
BuildRequires: python3.11-crashtest = 0.4.1
BuildRequires: python3.11-cryptography = 41.0.7
BuildRequires: python3.11-cython = 3.0.11
BuildRequires: python3.11-daphne = 4.1.2
BuildRequires: python3.11-deprecated = 1.2.15
BuildRequires: python3.11-distlib = 0.3.9
BuildRequires: python3.11-distro = 1.9.0
BuildRequires: python3.11-django = 4.2.16
BuildRequires: python3.11-django-ansible-base = 20250131
BuildRequires: python3.11-django+argon2 = 4.2.16
BuildRequires: python3.11-django+bcrypt = 4.2.16
BuildRequires: python3.11-django-cors-headers = 4.6.0
BuildRequires: python3.11-django-crum = 0.7.9
BuildRequires: python3.11-django-extensions = 3.2.3
BuildRequires: python3.11-django-flags = 5.0.13
BuildRequires: python3.11-django-guid = 3.5.0
BuildRequires: python3.11-django-oauth-toolkit = 1.7.1
BuildRequires: python3.11-django-polymorphic = 3.1.0
BuildRequires: python3.11-djangorestframework = 3.15.2
BuildRequires: python3.11-djangorestframework-yaml = 2.0.0
BuildRequires: python3.11-django-solo = 2.4.0
BuildRequires: python3.11-django-split-settings = 1.3.2
BuildRequires: python3.11-docutils = 0.21.2
BuildRequires: python3.11-dulwich = 0.22.7
BuildRequires: python3.11-durationpy = 0.9
BuildRequires: python3.11-enum-compat = 0.0.3
BuildRequires: python3.11-expandvars = 0.12.0
BuildRequires: python3.11-fastjsonschema = 2.21.1
BuildRequires: python3.11-filelock = 3.16.1
BuildRequires: python3.11-findpython = 0.6.2
BuildRequires: python3.11-frozenlist = 1.5.0
BuildRequires: python3.11-gitdb = 4.0.12
BuildRequires: python3.11-gitpython = 3.1.44
BuildRequires: python3.11-googleapis-common-protos = 1.66.0
BuildRequires: python3.11-googleapis-common-protos+grpc = 1.66.0
BuildRequires: python3.11-google-auth = 2.37.0
BuildRequires: python3.11-google-auth+aiohttp = 2.37.0
BuildRequires: python3.11-google-auth+enterprise-cert = 2.37.0
BuildRequires: python3.11-google-auth+pyjwt = 2.37.0
BuildRequires: python3.11-google-auth+pyopenssl = 2.37.0
BuildRequires: python3.11-google-auth+reauth = 2.37.0
BuildRequires: python3.11-google-auth+requests = 2.37.0
BuildRequires: python3.11-graphviz = 0.20.3
BuildRequires: python3.11-grpcio = 1.70.0
BuildRequires: python3.11-h11 = 0.14.0
BuildRequires: python3.11-h2 = 4.2.0
BuildRequires: python3.11-hatch = 1.14.0
BuildRequires: python3.11-hatch-fancy-pypi-readme = 24.1.0
BuildRequires: python3.11-hatchling = 1.27.0
BuildRequires: python3.11-hatch-vcs = 0.4.0
BuildRequires: python3.11-hiredis = 3.1.0
BuildRequires: python3.11-hpack = 4.1.0
BuildRequires: python3.11-httpcore = 1.0.7
BuildRequires: python3.11-httpx = 0.28.1
BuildRequires: python3.11-hyperframe = 6.1.0
BuildRequires: python3.11-hyperlink = 21.0.0
BuildRequires: python3.11-id = 1.5.0
BuildRequires: python3.11-idna = 3.10
BuildRequires: python3.11-importlib-metadata = 8.5.0
BuildRequires: python3.11-importlib-resources = 6.5.2
BuildRequires: python3.11-incremental = 24.7.2
BuildRequires: python3.11-incremental+scripts = 24.7.2
BuildRequires: python3.11-inflection = 0.5.1
BuildRequires: python3.11-installer = 0.7.0
BuildRequires: python3.11-irc = 20.5.0
BuildRequires: python3.11-isodate = 0.7.2
BuildRequires: python3.11-jaraco-classes = 3.4.0
BuildRequires: python3.11-jaraco-collections = 5.1.0
BuildRequires: python3.11-jaraco-context = 6.0.1
BuildRequires: python3.11-jaraco-functools = 4.1.0
BuildRequires: python3.11-jaraco-logging = 3.3.0
BuildRequires: python3.11-jaraco-stream = 3.0.4
BuildRequires: python3.11-jaraco-text = 4.0.0
BuildRequires: python3.11-jeepney = 0.8.0
BuildRequires: python3.11-jinja2 = 3.1.5
BuildRequires: python3.11-jinja2+i18n = 3.1.5
BuildRequires: python3.11-jmespath = 1.0.1
BuildRequires: python3.11-json-log-formatter = 1.1
BuildRequires: python3.11-jsonschema = 4.23.0
BuildRequires: python3.11-jsonschema-specifications = 2024.10.1
BuildRequires: python3.11-jwcrypto = 1.5.6
BuildRequires: python3.11-keyring = 25.6.0
BuildRequires: python3.11-kubernetes = 31.0.0
BuildRequires: python3.11-kubernetes+adal = 31.0.0
BuildRequires: python3.11-lockfile = 0.12.2
BuildRequires: python3.11-markdown = 3.7
BuildRequires: python3.11-markdown-it-py = 3.0.0
BuildRequires: python3.11-markupsafe = 3.0.2
BuildRequires: python3.11-maturin = 1.7.8
BuildRequires: python3.11-mdurl = 0.1.2
BuildRequires: python3.11-more-itertools = 10.5.0
BuildRequires: python3.11-msal = 1.31.1
BuildRequires: python3.11-msal+broker = 1.31.1
BuildRequires: python3.11-msal-extensions = 1.2.0
BuildRequires: python3.11-msgpack = 1.1.0
BuildRequires: python3.11-msrest = 0.7.1
BuildRequires: python3.11-msrest+async = 0.7.1
BuildRequires: python3.11-msrestazure = 0.6.4^post1
BuildRequires: python3.11-multidict = 6.1.0
BuildRequires: python3.11-mypy = 1.14.1
BuildRequires: python3.11-mypy+dmypy = 1.14.1
BuildRequires: python3.11-mypy-extensions = 1.0.0
BuildRequires: python3.11-mypy+faster-cache = 1.14.1
BuildRequires: python3.11-mypy+install-types = 1.14.1
BuildRequires: python3.11-mypy+mypyc = 1.14.1
BuildRequires: python3.11-mypy+reports = 1.14.1
BuildRequires: python3.11-nh3 = 0.2.20
BuildRequires: python3.11-oauthlib = 3.2.2
BuildRequires: python3.11-oauthlib+rsa = 3.2.2
BuildRequires: python3.11-oauthlib+signals = 3.2.2
BuildRequires: python3.11-oauthlib+signedtoken = 3.2.2
BuildRequires: python3.11-openshift = 0.13.2
BuildRequires: python3.11-opentelemetry-api = 1.29.0
BuildRequires: python3.11-opentelemetry-exporter-otlp = 1.29.0
BuildRequires: python3.11-opentelemetry-exporter-otlp-proto-common = 1.29.0
BuildRequires: python3.11-opentelemetry-exporter-otlp-proto-grpc = 1.29.0
BuildRequires: python3.11-opentelemetry-exporter-otlp-proto-http = 1.29.0
BuildRequires: python3.11-opentelemetry-instrumentation = 0.50~b0
BuildRequires: python3.11-opentelemetry-instrumentation-logging = 0.50~b0
BuildRequires: python3.11-opentelemetry-proto = 1.29.0
BuildRequires: python3.11-opentelemetry-sdk = 1.29.0
BuildRequires: python3.11-opentelemetry-semantic-conventions = 0.50~b0
BuildRequires: python3.11-orjson = 3.10.13
BuildRequires: python3.11-packaging = 24.2
BuildRequires: python3.11-parsley = 1.3
BuildRequires: python3.11-pathspec = 0.12.1
BuildRequires: python3.11-pbr = 6.1.0
BuildRequires: python3.11-pbs-installer = 2025.2.12
BuildRequires: python3.11-pbs-installer+all = 2025.2.12
BuildRequires: python3.11-pbs-installer+download = 2025.2.12
BuildRequires: python3.11-pbs-installer+install = 2025.2.12
BuildRequires: python3.11-pdm-backend = 2.4.3
BuildRequires: python3.11-pexpect = 4.9.0
BuildRequires: python3.11-pkgconfig = 1.5.5
BuildRequires: python3.11-pkginfo = 1.12.1.2
BuildRequires: python3.11-platformdirs = 4.3.6
BuildRequires: python3.11-portalocker = 2.10.1
BuildRequires: python3.11-priority = 1.3.0
BuildRequires: python3.11-prometheus-client = 0.21.1
BuildRequires: python3.11-prometheus-client+twisted = 0.21.1
BuildRequires: python3.11-propcache = 0.2.1
BuildRequires: python3.11-protobuf = 5.29.3
BuildRequires: python3.11-psutil = 6.1.1
BuildRequires: python3.11-psycopg = 3.2.3
BuildRequires: python3.11-ptyprocess = 0.7.0
BuildRequires: python3.11-pyasn1-modules = 0.5.1
BuildRequires: python3.11-pycares = 4.5.0
BuildRequires: python3.11-pycares+idna = 4.5.0
BuildRequires: python3.11-pycparser = 2.22
BuildRequires: python3.11-pygerduty = 0.38.3
BuildRequires: python3.11-pygments = 2.19.1
BuildRequires: python3.11-pyjwt = 2.10.1
BuildRequires: python3.11-pyjwt+crypto = 2.10.1
BuildRequires: python3.11-pyopenssl = 24.3.0
BuildRequires: python3.11-pyparsing = 2.4.6
BuildRequires: python3.11-pyproject-hooks = 1.2.0
BuildRequires: python3.11-python-daemon = 3.1.2
BuildRequires: python3.11-python-dateutil = 2.9.0^post0
BuildRequires: python3.11-python-dsv-sdk = 1.0.4
BuildRequires: python3.11-python-string-utils = 1.0.0
BuildRequires: python3.11-pytz = 2024.2
BuildRequires: python3.11-pyu2f = 0.1.5
BuildRequires: python3.11-pyyaml = 6.0.2
BuildRequires: python3.11-pyzstd = 0.16.2
BuildRequires: python3.11-rapidfuzz = 3.9.3
BuildRequires: python3.11-readme-renderer = 44.0
BuildRequires: python3.11-receptorctl = 1.5.2
BuildRequires: python3.11-redis = 5.2.1
BuildRequires: python3.11-referencing = 0.35.1
BuildRequires: python3.11-requests = 2.32.3
BuildRequires: python3.11-requests-oauthlib = 2.0.0
BuildRequires: python3.11-requests-oauthlib+rsa = 2.0.0
BuildRequires: python3.11-requests+socks = 2.32.3
BuildRequires: python3.11-requests-toolbelt = 1.0.0
BuildRequires: python3.11-requests+use-chardet-on-py3 = 2.32.3
BuildRequires: python3.11-rfc3986 = 2.0.0
BuildRequires: python3.11-rich = 13.9.4
BuildRequires: python3.11-rpds-py = 0.22.3
BuildRequires: python3.11-rsa = 4.9
BuildRequires: python3.11-s3transfer = 0.10.4
BuildRequires: python3.11-s3transfer+crt = 0.10.4
BuildRequires: python3.11-scikit-build = 0.17.6
BuildRequires: python3.11-secretstorage = 3.3.3
BuildRequires: python3.11-semantic-version = 2.10.0
BuildRequires: python3.11-semver = 3.0.4
BuildRequires: python3.11-service-identity = 24.2.0
BuildRequires: python3.11-setuptools = 75.8.0
BuildRequires: python3.11-setuptools-rust = 1.10.2
BuildRequires: python3.11-setuptools_scm = 8.1.0
BuildRequires: python3.11-setuptools_scm+toml = 8.1.0
BuildRequires: python3.11-setuptools-twine = 0.1.3
BuildRequires: python3.11-shellingham = 1.5.4
BuildRequires: python3.11-six = 1.17.0
BuildRequires: python3.11-slack-sdk = 3.34.0
BuildRequires: python3.11-smmap = 5.0.2
BuildRequires: python3.11-sniffio = 1.3.1
BuildRequires: python3.11-sqlparse = 0.5.3
BuildRequires: python3.11-tempora = 5.8.0
BuildRequires: python3.11-tomli-w = 1.2.0
BuildRequires: python3.11-tomlkit = 0.13.2
BuildRequires: python3.11-trove-classifiers = 2025.1.15.22
BuildRequires: python3.11-twilio = 9.4.2
BuildRequires: python3.11-twine = 6.1.0
BuildRequires: python3.11-twisted = 24.11.0
BuildRequires: python3.11-twisted+http2 = 24.11.0
BuildRequires: python3.11-twisted+tls = 24.11.0
BuildRequires: python3.11-txaio = 23.1.1
BuildRequires: python3.11-types-psutil = 7.0.0.20250218
BuildRequires: python3.11-types-setuptools = 75.8.0.20250210
BuildRequires: python3.11-typing-extensions = 4.12.2
BuildRequires: python3.11-urllib3 = 2.3.0
BuildRequires: python3.11-urllib3+brotli = 2.3.0
BuildRequires: python3.11-urllib3+h2 = 2.3.0
BuildRequires: python3.11-urllib3+socks = 2.3.0
BuildRequires: python3.11-urllib3+zstd = 2.3.0
BuildRequires: python3.11-userpath = 1.9.2
BuildRequires: python3.11-uv = 0.2.30
BuildRequires: python3.11-uwsgi = 2.0.26
BuildRequires: python3.11-uwsgitop = 0.12
BuildRequires: python3.11-versioneer = 0.29
BuildRequires: python3.11-versioneer+toml = 0.29
BuildRequires: python3.11-virtualenv = 20.29.2
BuildRequires: python3.11-websocket-client = 1.8.0
BuildRequires: python3.11-wrapt = 1.17.0
BuildRequires: python3.11-yarl = 1.18.3
BuildRequires: python3.11-zipp = 3.21.0
BuildRequires: python3.11-zope-interface = 7.2
BuildRequires: python3.11-zstandard = 0.23.0
BuildRequires: python3.11-pyasn1 python3.11-pip python3.11-urllib3 python3.11-pexpect 

#Requires: python%{python3_pkgversion} nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 
Requires: python%{python3_pkgversion} nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq
Requires: python3.11-adal = 1.2.7
Requires: python3.11-aiodns = 3.2.0
Requires: python3.11-aiohappyeyeballs = 2.4.4
Requires: python3.11-aiohttp = 3.11.11
Requires: python3.11-aiohttp-retry = 2.8.3
Requires: python3.11-aiohttp+speedups = 3.11.11
Requires: python3.11-aiosignal = 1.3.2
Requires: python3.11-ansi2html = 1.9.2
Requires: python3.11-ansible-builder = 3.1.0
Requires: python3.11-anyio = 4.8.0
Requires: python3.11-argon2-cffi = 23.1.0
Requires: python3.11-argon2-cffi-bindings = 21.2.0
Requires: python3.11-asciichartpy = 1.5.25
Requires: python3.11-asgiref = 3.8.1
Requires: python3.11-asn1 = 2.7.1
Requires: python3.11-async-timeout = 5.0.1
Requires: python3.11-attrs = 24.3.0
Requires: python3.11-autobahn = 24.4.2
Requires: python3.11-autocommand = 2.2.2
Requires: python3.11-automat = 24.8.1
Requires: python3.11-awscrt = 0.22.4
Requires: python3.11-azure-core = 1.32.0
Requires: python3.11-azure-core+aio = 1.32.0
Requires: python3.11-azure-identity = 1.19.0
Requires: python3.11-azure-keyvault = 4.2.0
Requires: python3.11-azure-keyvault-certificates = 4.9.0
Requires: python3.11-azure-keyvault-keys = 4.10.0
Requires: python3.11-azure-keyvault-secrets = 4.9.0
Requires: python3.11-babel = 2.17.0
Requires: python3.11-backports-tarfile = 1.2.0
Requires: python3.11-bcrypt = 4.2.1
Requires: python3.11-bcrypt+tests = 4.2.1
Requires: python3.11-bcrypt+typecheck = 4.2.1
Requires: python3.11-bindep = 2.12.0
Requires: python3.11-blinker = 1.9.0
Requires: python3.11-boto3 = 1.35.96
Requires: python3.11-boto3+crt = 1.35.96
Requires: python3.11-botocore = 1.35.96
Requires: python3.11-botocore+crt = 1.35.96
Requires: python3.11-brotli = 1.1.0
Requires: python3.11-build = 1.2.2^post1
Requires: python3.11-cachecontrol = 0.14.2
Requires: python3.11-cachecontrol+filecache = 0.14.2
Requires: python3.11-cachetools = 5.5.0
Requires: python3.11-calver = 2022.6.26
Requires: python3.11-certifi = 2025.1.31
Requires: python3.11-cffi = 1.17.1
Requires: python3.11-changelog-chug = 0.0.3
Requires: python3.11-channels = 4.2.0
Requires: python3.11-channels-redis = 4.2.1
Requires: python3.11-chardet = 5.2.0
Requires: python3.11-charset-normalizer = 3.4.1
Requires: python3.11-cleo = 2.1.0
Requires: python3.11-click = 8.1.8
Requires: python3.11-constantly = 23.10.4
Requires: python3.11-crashtest = 0.4.1
Requires: python3.11-cryptography = 41.0.7
Requires: python3.11-cython = 3.0.11
Requires: python3.11-daphne = 4.1.2
Requires: python3.11-deprecated = 1.2.15
Requires: python3.11-distlib = 0.3.9
Requires: python3.11-distro = 1.9.0
Requires: python3.11-django = 4.2.16
Requires: python3.11-django-ansible-base = 20250131
Requires: python3.11-django+argon2 = 4.2.16
Requires: python3.11-django+bcrypt = 4.2.16
Requires: python3.11-django-cors-headers = 4.6.0
Requires: python3.11-django-crum = 0.7.9
Requires: python3.11-django-extensions = 3.2.3
Requires: python3.11-django-flags = 5.0.13
Requires: python3.11-django-guid = 3.5.0
Requires: python3.11-django-oauth-toolkit = 1.7.1
Requires: python3.11-django-polymorphic = 3.1.0
Requires: python3.11-djangorestframework = 3.15.2
Requires: python3.11-djangorestframework-yaml = 2.0.0
Requires: python3.11-django-solo = 2.4.0
Requires: python3.11-django-split-settings = 1.3.2
Requires: python3.11-docutils = 0.21.2
Requires: python3.11-dulwich = 0.22.7
Requires: python3.11-durationpy = 0.9
Requires: python3.11-enum-compat = 0.0.3
Requires: python3.11-expandvars = 0.12.0
Requires: python3.11-fastjsonschema = 2.21.1
Requires: python3.11-filelock = 3.16.1
Requires: python3.11-findpython = 0.6.2
Requires: python3.11-frozenlist = 1.5.0
Requires: python3.11-gitdb = 4.0.12
Requires: python3.11-gitpython = 3.1.44
Requires: python3.11-googleapis-common-protos = 1.66.0
Requires: python3.11-googleapis-common-protos+grpc = 1.66.0
Requires: python3.11-google-auth = 2.37.0
Requires: python3.11-google-auth+aiohttp = 2.37.0
Requires: python3.11-google-auth+enterprise-cert = 2.37.0
Requires: python3.11-google-auth+pyjwt = 2.37.0
Requires: python3.11-google-auth+pyopenssl = 2.37.0
Requires: python3.11-google-auth+reauth = 2.37.0
Requires: python3.11-google-auth+requests = 2.37.0
Requires: python3.11-graphviz = 0.20.3
Requires: python3.11-grpcio = 1.70.0
Requires: python3.11-h11 = 0.14.0
Requires: python3.11-h2 = 4.2.0
Requires: python3.11-hatch = 1.14.0
Requires: python3.11-hatch-fancy-pypi-readme = 24.1.0
Requires: python3.11-hatchling = 1.27.0
Requires: python3.11-hatch-vcs = 0.4.0
Requires: python3.11-hiredis = 3.1.0
Requires: python3.11-hpack = 4.1.0
Requires: python3.11-httpcore = 1.0.7
Requires: python3.11-httpx = 0.28.1
Requires: python3.11-hyperframe = 6.1.0
Requires: python3.11-hyperlink = 21.0.0
Requires: python3.11-id = 1.5.0
Requires: python3.11-idna = 3.10
Requires: python3.11-importlib-metadata = 8.5.0
Requires: python3.11-importlib-resources = 6.5.2
Requires: python3.11-incremental = 24.7.2
Requires: python3.11-incremental+scripts = 24.7.2
Requires: python3.11-inflection = 0.5.1
Requires: python3.11-installer = 0.7.0
Requires: python3.11-irc = 20.5.0
Requires: python3.11-isodate = 0.7.2
Requires: python3.11-jaraco-classes = 3.4.0
Requires: python3.11-jaraco-collections = 5.1.0
Requires: python3.11-jaraco-context = 6.0.1
Requires: python3.11-jaraco-functools = 4.1.0
Requires: python3.11-jaraco-logging = 3.3.0
Requires: python3.11-jaraco-stream = 3.0.4
Requires: python3.11-jaraco-text = 4.0.0
Requires: python3.11-jeepney = 0.8.0
Requires: python3.11-jinja2 = 3.1.5
Requires: python3.11-jinja2+i18n = 3.1.5
Requires: python3.11-jmespath = 1.0.1
Requires: python3.11-json-log-formatter = 1.1
Requires: python3.11-jsonschema = 4.23.0
Requires: python3.11-jsonschema-specifications = 2024.10.1
Requires: python3.11-jwcrypto = 1.5.6
Requires: python3.11-keyring = 25.6.0
Requires: python3.11-kubernetes = 31.0.0
Requires: python3.11-kubernetes+adal = 31.0.0
Requires: python3.11-lockfile = 0.12.2
Requires: python3.11-markdown = 3.7
Requires: python3.11-markdown-it-py = 3.0.0
Requires: python3.11-markupsafe = 3.0.2
Requires: python3.11-maturin = 1.7.8
Requires: python3.11-mdurl = 0.1.2
Requires: python3.11-more-itertools = 10.5.0
Requires: python3.11-msal = 1.31.1
Requires: python3.11-msal+broker = 1.31.1
Requires: python3.11-msal-extensions = 1.2.0
Requires: python3.11-msgpack = 1.1.0
Requires: python3.11-msrest = 0.7.1
Requires: python3.11-msrest+async = 0.7.1
Requires: python3.11-msrestazure = 0.6.4^post1
Requires: python3.11-multidict = 6.1.0
Requires: python3.11-mypy = 1.14.1
Requires: python3.11-mypy+dmypy = 1.14.1
Requires: python3.11-mypy-extensions = 1.0.0
Requires: python3.11-mypy+faster-cache = 1.14.1
Requires: python3.11-mypy+install-types = 1.14.1
Requires: python3.11-mypy+mypyc = 1.14.1
Requires: python3.11-mypy+reports = 1.14.1
Requires: python3.11-nh3 = 0.2.20
Requires: python3.11-oauthlib = 3.2.2
Requires: python3.11-oauthlib+rsa = 3.2.2
Requires: python3.11-oauthlib+signals = 3.2.2
Requires: python3.11-oauthlib+signedtoken = 3.2.2
Requires: python3.11-openshift = 0.13.2
Requires: python3.11-opentelemetry-api = 1.29.0
Requires: python3.11-opentelemetry-exporter-otlp = 1.29.0
Requires: python3.11-opentelemetry-exporter-otlp-proto-common = 1.29.0
Requires: python3.11-opentelemetry-exporter-otlp-proto-grpc = 1.29.0
Requires: python3.11-opentelemetry-exporter-otlp-proto-http = 1.29.0
Requires: python3.11-opentelemetry-instrumentation = 0.50~b0
Requires: python3.11-opentelemetry-instrumentation-logging = 0.50~b0
Requires: python3.11-opentelemetry-proto = 1.29.0
Requires: python3.11-opentelemetry-sdk = 1.29.0
Requires: python3.11-opentelemetry-semantic-conventions = 0.50~b0
Requires: python3.11-orjson = 3.10.13
Requires: python3.11-packaging = 24.2
Requires: python3.11-parsley = 1.3
Requires: python3.11-pathspec = 0.12.1
Requires: python3.11-pbr = 6.1.0
Requires: python3.11-pbs-installer = 2025.2.12
Requires: python3.11-pbs-installer+all = 2025.2.12
Requires: python3.11-pbs-installer+download = 2025.2.12
Requires: python3.11-pbs-installer+install = 2025.2.12
Requires: python3.11-pdm-backend = 2.4.3
Requires: python3.11-pexpect = 4.9.0
Requires: python3.11-pkgconfig = 1.5.5
Requires: python3.11-pkginfo = 1.12.1.2
Requires: python3.11-platformdirs = 4.3.6
Requires: python3.11-portalocker = 2.10.1
Requires: python3.11-priority = 1.3.0
Requires: python3.11-prometheus-client = 0.21.1
Requires: python3.11-prometheus-client+twisted = 0.21.1
Requires: python3.11-propcache = 0.2.1
Requires: python3.11-protobuf = 5.29.3
Requires: python3.11-psutil = 6.1.1
Requires: python3.11-psycopg = 3.2.3
Requires: python3.11-ptyprocess = 0.7.0
Requires: python3.11-pyasn1-modules = 0.5.1
Requires: python3.11-pycares = 4.5.0
Requires: python3.11-pycares+idna = 4.5.0
Requires: python3.11-pycparser = 2.22
Requires: python3.11-pygerduty = 0.38.3
Requires: python3.11-pygments = 2.19.1
Requires: python3.11-pyjwt = 2.10.1
Requires: python3.11-pyjwt+crypto = 2.10.1
Requires: python3.11-pyopenssl = 24.3.0
Requires: python3.11-pyparsing = 2.4.6
Requires: python3.11-pyproject-hooks = 1.2.0
Requires: python3.11-python-daemon = 3.1.2
Requires: python3.11-python-dateutil = 2.9.0^post0
Requires: python3.11-python-dsv-sdk = 1.0.4
Requires: python3.11-python-string-utils = 1.0.0
Requires: python3.11-pytz = 2024.2
Requires: python3.11-pyu2f = 0.1.5
Requires: python3.11-pyyaml = 6.0.2
Requires: python3.11-pyzstd = 0.16.2
Requires: python3.11-rapidfuzz = 3.9.3
Requires: python3.11-readme-renderer = 44.0
Requires: python3.11-receptorctl = 1.5.2
Requires: python3.11-redis = 5.2.1
Requires: python3.11-referencing = 0.35.1
Requires: python3.11-requests = 2.32.3
Requires: python3.11-requests-oauthlib = 2.0.0
Requires: python3.11-requests-oauthlib+rsa = 2.0.0
Requires: python3.11-requests+socks = 2.32.3
Requires: python3.11-requests-toolbelt = 1.0.0
Requires: python3.11-requests+use-chardet-on-py3 = 2.32.3
Requires: python3.11-rfc3986 = 2.0.0
Requires: python3.11-rich = 13.9.4
Requires: python3.11-rpds-py = 0.22.3
Requires: python3.11-rsa = 4.9
Requires: python3.11-s3transfer = 0.10.4
Requires: python3.11-s3transfer+crt = 0.10.4
Requires: python3.11-scikit-build = 0.17.6
Requires: python3.11-secretstorage = 3.3.3
Requires: python3.11-semantic-version = 2.10.0
Requires: python3.11-semver = 3.0.4
Requires: python3.11-service-identity = 24.2.0
Requires: python3.11-setuptools = 75.8.0
Requires: python3.11-setuptools-rust = 1.10.2
Requires: python3.11-setuptools_scm = 8.1.0
Requires: python3.11-setuptools_scm+toml = 8.1.0
Requires: python3.11-setuptools-twine = 0.1.3
Requires: python3.11-shellingham = 1.5.4
Requires: python3.11-six = 1.17.0
Requires: python3.11-slack-sdk = 3.34.0
Requires: python3.11-smmap = 5.0.2
Requires: python3.11-sniffio = 1.3.1
Requires: python3.11-sqlparse = 0.5.3
Requires: python3.11-tempora = 5.8.0
Requires: python3.11-tomli-w = 1.2.0
Requires: python3.11-tomlkit = 0.13.2
Requires: python3.11-trove-classifiers = 2025.1.15.22
Requires: python3.11-twilio = 9.4.2
Requires: python3.11-twine = 6.1.0
Requires: python3.11-twisted = 24.11.0
Requires: python3.11-twisted+http2 = 24.11.0
Requires: python3.11-twisted+tls = 24.11.0
Requires: python3.11-txaio = 23.1.1
Requires: python3.11-types-psutil = 7.0.0.20250218
Requires: python3.11-types-setuptools = 75.8.0.20250210
Requires: python3.11-typing-extensions = 4.12.2
Requires: python3.11-urllib3 = 2.3.0
Requires: python3.11-urllib3+brotli = 2.3.0
Requires: python3.11-urllib3+h2 = 2.3.0
Requires: python3.11-urllib3+socks = 2.3.0
Requires: python3.11-urllib3+zstd = 2.3.0
Requires: python3.11-userpath = 1.9.2
Requires: python3.11-uv = 0.2.30
Requires: python3.11-uwsgi = 2.0.26
Requires: python3.11-uwsgitop = 0.12
Requires: python3.11-versioneer = 0.29
Requires: python3.11-versioneer+toml = 0.29
Requires: python3.11-virtualenv = 20.29.2
Requires: python3.11-websocket-client = 1.8.0
Requires: python3.11-wrapt = 1.17.0
Requires: python3.11-yarl = 1.18.3
Requires: python3.11-zipp = 3.21.0
Requires: python3.11-zope-interface = 7.2
Requires: python3.11-zstandard = 0.23.0
Requires: python3.11-pyasn1 python3.11-pip python3.11-urllib3 python3.11-pexpect 

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx
git checkout -f devel
git checkout -f %{version}

%build

%install
mkdir translations/
mv awx/locale/en-us/LC_MESSAGES/django.po translations/
#mv awx/ui/src/locales/en/messages.po translations/

echo 'node-options="--openssl-legacy-provider"' >> awx/ui/.npmrc
GIT_BRANCH=%{version} VERSION=%{version} python%{python3_pkgversion} -m build -s
#make ui-next/src
#cp %{_sourcedir}/awx-rpm-logo.svg-%{version} awx/ui_next/src/frontend/awx/main/awx-rpm-logo.svg
#sed -i "s/awx-logo.svg/awx-rpm-logo.svg/g" awx/ui_next/src/frontend/awx/main/AwxMasthead.tsx
make ui

mkdir -p /var/log/tower

mkdir -p %{buildroot}/opt/awx-rpm

pushd %{buildroot}/opt/awx-rpm

AWX_SETTINGS_FILE=awx/settings/production.py SKIP_SECRET_KEY_CHECK=yes SKIP_PG_VERSION_CHECK=yes python%{python3_pkgversion} manage.py collectstatic --noinput --clear

popd

#chmod +x tools/scripts/l18n/post_translation.sh
#./tools/scripts/l18n/post_translation.sh



#mkdir -p %{buildroot}%{_prefix}
#for i in `find -type f |grep mappings.wasm`; do
#	echo "Removing $i"
#	rm -f $i
#done

#popd

#rsync -avr awx/ $RPM_BUILD_ROOT/opt/awx-rpm/awx/
#cp -a /var/lib/awx/public/static /opt/awx-rpm/

#mkdir -p $RPM_BUILD_ROOT/var/lib/awx/rsyslog
#mkdir -p $RPM_BUILD_ROOT/var/lib/awx/projects
#mkdir -p $RPM_BUILD_ROOT/var/lib/awx/job_status

# Collect django static
#mkdir -p /var/log/tower/
#mkdir -p %{buildroot}%{service_homedir}
#mkdir -p %{buildroot}%{service_logdir}
#mkdir -p %{buildroot}%{_prefix}/bin
#mkdir -p %{buildroot}%{service_configdir}
#echo %{version} > %{buildroot}%{service_homedir}/.tower_version

#cp %{_sourcedir}/settings.py-%{version} %{buildroot}%{service_configdir}/settings.py
#mkdir -p %{buildroot}%{_prefix}/public
#rsync -avr /var/lib/awx/public/ %{buildroot}%{_prefix}/public/

%clean

%files
%defattr(0644, awx, awx, 0755)
%attr(0755, awx, awx) %{_prefix}
%{service_homedir}/.tower_version

%changelog
* Thu Feb 27 2025 12:41:53 AM CET +0100 Martin Juhl <m@rtinjuhl.dk> 30.0.0
- New version build: 30.0.0

