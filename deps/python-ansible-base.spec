%undefine __brp_mangle_shebangs
Name:           python-ansible-base
Version:        2.10.17
Release:        %autorelease
Summary:        Radically simple IT automation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://ansible.com/
Source:         %{pypi_source ansible-base}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansible-base' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ansible-base
Summary:        %{summary}

%description -n python3-ansible-base %_description


%prep
%autosetup -p1 -n ansible-base-%{version}


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


%files -n python3-ansible-base -f %{pyproject_files}


%changelog
%autochangelog
