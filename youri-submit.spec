%define name	youri-submit
%define version 0.10
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri submit tool
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{name}-%{version}.tar.bz2
Url:		http://youri.zarb.org
BuildRequires:	perl(Youri::Utils)
BuildRequires:	perl(Youri::Package::RPM::Test)
BuildRequires:	perl(Youri::Package::RPM::Generator)
BuildRequires:	perl(Youri::Repository::Test)
BuildRequires:	perl(Test::Exception)
BuildArch:	    noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

youri-submit is a generic package submission tool. It first runs a list of
tests on each submitted package, and if no one fails, runs a list of actions on
those packages.

%prep
%setup -q

%build
%configure2_5x
%make

%check
%__make check

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/youri
%{_bindir}/youri-submit*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_datadir}/youri
%{_sysconfdir}/bash_completion.d/%{name}
