
%global python3_pkgversion 3.11

Name:           python-ansible-builder
Version:        3.0.1
Release:        %autorelease
Summary:        "A tool for building Ansible Execution Environments"

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://ansible-builder.readthedocs.io
Source:         %{pypi_source ansible-builder}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-setuptools_scm
Patch: ansible-builder-scm-version.patch

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansible-builder' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-ansible-builder
Summary:        %{summary}

%description -n python%{python3_pkgversion}-ansible-builder %_description


%prep
%autosetup -p1 -n ansible-builder-%{version}


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
mv $RPM_BUILD_ROOT/usr/bin/ansible-builder $RPM_BUILD_ROOT/usr/bin/ansible-builder%{python3_pkgversion}
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
sed -i "s|/usr/bin/ansible-builder|/usr/bin/ansible-builder%{python3_pkgversion}|g" %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-ansible-builder -f %{pyproject_files}


%changelog
%autochangelog