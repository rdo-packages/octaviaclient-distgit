%global pypi_name octaviaclient

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Client for OpenStack Octavia (Load Balancer as a Service)

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
%{common_desc}

%package -n     python2-%{pypi_name}

BuildRequires:  git
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
BuildRequires:  python-cliff
BuildRequires:  python-keystoneauth1
BuildRequires:  python-mock
BuildRequires:  python-osc-lib
BuildRequires:  python-osc-lib-tests
BuildRequires:  python-oslo-log
BuildRequires:  python-openstackclient

Requires:       python-appdirs >= 1.3.0
Requires:       python-babel >= 2.3.4
Requires:       python-cliff >= 2.8.0
Requires:       python-cmd2 >= 0.6.7
Requires:       python-debtcollector >= 1.2.0
Requires:       python-funcsigs >= 0.4.0
Requires:       python-iso8601 >= 0.1.11
Requires:       python-keystoneauth1 >= 3.1.0
Requires:       python-monotonic >= 0.6
Requires:       python-netaddr >= 0.7.13
Requires:       python-netifaces >= 0.10.4
Requires:       python-os-client-config >= 1.28.0
Requires:       python-osc-lib >= 1.7.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-utils >= 3.20.0
Requires:       python-pbr
Requires:       python-positional >= 1.1.1
Requires:       python-prettytable >= 0.7.1
Requires:       pyparsing >= 2.1.0
Requires:       python-neutronclient >= 6.3.0
Requires:       python-openstackclient >= 3.11.0
Requires:       pytz >= 2013.6
Requires:       PyYAML >= 3.10
Requires:       python-requests >= 2.14.2
Requires:       python-requestsexceptions >= 1.2.0
Requires:       python-simplejson >= 2.2.0
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.20.0
Requires:       python-unicodecsv >= 0.8.0
Requires:       python-wrapt >= 1.7.0

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
Requires:       python3-funcsigs >= 0.4.0
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-keystoneauth1 >= 3.1.0
Requires:       python3-monotonic >= 0.6
Requires:       python3-netaddr >= 0.7.13
Requires:       python3-netifaces >= 0.10.4
Requires:       python3-os-client-config >= 1.28.0
Requires:       python3-osc-lib >= 1.7.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-utils >= 3.20.0
Requires:       python3-pbr
Requires:       python3-positional >= 1.1.1
Requires:       python3-prettytable >= 0.7.1
Requires:       python3-pyparsing >= 2.1.0
Requires:       python3-neutronclient >= 6.3.0
Requires:       python3-openstackclient >= 3.11.0
Requires:       python3-pytz >= 2013.6
Requires:       python3-PyYAML >= 3.10
Requires:       python3-requests >= 2.14.2
Requires:       python3-requestsexceptions >= 1.2.0
Requires:       python3-simplejson >= 2.2.0
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-unicodecsv >= 0.8.0
Requires:       python3-wrapt >= 1.7.0


%description -n python3-%{pypi_name}
%{common_desc}
%endif

# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for OpenStack Octavia Client

BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-keystoneauth1
BuildRequires:  python-keystoneclient
BuildRequires:  python-osc-lib
BuildRequires:  python-openstackclient
BuildRequires:  dos2unix

%description -n python-%{pypi_name}-doc
Documentation for the client library for interacting with Openstack
Octavia API.


# Documentation package
%package -n python2-%{pypi_name}-tests

Summary:        OpenStack Octavia client tests

Requires:       python2-%{pypi_name} = %{version}-%{release}
Requires:       python-coverage >= 4.0
Requires:       python-fixtures >= 1.3.1
Requires:       python-mock
Requires:       python-testrepository >= 0.0.18
Requires:       python-testscenarios >= 0.4
Requires:       python-testtools
Requires:       python-oslo-sphinx >= 4.7.0
Requires:       python-sphinx
Requires:       python-subunit >= 0.0.18
Requires:       python-webob >= 1.2.3
Requires:       python-osc-lib
Requires:       python-osc-lib-tests
Requires:       python-oslo-log
Requires:       python-openstackclient

%description -n python2-%{pypi_name}-tests
OpenStack Octavia client tests

This package contains the example client test files.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}-tests

Summary:        OpenStack Octavia client tests

Requires:       python3-%{pypi_name} = %{version}-%{release}
Requires:       python3-coverage >= 4.0
Requires:       python3-fixtures >= 1.3.1
Requires:       python3-mock
Requires:       python3-testrepository >= 0.0.18
Requires:       python3-testscenarios >= 0.4
Requires:       python3-testtools
Requires:       python3-osc-lib >= 1.5.1
Requires:       python3-oslo-sphinx >= 4.7.0
Requires:       python3-sphinx
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

# generate html docs
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
%endif

%py2_install

dos2unix doc/build/html/_static/jquery.js


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
%exclude %{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/python_%{pypi_name}-*-py?.?.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests
%endif

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%files -n python2-%{pypi_name}-tests
%{python2_sitelib}/%{pypi_name}/tests

%if 0%{?with_python3}
%files -n python3-%{pypi_name}-tests
%{python3_sitelib}/%{pypi_name}/tests
%endif


%changelog
* Tue Nov 21 2017 Carlos Goncalves <cgoncalves@redhat.com> 1.2.0-1
- Initial RPM release
