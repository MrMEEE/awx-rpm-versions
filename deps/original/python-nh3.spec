Name:           python-nh3
Version:        0.2.14
Release:        1%{?dist}
Summary:        Ammonia HTML sanitizer Python binding

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/nh3/
Source:         %{pypi_source nh3}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nh3' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-nh3
Summary:        %{summary}

%description -n python3-nh3 %_description


%prep
%autosetup -p1 -n nh3-%{version}


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


%files -n python3-nh3 -f %{pyproject_files}


%changelog
* Thu Sep 21 2023 Martin Juhl <m@rtinjuhl.dk> - 0.2.14-1
- Initial package