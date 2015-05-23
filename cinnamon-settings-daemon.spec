Name:		cinnamon-settings-daemon
Version:	2.6.0
Release:	1
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

