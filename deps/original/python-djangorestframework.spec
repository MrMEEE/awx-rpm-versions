
%global python3_pkgversion 3.11

Name:           python-djangorestframework
Version:        3.15.1
Release:        %autorelease
Summary:        Web APIs for Django, made easy.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://www.django-rest-framework.org/
Source:         %{pypi_source djangorestframework}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'djangorestframework' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-djangorestframework
Summary:        %{summary}

%description -n python%{python3_pkgversion}-djangorestframework %_description


%prep
%autosetup -p1 -n djangorestframework-%{version}


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


%files -n python%{python3_pkgversion}-djangorestframework -f %{pyproject_files}


%changelog
%autochangelog