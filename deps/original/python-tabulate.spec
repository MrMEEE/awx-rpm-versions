Name:           python-tabulate
Version:        0.9.0
Release:        1%{?dist}
Summary:        Pretty-print tabular data

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/astanin/python-tabulate
Source:         %{pypi_source tabulate}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tabulate' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-tabulate
Summary:        %{summary}

%description -n python3-tabulate %_description


%prep
%autosetup -p1 -n tabulate-%{version}


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


%files -n python3-tabulate -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 0.9.0-1
- Initial package