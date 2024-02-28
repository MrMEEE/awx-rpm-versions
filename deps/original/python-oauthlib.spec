Name:           python-oauthlib
Version:        3.2.2
Release:        %autorelease
Summary:        A generic, spec-compliant, thorough implementation of the OAuth request-signing logic

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/oauthlib/oauthlib
Source:         %{pypi_source oauthlib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oauthlib' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-oauthlib
Summary:        %{summary}

%description -n python3-oauthlib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-oauthlib rsa,signals,signedtoken


%prep
%autosetup -p1 -n oauthlib-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x rsa,signals,signedtoken


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-oauthlib -f %{pyproject_files}


%changelog
%autochangelog