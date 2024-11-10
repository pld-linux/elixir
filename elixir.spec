Summary:	Tools for Elixir language
Name:		elixir
Version:	1.17.3
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://github.com/elixir-lang/elixir/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ddd875a539536b4e4584d6aa93a1132e
URL:		https://elixir-lang.org/
BuildRequires:	erlang >= 2:25.0
Requires:	erlang >= 2:25.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elixir is a dynamic, functional language for building scalable and
maintainable applications. Elixir runs on the Erlang VM, known for
creating low-latency, distributed, and fault-tolerant systems. These
capabilities and Elixir tooling allow developers to be productive in
several domains, such as web development, embedded software, machine
learning, data pipelines, and multimedia processing, across a wide
range of industries.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env elixir,%{_bindir}/elixir,' bin/mix

%build
LC_ALL=C.UTF-8; export LC_ALL
%{__make} compile

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_lib}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/elixir
%attr(755,root,root) %{_bindir}/elixirc
%attr(755,root,root) %{_bindir}/iex
%attr(755,root,root) %{_bindir}/mix
%dir %{_libdir}/elixir
%dir %{_libdir}/elixir/bin
%attr(755,root,root) %{_libdir}/elixir/bin/elixir
%attr(755,root,root) %{_libdir}/elixir/bin/elixirc
%attr(755,root,root) %{_libdir}/elixir/bin/iex
%attr(755,root,root) %{_libdir}/elixir/bin/mix
%{_libdir}/elixir/lib
%{_mandir}/man1/elixir.1*
%{_mandir}/man1/elixirc.1*
%{_mandir}/man1/iex.1*
%{_mandir}/man1/mix.1*
