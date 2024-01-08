Name:           python-deprecated
Version:        1.2.13
Release:        1%{?dist}
Summary:        Python @deprecated decorator to deprecate old python classes, functions or methods.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/tantale/deprecated
Source:         %{pypi_source Deprecated}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'deprecated' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-deprecated
Summary:        %{summary}

%description -n python3-deprecated %_description


%prep
%autosetup -p1 -n Deprecated-%{version}


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


%files -n python3-deprecated -f %{pyproject_files}


%changelog
* Mon Jan 08 2024 Martin Juhl <m@rtinjuhl.dk> - 1.2.13-1
- Initial package