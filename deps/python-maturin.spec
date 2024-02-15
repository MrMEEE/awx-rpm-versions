Name:           python-maturin
Version:        1.4.0
Release:        %autorelease
Summary:        Build and publish crates with pyo3, rust-cpython and cffi bindings as well as rust binaries as python packages

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyo3/maturin
Source:         %{pypi_source maturin}

BuildArch:      x86_64
BuildRequires:  python3-devel rust cargo


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'maturin' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-maturin
Summary:        %{summary}

%description -n python3-maturin %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras


%prep
%autosetup -p1 -n maturin-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
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


%files -n python3-maturin -f %{pyproject_files}


%changelog
%autochangelog