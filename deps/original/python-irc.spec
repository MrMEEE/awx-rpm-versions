Name:           python-irc
Version:        20.1.0
Release:        %autorelease
Summary:        IRC (Internet Relay Chat) protocol library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/jaraco/irc
Source:         %{pypi_source irc}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'irc' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-irc
Summary:        %{summary}

%description -n python3-irc %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-irc docs,testing


%prep
%autosetup -p1 -n irc-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-irc -f %{pyproject_files}


%changelog
%autochangelog