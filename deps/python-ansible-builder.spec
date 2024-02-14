Name:           python-ansible-builder
Version:        3.0.0
Release:        %autorelease
Summary:        "A tool for building Ansible Execution Environments"

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://ansible-builder.readthedocs.io
Source:         %{pypi_source ansible-builder}

BuildArch:      noarch
BuildRequires:  python3-devel python-setuptools_scm
Patch: ansible-builder-scm-version.patch

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansible-builder' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ansible-builder
Summary:        %{summary}

%description -n python3-ansible-builder %_description


%prep
%autosetup -p1 -n ansible-builder-%{version}


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


%files -n python3-ansible-builder -f %{pyproject_files}


%changelog
%autochangelog