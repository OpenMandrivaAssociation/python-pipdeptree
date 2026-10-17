%define module pipdeptree

Name:		python-pipdeptree
Version:	4.2.8
Release:	1
Summary:	Command line utility to show dependency tree of packages
License:	MIT
Group:		Development/Python
URL:		https://github.com/tox-dev/pipdeptree
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz

BuildSystem:	python
BuildRequires:	cargo
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	python%{pyver}dist(pip)

%description
Command line utility to show the dependency tree of installed packages.
Version 4 resolves through nab and builds a Rust extension.
4.2.8 adds CycloneDX 1.5 JSON export.

%prep -a
tar -xf %{SOURCE1}
mkdir -p .cargo
cat > .cargo/config.toml << EOF
[net]
offline = true

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$PWD/vendor"
EOF
# Cooker rustc is 1.98. The crate asks for 1.99, and 4.2.8 builds on 1.98.
sed -i 's/rust-version = "1.99"/rust-version = "1.85"/' Cargo.toml
# meson.build lists rust-toolchain.toml as a cargo input. System cargo
# ignores that rustup pin, so leave the file in place.

%build -p
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true
export PIPDEPTREE_VERSION=%{version}
export CARGO_PROFILE_RELEASE_STRIP=none

%build -a
cargo tree --locked --offline --edges no-build,no-dev,no-proc-macro \
	--prefix none --format '{l}: {p}' \
	| sed -e "s: ($(pwd)[^)]*)::g" -e 's: / :/:g' -e 's:/: OR :g' \
	| sort -u > LICENSES.dependencies

%files
%doc README.md
%license LICENSE LICENSES.dependencies
%{_bindir}/%{module}
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
