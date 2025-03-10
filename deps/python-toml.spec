
%global python3_pkgversion 3.11

Name:           python-toml
Version:        0.10.2
Release:        %autorelease
Summary:        Python Library for Tom's Obvious, Minimal Language

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/uiri/toml
Source:         %{pypi_source toml}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'toml' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-toml
Summary:        %{summary}

%description -n python%{python3_pkgversion}-toml %_description


%prep
%autosetup -p1 -n toml-%{version}


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


%files -n python%{python3_pkgversion}-toml -f %{pyproject_files}


%changelog
%autochangelog