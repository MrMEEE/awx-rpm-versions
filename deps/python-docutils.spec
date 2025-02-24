
%global python3_pkgversion 3.11

Name:           python-docutils
Version:        0.21.2
Release:        %autorelease
Summary:        Docutils -- Python Documentation Utilities

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://docutils.sourceforge.io
Source:         %{pypi_source docutils}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'docutils' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-docutils
Summary:        %{summary}

%description -n python%{python3_pkgversion}-docutils %_description


%prep
%autosetup -p1 -n docutils-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files

# START RENAMING OF BINARIES 1
%if "%{python3_pkgversion}" != "3"
cd $RPM_BUILD_ROOT/usr/bin/
for i in `ls`;do
echo "Renaming $i to $(echo $i)%{python3_pkgversion}"
mv $RPM_BUILD_ROOT/usr/bin/$i $RPM_BUILD_ROOT/usr/bin/$(echo $i)%{python3_pkgversion}
done
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
cd $RPM_BUILD_ROOT/usr/bin/
for i in `ls |sed "s/%{python3_pkgversion}//g"`;do
echo "Renaming: $i to $(echo $i)%{python3_pkgversion}"
sed -i "s|/usr/bin/$i|/usr/bin/$(echo $i)%{python3_pkgversion}|g" %{pyproject_files}
done
rm -f $RPM_BUILD_ROOT/binfiles
%endif
# END RENAMING OF BINARIES 2




%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-docutils -f %{pyproject_files}


%changelog
%autochangelog
