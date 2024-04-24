
%global python3_pkgversion 3.11

Name:           python-django-ansible-base
Version:        20240411
Release:        %autorelease
Summary:        Reserved package

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/django-ansible-base/
Source:         https://github.com/MrMEEE/django-ansible-base/archive/refs/tags/v2024.04.11.tar.gz
Patch:		django-ansible-base-versionfix.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-ansible-base' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-ansible-base
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-ansible-base %_description

%pyproject_extras_subpkg -n python%{python3_pkgversion}-django-ansible-base rest_filters,jwt_consumer

%prep
%autosetup -p1 -n django-ansible-base-2024.04.11


%generate_buildrequires
%pyproject_buildrequires -x rest_filters,jwt_consumer


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-django-ansible-base -f %{pyproject_files}


%changelog
%autochangelog