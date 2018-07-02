#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-LibMagic
Version  : 1.16
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-LibMagic-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-LibMagic-1.16.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-libmagic-perl/libfile-libmagic-perl_1.16-1.debian.tar.xz
Summary  : 'Determine MIME types of data or files using libmagic'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-LibMagic-lib
Requires: perl-File-LibMagic-license
Requires: perl-File-LibMagic-man
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
# NAME
File::LibMagic - Determine MIME types of data or files using libmagic
# VERSION

%package lib
Summary: lib components for the perl-File-LibMagic package.
Group: Libraries
Requires: perl-File-LibMagic-license

%description lib
lib components for the perl-File-LibMagic package.


%package license
Summary: license components for the perl-File-LibMagic package.
Group: Default

%description license
license components for the perl-File-LibMagic package.


%package man
Summary: man components for the perl-File-LibMagic package.
Group: Default

%description man
man components for the perl-File-LibMagic package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n File-LibMagic-1.16
mkdir -p %{_topdir}/BUILD/File-LibMagic-1.16/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-LibMagic-1.16/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-File-LibMagic
cp LICENSE %{buildroot}/usr/share/doc/perl-File-LibMagic/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/File/LibMagic.pm

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/File/LibMagic/LibMagic.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-File-LibMagic/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/File::LibMagic.3
