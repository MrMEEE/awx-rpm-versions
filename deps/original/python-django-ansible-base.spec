
%global python3_pkgversion 3.11

Name:           python-django-ansible-base
Version:        2025.3.7
Release:        %autorelease
Summary:        A Django app used by ansible services

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/django-ansible-base/
Source:         %{pypi_source django_ansible_base}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-ansible-base' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-django-ansible-base
Summary:        %{summary}

%description -n python%{python3_pkgversion}-django-ansible-base %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-django-ansible-base all,api-documentation,authentication,channel-auth,feature-flags,jwt-consumer,oauth2-provider,redis-client,resource-registry,testing


%prep
%autosetup -p1 -n django_ansible_base-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,api-documentation,authentication,channel-auth,feature-flags,jwt-consumer,oauth2-provider,redis-client,resource-registry,testing


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