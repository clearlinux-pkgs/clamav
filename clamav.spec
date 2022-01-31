#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x609B024F2B3EDD07 (research@sourcefire.com)
#
Name     : clamav
Version  : 0.103.3
Release  : 40
URL      : https://www.clamav.net/downloads/production/clamav-0.103.3.tar.gz
Source0  : https://www.clamav.net/downloads/production/clamav-0.103.3.tar.gz
Source1  : clamav.tmpfiles
Source2  : https://www.clamav.net/downloads/production/clamav-0.103.3.tar.gz.sig
Summary  : A GPL virus scanner
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-2.0 LGPL-2.1 MIT NCSA NTP Zlib bzip2-1.0.6
Requires: clamav-bin = %{version}-%{release}
Requires: clamav-config = %{version}-%{release}
Requires: clamav-data = %{version}-%{release}
Requires: clamav-filemap = %{version}-%{release}
Requires: clamav-lib = %{version}-%{release}
Requires: clamav-license = %{version}-%{release}
Requires: clamav-man = %{version}-%{release}
Requires: clamav-services = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : bzip2-dev
BuildRequires : check
BuildRequires : curl-dev
BuildRequires : flex
BuildRequires : libxml2-dev
BuildRequires : llvm-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : pcre2-dev
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(systemd)
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: 0001-Stateless-enablement.patch

%description
This is GNU libltdl, a system independent dlopen wrapper for GNU libtool.
It supports the following dlopen interfaces:
* dlopen (POSIX)
* shl_load (HP-UX)
* LoadLibrary (Win16 and Win32)
* load_add_on (BeOS)
* GNU DLD (emulates dynamic linking for static libraries)
* dyld (darwin/Mac OS X)
* libtool's dlpreopen
--
Written by Thomas Tanner, 1999

%package bin
Summary: bin components for the clamav package.
Group: Binaries
Requires: clamav-data = %{version}-%{release}
Requires: clamav-config = %{version}-%{release}
Requires: clamav-license = %{version}-%{release}
Requires: clamav-services = %{version}-%{release}
Requires: clamav-filemap = %{version}-%{release}

%description bin
bin components for the clamav package.


%package config
Summary: config components for the clamav package.
Group: Default

%description config
config components for the clamav package.


%package data
Summary: data components for the clamav package.
Group: Data

%description data
data components for the clamav package.


%package dev
Summary: dev components for the clamav package.
Group: Development
Requires: clamav-lib = %{version}-%{release}
Requires: clamav-bin = %{version}-%{release}
Requires: clamav-data = %{version}-%{release}
Provides: clamav-devel = %{version}-%{release}
Requires: clamav = %{version}-%{release}

%description dev
dev components for the clamav package.


%package filemap
Summary: filemap components for the clamav package.
Group: Default

%description filemap
filemap components for the clamav package.


%package lib
Summary: lib components for the clamav package.
Group: Libraries
Requires: clamav-data = %{version}-%{release}
Requires: clamav-license = %{version}-%{release}
Requires: clamav-filemap = %{version}-%{release}

%description lib
lib components for the clamav package.


%package license
Summary: license components for the clamav package.
Group: Default

%description license
license components for the clamav package.


%package man
Summary: man components for the clamav package.
Group: Default

%description man
man components for the clamav package.


%package services
Summary: services components for the clamav package.
Group: Systemd services

%description services
services components for the clamav package.


%prep
%setup -q -n clamav-0.103.3
cd %{_builddir}/clamav-0.103.3
%patch1 -p1
pushd ..
cp -a clamav-0.103.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634665692
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 -std=gnu++98"
%configure --disable-static --with-dbdir=/var/lib/clamav \
--enable-clamonacc \
--enable-check
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-dbdir=/var/lib/clamav \
--enable-clamonacc \
--enable-check
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1634665692
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clamav
cp %{_builddir}/clamav-0.103.3/COPYING %{buildroot}/usr/share/package-licenses/clamav/9a3515c3da4762b6ddbe88f02755b6edc8ce7f15
cp %{_builddir}/clamav-0.103.3/COPYING.LGPL %{buildroot}/usr/share/package-licenses/clamav/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/clamav-0.103.3/COPYING.YARA %{buildroot}/usr/share/package-licenses/clamav/c9b166c9c918ac6f123f0c70778297eb118537bc
cp %{_builddir}/clamav-0.103.3/COPYING.bzip2 %{buildroot}/usr/share/package-licenses/clamav/521256a2cd47b39b31811a5df9bb724662ae326e
cp %{_builddir}/clamav-0.103.3/COPYING.file %{buildroot}/usr/share/package-licenses/clamav/6178fe3d7980af9da8d734c13c56599b6775a20b
cp %{_builddir}/clamav-0.103.3/COPYING.getopt %{buildroot}/usr/share/package-licenses/clamav/a4b006d9829d39c162d3853cf45ef8aa2844615c
cp %{_builddir}/clamav-0.103.3/COPYING.llvm %{buildroot}/usr/share/package-licenses/clamav/4bdc478d273e3e8c75dbafbce0dc50bb8abc3628
cp %{_builddir}/clamav-0.103.3/COPYING.pcre %{buildroot}/usr/share/package-licenses/clamav/24c848a024de84cdf4f7db7e65d5102b329a43bd
cp %{_builddir}/clamav-0.103.3/COPYING.regex %{buildroot}/usr/share/package-licenses/clamav/28f373b92a4e7883d7243dfc65bb6fc0c9ca167e
cp %{_builddir}/clamav-0.103.3/COPYING.zlib %{buildroot}/usr/share/package-licenses/clamav/0e1e05a11f29e9060b21c3926ddf6e80d441ca37
cp %{_builddir}/clamav-0.103.3/libclamav/c++/llvm/LICENSE.TXT %{buildroot}/usr/share/package-licenses/clamav/22b913e80d34b4b5eba70ee11d70f1f487d97348
cp %{_builddir}/clamav-0.103.3/libclamav/c++/llvm/autoconf/LICENSE.TXT %{buildroot}/usr/share/package-licenses/clamav/7aecc4590c57a3f3a0735a7e339d8635938d330f
cp %{_builddir}/clamav-0.103.3/libclammspack/COPYING.LIB %{buildroot}/usr/share/package-licenses/clamav/e60c2e780886f95df9c9ee36992b8edabec00bcc
cp %{_builddir}/clamav-0.103.3/libltdl/COPYING.LIB %{buildroot}/usr/share/package-licenses/clamav/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/clamav-0.103.3/unit_tests/input/COPYING %{buildroot}/usr/share/package-licenses/clamav/dfac199a7539a404407098a2541b9482279f690d
pushd ../buildavx2/
%make_install_v3
popd
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/clamav.conf
## install_append content
for sample in clamav-milter.conf clamd.conf freshclam.conf; do
install -D -m0644 etc/$sample.sample %{buildroot}/usr/share/defaults/clamav/$sample
done
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clamav-config
/usr/bin/clambc
/usr/bin/clamconf
/usr/bin/clamd
/usr/bin/clamdscan
/usr/bin/clamdtop
/usr/bin/clamonacc
/usr/bin/clamscan
/usr/bin/freshclam
/usr/bin/sigtool
/usr/share/clear/optimized-elf/bin*

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/clamav.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/clamav/clamav-milter.conf
/usr/share/defaults/clamav/clamd.conf
/usr/share/defaults/clamav/freshclam.conf

%files dev
%defattr(-,root,root,-)
/usr/include/clamav-types.h
/usr/include/clamav-version.h
/usr/include/clamav.h
/usr/include/libfreshclam.h
/usr/lib64/libclamav.so
/usr/lib64/libclammspack.so
/usr/lib64/libclamunrar.so
/usr/lib64/libclamunrar_iface.so
/usr/lib64/libfreshclam.so
/usr/lib64/pkgconfig/libclamav.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-clamav

%files lib
%defattr(-,root,root,-)
/usr/lib64/libclamav.so.9
/usr/lib64/libclamav.so.9.0.5
/usr/lib64/libclammspack.so.0
/usr/lib64/libclammspack.so.0.1.0
/usr/lib64/libclamunrar.so.9
/usr/lib64/libclamunrar.so.9.0.5
/usr/lib64/libclamunrar_iface.so.9
/usr/lib64/libclamunrar_iface.so.9.0.5
/usr/lib64/libfreshclam.so.2
/usr/lib64/libfreshclam.so.2.0.1
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clamav/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/clamav/0e1e05a11f29e9060b21c3926ddf6e80d441ca37
/usr/share/package-licenses/clamav/22b913e80d34b4b5eba70ee11d70f1f487d97348
/usr/share/package-licenses/clamav/24c848a024de84cdf4f7db7e65d5102b329a43bd
/usr/share/package-licenses/clamav/28f373b92a4e7883d7243dfc65bb6fc0c9ca167e
/usr/share/package-licenses/clamav/4bdc478d273e3e8c75dbafbce0dc50bb8abc3628
/usr/share/package-licenses/clamav/521256a2cd47b39b31811a5df9bb724662ae326e
/usr/share/package-licenses/clamav/6178fe3d7980af9da8d734c13c56599b6775a20b
/usr/share/package-licenses/clamav/7aecc4590c57a3f3a0735a7e339d8635938d330f
/usr/share/package-licenses/clamav/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/clamav/9a3515c3da4762b6ddbe88f02755b6edc8ce7f15
/usr/share/package-licenses/clamav/a4b006d9829d39c162d3853cf45ef8aa2844615c
/usr/share/package-licenses/clamav/c9b166c9c918ac6f123f0c70778297eb118537bc
/usr/share/package-licenses/clamav/dfac199a7539a404407098a2541b9482279f690d
/usr/share/package-licenses/clamav/e60c2e780886f95df9c9ee36992b8edabec00bcc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clambc.1
/usr/share/man/man1/clamconf.1
/usr/share/man/man1/clamdscan.1
/usr/share/man/man1/clamdtop.1
/usr/share/man/man1/clamscan.1
/usr/share/man/man1/freshclam.1
/usr/share/man/man1/sigtool.1
/usr/share/man/man5/clamav-milter.conf.5
/usr/share/man/man5/clamd.conf.5
/usr/share/man/man5/freshclam.conf.5
/usr/share/man/man8/clamav-milter.8
/usr/share/man/man8/clamd.8
/usr/share/man/man8/clamonacc.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/clamav-clamonacc.service
/usr/lib/systemd/system/clamav-daemon.service
/usr/lib/systemd/system/clamav-daemon.socket
/usr/lib/systemd/system/clamav-freshclam.service
