#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-welcome
Version  : 6.3.2
Release  : 23
URL      : https://download.kde.org/stable/plasma/6.3.2/plasma-welcome-6.3.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.2/plasma-welcome-6.3.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.2/plasma-welcome-6.3.2.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-SA-4.0 CC0-1.0 GPL-2.0 GPL-3.0
Requires: plasma-welcome-bin = %{version}-%{release}
Requires: plasma-welcome-data = %{version}-%{release}
Requires: plasma-welcome-lib = %{version}-%{release}
Requires: plasma-welcome-license = %{version}-%{release}
Requires: plasma-welcome-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: CC0-1.0
-->
# Plasma Welcome App
Friendly onboarding wizard for Plasma

%package bin
Summary: bin components for the plasma-welcome package.
Group: Binaries
Requires: plasma-welcome-data = %{version}-%{release}
Requires: plasma-welcome-license = %{version}-%{release}

%description bin
bin components for the plasma-welcome package.


%package data
Summary: data components for the plasma-welcome package.
Group: Data

%description data
data components for the plasma-welcome package.


%package lib
Summary: lib components for the plasma-welcome package.
Group: Libraries
Requires: plasma-welcome-data = %{version}-%{release}
Requires: plasma-welcome-license = %{version}-%{release}

%description lib
lib components for the plasma-welcome package.


%package license
Summary: license components for the plasma-welcome package.
Group: Default

%description license
license components for the plasma-welcome package.


%package locales
Summary: locales components for the plasma-welcome package.
Group: Default

%description locales
locales components for the plasma-welcome package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n plasma-welcome-6.3.2
cd %{_builddir}/plasma-welcome-6.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1741240709
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1741240709
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-welcome
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/f26cccd93362d640ef2c05d1c52b5efe1620a9b2 || :
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/plasma-welcome-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-welcome/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang plasma-welcome

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/plasma-welcome

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.plasma-welcome.desktop
/usr/share/metainfo/org.kde.plasma-welcome.appdata.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/kf6/kded/kded_plasma-welcome.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-welcome/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/plasma-welcome/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/plasma-welcome/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/plasma-welcome/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/plasma-welcome/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-welcome/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/plasma-welcome/f26cccd93362d640ef2c05d1c52b5efe1620a9b2

%files locales -f plasma-welcome.lang
%defattr(-,root,root,-)

