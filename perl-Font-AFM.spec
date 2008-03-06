
%define rel 5
%define realname	Font-AFM

Name:		perl-%{realname}
Version:	1.19
Release:	%mkrel %rel
License:	GPL or Artistic
Group:		Development/Perl
Summary:    	Interface to Adobe Font Metrics files
Source0:   http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{realname}-%{version}.tar.bz2 
Url:		http://www.cpan.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch:      noarch
%description
This module implements the Font::AFM class. Objects of this
class are initialised from an AFM-file and allows you to obtain
information about the font and the metrics of the various glyphs
in the font.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/man3/*
