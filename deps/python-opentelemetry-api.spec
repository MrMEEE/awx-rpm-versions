
%global python3_pkgversion 3.11

Name:           python-opentelemetry-api
Version:        1.24.0
Release:        %autorelease
Summary:        OpenTelemetry Python API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api
Source:         %{pypi_source opentelemetry_api}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-api' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-opentelemetry-api
Summary:        %{summary}

%description -n python%{python3_pkgversion}-opentelemetry-api %_description


%prep
%autosetup -p1 -n opentelemetry_api-%{version}


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


%files -n python%{python3_pkgversion}-opentelemetry-api -f %{pyproject_files}


%changelog
%autochangelog