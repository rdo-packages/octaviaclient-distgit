# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global pypi_name octaviaclient

%global common_desc \
Client for OpenStack Octavia (Load Balancer as a Service)

Name:           python-%{pypi_name}
Version:        1.8.1
Release:        1%{?dist}
Summary:        Client for OpenStack Octavia (Load Balancer as a Service)

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
%{common_desc}

%package -n     python%{pyver}-%{pypi_name}

BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-keystoneauth1
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-osc-lib
BuildRequires:  python%{pyver}-osc-lib-tests
BuildRequires:  python%{pyver}-oslo-log
BuildRequires:  python%{pyver}-openstackclient
BuildRequires:  python%{pyver}-cliff
BuildRequires:  python%{pyver}-stestr

Requires:       python%{pyver}-appdirs >= 1.3.0
Requires:       python%{pyver}-babel >= 2.3.4
Requires:       python%{pyver}-cliff >= 2.8.0
Requires:       python%{pyver}-debtcollector >= 1.2.0
Requires:       python%{pyver}-funcsigs >= 1.0.0
Requires:       python%{pyver}-iso8601 >= 0.1.11
Requires:       python%{pyver}-keystoneauth1 >= 3.4.0
Requires:       python%{pyver}-os-client-config >= 1.28.0
Requires:       python%{pyver}-osc-lib >= 1.8.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-pbr
Requires:       python%{pyver}-prettytable >= 0.7.2
Requires:       python%{pyver}-neutronclient >= 6.7.0
Requires:       python%{pyver}-openstackclient >= 3.12.0
Requires:       python%{pyver}-pytz >= 2013.6
Requires:       python%{pyver}-requests >= 2.14.2
Requires:       python%{pyver}-requestsexceptions >= 1.2.0
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-stevedore >= 1.20.0
Requires:       python%{pyver}-unicodecsv >= 0.8.0
Requires:       python%{pyver}-netaddr >= 0.7.18
%if %{pyver} == 2
Requires:       python-cmd2 >= 0.6.7
Requires:       python-monotonic >= 0.6
Requires:       python-netifaces >= 0.10.4
Requires:       pyparsing >= 2.1.0
Requires:       PyYAML >= 3.10
Requires:       python-simplejson >= 3.5.1
Requires:       python-wrapt >= 1.7.0
%else
Requires:       python%{pyver}-cmd2 >= 0.6.7
Requires:       python%{pyver}-monotonic >= 0.6
Requires:       python%{pyver}-netifaces >= 0.10.4
Requires:       python%{pyver}-pyparsing >= 2.1.0
Requires:       python%{pyver}-yaml >= 3.10
Requires:       python%{pyver}-simplejson >= 3.5.1
Requires:       python%{pyver}-wrapt >= 1.7.0
%endif

Summary:        Client for OpenStack Octavia (Load Balancer as a Service)
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}

%description -n python%{pyver}-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for OpenStack Octavia Client

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-keystoneclient
BuildRequires:  python%{pyver}-osc-lib
BuildRequires:  python%{pyver}-openstackclient

%description -n python-%{pypi_name}-doc
Documentation for the client library for interacting with Openstack
Octavia API.
%endif


# Test package
%package -n python%{pyver}-%{pypi_name}-tests
Summary:        OpenStack Octavia client tests
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}-tests}

Requires:       python%{pyver}-%{pypi_name} = %{version}-%{release}
Requires:       python%{pyver}-fixtures >= 1.3.1
Requires:       python%{pyver}-mock
Requires:       python%{pyver}-testtools
Requires:       python%{pyver}-subunit >= 0.0.18
Requires:       python%{pyver}-osc-lib
Requires:       python%{pyver}-osc-lib-tests
Requires:       python%{pyver}-oslo-log
Requires:       python%{pyver}-openstackclient
Requires:       python%{pyver}-stestr
%if %{pyver} == 2
Requires:       python-webob >= 1.2.3
%else
Requires:       python%{pyver}-webob >= 1.2.3
%endif

%description -n python%{pyver}-%{pypi_name}-tests
OpenStack Octavia client tests

This package contains the example client test files.

%prep
%autosetup -n %{name}-%{upstream_version} -S git

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%{pyver_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-%{pyver} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyver_install}


%check
export PYTHON=%{pyver_bin}
export OS_TEST_PATH='./octaviaclient/tests/unit'
export PATH=$PATH:$RPM_BUILD_ROOT/usr/bin
export PYTHONPATH=$PWD
stestr-%{pyver} --test-path $OS_TEST_PATH run


%files -n python%{pyver}-%{pypi_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/%{pypi_name}
%{pyver_sitelib}/python_%{pypi_name}-*-py?.?.egg-info
%exclude %{pyver_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python%{pyver}-%{pypi_name}-tests
%{pyver_sitelib}/%{pypi_name}/tests

%changelog
* Mon Jun 17 2019 RDO <dev@lists.rdoproject.org> 1.8.1-1
- Update to 1.8.1

* Fri May 10 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.8.0-2
- Add stestr as BR and set PYTHON variable to versioned python.

* Mon Mar 11 2019 RDO <dev@lists.rdoproject.org> 1.8.0-1
- Update to 1.8.0

