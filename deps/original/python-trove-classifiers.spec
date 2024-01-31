Name:           python-trove-classifiers
Version:        2024.1.31
Release:        %autorelease
Summary:        Canonical source for classifiers on PyPI (pypi.org).

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/pypa/trove-classifiers
Source:         %{pypi_source trove-classifiers}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'trove-classifiers' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-trove-classifiers
Summary:        %{summary}

%description -n python3-trove-classifiers %_description


%prep
%autosetup -p1 -n trove-classifiers-%{version}


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


%files -n python3-trove-classifiers -f %{pyproject_files}


%changelog
%autochangelog