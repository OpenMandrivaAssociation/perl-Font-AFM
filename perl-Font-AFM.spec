%define modname	Font-AFM
%define modver	1.20

Summary:	Interface to Adobe Font Metrics files
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{modname}-%{modver}.tar.bz2 
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module implements the Font::AFM class. Objects of this
class are initialised from an AFM-file and allows you to obtain
information about the font and the metrics of the various glyphs
in the font.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}/%{perl_vendorarch}

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

