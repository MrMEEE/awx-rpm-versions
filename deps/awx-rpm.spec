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

Summary: Ansible AWX-RPM
Name: awx-rpm
Version: 30.0.0
Release: 38%{dist}
#Source0: awx-30.0.0.tar.gz
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
#Patch0: awx-patch.patch-%{version}
#Patch1: awx-rpm-extract-strings.patch-%{version}
#Patch2: awx-rpm-branding.patch-%{version}
License: GPLv3
Group: AWX
URL: https://awx.wiki
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

Requires: python%{python3_pkgversion} awx-core awx-ui awx-rpm-manage
Requires: python3.11-adal = 1.2.7
Requires: python3.11-aiodns = 3.2.0
Requires: python3.11-aiohappyeyeballs = 2.4.4
Requires: python3.11-aiohttp = 3.11.11
Requires: python3.11-aiohttp-retry = 2.8.3
Requires: python3.11-aiohttp+speedups = 3.11.11
Requires: python3.11-aiosignal = 1.3.2
Requires: python3.11-ansi2html = 1.9.2
Requires: python3.11-ansible-builder = 3.1.0
Requires: python3.11-ansible-runner = 2.4.0
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
Requires: python3.11-awx-plugins-core = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-aim = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-aws-secretsmanager-credential = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-azure-kv = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-centrify-vault-kv = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-conjur = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-github-app = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-hashivault-kv = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-hashivault-ssh = 0.0.1~a9
Requires: python3.11-awx-plugins-core+credentials-thycotic-dsv = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-azure-rm = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-constructed = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-controller = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-ec2 = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-gce = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-insights = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-openshift-virtualization = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-openstack = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-rhv = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-satellite6 = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-terraform = 0.0.1~a9
Requires: python3.11-awx-plugins-core+inventory-vmware = 0.0.1~a9
Requires: python3.11-awx-plugins-interfaces = 0.0.1~a4
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
Requires: python3.11-boto = 2.49.0
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
Requires: python3.11-decorator = 5.2.1
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
Requires: python3.11-fabric = 3.2.2
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
Requires: python3.11-invoke = 2.2.0
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
Requires: python3.11-paramiko = 3.5.1
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
Requires: python3.11-prettytable = 3.15.1
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
Requires: python3.11-pygithub = 2.6.1
Requires: python3.11-pygments = 2.19.1
Requires: python3.11-pyjwt = 2.10.1
Requires: python3.11-pyjwt+crypto = 2.10.1
Requires: python3.11-pynacl = 1.5.0
Requires: python3.11-pyopenssl = 24.3.0
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
Requires: python3.11-wcwidth = 0.2.13
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

%build

%install

mkdir -p $RPM_BUILD_ROOT/var/lib/awx/rsyslog
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/projects
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/job_status
mkdir -p %{buildroot}/etc/tower

cp %{_sourcedir}/settings.py-%{version} %{buildroot}%{service_configdir}/settings.py
mkdir -p %{buildroot}%{_prefix}/public
mkdir -p %{buildroot}/usr/lib/systemd/system
# awx-channels-worker awx
#for service in awx-wsrelay awx-ws-heartbeat awx-daphne awx-dispatcher awx-receiver awx-receptor awx-receptor-hop awx-receptor-worker; do
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

mkdir -p $RPM_BUILD_ROOT/etc/nginx/conf.d/

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
#%attr(0755, root, root) /usr/bin/awx-manage
%attr(0755, root, root) /usr/lib/systemd/system/*.service
#%attr(0755, root, root) /usr/lib/python%{python3_pkgversion}/site-packages/awx*
#%attr(0755, awx, awx) %{_prefix}
#%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
#%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
#%{service_homedir}/.tower_version
#%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config(noreplace) %{service_configdir}/settings.py
%config /etc/nginx/conf.d/awx-rpm.conf
/usr/lib/systemd/system/awx.target
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

%changelog
* Thu Mar 06 2025 01:59:30 AM CET +0100 Martin Juhl <m@rtinjuhl.dk> 30.0.0
- New version build: 30.0.0
- (HEAD -> devel, tag: 30.0.0, origin/devel, origin/HEAD) Test
- Update calver.yml
- Update calver.yml
- Token
- Update calver.yml
- Update calver.yml
- Update calver.yml
- Create calver.yml
- Remove workflows
- remove actions
- Use correct devel image for docker-compose (#15836)
- Continue if pre-warm cache fail in container build (#15835)
- Fix git credential for devel_image build (#15834)
- Add ability to provide token for private repo for requirements_git in container build (#15831)
- Update feature flag list test (#15830)
- Publish image base on git repo name instead of hard coded to AWX (#15828)
- Make awx/main/tests/live dramatically faster (#15780)
- Fix rsyslog permission error in github ubuntu tests from apparmor (#15717)
- Fix rrule fast forwarding across DST boundaries (#15809)
- Set feature flag base on setting (#15808)
- [AAP-39138] - Add DAB Feature Flag common API (#15786)
- AAP-38528 Make default state passing for coverage targets (#15772)
- Add helper to proxy analytics requests
- Put duplicate plugin location in error message (#15781)
- Removing some (but not all) dead pytest fixtures (#15782)
- Address Lookup Plugins AttributeError (#15770)
- fix: compatibility with black v25+ (#15789)
- Remove old jwcrypto tar from licenses since we included the upgraded version (#15783)
- Remove Docker Desktop if statement (#15778)
- Move some more tests out of root functional folder (#15753)
- Add ee cleanup tests
- Use upload artifact v4
- remove old psycopg tar file that we do not use
- fix: azure credential awxkit client_id collision
- Establish a feature flag for indirect host counting feature (#15759)
- Create test for using manual ¤CHANGELOG¤ file projects (#15754)
- fix: invalid f-string and oidc url for insights plugin
- feat: support insights service account credentials for project update
- feat: update insights action plugin to handle oauth (#15742)
- Add new credential entry point discovery (#15685)
- Add changelog to awx collection
- Use advisory_lock from DAB (#15676)
- Bump awx collection ansible required version
- Remove coarse grain unused import
- Fix ansible-lint empty lines in module docstrings
- Fix ansible-lint truthy in module docstrings
- Fix ansible-lint indentation in module docstrings
- Fix editable dependencies volume name
- Add client_secret and client_id to credential_input_fields (#15734)
- Update logstash container image and remove ELK stack (#15744)
- Switch from dockerhub to gcr mirror (#15743)
- bust the cache
- Add insights service account support to collection
- Add test to ensure bootstrap reqs are good (#15733)
- Add input_inventories to ordered_associations (#15710)
- Fix dependency upgrades (#15740)
- Delete test file that should have been removed and fix checks (#15739)
- AAP-37080 Delete the cleanup_tokens system job template (#15711)
- Fix API documentation rendering (#15116) (#15726)
- General upgrade of dependencies (#15705)
- AAP-37989 Tests for exclude list with multiple jobs (#15722)
- Disable color logs in CI (#15719)
- Bugfix: adjust incorrectly passed keywords with exclude-strings argument (#15721)
- Move RBAC functional tests into folder (#15723)
- Move cred type unite tests to awx-plugins
- Remove inject_credential from awx
- Point at inject credentials
- AAP-36604 (analytics) Thousands of zombie/orphaned Slow/Stuck DB queries in controller querying active host count (#15715)
- Cleanup in-memory data from test that randomly causes other failures (#15716)
- Fix test warnings that escaped somehow (#15714)
- Upload container logs for live tests (#15713)
- Min value should be Decimal (#15413)
- AAP-36536 Send job_lifecycle logs to external loggers (#15701)
- host_metrics date fix to make summary dates (datetime.datetime) comparable to month: datetime.date (#15704)
- Pull the correct collection plugin for the product (#15658)
- Do not fast forward rrule if count is set (#15696)
- Use runtime log utility moved to DAB (#15675)
- bump sqlparse to meet DAB requirement (#15697)
- Fix misused project cache identifier (#15690)
- Flake8 fix
- Add custom_injectors to test code path
- Load all plugins in order to test them
- Rename post_injectors to custom_injectors
- Adopt post_injectors change from awx-plugins
- Fix missing exception catch in `create_partition` (#15691)
- Make dev script work in combined environment (#15684)
- Create a new pytest folder for live system testing with normal services (#15688)
- Update defaults.py receptor typo (#15682)
- fix: reset state before evaluating named urls (#15683)
- Fix receptor work unit release after completion (#15679)
- feat: enable django flags support (#15660)
- use subproject url prefix (#15681)
- Add the Sphinx notfound page extension (#15669)
- Fix missing dependencies due to extras `-` vs `_` (#15677)
- Ignore warnings so people can run tests on python 3.12 (#15663)
- Decouple inject_credentials from dynamic inputs
- add custom 404 page (#15668)
- Remove oauth provider (#15666)
- Address unclosed fd warnings
- 🧪 Make pytest notify us about future warnings
- Add descriptions for plugin names (#15643)
- Removed UI-focused user docs from AWX. (#15641)
- Do not check error state if null (#15655)
- Revive the logstash container for testing (#15654)
- Make rrule fast forwarding stable (#15601)
- feat: remove collection support for oauth (#15623)
- Removal of OAuth2 stuff from CLI
- Fix server error from system job detail view (#15640)
- Add option to skip credential type discovery
- Fix error with CLI monitor of ad hoc output (#15642)
- Add test that resource list does not server error (#15635)
- fix: invalid response type on post request (#15609)
- Set coverage limits so we do not have current failures (#15629)
- Make lookup plugins return lists to fix failures (#15625)
- Fix for 'relation "social_auth_usersocialauth" does not exist' error (#15626)
- feat: install awx collection from source (#15617)
- Metrics dispatcher callback receiver swaparoo
- Install awx collection from branch for operator ci
- Updated Authentication section to reflect AWX only method. (#15602)
- Removed oAuth methods from collection docs. (#15606)
- Fix bug where unrelated jobs were linked as dependencies (#15610)
- fix: increase max verbosity level for constructed inventory (#15604)
- Add back git requirements as comments ¤CHANGELOG¤ re-run script (#15317)
- Make cloud providers dynamic (#15537)
- bump django 4.2.16 to be in line with DAB (#15596)
- Add gateway support to awxkit (#15576)
- remove oauth use
- 3rd party auth removal cleanup
- Remove sso app (#15550)
- Remove SAML authentication (#15568)
- Remove OIDC (#15569)
- Removed more mentions about SAML. (#15565)
- Remove Keycloak (#15567)
- Remove social oauth (Azure, Github, Google) (#15549)
- Remove RADIUS authentication (#15548)
- Remove TACACS+ authentication (#15547)
- Remove LDAP authentication (#15546)
- Prettier DRF pages when using trusted proxy (#15579)
- Add splitted up inventory source plugins (#15584)
- Fix CI for newer debian image (#15583)
- Adding podAntiAffinity (#15578)
- Update AWX collection to use basic authentication (#15554)
- Use awx-plugins-shared code from `awx_plugins.interfaces` (#15566)
- Fix 500 error due to None data in DAB response (#15562)
- Removed docs associated with SAML auth. (#15563)
- Filter out ANSIBLE_BASE_ from job env var (#15558)
- Removed docs associated with OIDC auth (#15557)
- Enable service redirect auth and reverse-sync from DAB (#15489)
- Upload the test results for awx-collection to dashboard (#15543)
- 🧪 Publish awxkit's coverage to Codecov (#15525)
- Make analytics job ts settings hidden
- 🧪 Run sanity tests w/ ansible-test-gh-action (#15539)
- 🧪🚑 Fix escaping EOLs in `curl` invocation (#15538)
- 🧪 Upload ansible-test coverage to Codecov (#15527)
- Upload API unit test results to dashboard (#15532)
- 🧪 Upload coverage from the rest of CI jobs (#15526)
- 🧪 Delegate source filtering to coverage.py (#15528)
- 🧪 Use xunit1 in pytest by default (#15524)
- 🧪💅 Unignore errors in `coveragerc` (#15523)
- 🧪 Include coverage measurement @ site-packages (#15521)
- Docs: change Getting started EE guide reference to point to the relevant location (#15502)
- fix: maintain order of insertions into m2m relationship tables (#15536)
- Plugin removals for docs (#15505)
- Remove ML remnants from docs (#15500)
- update remaining urls for new UI (#15529)
- fix workflow job url (#15522)
- 🧪 Use modern `source_pkgs` @ `coveragerc` (#15519)
- 🧪 Pass specific report files to `codecov-cli` (#15520)
- Validate org-user membership from gateway (#15508)
- Fix instance UI URL generated by API (#15517)
- fix: change to url in platform ui (#15518)
- 🧪💅 Categorize the Codecov status checks (#15516)
- 🧪💅 Migrate to `exclude_also` @ `coveragerc` (#15513)
- 🧪🚑 Fix checking schema in CI on merge (#15514)
- 🧪💄 Order settings in `coveragerc` (#15515)
- 🧪 Unmeasure coverage in tests expected to fail (#15512)
- 🧪🚑 Fix running awx image in CI on merge (#15510)
- 🧪🚑 Fix fetching the CI image on merges (#15509)
- Replace `pkg_resources` with `importlib.metadata` (#15441)
- 🧪 Upload the `devel` branch coverage to Codecov (#15507)
- Add OPTIONAL_UI_URL_PREFIX (#15506)
- 🧪 Gather coverage @ CI and upload to Codecov (#15499)
- fix: avoid race conditions when removing multiple instance  (#15495)
- Register CredentialType(s) every time Django loads
- Removes collection of unpartitioned_events table (#15501)
- Hide AUTOMATION_ANALYTICS_LAST_GATHER (#15497)
- Unpin OpenSSL (#15498)
- Fix analytic ship (#15496)
- Translate new RBAC to old RBAC (#15490)
- Fix subscription username password setting name (#15493)
- CONTRIBUTING.md: remove IRC remnants (#15492)
- Move credential code up a dir
- Fix awx-plugins to use #egg=<package_name>
- Use awx-plugins instead
- Delete cred and inv plugins
- move inv and cred plugins into awx_plugins
- Remove references to IRC ¤CHANGELOG¤ Google Groups (#15480)
- Fix SAMLAuth backend to correctly return social auth pipeline results (#15457)
- Fallback to use subscription cred for analytic upload (#15479)
- catch harakiri graceful signal in middlware and log debug info
- Remove archaic monkey patches (#15338)
- Docs: add Communication guide (#15469)
- Rename System Auditor to Controller System Auditor (#15470)
- Pin DAB to devel again (#15467)
- Fix 500 error when ordinary user viewed system JTs (#15465)
- Make controller specific team and org roles (#15445)
- Remove old UI (#15414)
- fix: avoid calling undefined method for anonymous users (#15440)
- fix: catch correct exception when parsing filter (#15458)
- Replace ansiconv with ansi2html (#15328)
- Update django-ansible-base version to 2024.8.19 (#15454)
- Rewrite more access logic in terms of permissions instead of roles (#15453)
- SSO login should redirect to new UI index (#15456)
- Guard around race condition (#15452)
- Update editable deps docs (#15451)
- Unpin django-guid and update license (#15381)
- Unpin django-split-settings (#15379)
- Fixes pytest CI error
- Bump DAB version manually because bot is on vacation (#15434)
- Remove 'AWX' from setting endpoint (#15432)
- Fix a test in preparation for syncing description
- Only refresh session if updating own password (#15426)
- Unpin channels-redis (#15329)
- Re-do PR #14685 for alt-text inventories. (#15394)
- Added docs for OTel - awx integration (#15408)
- Make ui_next the default UI (#15405)
- Bump django-ansible-base to 2024.7.17 (#15373)
- Improve asyncio debugging (#15398)
- Replaced all references of downstream docs to upstream docs (#15388)
- Add UI for RECEPTOR_KEEP_WORK_ON_ERROR
- Add RECEPTOR_KEEP_WORK_ON_ERROR setting
- Fix depends_on for awx devel when editable dependencies is enabled (#15393)
- Loosen up team EE restrictions (#15384)
- Upgrade to v4 checkout, hide output (#15322)
- Update test to conform with new DAB change (#15385)
- Fix create_preload_data to allow running without an admin user created (#15356)
- Remove remnants of controller terms from quickstart docs (#15350)
- Remove references to translated versions of the docs (#15354)
- Remove links from docker-compose template (#15386)
- Fix test_url_base_defaults_to_request to reference local host instead… (#15367)
- Create receptor group if missing (#15276)
- Update  docs replacements to AWX (#15349)
- Fix ui-next build for release staging GHA (#15383)
- Disable dab-release GHA on fork unless explicitly triggered  (#15382)
- Update DAB update automation PR template (#15376)
- Allow deleting org of a running workflow job (#15374)
- update terminology (#15357)
- Pin 3rd party action at SHA
- Put DAB version in the PR title
- Run at 6 am every day
- Update .github/workflows/dab-release.yml
- Update .github/workflows/dab-release.yml
- Check and update django-ansible-base
- Updated the api file to reflect 2024 date (#15369)
- Build new/old UI with different nodejs version (#15368)
- Fix minor docker build warning (#15362)
- Fix task ending in error due to bad iterator (#15355)
- Check member of org when granting cred (#15353)
- Fix command to set db session timeout for locks (#15352)
- Fix EE admin not being able to PATCH/PUT object while providing `organization` (#15348)
- Log conflicts and created items by the periodic resource sync (#15337)
- Update ActivityStream UI query to order by id (#15346)
- Added note to API guide for filtering exact matches (#15332)
- Callback for role assignment (#15339)
- Do not reference self.messages when it does not exist (#15331)
- Add complete test that we have analogs to old versions of roles, fix some mismatches (#15321)
- Suppress docker pull output in checks (#15323)
- Fix server error assigning teams EE object roles (#15320)
