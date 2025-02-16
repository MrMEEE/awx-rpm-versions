
%global python3_pkgversion 3.11

Name:           python-aiohappyeyeballs
Version:        2.4.4
Release:        %autorelease
Summary:        Happy Eyeballs for asyncio

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/aio-libs/aiohappyeyeballs
Source:         %{pypi_source aiohappyeyeballs}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiohappyeyeballs' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-aiohappyeyeballs
Summary:        %{summary}

%description -n python%{python3_pkgversion}-aiohappyeyeballs %_description


%prep
%autosetup -p1 -n aiohappyeyeballs-%{version}


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


%files -n python%{python3_pkgversion}-aiohappyeyeballs -f %{pyproject_files}


%changelog
%autochangelog