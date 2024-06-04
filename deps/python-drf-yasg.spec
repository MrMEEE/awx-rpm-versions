
%global python3_pkgversion 3.11

Name:           python-drf-yasg
Version:        1.21.7
Release:        %autorelease
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/axnsan12/drf-yasg
Source:         %{pypi_source drf-yasg}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'drf_yasg' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-drf-yasg
Summary:        %{summary}

%description -n python%{python3_pkgversion}-drf-yasg %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-drf-yasg coreapi,validation


%prep
%autosetup -p1 -n drf-yasg-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x coreapi,validation


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-drf-yasg -f %{pyproject_files}


%changelog
%autochangelog