Name:           python-sqlparse
Version:        0.4.4
Release:        1%{?dist}
Summary:        A non-validating SQL parser.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/sqlparse/
Source:         %{pypi_source sqlparse}
Patch:		sqlparse-python-explicit.patch

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlparse' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-sqlparse
Summary:        %{summary}

%description -n python3-sqlparse %_description


%prep
%autosetup -p1 -n sqlparse-%{version}


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


%files -n python3-sqlparse -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 0.4.4-1
- Initial package