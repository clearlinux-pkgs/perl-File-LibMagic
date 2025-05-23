#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-File-LibMagic
Version  : 1.23
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-LibMagic-1.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-LibMagic-1.23.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-libmagic-perl/libfile-libmagic-perl_1.16-1.debian.tar.xz
Summary  : 'Determine MIME types of data or files using libmagic'
Group    : Development/Tools
License  : Apache-2.0 Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0 MIT
Requires: perl-File-LibMagic-license = %{version}-%{release}
Requires: perl-File-LibMagic-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : file-dev
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(Config::AutoConf)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
File::LibMagic - Determine MIME types of data or files using libmagic
# VERSION

%package dev
Summary: dev components for the perl-File-LibMagic package.
Group: Development
Provides: perl-File-LibMagic-devel = %{version}-%{release}
Requires: perl-File-LibMagic = %{version}-%{release}

%description dev
dev components for the perl-File-LibMagic package.


%package license
Summary: license components for the perl-File-LibMagic package.
Group: Default

%description license
license components for the perl-File-LibMagic package.


%package perl
Summary: perl components for the perl-File-LibMagic package.
Group: Default
Requires: perl-File-LibMagic = %{version}-%{release}

%description perl
perl components for the perl-File-LibMagic package.


%prep
%setup -q -n File-LibMagic-1.23
cd %{_builddir}
tar xf %{_sourcedir}/libfile-libmagic-perl_1.16-1.debian.tar.xz
cd %{_builddir}/File-LibMagic-1.23
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-LibMagic-1.23/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-LibMagic
cp %{_builddir}/File-LibMagic-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-LibMagic/c24c1713d32e06b8b5935544493d7b40cefeb13e || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-LibMagic/817a05d17d7e2ca546655f7b38744dbea0d6f0d0 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::LibMagic.3
/usr/share/man/man3/File::LibMagic::Constants.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-LibMagic/817a05d17d7e2ca546655f7b38744dbea0d6f0d0
/usr/share/package-licenses/perl-File-LibMagic/c24c1713d32e06b8b5935544493d7b40cefeb13e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
