
%global python3_pkgversion 3.11

Name:           python-semver
Version:        3.0.4
Release:        %autorelease
Summary:        Python helper for Semantic Versioning (https://semver.org)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/semver/
Source:         %{pypi_source semver}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'semver' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-semver
Summary:        %{summary}

%description -n python%{python3_pkgversion}-semver %_description


%prep
%autosetup -p1 -n semver-%{version}


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


%files -n python%{python3_pkgversion}-semver -f %{pyproject_files}


%changelog
%autochangelog