Summary:	Tools for Elixir language
Summary(pl.UTF-8):	Narzędzia dla języka Elixir
Name:		elixir
Version:	1.20.4
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	https://github.com/elixir-lang/elixir/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	47ad2492e884cdb0f4e0b254554c6f0e
URL:		https://elixir-lang.org/
BuildRequires:	erlang >= 2:27.0
BuildRequires:	rpmbuild(macros) >= 2.035
%{?erlang_requires}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Elixir is a dynamic, functional language for building scalable and
maintainable applications. Elixir runs on the Erlang VM, known for
creating low-latency, distributed, and fault-tolerant systems. These
capabilities and Elixir tooling allow developers to be productive in
several domains, such as web development, embedded software, machine
learning, data pipelines, and multimedia processing, across a wide
range of industries.

%description -l pl.UTF-8
Elixir to dynamiczny język funkcyjny do tworzenia skalowalnych i
utrzymywalnych aplikacji. Działa na VM Erlanga, znanego z tworzenia
szybko responsywnych, rozproszonych i odpornych na awarie systemów.
Te cechy te oraz narzędzia języka Elixir pozwalają programistom być
produktywnymi w różnych dziedzinach, takich jak tworzenie stron WWW,
oprogramowanie wbudowane, uczenie maszynowe, potoki przetwarzania
danych i przetwarzanie multimediów - w wielu dziedzinach przemysłu.

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
