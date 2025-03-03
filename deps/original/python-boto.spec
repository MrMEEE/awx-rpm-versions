
%global python3_pkgversion 3.11

Name:           python-boto
Version:        2.49.0
Release:        %autorelease
Summary:        Amazon Web Services Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/boto/boto/
Source:         %{pypi_source boto}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'boto' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-boto
Summary:        %{summary}

%description -n python%{python3_pkgversion}-boto %_description


%prep
%autosetup -p1 -n boto-%{version}


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


%files -n python%{python3_pkgversion}-boto -f %{pyproject_files}


%changelog
%autochangelog