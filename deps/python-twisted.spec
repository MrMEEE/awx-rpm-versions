%bcond_without check
%global python3_pkgversion 3.11

Name:           python-twisted
Version:        23.10.0
Release:        %autorelease
Summary:        An asynchronous networking framework written in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://twistedmatrix.com/
Source:         %{pypi_source twisted}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel python%{python3_pkgversion}-cryptography python%{python3_pkgversion}-bcrypt python%{python3_pkgversion}-pyasn1 python%{python3_pkgversion}-tkinter python%{python3_pkgversion}-hamcrest glibc-langpack-en python%{python3_pkgversion}-pyopenssl


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twisted' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-twisted
Summary:        %{summary}

%description -n python%{python3_pkgversion}-twisted %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-twisted python3-twisted http2,tls


%prep
%autosetup -p1 -n twisted-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x http2,tls


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-twisted -f %{pyproject_files}


%changelog
%autochangelog
