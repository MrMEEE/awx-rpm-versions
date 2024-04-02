
%global python3_pkgversion 3.11

Name:           python-pyasn1
Version:        0.6.0
Release:        %autorelease
Summary:        Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pyasn1/pyasn1
Source:         %{pypi_source pyasn1}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyasn1' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-pyasn1
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyasn1 %_description


%prep
%autosetup -p1 -n pyasn1-%{version}


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


%files -n python%{python3_pkgversion}-pyasn1 -f %{pyproject_files}


%changelog
%autochangelog