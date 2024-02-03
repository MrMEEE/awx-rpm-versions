Name:           python-cryptography
Version:        36.0.2
Release:        %autorelease
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyca/cryptography
Source:         %{pypi_source cryptography}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libopenssl-devel
BuildRequires:  gcc-c++

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
%autochangelog
