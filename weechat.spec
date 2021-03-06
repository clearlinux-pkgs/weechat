#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF82F4B16DEC408F8 (webmaster@weechat.org)
#
Name     : weechat
Version  : 3.2
Release  : 37
URL      : https://weechat.org/files/src/weechat-3.2.tar.xz
Source0  : https://weechat.org/files/src/weechat-3.2.tar.xz
Source1  : https://weechat.org/files/src/weechat-3.2.tar.xz.asc
Summary  : WeeChat plugins headers
Group    : Development/Tools
License  : GPL-3.0
Requires: weechat-bin = %{version}-%{release}
Requires: weechat-data = %{version}-%{release}
Requires: weechat-lib = %{version}-%{release}
Requires: weechat-license = %{version}-%{release}
Requires: weechat-locales = %{version}-%{release}
BuildRequires : aspell-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : gettext-bin
BuildRequires : gnutls-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : lua-dev
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : php
BuildRequires : php-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(python3)
BuildRequires : pkgconfig(python3-embed)
BuildRequires : python3-dev
BuildRequires : ruby
Patch1: pkgconfig-curl.patch

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
%setup -q -n weechat-3.2
cd %{_builddir}/weechat-3.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624502411
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%autogen --disable-static --enable-python3 \
--disable-perl
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1624502411
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/weechat
cp %{_builddir}/weechat-3.2/COPYING %{buildroot}/usr/share/package-licenses/weechat/0dd432edfab90223f22e49c02e2124f87d6f0a56
%make_install
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
/usr/lib64/weechat/plugins/alias.so
/usr/lib64/weechat/plugins/alias.so.0
/usr/lib64/weechat/plugins/alias.so.0.0.0
/usr/lib64/weechat/plugins/buflist.so
/usr/lib64/weechat/plugins/buflist.so.0
/usr/lib64/weechat/plugins/buflist.so.0.0.0
/usr/lib64/weechat/plugins/charset.so
/usr/lib64/weechat/plugins/charset.so.0
/usr/lib64/weechat/plugins/charset.so.0.0.0
/usr/lib64/weechat/plugins/exec.so
/usr/lib64/weechat/plugins/exec.so.0
/usr/lib64/weechat/plugins/exec.so.0.0.0
/usr/lib64/weechat/plugins/fifo.so
/usr/lib64/weechat/plugins/fifo.so.0
/usr/lib64/weechat/plugins/fifo.so.0.0.0
/usr/lib64/weechat/plugins/fset.so
/usr/lib64/weechat/plugins/fset.so.0
/usr/lib64/weechat/plugins/fset.so.0.0.0
/usr/lib64/weechat/plugins/irc.so
/usr/lib64/weechat/plugins/irc.so.0
/usr/lib64/weechat/plugins/irc.so.0.0.0
/usr/lib64/weechat/plugins/logger.so
/usr/lib64/weechat/plugins/logger.so.0
/usr/lib64/weechat/plugins/logger.so.0.0.0
/usr/lib64/weechat/plugins/lua.so
/usr/lib64/weechat/plugins/lua.so.0
/usr/lib64/weechat/plugins/lua.so.0.0.0
/usr/lib64/weechat/plugins/python.so
/usr/lib64/weechat/plugins/python.so.0
/usr/lib64/weechat/plugins/python.so.0.0.0
/usr/lib64/weechat/plugins/relay.so
/usr/lib64/weechat/plugins/relay.so.0
/usr/lib64/weechat/plugins/relay.so.0.0.0
/usr/lib64/weechat/plugins/script.so
/usr/lib64/weechat/plugins/script.so.0
/usr/lib64/weechat/plugins/script.so.0.0.0
/usr/lib64/weechat/plugins/spell.so
/usr/lib64/weechat/plugins/spell.so.0
/usr/lib64/weechat/plugins/spell.so.0.0.0
/usr/lib64/weechat/plugins/trigger.so
/usr/lib64/weechat/plugins/trigger.so.0
/usr/lib64/weechat/plugins/trigger.so.0.0.0
/usr/lib64/weechat/plugins/xfer.so
/usr/lib64/weechat/plugins/xfer.so.0
/usr/lib64/weechat/plugins/xfer.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/weechat/0dd432edfab90223f22e49c02e2124f87d6f0a56

%files locales -f weechat.lang
%defattr(-,root,root,-)

