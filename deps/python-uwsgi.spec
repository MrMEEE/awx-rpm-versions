%global python3_pkgversion 3.11
%global python3_sitelib /usr/lib64/python%{python3_pkgversion}/site-packages

Name:           python-uwsgi
Version:        2.0.26
Release:        %autorelease
Summary:        The uWSGI server

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://uwsgi-docs.readthedocs.io/en/latest/
Source:         %{pypi_source uwsgi}

BuildArch:      x86_64

BuildRequires:  python%{python3_pkgversion}-devel gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uwsgi' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-uwsgi
Summary:        %{summary}

%description -n python%{python3_pkgversion}-uwsgi %_description
# START ALTERNATIVES
%post -n python%{python3_pkgversion}-uwsgi
if [[   "uwsgi" ==  "1" ]]; then
for i in `cat /usr/bin/%{name}-binfiles`;do
        alternatives --install /usr/bin/$i $i /usr/bin/${i}3.11 10
done
fi

%preun -n python%{python3_pkgversion}-uwsgi
if [[ "uwsgi" ==  "0" ]]; then
for i in `cat /usr/bin/%{name}-binfiles`;do
        alternatives --remove $i /usr/bin/${i}3.11
done
fi
# END ALTERNATIVES



%prep
%autosetup -p1 -n uwsgi-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
#touch $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/uWSGI-%{version}.dist-info/RECORD
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


%files -n python%{python3_pkgversion}-uwsgi -f %{pyproject_files}
/usr/lib/python%{python3_pkgversion}/site-packages/__pycache__/uwsgidecorators*

%changelog
%autochangelog