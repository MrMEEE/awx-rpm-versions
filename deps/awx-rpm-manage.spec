%define  debug_package %{nil}

Summary: Ansible AWX-RPM Management Tools
Name: awx-rpm-manage
Version: 1.0
Release: 2%{dist}
Source0: awx-rpm-manage-1.0.tar.gz
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: python3 
Requires: python3 

%description
%{summary}

%prep
%setup -n awx-rpm-manage-%version
%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp awx-rpm-manage $RPM_BUILD_ROOT/usr/bin/awx-rpm-manage

%pre
/usr/bin/getent group awx >/dev/null || /usr/sbin/groupadd --system awx
/usr/bin/getent passwd awx >/dev/null || /usr/sbin/useradd --no-create-home --system -g awx --home-dir /opt/awx-rpm -s /bin/bash awx
/usr/sbin/usermod -s /bin/bash awx

%clean

%files
%defattr(0755, awx, awx, 0755)
/usr/bin/awx-rpm-manage

%changelog
* Fri Mar 15 2024 11:35:20 PM CET +0100 Martin Juhl <m@rtinjuhl.dk> 1.0
- New version build: 1.0

