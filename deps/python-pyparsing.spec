
%global python3_pkgversion 3.11

Name:           python-pyparsing
Version:        3.1.2
Release:        %autorelease
Summary:        pyparsing module - Classes and methods to define and execute parsing grammars

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyparsing/pyparsing/
Source:         %{pypi_source pyparsing}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyparsing' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyparsing
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyparsing %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-pyparsing diagrams


%prep
%autosetup -p1 -n pyparsing-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x diagrams


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-pyparsing -f %{pyproject_files}


%changelog
%autochangelog