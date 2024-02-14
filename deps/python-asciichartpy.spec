Name:           python-asciichartpy
Version:        1.5.25
Release:        %autorelease
Summary:        Nice-looking lightweight console ASCII line charts ╭┈╯ with no dependencies

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/kroitor/asciichart
Source:         %{pypi_source asciichartpy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'asciichartpy' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-asciichartpy
Summary:        %{summary}

%description -n python3-asciichartpy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-asciichartpy qa


%prep
%autosetup -p1 -n asciichartpy-%{version}
touch README.md

%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x qa


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-asciichartpy -f %{pyproject_files}


%changelog
%autochangelog