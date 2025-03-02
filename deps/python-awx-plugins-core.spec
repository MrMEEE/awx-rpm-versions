
%global python3_pkgversion 3.11

Name:           python-awx-plugins-core
Version:        0.0.1~a9
Release:        %autorelease
Summary:        A temporary home for the essential AWX plugins

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://docs.ansible.com
Source:         %{pypi_source awx_plugins_core 0.0.1a9}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'awx-plugins-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python%{python3_pkgversion}-awx-plugins-core
Summary:        %{summary}

%description -n python%{python3_pkgversion}-awx-plugins-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python%{python3_pkgversion}-awx-plugins-core credentials-aim,credentials-aws-secretsmanager-credential,credentials-azure-kv,credentials-centrify-vault-kv,credentials-conjur,credentials-github-app,credentials-hashivault-kv,credentials-hashivault-ssh,credentials-thycotic-dsv,credentials-thycotic-tss,inventory-azure-rm,inventory-constructed,inventory-controller,inventory-ec2,inventory-gce,inventory-insights,inventory-openshift-virtualization,inventory-openstack,inventory-rhv,inventory-satellite6,inventory-terraform,inventory-vmware


%prep
%autosetup -p1 -n awx_plugins_core-0.0.1a9


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x credentials-aim,credentials-aws-secretsmanager-credential,credentials-azure-kv,credentials-centrify-vault-kv,credentials-conjur,credentials-github-app,credentials-hashivault-kv,credentials-hashivault-ssh,credentials-thycotic-dsv,credentials-thycotic-tss,inventory-azure-rm,inventory-constructed,inventory-controller,inventory-ec2,inventory-gce,inventory-insights,inventory-openshift-virtualization,inventory-openstack,inventory-rhv,inventory-satellite6,inventory-terraform,inventory-vmware


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-awx-plugins-core -f %{pyproject_files}


%changelog
%autochangelog