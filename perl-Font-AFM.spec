%define upstream_name	 Font-AFM
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    	Interface to Adobe Font Metrics files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:   http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2 

BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements the Font::AFM class. Objects of this
class are initialised from an AFM-file and allows you to obtain
information about the font and the metrics of the various glyphs
in the font.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}/%{perl_vendorarch}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/man3/*
