Name:           python-cachecontrol
Version:        0.13.1
Release:        1%{?dist}
Summary:        httplib2 caching for requests

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/CacheControl/
Source:         %{pypi_source cachecontrol}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cachecontrol' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-cachecontrol
Summary:        %{summary}

%description -n python3-cachecontrol %_description


%prep
%autosetup -p1 -n cachecontrol-%{version}


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


%files -n python3-cachecontrol -f %{pyproject_files}


%changelog
* Wed Sep 20 2023 Martin Juhl <m@rtinjuhl.dk> - 0.13.1-1
- Initial package