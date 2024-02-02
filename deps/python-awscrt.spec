Name:           python-awscrt
Version:        0.20.3
Release:        %autorelease
Summary:        A common runtime for AWS Python projects

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/awslabs/aws-crt-python
Source:         %{pypi_source awscrt}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'awscrt' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-awscrt
Summary:        %{summary}

%description -n python3-awscrt %_description


%prep
%autosetup -p1 -n awscrt-%{version}


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


%files -n python3-awscrt -f %{pyproject_files}


%changelog
%autochangelog
