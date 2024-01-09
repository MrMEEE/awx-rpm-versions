Name:           python-django-ansible-base
Version:        20240109
Release:        1
Summary:        Django-ansible-base is exactly what it says it is. A base for any Ansible application which will leverage Django.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/django-ansible-base/
Source:         django-ansible-base-0.1.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel python3-django-auth-ldap


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-ansible-base' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-django-ansible-base
Summary:        %{summary}

%description -n python3-django-ansible-base %_description


%prep
%autosetup -p1 -n django-ansible-base


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


%files -n python3-django-ansible-base -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 20240109-1
- Initial package
