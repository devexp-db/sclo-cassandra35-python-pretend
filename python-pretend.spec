# needed for epel6
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

# enable python3 on fedora
%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

%global srcname pretend

Name:           python-pretend
Version:        1.0.8
Release:        7%{?dist}
Summary:        A library for stubbing in Python

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/alex/pretend
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif


%description
Pretend is a library to make stubbing with Python easier.


%if %{with python3}
%package -n python3-pretend
Summary:        A library for stubbing in Python
License:        BSD


%description -n python3-pretend
Pretend is a library to make stubbing with Python easier.
%endif


%prep
%setup -q -n %{srcname}-%{version}

# Delete upstream supplied egg-info
rm -rf *.egg-info

%if %{with python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if %{with python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%if %{with python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc PKG-INFO README.rst LICENSE.rst
%{python2_sitelib}/pretend.py*
%{python2_sitelib}/pretend-%{version}-py2.?.egg-info

%if %{with python3}
%files -n python3-pretend
%doc PKG-INFO README.rst LICENSE.rst
%{python3_sitelib}/pretend.py
%{python3_sitelib}/__pycache__/pretend.cpython-3?*
%{python3_sitelib}/pretend-%{version}-py3.?.egg-info
%endif


%changelog
* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.0.8-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 1.0.8-4
- Rebuilt for Python3.5 rebuild
- Change pattern for listed files under __pycache__ folder to follow new naming of bytecompiled files

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 22 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.0.8-2
- Added epel support

* Mon Oct 20 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.0.8-1
- Initial package
