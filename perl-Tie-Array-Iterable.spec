%define upstream_name    Tie-Array-Iterable
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Forward Iterator object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
'Tie::Hash::Iterable' allows one to create iterators for lists and arrays.
The concept of iterators is borrowed from the C++ STL [1], in which most of
the collections have iterators, though this class does not attempt to fully
mimic it.

Typically, in C/C++ or Perl, the 'easy' way to visit each item on a list is
to use a counter, and then a for( ;; ) loop. However, this requires
knowledge on how long the array is to know when to end. In addition, if
items are removed or inserted into the array during the loop, then the
counter will be incorrect on the next run through the loop, and will cause
problems.

While some aspects of this are fixed in Perl by the use of for or foreach,
these commands still suffer when items are removed or added to the array
while in these loops. Also, if one wished to use break to step out of a
foreach loop, then restart where they left at some later point, there is no
way to do this without maintaining some additional state information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.30.0-3mdv2011.0
+ Revision: 655237
- rebuild for updated spec-helper

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 466616
- rebuild
- import perl-Tie-Array-Iterable


* Sun Oct 18 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
