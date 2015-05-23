Name:		cinnamon-settings-daemon
Version:	2.4.3
Release:	%mkrel 2
Summary:	The daemon sharing settings from CINNAMON to GTK+/KDE applications
Group:		Graphical desktop/Cinnamon
License:	GPLv2+ and LGPLv2+
URL:		http://cinnamon.linuxmint.com
Source0:        %{name}-%{version}.tar.gz
#SourceGet0:	https://github.com/linuxmint/cinnamon-settings-daemon/archive/%{version}.tar.gz
Patch0: upower_critical-action.patch

BuildRequires:	pkgconfig(cinnamon-desktop) >= 1.0.0
BuildRequires:	pkgconfig(colord) >= 0.1.9
BuildRequires:	pkgconfig(dbus-1) >= 1.1.2
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(gio-2.0) >= 2.26.0
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.3.18
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(kbproto)
BuildRequires:	pkgconfig(lcms2) >= 2.2
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libgnomekbd) >= 2.91.1
BuildRequires:	pkgconfig(libgnomekbdui) >= 2.91.1
BuildRequires:	pkgconfig(libnotify) >= 0.7.3
BuildRequires:	pkgconfig(libpulse) >= 0.9.16
BuildRequires:	pkgconfig(libpulse-mainloop-glib) >= 0.9.16
BuildRequires:	pkgconfig(libsystemd-login)
BuildRequires:	pkgconfig(libxklavier) >= 5.0
BuildRequires:	pkgconfig(nss) >= 3.11.2
BuildRequires:	pkgconfig(polkit-gobject-1) >= 0.97
BuildRequires:	pkgconfig(upower-glib) >= 0.99.0
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xi)
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	cups-devel
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires: pkgconfig(xorg-wacom)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(xtst)

%description
A daemon to share settings from CINNAMON to other applications. It also
handles global keybindings, and many of desktop-wide settings.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dbus-glib-devel

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.
 

%prep
%setup -q -n cinnamon-settings-daemon-%{version}
%patch0 -p1

%build
sed -i -e 's@{ACLOCAL_FLAGS}@{ACLOCAL_FLAGS} -I m4@g' Makefile.am
echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac
NOCONFIGURE=1 ./autogen.sh
%configure2_5x --disable-static \
           --enable-profiling \
           --enable-systemd
%make


%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS COPYING
%config %{_sysconfdir}/dbus-1/system.d/org.cinnamon.SettingsDaemon.DateTimeMechanism.conf
%{_libdir}/cinnamon-settings-daemon-3.0/
%{_libexecdir}/cinnamon-settings-daemon
%{_libexecdir}/csd-backlight-helper
%{_libexecdir}/csd-datetime-mechanism
%{_libexecdir}/csd-locate-pointer
%{_libexecdir}/csd-printer
%{_libexecdir}/csd-list-wacom
%{_libexecdir}/csd-wacom-led-helper
%{_datadir}/applications/cinnamon-settings-daemon.desktop
%{_datadir}/cinnamon-settings-daemon/
%{_datadir}/dbus-1/system-services/org.cinnamon.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/glib-2.0/schemas/org.cinnamon.settings-daemon*.xml
%{_datadir}/icons/hicolor/*/apps/csd-xrandr.*
%{_datadir}/polkit-1/actions/org.cinnamon.settings*.policy
%{_mandir}/man1/cinnamon-settings-daemon.1.*

%files devel
%{_includedir}/cinnamon-settings-daemon-3.0/
%{_libdir}/pkgconfig/cinnamon-settings-daemon.pc
%{_libexecdir}/csd-test-*
%{_datadir}/cinnamon-settings-daemon-3.0/


%changelog
* Thu Nov 27 2014 joequant <joequant> 2.4.3-2.mga5
+ Revision: 799549
- bump for main build

* Sun Nov 23 2014 joequant <joequant> 2.4.3-1.mga5
+ Revision: 798402
- upgrade to 2.4

* Wed Oct 15 2014 umeabot <umeabot> 2.2.4-6.mga5
+ Revision: 747339
- Second Mageia 5 Mass Rebuild

* Thu Sep 18 2014 umeabot <umeabot> 2.2.4-5.mga5
+ Revision: 693611
- Rebuild to fix library dependencies

* Tue Sep 16 2014 umeabot <umeabot> 2.2.4-4.mga5
+ Revision: 678401
- Mageia 5 Mass Rebuild

* Thu Sep 04 2014 colin <colin> 2.2.4-3.mga5
+ Revision: 672041
- Rebuild for new systemd

* Wed Aug 27 2014 fwang <fwang> 2.2.4-2.mga5
+ Revision: 668649
- rebuild for new upower

* Mon Jun 09 2014 joequant <joequant> 2.2.4-1.mga5
+ Revision: 635272
- upgrade to 2.2.4

* Wed May 14 2014 joequant <joequant> 2.2.3-1.mga5
+ Revision: 622793
- fix for wacom compile
- upgrade to 2.2.3

* Fri Apr 18 2014 joequant <joequant> 2.2.1-1.mga5
+ Revision: 616816
- upgrade to 2.2

* Sun Mar 30 2014 joequant <joequant> 2.0.10-3.mga5
+ Revision: 610299
- upgrade to upower 1.0

  + dams <dams>
    - rebuild for new upower

  + fwang <fwang>
    - 2.0.10

* Wed Jan 08 2014 joequant <joequant> 2.0.8-2.mga4
+ Revision: 565561
- push to core/release

* Wed Jan 01 2014 joequant <joequant> 2.0.8-1.mga4
+ Revision: 563793
- upgrade to 2.0.8

* Wed Oct 23 2013 joequant <joequant> 2.0.3-2.mga4
+ Revision: 546393
- upgrade to 2.0.3

* Mon Oct 21 2013 umeabot <umeabot> 2.0.1-2.mga4
+ Revision: 539588
- Mageia 4 Mass Rebuild

* Mon Oct 07 2013 joequant <joequant> 2.0.1-1.mga4
+ Revision: 492502
- update to 2.0.1

* Tue Oct 01 2013 joequant <joequant> 1.9.1-1.mga4
+ Revision: 490040
- update to 1.9.1

* Wed Sep 18 2013 joequant <joequant> 1.0.0-0.20130905gitcb4d724.5.mga4
+ Revision: 481143
- update to git

* Sat Sep 14 2013 wally <wally> 1.0.0-0.4.git0dc4921.mga4
+ Revision: 478952
- rebuild for new colord
- use %%makeinstall_std macro
- move autogen.sh usage to %%build section
- remove unneeded post/postun/posttrans scripts

* Mon Sep 02 2013 joequant <joequant> 1.0.0-0.3.git0dc4921.mga4
+ Revision: 474271
- update to latest git

* Sun Aug 25 2013 joequant <joequant> 1.0.0-0.2.gitb8b57d9.mga4
+ Revision: 471618
- fix color plugin

* Fri Aug 23 2013 joequant <joequant> 1.0.0-0.1.gitb8b57d9.mga4
+ Revision: 470053
- add libcanberra-gtk3 buildrequires
- imported package cinnamon-settings-daemon

