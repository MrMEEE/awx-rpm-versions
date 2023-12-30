Name:           python-jwcrypto
Version:        1.4.2
Release:        1%{?dist}
Summary:        Implementation of JOSE Web standards

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/latchset/jwcrypto
Source:         %{pypi_source jwcrypto}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jwcrypto' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-jwcrypto
Summary:        %{summary}

%description -n python3-jwcrypto %_description


%prep
%autosetup -p1 -n jwcrypto-%{version}


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


%files -n python3-jwcrypto -f %{pyproject_files}


%changelog
* Sat Dec 30 2023 Martin Juhl <m@rtinjuhl.dk> - 1.4.2-1
- Initial package