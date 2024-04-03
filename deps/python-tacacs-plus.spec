
%global python3_pkgversion 3.11

Name:           python-tacacs-plus
Version:        1.0
Release:        %autorelease
Summary:        A client for interacting with TACACS+ servers

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://github.com/ansible/tacacs_plus
Source:         %{pypi_source tacacs_plus}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tacacs-plus' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-tacacs-plus
Summary:        %{summary}

%description -n python%{python3_pkgversion}-tacacs-plus %_description


%prep
%autosetup -p1 -n tacacs_plus-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
mv $RPM_BUILD_ROOT/usr/bin/tacacs_plus $RPM_BUILD_ROOT/usr/bin/tacacs_plus%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/tacacs_plus|/usr/bin/tacacs_plus%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-tacacs-plus -f %{pyproject_files}


%changelog
%autochangelog