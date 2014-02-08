%define upstream_name	 Font-AFM
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Interface to Adobe Font Metrics files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2 

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements the Font::AFM class. Objects of this
class are initialised from an AFM-file and allows you to obtain
information about the font and the metrics of the various glyphs
in the font.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-4mdv2012.0
+ Revision: 765278
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-3
+ Revision: 763771
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-2
+ Revision: 667150
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 406026
- rebuild using %%perl_convert_version

* Fri Jun 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2009.0
+ Revision: 216416
- update to new version 1.20

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.19-5mdv2008.1
+ Revision: 180399
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 1.19-4mdv2008.0
+ Revision: 21207
- Rebuild


* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 1.19-3mdk
- Do not ship empty dir
- use check
- remove MANIFEST from doc
- use mkrel

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.19-2mdk
- rebuild for new perl

* Fri Aug 06 2004 Michael Scherer <misc@mandrake.org> 1.19-1mdk
- First Mandrakelinux package

