%undefine __brp_python_bytecompile
%global python3_pkgversion 3.11

Name:           python-ntlm
Version:        1.1.0
Release:        %autorelease
Summary:        Python library that provides NTLM support, including an authentication handler for urllib2. Works with pass-the-hash in additon to password authentication.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://code.google.com/p/python-ntlm
Source:         %{pypi_source python-ntlm}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-ntlm' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python-ntlm
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python-ntlm %_description


%prep
%autosetup -p1 -n python-ntlm-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build


%install

%check

%files -n python%{python3_pkgversion}-python-ntlm 

%changelog
%autochangelog
