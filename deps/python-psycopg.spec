%global debug_package %{nil}

Name:           python-psycopg
Version:        3.1.9
Release:        1%{?dist}
Summary:        PostgreSQL database adapter for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://psycopg.org/
Source:         %{pypi_source psycopg}
Patch:		psycopg-deps.patch

BuildArch:      x86_64
BuildRequires:  python3-devel libpq-devel gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'psycopg' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-psycopg
Summary:        %{summary}


%description -n python3-psycopg %_description


%prep
%autosetup -p1 -n psycopg-%{version}


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


%files -n python3-psycopg -f %{pyproject_files}


%changelog
* Sat Dec 30 2023 Martin Juhl <m@rtinjuhl.dk> - 3.1.9-1
- Initial package
