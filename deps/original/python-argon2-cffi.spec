
%global python3_pkgversion 3.11

Name:           python-argon2-cffi
Version:        23.1.0
Release:        %autorelease
Summary:        Argon2 for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/argon2-cffi/
Source:         %{pypi_source argon2_cffi}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'argon2-cffi' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-argon2-cffi
Summary:        %{summary}

%description -n python%{python3_pkgversion}-argon2-cffi %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-argon2-cffi dev,docs,tests,typing


%prep
%autosetup -p1 -n argon2_cffi-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,tests,typing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-argon2-cffi -f %{pyproject_files}


%changelog
%autochangelog