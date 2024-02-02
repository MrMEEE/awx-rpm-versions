Name:           python-mkdocs-entangled-plugin
Version:        0.4.0
Release:        %autorelease
Summary:        Plugin for MkDocs helping with rendering Entangled (entangled.github.io) projects.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/mkdocs-entangled-plugin/
Source:         %{pypi_source mkdocs_entangled_plugin}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mkdocs-entangled-plugin' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mkdocs-entangled-plugin
Summary:        %{summary}

%description -n python3-mkdocs-entangled-plugin %_description


%prep
%autosetup -p1 -n mkdocs_entangled_plugin-%{version}


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


%files -n python3-mkdocs-entangled-plugin -f %{pyproject_files}


%changelog
%autochangelog