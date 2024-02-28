Name:           python-azure-core
Version:        1.26.1
Release:        %autorelease
Summary:        Microsoft Azure Core Library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core
Source:         %{pypi_source azure-core %{version} zip}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'azure-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-azure-core
Summary:        %{summary}

%description -n python3-azure-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-azure-core aio


%prep
%autosetup -p1 -n azure-core-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aio


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-azure-core -f %{pyproject_files}


%changelog
%autochangelog