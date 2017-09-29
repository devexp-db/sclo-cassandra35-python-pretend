%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with python3
%endif

%global srcname pretend

Name:           python-pretend
Version:        1.0.8
Release:        11%{?dist}
Summary:        A library for stubbing in Python

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/alex/pretend
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif


%description
Pretend is a library to make stubbing with Python easier.


%package -n python2-pretend
Summary:        A library for stubbing in Python
License:        BSD
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-pretend
Pretend is a library to make stubbing with Python easier.


%if %{with python3}
%package -n python3-pretend
Summary:        A library for stubbing in Python
License:        BSD
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-pretend
Pretend is a library to make stubbing with Python easier.
%endif


%prep
%autosetup -n %{srcname}-%{version}


%build
%py2_build

%if %{with python3}
%py3_build
%endif


%install
%py2_install

%if %{with python3}
%py3_install
%endif


%files -n python2-pretend
%doc PKG-INFO README.rst
%license LICENSE.rst
%{python2_sitelib}/pretend.py*
%{python2_sitelib}/pretend-%{version}-py2.?.egg-info

%if %{with python3}
%files -n python3-pretend
%doc PKG-INFO README.rst
%license LICENSE.rst
%{python3_sitelib}/pretend.py
%{python3_sitelib}/__pycache__/pretend.cpython-3?*
%{python3_sitelib}/pretend-%{version}-py3.?.egg-info
%endif


%changelog
* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.0.8-11
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.0.8-9
- Update to new package guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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
