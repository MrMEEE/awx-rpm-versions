Name:           python-cryptography
Version:        41.0.3
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/cryptography/
Source:         %{pypi_source cryptography}

BuildArch:      x86_64
BuildRequires:  python3-devel rust cargo openssl-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cryptography' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-cryptography
Summary:        %{summary}

%description -n python3-cryptography %_description


%prep
%autosetup -p1 -n cryptography-%{version}


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


%files -n python3-cryptography -f %{pyproject_files}


%changelog
* Sat Dec 30 2023 Martin Juhl <m@rtinjuhl.dk> - 41.0.3-1
- Initial package