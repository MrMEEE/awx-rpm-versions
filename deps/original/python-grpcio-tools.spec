
%global python3_pkgversion 3.11

Name:           python-grpcio-tools
Version:        1.70.0
Release:        %autorelease
Summary:        Protobuf code generator for gRPC

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://grpc.io
Source:         %{pypi_source grpcio_tools}


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'grpcio-tools' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-grpcio-tools
Summary:        %{summary}

%description -n python%{python3_pkgversion}-grpcio-tools %_description


%prep
%autosetup -p1 -n grpcio_tools-%{version}


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


%files -n python%{python3_pkgversion}-grpcio-tools -f %{pyproject_files}


%changelog
%autochangelog