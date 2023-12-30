Name:           python-setuptools-scm
Version:        7.1.0
Release:        1%{?dist}
Summary:        the blessed package to manage your versions by scm tags

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/setuptools-scm/
Source:         %{pypi_source setuptools_scm}

BuildArch:      noarch
BuildRequires:  python3-devel python3-toml


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools-scm' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-setuptools-scm
Summary:        %{summary}

%description -n python3-setuptools-scm %_description

%pyproject_extras_subpkg -n python3-setuptools-scm toml

%prep
%autosetup -p1 -n setuptools_scm-%{version}


%generate_buildrequires
%pyproject_buildrequires -x toml


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-setuptools-scm -f %{pyproject_files}


%changelog
* Sat Dec 30 2023 Martin Juhl <m@rtinjuhl.dk> - 7.1.0-1
- Initial package