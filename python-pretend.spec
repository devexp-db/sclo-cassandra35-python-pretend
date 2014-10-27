%global with_python3 1
%global srcname pretend

Name:           python-pretend
Version:        1.0.8
Release:        1%{?dist}
Summary:        A library for stubbing in Python

License:        BSD
URL:            https://github.com/alex/pretend
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif


%description
Pretend is a library to make stubbing with Python easier.


%if 0%{?with_python3}
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

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc PKG-INFO README.rst LICENSE.rst
%{python2_sitelib}/pretend.py*
%{python2_sitelib}/pretend-%{version}-py2.?.egg-info

%if 0%{?with_python3}
%files -n python3-pretend
%doc PKG-INFO README.rst LICENSE.rst
%{python3_sitelib}/pretend.py
%{python3_sitelib}/__pycache__/pretend.cpython-3?.py*
%{python3_sitelib}/pretend-%{version}-py3.?.egg-info
%endif


%changelog
* Mon Oct 20 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.0.8-1
- Initial package
