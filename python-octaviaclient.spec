%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global pypi_name octaviaclient

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global common_desc \
Client for OpenStack Octavia (Load Balancer as a Service)

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
%{common_desc}

%package -n     python2-%{pypi_name}

BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
BuildRequires:  python2-keystoneauth1
BuildRequires:  python2-mock
BuildRequires:  python2-osc-lib
BuildRequires:  python2-osc-lib-tests
BuildRequires:  python2-oslo-log
BuildRequires:  python2-openstackclient
%if 0%{?fedora} > 0
BuildRequires:  python2-cliff
%else
BuildRequires:  python-cliff
%endif

Requires:       python2-appdirs >= 1.3.0
Requires:       python2-babel >= 2.3.4
Requires:       python2-debtcollector >= 1.2.0
Requires:       python2-funcsigs >= 1.0.0
Requires:       python2-iso8601 >= 0.1.11
Requires:       python2-keystoneauth1 >= 3.3.0
Requires:       python2-os-client-config >= 1.28.0
Requires:       python2-osc-lib >= 1.8.0
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-pbr
Requires:       python2-prettytable >= 0.7.1
Requires:       python2-neutronclient >= 6.3.0
Requires:       python2-openstackclient >= 3.12.0
Requires:       python2-pytz >= 2013.6
Requires:       python2-requests >= 2.14.2
Requires:       python2-requestsexceptions >= 1.2.0
Requires:       python2-six >= 1.10.0
Requires:       python2-stevedore >= 1.20.0
Requires:       python2-unicodecsv >= 0.8.0
Requires:       python2-wrapt >= 1.7.0
%if 0%{?fedora} > 0
Requires:       python2-cliff >= 2.8.0
Requires:       python2-cmd2 >= 0.6.7
Requires:       python2-monotonic >= 0.6
Requires:       python2-netaddr >= 0.7.18
Requires:       python2-netifaces >= 0.10.4
Requires:       python2-pyparsing >= 2.1.0
Requires:       python2-pyyaml >= 3.10
Requires:       python2-simplejson >= 3.5.1
%else
Requires:       python-cliff >= 2.8.0
Requires:       python-cmd2 >= 0.6.7
Requires:       python-monotonic >= 0.6
Requires:       python-netaddr >= 0.7.18
Requires:       python-netifaces >= 0.10.4
Requires:       pyparsing >= 2.1.0
Requires:       PyYAML >= 3.10
Requires:       python-simplejson >= 3.5.1
%endif

Summary:        Client for OpenStack Octavia (Load Balancer as a Service)
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{common_desc}

# Python3 package
%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-cliff
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-mock
BuildRequires:  python3-osc-lib
BuildRequires:  python3-osc-lib-tests
BuildRequires:  python3-oslo-log
BuildRequires:  python3-openstackclient

Requires:       python3-appdirs >= 1.3.0
Requires:       python3-babel >= 2.3.4
Requires:       python3-cliff >= 2.8.0
Requires:       python3-cmd2 >= 0.6.7
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-funcsigs >= 1.0.0
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-keystoneauth1 >= 3.3.0
Requires:       python3-monotonic >= 0.6
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-netifaces >= 0.10.4
Requires:       python3-os-client-config >= 1.28.0
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pbr
Requires:       python3-prettytable >= 0.7.1
Requires:       python3-pyparsing >= 2.1.0
Requires:       python3-neutronclient >= 6.3.0
Requires:       python3-openstackclient >= 3.12.0
Requires:       python3-pytz >= 2013.6
Requires:       python3-PyYAML >= 3.10
Requires:       python3-requests >= 2.14.2
Requires:       python3-requestsexceptions >= 1.2.0
Requires:       python3-simplejson >= 3.5.1
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-unicodecsv >= 0.8.0
Requires:       python3-wrapt >= 1.7.0


%description -n python3-%{pypi_name}
%{common_desc}
%endif

%if 0%{?with_doc}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for OpenStack Octavia Client

BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-osc-lib
BuildRequires:  python2-openstackclient
BuildRequires:  dos2unix

%description -n python-%{pypi_name}-doc
Documentation for the client library for interacting with Openstack
Octavia API.
%endif


# Test package
%package -n python2-%{pypi_name}-tests

Summary:        OpenStack Octavia client tests

Requires:       python2-%{pypi_name} = %{version}-%{release}
Requires:       python2-fixtures >= 1.3.1
Requires:       python2-mock
Requires:       python2-testtools
Requires:       python2-subunit >= 0.0.18
Requires:       python2-osc-lib
Requires:       python2-osc-lib-tests
Requires:       python2-oslo-log
Requires:       python2-openstackclient
%if 0%{?fedora} > 0
Requires:       python2-testrepository >= 0.0.18
Requires:       python2-testscenarios >= 0.4
Requires:       python2-webob >= 1.2.3
%else
Requires:       python-testrepository >= 0.0.18
Requires:       python-testscenarios >= 0.4
Requires:       python-webob >= 1.2.3
%endif

%description -n python2-%{pypi_name}-tests
OpenStack Octavia client tests

This package contains the example client test files.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}-tests

Summary:        OpenStack Octavia client tests

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-fixtures >= 1.3.1
Requires:       python3-mock
Requires:       python3-testrepository >= 0.0.18
Requires:       python3-testscenarios >= 0.4
Requires:       python3-testtools
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-subunit >= 0.0.18
Requires:       python3-webob >= 1.2.3
Requires:       python3-osc-lib
Requires:       python3-osc-lib-tests
Requires:       python3-oslo-log
Requires:       python3-openstackclient

%description -n python3-%{pypi_name}-tests
OpenStack Octavia client tests

This package contains the example client test files.
%endif


%prep
%autosetup -n %{name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%if 0%{?with_doc}
# generate html docs
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
dos2unix doc/build/html/_static/jquery.js
%endif

%install
%if 0%{?with_python3}
%py3_install
%endif

%py2_install


%check
%if 0%{?with_python3}
%{__python3} setup.py test
rm -rf .testrepository
%endif
%{__python2} setup.py test


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/python_%{pypi_name}-*-py?.?.egg-info
%exclude %{python2_sitelib}/%{pypi_name}/tests

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_%{pypi_name}-*-py?.?.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests
%endif

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python2-%{pypi_name}-tests
%{python2_sitelib}/%{pypi_name}/tests

%if 0%{?with_python3}
%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/%{pypi_name}/tests
%endif


%changelog
