
%global python3_pkgversion 3.11

Name:           python-awx-plugins-interfaces
Version:        0.0.1~a4
Release:        %autorelease
Summary:        Common interfaces for implementing plugins to AWX.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://docs.ansible.com
Source:         %{pypi_source awx_plugins_interfaces 0.0.1a4}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'awx-plugins.interfaces' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-awx-plugins-interfaces
Summary:        %{summary}

%description -n python%{python3_pkgversion}-awx-plugins-interfaces %_description


%prep
%autosetup -p1 -n awx_plugins_interfaces-0.0.1a4


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


%files -n python%{python3_pkgversion}-awx-plugins-interfaces -f %{pyproject_files}


%changelog
%autochangelog