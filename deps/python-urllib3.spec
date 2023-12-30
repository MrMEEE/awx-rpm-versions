Name:           python-urllib3
Version:        1.26.13
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/urllib3/
Source:         %{pypi_source urllib3}

BuildArch:      noarch
BuildRequires:  python3-devel python-ntlm


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'urllib3' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-urllib3
Summary:        %{summary}

%description -n python3-urllib3 %_description


%prep
%autosetup -p1 -n urllib3-%{version}


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


%files -n python3-urllib3 -f %{pyproject_files}


%changelog
* Sat Dec 30 2023 Martin Juhl <m@rtinjuhl.dk> - 1.26.13-1
- Initial package