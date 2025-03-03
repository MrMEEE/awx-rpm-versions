
%global python3_pkgversion 3.11

Name:           python-chardet
Version:        5.2.0
Release:        %autorelease
Summary:        Universal encoding detector for Python 3

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/chardet/chardet
Source:         %{pypi_source chardet}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'chardet' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-chardet
Summary:        %{summary}

%description -n python%{python3_pkgversion}-chardet %_description
# START ALTERNATIVES
%post -n python%{python3_pkgversion}-chardet
if [[   "chardet" ==  "1" ]]; then
for i in `cat /usr/bin/%{name}-binfiles`;do
        alternatives --install /usr/bin/$i $i /usr/bin/${i}3.11 10
done
fi

%preun -n python%{python3_pkgversion}-chardet
if [[ "chardet" ==  "0" ]]; then
for i in `cat /usr/bin/%{name}-binfiles`;do
        alternatives --remove $i /usr/bin/${i}3.11
done
fi
# END ALTERNATIVES



%prep
%autosetup -p1 -n chardet-%{version}


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
ls | tee $RPM_BUILD_ROOT/usr/bin/%{name}-binfiles
sed -i "/%{name}-binfiles/d" $RPM_BUILD_ROOT/usr/bin/%{name}-binfiles
for i in `cat $RPM_BUILD_ROOT/usr/bin/%{name}-binfiles`;do
echo "Renaming $i to $(echo $i)%{python3_pkgversion}"
mv $RPM_BUILD_ROOT/usr/bin/$i $RPM_BUILD_ROOT/usr/bin/$(echo $i)%{python3_pkgversion}
done
%endif
# END RENAMING OF BINARIES 1

%pyproject_save_files '*' +auto
# START RENAMING OF BINARIES 2
%if "%{python3_pkgversion}" != "3"
cd $RPM_BUILD_ROOT/usr/bin/
for i in `cat $RPM_BUILD_ROOT/usr/bin/%{name}-binfiles`;do
echo "Renaming: $i to $(echo $i)%{python3_pkgversion}"
sed -i "s|/usr/bin/$i$|/usr/bin/$(echo $i)%{python3_pkgversion}|g" %{pyproject_files}
done
echo /usr/bin/%{name}-binfiles >> %{pyproject_files}
%endif
# END RENAMING OF BINARIES 2



%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-chardet -f %{pyproject_files}


%changelog
%autochangelog