Name:           python-pyopenssl
Version:        23.2.0
Release:        %autorelease
Summary:        Python wrapper module around the OpenSSL library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pyopenssl.org/
Source:         %{pypi_source pyOpenSSL}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyopenssl' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyopenssl
Summary:        %{summary}

%description -n python3-pyopenssl %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pyopenssl docs,test


%prep
%autosetup -p1 -n pyOpenSSL-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-pyopenssl -f %{pyproject_files}


%changelog
%autochangelog