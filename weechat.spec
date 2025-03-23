#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xF82F4B16DEC408F8 (webmaster@weechat.org)
#
Name     : weechat
Version  : 4.6.0
Release  : 66
URL      : https://weechat.org/files/src/weechat-4.6.0.tar.gz
Source0  : https://weechat.org/files/src/weechat-4.6.0.tar.gz
Source1  : https://weechat.org/files/src/weechat-4.6.0.tar.gz.asc
Source2  : F82F4B16DEC408F8.pkey
Summary  : WeeChat plugins headers
Group    : Development/Tools
License  : GPL-3.0
Requires: weechat-bin = %{version}-%{release}
Requires: weechat-data = %{version}-%{release}
Requires: weechat-lib = %{version}-%{release}
Requires: weechat-license = %{version}-%{release}
Requires: weechat-locales = %{version}-%{release}
BuildRequires : aspell-dev
BuildRequires : buildreq-cmake
BuildRequires : gettext-dev
BuildRequires : glibc-dev
BuildRequires : gnupg
BuildRequires : gnutls-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : lua-dev
BuildRequires : ncurses-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : php-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libcjson)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libgcrypt)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(python3-embed)
BuildRequires : pkgconfig(xrender)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : ruby
BuildRequires : tcl-dev
BuildRequires : tk-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains patches that must be applied for some old Debian/Ubuntu
versions, in order to build Debian packages.

%package bin
Summary: bin components for the weechat package.
Group: Binaries
Requires: weechat-data = %{version}-%{release}
Requires: weechat-license = %{version}-%{release}

%description bin
bin components for the weechat package.


%package data
Summary: data components for the weechat package.
Group: Data

%description data
data components for the weechat package.


%package dev
Summary: dev components for the weechat package.
Group: Development
Requires: weechat-lib = %{version}-%{release}
Requires: weechat-bin = %{version}-%{release}
Requires: weechat-data = %{version}-%{release}
Provides: weechat-devel = %{version}-%{release}
Requires: weechat = %{version}-%{release}

%description dev
dev components for the weechat package.


%package lib
Summary: lib components for the weechat package.
Group: Libraries
Requires: weechat-data = %{version}-%{release}
Requires: weechat-license = %{version}-%{release}

%description lib
lib components for the weechat package.


%package license
Summary: license components for the weechat package.
Group: Default

%description license
license components for the weechat package.


%package locales
Summary: locales components for the weechat package.
Group: Default

%description locales
locales components for the weechat package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) F82F4B16DEC408F8' gpg.status
%setup -q -n weechat-4.6.0
cd %{_builddir}/weechat-4.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742761992
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DENABLE_GUILE=NO \
-DENABLE_JAVASCRIPT=NO \
-DENABLE_PHP=NO \
-DENABLE_RUBY=NO \
-DENABLE_TCL=NO \
-Wno-dev  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742761992
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/weechat
cp %{_builddir}/weechat-%{version}/COPYING %{buildroot}/usr/share/package-licenses/weechat/31a3d460bb3c7d98845187c716a30db81c44b615 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang weechat

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/weechat
/usr/bin/weechat-curses
/usr/bin/weechat-headless

%files data
%defattr(-,root,root,-)
/usr/share/applications/weechat.desktop
/usr/share/icons/hicolor/128x128/apps/weechat.png
/usr/share/icons/hicolor/16x16/apps/weechat.png
/usr/share/icons/hicolor/256x256/apps/weechat.png
/usr/share/icons/hicolor/32x32/apps/weechat.png
/usr/share/icons/hicolor/512x512/apps/weechat.png
/usr/share/icons/hicolor/64x64/apps/weechat.png

%files dev
%defattr(-,root,root,-)
/usr/include/weechat/weechat-plugin.h
/usr/lib64/pkgconfig/weechat.pc

%files lib
%defattr(-,root,root,-)
/usr/lib/weechat/plugins/alias.so
/usr/lib/weechat/plugins/buflist.so
/usr/lib/weechat/plugins/charset.so
/usr/lib/weechat/plugins/exec.so
/usr/lib/weechat/plugins/fifo.so
/usr/lib/weechat/plugins/fset.so
/usr/lib/weechat/plugins/irc.so
/usr/lib/weechat/plugins/logger.so
/usr/lib/weechat/plugins/lua.so
/usr/lib/weechat/plugins/perl.so
/usr/lib/weechat/plugins/python.so
/usr/lib/weechat/plugins/relay.so
/usr/lib/weechat/plugins/script.so
/usr/lib/weechat/plugins/spell.so
/usr/lib/weechat/plugins/trigger.so
/usr/lib/weechat/plugins/typing.so
/usr/lib/weechat/plugins/xfer.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/weechat/31a3d460bb3c7d98845187c716a30db81c44b615

%files locales -f weechat.lang
%defattr(-,root,root,-)

