%define  debug_package %{nil}
%define _prefix /opt/awx-rpm
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/tower
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX
Name: awx-rpm
Version: 24.0.0
Release: 9%{dist}
Source0: awx-24.0.0.tar.gz
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
Patch0: awx-patch.patch-%{version}
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: make python3 python3-devel nodejs npm gettext git python3-build rsync libpq libpq-devel 
BuildRequires: python3-adal = 1.2.7
BuildRequires: python3-aiohttp = 3.9.3
BuildRequires: python3-aioredis = 1.3.1
BuildRequires: python3-aiosignal = 1.3.1
BuildRequires: python3-ansible-builder = 3.0.1
BuildRequires: python3-ansible-runner = 2.3.6
BuildRequires: python3-ansiconv = 1.0.0
BuildRequires: python3-asciichartpy = 1.5.25
BuildRequires: python3-asciichartpy+qa = 1.5.25
BuildRequires: python3-asgiref = 3.6.0
BuildRequires: python3-asn1 = 2.6.0
BuildRequires: python3-asyncpg = 0.27.0
BuildRequires: python3-async-timeout = 4.0.2
BuildRequires: python3-attrs = 22.1.0
BuildRequires: python3-autobahn = 22.7.1
BuildRequires: python3-autocommand = 2.2.2
BuildRequires: python3-automat = 22.10.0
BuildRequires: python3-automat+visualize = 22.10.0
BuildRequires: python3-awscrt = 0.16.9
BuildRequires: python3-azure-common = 1.1.28
BuildRequires: python3-azure-core = 1.26.1
BuildRequires: python3-azure-core+aio = 1.26.1
BuildRequires: python3-azure-keyvault = 1.1.0
BuildRequires: python3-azure-nspkg = 3.0.2
BuildRequires: python3-boto3 = 1.26.102
BuildRequires: python3-boto3+crt = 1.26.102
BuildRequires: python3-botocore = 1.29.102
BuildRequires: python3-botocore+crt = 1.29.102
BuildRequires: python3-build = 1.1.1
BuildRequires: python3-cachecontrol = 0.14.0
BuildRequires: python3-cachecontrol+filecache = 0.14.0
BuildRequires: python3-cachecontrol+redis = 0.14.0
BuildRequires: python3-cachetools = 5.2.0
BuildRequires: python3-calver = 2022.6.26
BuildRequires: python3-cffi = 1.15.1
BuildRequires: python3-channels = 3.0.5
BuildRequires: python3-channels-redis = 3.4.1
BuildRequires: python3-charset-normalizer = 2.1.1
BuildRequires: python3-cleo = 2.1.0
BuildRequires: python3-click = 8.1.3
BuildRequires: python3-constantly = 15.1.0
BuildRequires: python3-crashtest = 0.4.1
BuildRequires: python3-cryptography = 41.0.7
BuildRequires: python3-cython = 0.29.37
BuildRequires: python3-daphne = 3.0.2
BuildRequires: python3-defusedxml = 0.7.1
BuildRequires: python3-deprecated = 1.2.13
BuildRequires: python3-distro = 1.8.0
BuildRequires: python3-django = 4.2.6
BuildRequires: python3-django-ansible-base = 20240212
BuildRequires: python3-django-ansible-base+jwt_consumer = 20240212
BuildRequires: python3-django-ansible-base+rest_filters = 20240212
BuildRequires: python3-django+argon2 = 4.2.6
BuildRequires: python3-django-auth-ldap = 4.6.0
BuildRequires: python3-django+bcrypt = 4.2.6
BuildRequires: python3-django-cors-headers = 3.13.0
BuildRequires: python3-django-crum = 0.7.9
BuildRequires: python3-django-debug-toolbar = 4.3.0
BuildRequires: python3-django-extensions = 3.2.1
BuildRequires: python3-django-guid = 3.2.1
BuildRequires: python3-django-oauth-toolkit = 1.7.1
BuildRequires: python3-django-pglocks = 1.0.4
BuildRequires: python3-django-polymorphic = 3.1.0
BuildRequires: python3-django-radius = 1.5.0
BuildRequires: python3-djangorestframework = 3.14.0
BuildRequires: python3-djangorestframework-yaml = 2.0.0
BuildRequires: python3-django-rest-swagger = 2.2.0
BuildRequires: python3-django-solo = 2.0.0
BuildRequires: python3-django-split-settings = 1.0.0
BuildRequires: python3-dm-xmlsec-binding = 2.2
BuildRequires: python3-docutils = 0.19
BuildRequires: python3-drf-yasg = 1.21.7
BuildRequires: python3-drf-yasg+coreapi = 1.21.7
BuildRequires: python3-drf-yasg+validation = 1.21.7
BuildRequires: python3-ecdsa = 0.18.0
BuildRequires: python3-enum-compat = 0.0.3
BuildRequires: python3-filelock = 3.8.0
BuildRequires: python3-frozenlist = 1.3.3
BuildRequires: python3-gitdb = 4.0.10
BuildRequires: python3-gitpython = 3.1.42
BuildRequires: python3-google-auth = 2.14.1
BuildRequires: python3-hatch-fancy-pypi-readme = 24.1.0
BuildRequires: python3-hatchling = 1.21.1
BuildRequires: python3-hatch-vcs = 0.4.0
BuildRequires: python3-hiredis = 2.0.0
BuildRequires: python3-hyperlink = 21.0.0
BuildRequires: python3-idna = 3.4
BuildRequires: python3-incremental = 22.10.0
BuildRequires: python3-inflect = 6.0.2
BuildRequires: python3-inflection = 0.5.1
BuildRequires: python3-irc = 20.1.0
BuildRequires: python3-isodate = 0.6.1
BuildRequires: python3-jaraco-classes = 3.2.3
BuildRequires: python3-jaraco-collections = 3.8.0
BuildRequires: python3-jaraco-context = 4.2.0
BuildRequires: python3-jaraco-functools = 3.5.2
BuildRequires: python3-jaraco-logging = 3.1.2
BuildRequires: python3-jaraco-stream = 3.0.3
BuildRequires: python3-jaraco-text = 3.11.0
BuildRequires: python3-jinja2 = 3.1.3
BuildRequires: python3-jinja2+i18n = 3.1.3
BuildRequires: python3-jmespath = 1.0.1
BuildRequires: python3-json-log-formatter = 0.5.1
BuildRequires: python3-jsonschema = 4.17.3
BuildRequires: python3-jwcrypto = 1.4.2
BuildRequires: python3-keyring = 24.3.1
BuildRequires: python3-kubernetes = 25.3.0
BuildRequires: python3-kubernetes+adal = 25.3.0
BuildRequires: python3-lockfile = 0.12.2
BuildRequires: python3-markdown = 3.4.1
BuildRequires: python3-markupsafe = 2.1.1
BuildRequires: python3-maturin = 1.5.0
BuildRequires: python3-more-itertools = 9.0.0
BuildRequires: python3-msgpack = 1.0.4
BuildRequires: python3-msrest = 0.7.1
BuildRequires: python3-msrest+async = 0.7.1
BuildRequires: python3-msrestazure = 0.6.4
BuildRequires: python3-multidict = 6.0.2
BuildRequires: python3-netaddr = 0.8.0
BuildRequires: python3-nh3 = 0.2.15
BuildRequires: python3-oauthlib = 3.2.2
BuildRequires: python3-oauthlib+rsa = 3.2.2
BuildRequires: python3-oauthlib+signals = 3.2.2
BuildRequires: python3-oauthlib+signedtoken = 3.2.2
BuildRequires: python3-openapi-codec = 1.3.2
BuildRequires: python3-openshift = 0.13.1
BuildRequires: python3-packaging = 21.3
BuildRequires: python3-pbr = 5.11.0
BuildRequires: python3-pip = 21.2.4
BuildRequires: python3-pkgconfig = 1.5.5
BuildRequires: python3-platformdirs = 3.11.0
BuildRequires: python3-priority = 1.3.0
BuildRequires: python3-prometheus-client = 0.20.0
BuildRequires: python3-prometheus-client+twisted = 0.20.0
BuildRequires: python3-psutil = 5.9.4
BuildRequires: python3-psycopg = 3.1.9
BuildRequires: python3-ptyprocess = 0.7.0
BuildRequires: python3-pyasn1-modules = 0.5.1
BuildRequires: python3-pycparser = 2.21
BuildRequires: python3-pydantic = 1.10.2
BuildRequires: python3-pygerduty = 0.38.3
BuildRequires: python3-pyjwt = 2.6.0
BuildRequires: python3-pyopenssl = 23.2.0
BuildRequires: python3-pyproject-hooks = 1.0.0
BuildRequires: python3-pyrad = 2.4
BuildRequires: python3-pyrsistent = 0.19.2
BuildRequires: python3-python3-openid = 3.2.0
BuildRequires: python3-python3-saml = 1.14.0
BuildRequires: python3-python-daemon = 3.0.1
BuildRequires: python3-python-dsv-sdk = 1.0.4
BuildRequires: python3-python-jose = 3.3.0
BuildRequires: python3-python-string-utils = 1.0.0
BuildRequires: python3-pytz = 2022.6
BuildRequires: python3-rapidfuzz = 3.6.2
BuildRequires: python3-readme-renderer = 43.0
BuildRequires: python3-receptorctl = 1.4.4
BuildRequires: python3-redis = 4.3.5
BuildRequires: python3-requests = 2.28.1
BuildRequires: python3-requests-oauthlib = 1.3.1
BuildRequires: python3-requests-oauthlib+rsa = 1.3.1
BuildRequires: python3-requests+socks = 2.28.1
BuildRequires: python3-requests+use-chardet-on-py3 = 2.28.1
BuildRequires: python3-requirements-parser = 0.5.0
BuildRequires: python3-rsa = 4.9
BuildRequires: python3-s3transfer = 0.6.0
BuildRequires: python3-scikit-build = 0.17.6
BuildRequires: python3-semantic-version = 2.10.0
BuildRequires: python3-service-identity = 21.1.0
BuildRequires: python3-setuptools = 65.6.3
BuildRequires: python3-setuptools-rust = 1.5.2
BuildRequires: python3-setuptools_scm = 8.0.4
BuildRequires: python3-setuptools_scm+toml = 8.0.4
BuildRequires: python3-setuptools-twine = 0.1.3
BuildRequires: python3-shellingham = 1.5.4
BuildRequires: python3-six = 1.16.0
BuildRequires: python3-slack-sdk = 3.19.4
BuildRequires: python3-smmap = 5.0.0
BuildRequires: python3-social-auth-app-django = 5.4.0
BuildRequires: python3-social-auth-core = 4.4.2
BuildRequires: python3-social-auth-core+all = 4.4.2
BuildRequires: python3-social-auth-core+allpy3 = 4.4.2
BuildRequires: python3-social-auth-core+azuread = 4.4.2
BuildRequires: python3-social-auth-core+openidconnect = 4.4.2
BuildRequires: python3-social-auth-core+saml = 4.4.2
BuildRequires: python3-sqlparse = 0.4.4
BuildRequires: python3-tacacs-plus = 1.0
BuildRequires: python3-tempora = 5.1.0
BuildRequires: python3-tomli = 2.0.1
BuildRequires: python3-trove-classifiers = 2024.3.3
BuildRequires: python3-twilio = 7.15.3
BuildRequires: python3-twine = 5.0.0
BuildRequires: python3-twisted = 23.10.0
BuildRequires: python3-twisted+http2 = 23.10.0
BuildRequires: python3-twisted+tls = 23.10.0
BuildRequires: python3-txaio = 22.2.1
BuildRequires: python3-types-setuptools = 69.1.0.20240310
BuildRequires: python3-typing-extensions = 4.4.0
BuildRequires: python3-urllib3 = 1.26.17
BuildRequires: python3-uwsgi = 2.0.21
BuildRequires: python3-uwsgitop = 0.11
BuildRequires: python3-websocket-client = 1.4.2
BuildRequires: python3-wheel = 0.43.0
BuildRequires: python3-wrapt = 1.15.0
BuildRequires: python3-xmlsec = 1.3.13
BuildRequires: python3-yarl = 1.8.1
BuildRequires: python3-zipp = 3.11.0
BuildRequires: python3-zope-interface = 5.5.2
BuildRequires: python-ntlm = 1.1.0
BuildRequires: python3-pyyaml python3-lxml python3-dulwich python3-importlib-metadata python3-dateutil python3-ldap python3-pyasn1 python3-pexpect python3-pyparsing python3-resolvelib 

Requires: python3 nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 
Requires: python3-adal = 1.2.7
Requires: python3-aiohttp = 3.9.3
Requires: python3-aioredis = 1.3.1
Requires: python3-aiosignal = 1.3.1
Requires: python3-ansible-builder = 3.0.1
Requires: python3-ansible-runner = 2.3.6
Requires: python3-ansiconv = 1.0.0
Requires: python3-asciichartpy = 1.5.25
Requires: python3-asciichartpy+qa = 1.5.25
Requires: python3-asgiref = 3.6.0
Requires: python3-asn1 = 2.6.0
Requires: python3-asyncpg = 0.27.0
Requires: python3-async-timeout = 4.0.2
Requires: python3-attrs = 22.1.0
Requires: python3-autobahn = 22.7.1
Requires: python3-autocommand = 2.2.2
Requires: python3-automat = 22.10.0
Requires: python3-automat+visualize = 22.10.0
Requires: python3-awscrt = 0.16.9
Requires: python3-azure-common = 1.1.28
Requires: python3-azure-core = 1.26.1
Requires: python3-azure-core+aio = 1.26.1
Requires: python3-azure-keyvault = 1.1.0
Requires: python3-azure-nspkg = 3.0.2
Requires: python3-boto3 = 1.26.102
Requires: python3-boto3+crt = 1.26.102
Requires: python3-botocore = 1.29.102
Requires: python3-botocore+crt = 1.29.102
Requires: python3-build = 1.1.1
Requires: python3-cachecontrol = 0.14.0
Requires: python3-cachecontrol+filecache = 0.14.0
Requires: python3-cachecontrol+redis = 0.14.0
Requires: python3-cachetools = 5.2.0
Requires: python3-calver = 2022.6.26
Requires: python3-cffi = 1.15.1
Requires: python3-channels = 3.0.5
Requires: python3-channels-redis = 3.4.1
Requires: python3-charset-normalizer = 2.1.1
Requires: python3-cleo = 2.1.0
Requires: python3-click = 8.1.3
Requires: python3-constantly = 15.1.0
Requires: python3-crashtest = 0.4.1
Requires: python3-cryptography = 41.0.7
Requires: python3-cython = 0.29.37
Requires: python3-daphne = 3.0.2
Requires: python3-defusedxml = 0.7.1
Requires: python3-deprecated = 1.2.13
Requires: python3-distro = 1.8.0
Requires: python3-django = 4.2.6
Requires: python3-django-ansible-base = 20240212
Requires: python3-django-ansible-base+jwt_consumer = 20240212
Requires: python3-django-ansible-base+rest_filters = 20240212
Requires: python3-django+argon2 = 4.2.6
Requires: python3-django-auth-ldap = 4.6.0
Requires: python3-django+bcrypt = 4.2.6
Requires: python3-django-cors-headers = 3.13.0
Requires: python3-django-crum = 0.7.9
Requires: python3-django-debug-toolbar = 4.3.0
Requires: python3-django-extensions = 3.2.1
Requires: python3-django-guid = 3.2.1
Requires: python3-django-oauth-toolkit = 1.7.1
Requires: python3-django-pglocks = 1.0.4
Requires: python3-django-polymorphic = 3.1.0
Requires: python3-django-radius = 1.5.0
Requires: python3-djangorestframework = 3.14.0
Requires: python3-djangorestframework-yaml = 2.0.0
Requires: python3-django-rest-swagger = 2.2.0
Requires: python3-django-solo = 2.0.0
Requires: python3-django-split-settings = 1.0.0
Requires: python3-dm-xmlsec-binding = 2.2
Requires: python3-docutils = 0.19
Requires: python3-drf-yasg = 1.21.7
Requires: python3-drf-yasg+coreapi = 1.21.7
Requires: python3-drf-yasg+validation = 1.21.7
Requires: python3-ecdsa = 0.18.0
Requires: python3-enum-compat = 0.0.3
Requires: python3-filelock = 3.8.0
Requires: python3-frozenlist = 1.3.3
Requires: python3-gitdb = 4.0.10
Requires: python3-gitpython = 3.1.42
Requires: python3-google-auth = 2.14.1
Requires: python3-hatch-fancy-pypi-readme = 24.1.0
Requires: python3-hatchling = 1.21.1
Requires: python3-hatch-vcs = 0.4.0
Requires: python3-hiredis = 2.0.0
Requires: python3-hyperlink = 21.0.0
Requires: python3-idna = 3.4
Requires: python3-incremental = 22.10.0
Requires: python3-inflect = 6.0.2
Requires: python3-inflection = 0.5.1
Requires: python3-irc = 20.1.0
Requires: python3-isodate = 0.6.1
Requires: python3-jaraco-classes = 3.2.3
Requires: python3-jaraco-collections = 3.8.0
Requires: python3-jaraco-context = 4.2.0
Requires: python3-jaraco-functools = 3.5.2
Requires: python3-jaraco-logging = 3.1.2
Requires: python3-jaraco-stream = 3.0.3
Requires: python3-jaraco-text = 3.11.0
Requires: python3-jinja2 = 3.1.3
Requires: python3-jinja2+i18n = 3.1.3
Requires: python3-jmespath = 1.0.1
Requires: python3-json-log-formatter = 0.5.1
Requires: python3-jsonschema = 4.17.3
Requires: python3-jwcrypto = 1.4.2
Requires: python3-keyring = 24.3.1
Requires: python3-kubernetes = 25.3.0
Requires: python3-kubernetes+adal = 25.3.0
Requires: python3-lockfile = 0.12.2
Requires: python3-markdown = 3.4.1
Requires: python3-markupsafe = 2.1.1
Requires: python3-maturin = 1.5.0
Requires: python3-more-itertools = 9.0.0
Requires: python3-msgpack = 1.0.4
Requires: python3-msrest = 0.7.1
Requires: python3-msrest+async = 0.7.1
Requires: python3-msrestazure = 0.6.4
Requires: python3-multidict = 6.0.2
Requires: python3-netaddr = 0.8.0
Requires: python3-nh3 = 0.2.15
Requires: python3-oauthlib = 3.2.2
Requires: python3-oauthlib+rsa = 3.2.2
Requires: python3-oauthlib+signals = 3.2.2
Requires: python3-oauthlib+signedtoken = 3.2.2
Requires: python3-openapi-codec = 1.3.2
Requires: python3-openshift = 0.13.1
Requires: python3-packaging = 21.3
Requires: python3-pbr = 5.11.0
Requires: python3-pip = 21.2.4
Requires: python3-pkgconfig = 1.5.5
Requires: python3-platformdirs = 3.11.0
Requires: python3-priority = 1.3.0
Requires: python3-prometheus-client = 0.20.0
Requires: python3-prometheus-client+twisted = 0.20.0
Requires: python3-psutil = 5.9.4
Requires: python3-psycopg = 3.1.9
Requires: python3-ptyprocess = 0.7.0
Requires: python3-pyasn1-modules = 0.5.1
Requires: python3-pycparser = 2.21
Requires: python3-pydantic = 1.10.2
Requires: python3-pygerduty = 0.38.3
Requires: python3-pyjwt = 2.6.0
Requires: python3-pyopenssl = 23.2.0
Requires: python3-pyproject-hooks = 1.0.0
Requires: python3-pyrad = 2.4
Requires: python3-pyrsistent = 0.19.2
Requires: python3-python3-openid = 3.2.0
Requires: python3-python3-saml = 1.14.0
Requires: python3-python-daemon = 3.0.1
Requires: python3-python-dsv-sdk = 1.0.4
Requires: python3-python-jose = 3.3.0
Requires: python3-python-string-utils = 1.0.0
Requires: python3-pytz = 2022.6
Requires: python3-rapidfuzz = 3.6.2
Requires: python3-readme-renderer = 43.0
Requires: python3-receptorctl = 1.4.4
Requires: python3-redis = 4.3.5
Requires: python3-requests = 2.28.1
Requires: python3-requests-oauthlib = 1.3.1
Requires: python3-requests-oauthlib+rsa = 1.3.1
Requires: python3-requests+socks = 2.28.1
Requires: python3-requests+use-chardet-on-py3 = 2.28.1
Requires: python3-requirements-parser = 0.5.0
Requires: python3-rsa = 4.9
Requires: python3-s3transfer = 0.6.0
Requires: python3-scikit-build = 0.17.6
Requires: python3-semantic-version = 2.10.0
Requires: python3-service-identity = 21.1.0
Requires: python3-setuptools = 65.6.3
Requires: python3-setuptools-rust = 1.5.2
Requires: python3-setuptools_scm = 8.0.4
Requires: python3-setuptools_scm+toml = 8.0.4
Requires: python3-setuptools-twine = 0.1.3
Requires: python3-shellingham = 1.5.4
Requires: python3-six = 1.16.0
Requires: python3-slack-sdk = 3.19.4
Requires: python3-smmap = 5.0.0
Requires: python3-social-auth-app-django = 5.4.0
Requires: python3-social-auth-core = 4.4.2
Requires: python3-social-auth-core+all = 4.4.2
Requires: python3-social-auth-core+allpy3 = 4.4.2
Requires: python3-social-auth-core+azuread = 4.4.2
Requires: python3-social-auth-core+openidconnect = 4.4.2
Requires: python3-social-auth-core+saml = 4.4.2
Requires: python3-sqlparse = 0.4.4
Requires: python3-tacacs-plus = 1.0
Requires: python3-tempora = 5.1.0
Requires: python3-tomli = 2.0.1
Requires: python3-trove-classifiers = 2024.3.3
Requires: python3-twilio = 7.15.3
Requires: python3-twine = 5.0.0
Requires: python3-twisted = 23.10.0
Requires: python3-twisted+http2 = 23.10.0
Requires: python3-twisted+tls = 23.10.0
Requires: python3-txaio = 22.2.1
Requires: python3-types-setuptools = 69.1.0.20240310
Requires: python3-typing-extensions = 4.4.0
Requires: python3-urllib3 = 1.26.17
Requires: python3-uwsgi = 2.0.21
Requires: python3-uwsgitop = 0.11
Requires: python3-websocket-client = 1.4.2
Requires: python3-wheel = 0.43.0
Requires: python3-wrapt = 1.15.0
Requires: python3-xmlsec = 1.3.13
Requires: python3-yarl = 1.8.1
Requires: python3-zipp = 3.11.0
Requires: python3-zope-interface = 5.5.2
Requires: python-ntlm = 1.1.0
Requires: python3-pyyaml python3-lxml python3-dulwich python3-importlib-metadata python3-dateutil python3-ldap python3-pyasn1 python3-pexpect python3-pyparsing python3-resolvelib 

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx
git checkout -f devel
git checkout -f %{version}
%patch0 -p0

%build

%install
echo 'node-options="--openssl-legacy-provider"' >> awx/ui/.npmrc
GIT_BRANCH=%{version} VERSION=%{version} python3 -m build -s
make ui-next/src
cp %{_sourcedir}/awx-rpm-logo.svg-%{version} awx/ui_next/src/frontend/awx/main/awx-rpm-logo.svg
sed -i "s/awx-logo.svg/awx-rpm-logo.svg/g" awx/ui_next/src/frontend/awx/main/AwxMasthead.tsx
make ui-next
make ui-release

mkdir -p /var/log/tower
#python3 manage.py collectstatic --clear --noinput
AWX_SETTINGS_FILE=awx/settings/production.py SKIP_SECRET_KEY_CHECK=yes SKIP_PG_VERSION_CHECK=yes python3 manage.py collectstatic --noinput --clear
mkdir -p %{buildroot}%{_prefix}
for i in `find -type f |grep mappings.wasm`; do
	echo "Removing $i"
	rm -f $i
done
cp dist/awx-*.tar.gz %{buildroot}%{_prefix}/
pushd %{buildroot}%{_prefix}
tar zxvf awx-*.tar.gz
rm awx-*.tar.gz
mv awx-*/* .
rm -rf awx-*
pip3 install --root=%{buildroot}/ .
popd
sed -i "s|/builddir.*.x86_64||g" $RPM_BUILD_ROOT/usr/bin/awx-manage
pushd %{buildroot}/usr/lib/python3.9/site-packages/
for i in `find -type f`; do
	sed -i "s|/builddir.*.x86_64||g" $i
done
popd

rsync -avr awx/ $RPM_BUILD_ROOT/opt/awx-rpm/awx/
cp -a /var/lib/awx/public/static /opt/awx-rpm/

mkdir -p $RPM_BUILD_ROOT/var/lib/awx/rsyslog
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/projects
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/job_status

# Collect django static
mkdir -p /var/log/tower/
mkdir -p %{buildroot}%{service_homedir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{service_configdir}
echo %{version} > %{buildroot}%{service_homedir}/.tower_version

cp %{_sourcedir}/settings.py-%{version} %{buildroot}%{service_configdir}/settings.py
mkdir -p %{buildroot}%{_prefix}/public
rsync -avr /var/lib/awx/public/ %{buildroot}%{_prefix}/public/

mkdir -p %{buildroot}/usr/lib/systemd/system
# awx-channels-worker awx
for service in awx-web awx-wsrelay awx-ws-heartbeat awx-daphne awx-dispatcher awx-receiver awx-receptor awx-receptor-hop awx-receptor-worker; do
    cp %{_sourcedir}/${service}.service-%{version} %{buildroot}/usr/lib/systemd/system/${service}.service
done

cp %{_sourcedir}/awx.target-%{version} %{buildroot}/usr/lib/systemd/system/awx.target

mkdir -p %{buildroot}/etc/receptor

for receptor in receptor receptor-hop receptor-worker; do
	cp %{_sourcedir}/$receptor.conf-%{version} %{buildroot}/etc/receptor/$receptor.conf
done

mkdir -p %{buildroot}/etc/nginx/conf.d

cp %{_sourcedir}/awx-rpm-nginx.conf-%{version} %{buildroot}/etc/nginx/conf.d/awx-rpm.conf

# Create Virtualenv folder
mkdir -p %{buildroot}%{service_homedir}/venv

# Install docs
#cp %{_sourcedir}/nginx.conf.example ./

# Install VENV Script
#cp %{_sourcedir}/awx-create-venv $RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/bin/
#mkdir -p $RPM_BUILD_ROOT/usr/bin/

mkdir -p $RPM_BUILD_ROOT/etc/nginx/conf.d/

sed -i "s/supervisor_service_command(command='restart', service='awx-rsyslogd')//g" $RPM_BUILD_ROOT/usr/lib/python3.9/site-packages/awx/main/utils/external_logging.py

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}
/usr/bin/gpasswd -a awx redis

%post
if [ ! -f /etc/nginx/nginx.crt ];then
sscg -q --cert-file /etc/nginx/nginx.crt --cert-key-file /etc/nginx/nginx.key --ca-file /etc/nginx/ca.crt --lifetime 3650 --hostname $HOSTNAME --email root@$HOSTNAME
fi

%preun

%postun

%clean

%files
%defattr(0644, awx, awx, 0755)
#%doc nginx.conf.example
%attr(0755, root, root) /usr/bin/awx-manage
#%attr(0755, root, root) /opt/rh/rh-python36/root/usr/bin/awx-create-venv
#/usr/bin/awx-create-venv
%attr(0755, root, root) /usr/lib/systemd/system/*.service
%attr(0755, root, root) /usr/lib/python3.9/site-packages/awx*
%attr(0755, awx, awx) %{_prefix}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config %{service_configdir}/settings.py
%config /etc/nginx/conf.d/awx-rpm.conf
/usr/lib/systemd/system/awx.target
/etc/receptor/receptor-hop.conf
/etc/receptor/receptor-worker.conf
/etc/receptor/receptor.conf
/etc/receptor
#/usr/bin/ansible-tower-service
#/usr/bin/ansible-tower-setup
#/usr/bin/awx-python
#/usr/bin/failure-event-handler
#/usr/share/awx
#/usr/share/sosreport/sos/plugins/tower.py
#/var/lib/awx/favicon.ico
#/var/lib/awx/wsgi.py
/var/lib/awx/rsyslog
/var/lib/awx/projects
/var/lib/awx/job_status

%if 0%{?el7}
%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-dispatcher.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%attr(0644, root, root) %{_unitdir}/awx.service
%endif

%changelog
* Mon Feb 13 2023 22:55:34 +0000 Martin Juhl <m@rtinjuhl.dk> 21.11.0
- New version build: 21.11.0

