#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Compress
%define		pnam	Raw-Lzma
Summary:	Compress::Raw::Lzma - low-level Interface to lzma compression library
Summary(pl.UTF-8):	Compress::Raw::Lzma - niskopoziomowy interfejs do biblioteki kompresji lzma
Name:		perl-Compress-Raw-Lzma
Version:	2.212
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Compress/Compress-Raw-Lzma-%{version}.tar.gz
# Source0-md5:	dd5e1b2d76ad20c69843d1419fde09ca
URL:		https://metacpan.org/dist/Compress-Raw-Lzma
BuildRequires:	perl-ExtUtils-MakeMaker >= 5.16
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compress::Raw::Lzma provides an interface to the in-memory
compression/uncompression functions from the lzma compression library.

Although the primary purpose for the existence of Compress::Raw::Lzma
is for use by the IO::Compress::Lzma, IO::Uncompress::UnLzma,
IO::Compress::Xz and IO::Uncompress::UnXz modules, it can be used on
its own for simple compression/uncompression tasks.

%description -l pl.UTF-8
Compress::Raw::Lzma udostępnia interfejs do funkcji kompresji i
dekompresji w pamięci biblioteki kompresji lzma.

Mimo że głównym celem istnienia modułu Compres::Raw::Lzma jest
wykorzystywanie przez moduły IO::Compres::Lzma,
IO::Uncompress::UnLzma, IO::Compress::Xz i IO::Uncompress::UnXz, może
być używany także samodzielnie do prostych zadań
kompresji/dekompresji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Compress/Raw/Lzma.pm
%dir %{perl_vendorarch}/auto/Compress/Raw/Lzma
%{perl_vendorarch}/auto/Compress/Raw/Lzma/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Raw/Lzma/Lzma.so
%{_mandir}/man3/Compress::Raw::Lzma.3pm*
