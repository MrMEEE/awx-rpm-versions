Name:           python-django-filter
Version:        23.5
Release:        1%{?dist}
Summary:        Django-filter is a reusable Django application for allowing users to filter querysets dynamically.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/carltongibson/django-filter/tree/main
Source:         %{pypi_source django-filter}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-filter' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-filter
Summary:        %{summary}

%description -n python3-django-filter %_description


%prep
%autosetup -p1 -n django-filter-%{version}


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


%files -n python3-django-filter -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 23.5-1
- Initial package