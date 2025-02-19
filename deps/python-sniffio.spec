
%global python3_pkgversion 3.11

Name:           python-sniffio
Version:        1.3.1
Release:        %autorelease
Summary:        Sniff out which async library your code is running under

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-trio/sniffio
Source:         %{pypi_source sniffio}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sniffio' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-sniffio
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sniffio %_description


%prep
%autosetup -p1 -n sniffio-%{version}


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


%files -n python%{python3_pkgversion}-sniffio -f %{pyproject_files}


%changelog
%autochangelog