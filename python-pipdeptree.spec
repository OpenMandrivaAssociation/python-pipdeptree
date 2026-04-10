%define module pipdeptree

Name:		python-pipdeptree
Version:	2.35.0
Release:	1
Summary:	Command line utility to show dependency tree of packages.
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pipdeptree/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
Command line utility to show dependency tree of packages.

%prep -a
# relax lower bound for python-packaging until we have upgraded it.
sed -i 's/packaging>=26/packaging>=25/g' pyproject.toml

%files
%doc README.md
%{_bindir}/%{module}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
