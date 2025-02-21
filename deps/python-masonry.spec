
%global python3_pkgversion 3.11

Name:           python-masonry
Version:        0.1.2
Release:        %autorelease
Summary:        A command line tool for composable project templating.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/MrKriss/masonry
Source:         %{pypi_source masonry}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'masonry' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-masonry
Summary:        %{summary}

%description -n python%{python3_pkgversion}-masonry %_description


%prep
%autosetup -p1 -n masonry-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
touch README.rst

%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-masonry -f %{pyproject_files}


%changelog
%autochangelog
