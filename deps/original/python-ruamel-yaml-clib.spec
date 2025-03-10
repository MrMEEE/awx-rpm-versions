
%global python3_pkgversion 3.11

Name:           python-ruamel-yaml-clib
Version:        0.2.12
Release:        %autorelease
Summary:        C version of reader, parser and emitter for ruamel.yaml derived from libyaml

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/ruamel.yaml.clib/
Source:         %{pypi_source ruamel.yaml.clib}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ruamel-yaml-clib' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-ruamel-yaml-clib
Summary:        %{summary}

%description -n python%{python3_pkgversion}-ruamel-yaml-clib %_description


%prep
%autosetup -p1 -n ruamel.yaml.clib-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-ruamel-yaml-clib -f %{pyproject_files}


%changelog
%autochangelog