#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF82F4B16DEC408F8 (webmaster@weechat.org)
#
Name     : weechat
Version  : 2.3
Release  : 11
URL      : https://weechat.org/files/src/weechat-2.3.tar.xz
Source0  : https://weechat.org/files/src/weechat-2.3.tar.xz
Source99 : https://weechat.org/files/src/weechat-2.3.tar.xz.asc
Summary  : Weechat plugins headers
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
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : php
BuildRequires : php-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(enchant)
BuildRequires : pkgconfig(zlib)
BuildRequires : python
BuildRequires : python-core
BuildRequires : ruby
BuildRequires : zlib-dev
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
%setup -q -n weechat-2.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540119371
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1540119371
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/weechat
cp COPYING %{buildroot}/usr/share/package-licenses/weechat/COPYING
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
/usr/share/icons/hicolor/32x32/apps/weechat.png

%files dev
%defattr(-,root,root,-)
/usr/include/weechat/weechat-plugin.h
/usr/lib64/pkgconfig/weechat.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/weechat/plugins/alias.so
/usr/lib64/weechat/plugins/alias.so.0
/usr/lib64/weechat/plugins/alias.so.0.0.0
/usr/lib64/weechat/plugins/aspell.so
/usr/lib64/weechat/plugins/aspell.so.0
/usr/lib64/weechat/plugins/aspell.so.0.0.0
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
/usr/lib64/weechat/plugins/perl.so
/usr/lib64/weechat/plugins/perl.so.0
/usr/lib64/weechat/plugins/perl.so.0.0.0
/usr/lib64/weechat/plugins/relay.so
/usr/lib64/weechat/plugins/relay.so.0
/usr/lib64/weechat/plugins/relay.so.0.0.0
/usr/lib64/weechat/plugins/script.so
/usr/lib64/weechat/plugins/script.so.0
/usr/lib64/weechat/plugins/script.so.0.0.0
/usr/lib64/weechat/plugins/trigger.so
/usr/lib64/weechat/plugins/trigger.so.0
/usr/lib64/weechat/plugins/trigger.so.0.0.0
/usr/lib64/weechat/plugins/xfer.so
/usr/lib64/weechat/plugins/xfer.so.0
/usr/lib64/weechat/plugins/xfer.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/weechat/COPYING

%files locales -f weechat.lang
%defattr(-,root,root,-)

