
%global python3_pkgversion 3.11

Name:           python-h11
Version:        0.14.0
Release:        %autorelease
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/1.1

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-hyper/h11
Source:         %{pypi_source h11}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'h11' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-h11
Summary:        %{summary}

%description -n python%{python3_pkgversion}-h11 %_description


%prep
%autosetup -p1 -n h11-%{version}


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


%files -n python%{python3_pkgversion}-h11 -f %{pyproject_files}


%changelog
%autochangelog