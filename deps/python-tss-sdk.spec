
%global python3_pkgversion 3.11

Name:           python-tss-sdk
Version:        1.2.3
Release:        %autorelease
Summary:        The Delinea Secret Server Python SDK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/python-tss-sdk/
Source:         %{pypi_source python_tss_sdk}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-tss-sdk' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-python-tss-sdk
Summary:        %{summary}

%description -n python%{python3_pkgversion}-python-tss-sdk %_description


%prep
%autosetup -p1 -n python_tss_sdk-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
rm -rf $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/delinea/__init__.py
rm -rf $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/delinea/__pycache__
rm -rf $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/delinea/secrets/__init__.py
rm -rf $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/delinea/secrets/__pycache__/__init__*
%pyproject_save_files '*' +auto
sed -i "/__init__.py/d" %{pyproject_files}
sed -i "/delinea\/__pycache__/d" %{pyproject_files}
sed -i "/__pycache__\/__init__/d" %{pyproject_files}

%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-python-tss-sdk -f %{pyproject_files}


%changelog
%autochangelog
