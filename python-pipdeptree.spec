Name:		python-pipdeptree
Version:	2.28.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pipdeptree/pipdeptree-%{version}.tar.gz
Summary:	Command line utility to show dependency tree of packages.
URL:		https://pypi.org/project/pipdeptree/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(hatch-vcs)
BuildSystem:	python
BuildArch:	noarch

%description
Command line utility to show dependency tree of packages.

%files
%{_bindir}/pipdeptree
%{py_sitedir}/pipdeptree
%{py_sitedir}/pipdeptree-*.*-info
