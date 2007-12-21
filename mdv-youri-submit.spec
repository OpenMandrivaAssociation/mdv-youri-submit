%define rname	youri-submit
%define name	mdv-%{rname}
%define version 0.9
%define svn	20071221
%define rel	1
%define release %mkrel 1.%{svn}.%{rel}
%define distname %{rname}-%{version}-%{svn}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri submit tool
License:	GPL or Artistic
Group:		Development/Other
Source:		%{distname}.tar.bz2
Url:		http://youri.zarb.org
BuildRequires:	perl(Youri::Utils)
BuildRequires:	perl(Youri::Package::RPM::Test)
BuildRequires:	perl(Youri::Package::RPM::Generator)
BuildRequires:	perl(Youri::Repository::Test)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

youri-submit is a generic package submission tool. It first runs a list of
tests on each submitted package, and if no one fails, runs a list of actions on
those packages.

%prep
%setup -q -n %{distname}

%build
%{__perl} Makefile.PL \
  INSTALLDIRS=vendor \
  INSTALLVENDORSCRIPT=%{_datadir}/%{name}/bin \
  INSTALLVENDORLIB=%{_datadir}/%{name}/lib
%make pure_all

%install
rm -rf %{buildroot}
%make DESTDIR=%{buildroot} pure_install

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{_datadir}/%{name}/bin/%{rname}*
%{_datadir}/%{name}/lib/Youri
%{_datadir}/%{name}/lib/auto/%{rname}
