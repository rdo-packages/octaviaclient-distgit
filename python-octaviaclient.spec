%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global pypi_name octaviaclient

%global common_desc \
Client for OpenStack Octavia (Load Balancer as a Service)

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
%{common_desc}

%package -n     python3-%{pypi_name}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-mock
BuildRequires:  python3-osc-lib
BuildRequires:  python3-osc-lib-tests
BuildRequires:  python3-oslo-log
BuildRequires:  python3-openstackclient
BuildRequires:  python3-cliff
BuildRequires:  python3-stestr
BuildRequires:  python3-munch

Requires:       python3-cliff >= 2.8.0
Requires:       python3-keystoneauth1 >= 3.18.0
Requires:       python3-osc-lib >= 1.14.1
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pbr
Requires:       python3-neutronclient >= 6.7.0
Requires:       python3-openstackclient >= 3.12.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-munch >= 2.1.0

Summary:        Client for OpenStack Octavia (Load Balancer as a Service)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for OpenStack Octavia Client

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-osc-lib
BuildRequires:  python3-openstackclient

%description -n python-%{pypi_name}-doc
Documentation for the client library for interacting with Openstack
Octavia API.
%endif


# Test package
%package -n python3-%{pypi_name}-tests
Summary:        OpenStack Octavia client tests
%{?python_provide:%python_provide python3-%{pypi_name}-tests}

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-fixtures >= 1.3.1
Requires:       python3-mock
Requires:       python3-testtools
Requires:       python3-subunit >= 0.0.18
Requires:       python3-osc-lib >= 1.14.1
Requires:       python3-osc-lib-tests
Requires:       python3-oslo-log
Requires:       python3-openstackclient
Requires:       python3-stestr
%if 3 == 2
Requires:       python-webob >= 1.2.3
%else
Requires:       python3-webob >= 1.2.3
%endif

%description -n python3-%{pypi_name}-tests
OpenStack Octavia client tests

This package contains the example client test files.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}


%check
rm -f ./octaviaclient/tests/unit/test_hacking.py
export PYTHON=%{__python3}
export OS_TEST_PATH='./octaviaclient/tests/unit'
export PATH=$PATH:$RPM_BUILD_ROOT/usr/bin
export PYTHONPATH=$PWD
stestr --test-path $OS_TEST_PATH run


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_%{pypi_name}-*-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/%{pypi_name}/tests

%changelog
