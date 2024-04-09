
%global python3_pkgversion 3.11

Name:           python-uwsgi
Version:        2.0.24
Release:        %autorelease
Summary:        The uWSGI server

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://uwsgi-docs.readthedocs.io/en/latest/
Source:         %{pypi_source uwsgi}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uwsgi' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-uwsgi
Summary:        %{summary}

%description -n python%{python3_pkgversion}-uwsgi %_description


%prep
%autosetup -p1 -n uwsgi-%{version}


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


%files -n python%{python3_pkgversion}-uwsgi -f %{pyproject_files}


%changelog
%autochangelog