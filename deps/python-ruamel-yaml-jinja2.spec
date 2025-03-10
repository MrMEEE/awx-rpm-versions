
%global python3_pkgversion 3.11

Name:           python-ruamel-yaml-jinja2
Version:        0.2.7
Release:        %autorelease
Summary:        jinja2 pre and post-processor to update with YAML

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://sourceforge.net/p/ruamel-yaml-jinja2/code/ci/default/tree
Source:         %{pypi_source ruamel.yaml.jinja2}
Patch:		ruamel-yaml-jinja2-circular-deps.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ruamel-yaml-jinja2' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-ruamel-yaml-jinja2
Summary:        %{summary}

%description -n python%{python3_pkgversion}-ruamel-yaml-jinja2 %_description


%prep
%autosetup -p1 -n ruamel.yaml.jinja2-%{version}


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


%files -n python%{python3_pkgversion}-ruamel-yaml-jinja2 -f %{pyproject_files}


%changelog
%autochangelog
