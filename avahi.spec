%{?!WITH_MONO:  %define WITH_MONO 1}
%{?!WITH_COMPAT_DNSSD:  %define WITH_COMPAT_DNSSD 1}
%{?!WITH_COMPAT_HOWL:   %define WITH_COMPAT_HOWL  1}
%ifarch sparc64
%define WITH_MONO 0
%endif
%if 0%{?rhel}
%define WITH_MONO 0
%endif

Name:           avahi
Version:        0.6.25
Release:        8%{?dist}
Summary:        Local network service discovery
Group:          System Environment/Base
License:        LGPLv2
URL:            http://avahi.org
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       dbus, expat
Requires:       libdaemon >= 0.11
Requires(post): initscripts, chkconfig, ldconfig
Requires(pre):  shadow-utils
Requires:       %{name}-libs = %{version}-%{release}
BuildRequires:  automake libtool
BuildRequires:  dbus-devel >= 0.90
BuildRequires:  dbus-glib-devel >= 0.70
BuildRequires:  dbus-python
BuildRequires:  libxml2-python
BuildRequires:  gtk2-devel
BuildRequires:  qt3-devel
BuildRequires:  qt4-devel
BuildRequires:  libglade2-devel
BuildRequires:  libdaemon-devel >= 0.11
BuildRequires:  glib2-devel
BuildRequires:  libcap-devel
BuildRequires:  expat-devel
BuildRequires:  python
BuildRequires:  gdbm-devel
BuildRequires:  pygtk2
BuildRequires:	intltool perl-XML-Parser
%if %{WITH_MONO}
BuildRequires:  mono-devel >= 1.1.13
%endif
Obsoletes:            howl
Source0:        http://avahi.org/download/%{name}-%{version}.tar.gz
# enable mono's mcs to work in beehive buildroot:
Patch2:     avahi-0.6.3-MONO_SHARED_DIR.patch
Patch3:     CVE-2010-2244.patch
Patch4:     0.6.26-initscript.patch

%description
Avahi is a system which facilitates service discovery on
a local network -- this means that you can plug your laptop or
computer into a network and instantly be able to view other people who
you can chat with, find printers to print to or find files being
shared. This kind of technology is already found in MacOS X (branded
'Rendezvous', 'Bonjour' and sometimes 'ZeroConf') and is very
convenient.

%package tools
Summary: Command line tools for mDNS browsing and publishing
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}

%description tools
Command line tools that use avahi to browse and publish mDNS services.

%package ui-tools
Summary: UI tools for mDNS browsing
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: %{name}-ui = %{version}-%{release}
Requires: vnc
Requires: openssh-clients
Requires: gtk2, pygtk2, pygtk2-libglade, gdbm, python, dbus-python

%description ui-tools
Graphical user interface tools that use Avahi to browse for mDNS services.

%package glib
Summary: Glib libraries for avahi
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}
Requires: glib2

%description glib
Libraries for easy use of avahi from glib applications.

%package glib-devel
Summary: Libraries and header files for avahi glib development
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-glib = %{version}-%{release}
Requires: glib2-devel

%description glib-devel
The avahi-devel package contains the header files and libraries
necessary for developing programs using avahi with glib.

%package gobject
Summary: GObject wrapper library for Avahi
Group: System Environment/Base
Requires: glib2
Requires: %{name}-glib = %{version}-%{release}

%description gobject
This library contains a GObject wrapper for the Avahi API

%package gobject-devel
Summary: Libraries and header files for Avahi GObject development
Group: Development/Libraries
Requires: %{name}-gobject = %{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-glib-devel = %{version}-%{release}

%description gobject-devel
The avahi-gobject-devel package contains the header files and libraries
necessary for developing programs using avahi-gobject.

%package ui
Summary: Gtk user interface library for Avahi
Group: System Environment/Base
Requires: gtk2

%description ui
This library contains a Gtk widget for browsing services.

%package ui-devel
Summary: Libraries and header files for Avahi UI development
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-ui = %{version}-%{release}
Requires: %{name}-glib-devel = %{version}-%{release}

%description ui-devel
The avahi-ui-devel package contains the header files and libraries
necessary for developing programs using avahi-ui.

%package qt3
Summary: Qt3 libraries for avahi
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}

%description qt3
Libraries for easy use of avahi from Qt3 applications.

%package qt3-devel
Summary: Libraries and header files for avahi Qt3 development
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-qt3 = %{version}-%{release}
Requires: qt3-devel

%description qt3-devel
The avahi-qt3-devel package contains the header files and libraries
necessary for developing programs using avahi with Qt3.

%package qt4
Summary: Qt4 libraries for avahi
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}

%description qt4
Libraries for easy use of avahi from Qt4 applications.

%package qt4-devel
Summary: Libraries and header files for avahi Qt4 development
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-qt4 = %{version}-%{release}
Requires: qt4-devel

%description qt4-devel
Th avahi-qt4-devel package contains the header files and libraries
necessary for developing programs using avahi with Qt4.

%if %{WITH_MONO}
%package sharp
Summary:   Mono language bindings for avahi mono development
Group:            Development/Libraries
Requires:  mono-core >= 1.1.13

%description sharp
The avahi-sharp package contains the files needed to develop
mono programs that use avahi.

%package ui-sharp
Summary:   Mono language bindings for avahi-ui
Group:     System Environment/Libraries
Requires:  mono-core >= 1.1.13
Requires:  gtk-sharp2
BuildRequires:  gtk-sharp2-devel

%description ui-sharp
The avahi-sharp package contains the files needed to run
Mono programs that use avahi-ui.

%package ui-sharp-devel
Summary:   Mono language bindings for developing with avahi-ui
Group:     Development/Libraries
Requires:  %{name}-ui-sharp = %{version}-%{release}

%description ui-sharp-devel
The avahi-sharp-ui-devel package contains the files needed to develop
Mono programs that use avahi-ui.
%endif

%package libs
Summary:  Libraries for avahi run-time use
Group:    System Environment/Libraries

%description libs
The avahi-libs package contains the libraries needed
to run programs that use avahi.

%package devel
Summary:  Libraries and header files for avahi development
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: pkgconfig

%description devel
The avahi-devel package contains the header files and libraries
necessary for developing programs using avahi.

%package   compat-howl
Summary:   Libraries for howl compatibility
Group:     Development/Libraries
Requires:  %{name} = %{version}-%{release}
Obsoletes: howl-libs
Provides:  howl-libs

%description compat-howl
Libraries that are compatible with those provided by the howl package.

%package   compat-howl-devel
Summary:   Header files for development with the howl compatibility libraries
Group:     Development/Libraries
Requires:  avahi-compat-howl = %{version}-%{release}
Obsoletes: howl-devel
Provides:  howl-devel

%description compat-howl-devel
Header files for development with the howl compatibility libraries.

%package   compat-libdns_sd
Summary:   Libraries for Apple Bonjour mDNSResponder compatibility
Group:     Development/Libraries
Requires:  %{name} = %{version}-%{release}

%description compat-libdns_sd
Libraries for Apple Bonjour mDNSResponder compatibility.

%package   compat-libdns_sd-devel
Summary:   Header files for the Apple Bonjour mDNSResponder compatibility libraries
Group:     Development/Libraries
Requires:  avahi-compat-libdns_sd = %{version}-%{release}

%description compat-libdns_sd-devel
Header files for development with the Apple Bonjour mDNSResponder compatibility
libraries.

%package   autoipd
Summary:   Link-local IPv4 address automatic configuration daemon (IPv4LL)
Group:     System Environment/Base
Requires(pre):        shadow-utils

%description autoipd
avahi-autoipd implements IPv4LL, "Dynamic Configuration of IPv4
Link-Local Addresses"  (IETF RFC3927), a protocol for automatic IP address
configuration from the link-local 169.254.0.0/16 range without the need for a
central server. It is primarily intended to be used in ad-hoc networks which
lack a DHCP server.

%package   dnsconfd
Summary:   Configure local unicast DNS settings based on information published in mDNS
Group:     System Environment/Base
Requires:  %{name} = %{version}-%{release}

%description dnsconfd
avahi-dnsconfd connects to a running avahi-daemon and runs the script
/etc/avahi/dnsconfd.action for each unicast DNS server that is announced on the
local LAN. This is useful for configuring unicast DNS servers in a DHCP-like
fashion with mDNS.

%prep
%setup -q
%if %{WITH_MONO}
%patch2 -p1 -b .MONO_SHARED_DIR
%endif
%patch3 -p1
%patch4 -p1

# nuke rpath, TODO: double-check if still required on new releases
autoreconf -i

%build
%configure --with-distro=fedora --disable-monodoc --without-python-twisted --with-avahi-user=avahi --with-avahi-group=avahi --enable-compat-howl --with-avahi-priv-access-group=avahi --with-autoipd-user=avahi-autoipd --with-autoipd-group=avahi-autoipd \
%if %{WITH_COMPAT_DNSSD}
        --enable-compat-libdns_sd \
%endif
%if ! %{WITH_MONO}
        --disable-mono \
%endif
;

# less invasible anti-rpath hack if one wants to avoid auto*foo
#sed -i -e 's/hardcode_into_libs=yes/hardcode_into_libs=no/' libtool

make %{?_smp_mflags} CFLAGS="-fno-strict-aliasing"
#make %{?_smp_mflags} avahi.devhelp doxygen-run

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# remove example
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/avahi/services/sftp-ssh.service

# remove desktop file for avahi-discover
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/avahi-discover.desktop

# create /var/run/avahi-daemon to ensure correct selinux policy for it:
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/avahi-daemon
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/avahi-autoipd

# remove the documentation directory - let \%doc handle it:
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# remove avahi-bookmarks - unusable without python-twisted,
# which has been judged dangerous and is removed from the
# Fedora Core distribution:
rm -f $RPM_BUILD_ROOT/%{_bindir}/avahi-bookmarks $RPM_BUILD_ROOT/%{_mandir}/man1/avahi-bookmarks*
#
# Make /etc/avahi/etc/localtime owned by avahi:
mkdir -p $RPM_BUILD_ROOT/etc/avahi/etc
touch $RPM_BUILD_ROOT/etc/avahi/etc/localtime
#
# fix bug 197414 - add missing symlinks for avahi-compat-howl and avahi-compat-dns-sd
%if %{WITH_COMPAT_HOWL}
ln -s avahi-compat-howl.pc  $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/howl.pc
%endif
%if %{WITH_COMPAT_DNSSD}
ln -s avahi-compat-libdns_sd.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/libdns_sd.pc
ln -s avahi-compat-libdns_sd/dns_sd.h $RPM_BUILD_ROOT/%{_includedir}/
%endif
#
:;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent group avahi >/dev/null 2>&1 || groupadd \
        -r \
        -g 70 \
        avahi
getent passwd avahi >/dev/null 2>&1 || useradd \
        -r -l \
        -u 70 \
        -g avahi \
        -d %{_localstatedir}/run/avahi-daemon \
        -s /sbin/nologin \
        -c "Avahi mDNS/DNS-SD Stack" \
        avahi
:;

%post
/sbin/ldconfig
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :
# Run avahi-daemon by default:
/sbin/chkconfig --add avahi-daemon >/dev/null 2>&1 || :
if [ "$1" -eq 1 ]; then
   if [ -s /etc/localtime ]; then
        cp -cfp /etc/localtime /etc/avahi/etc/localtime || :
   fi
fi

%preun
if [ "$1" -eq 0 ]; then
    /sbin/service avahi-daemon stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del avahi-daemon
fi

%postun
/sbin/ldconfig || :
if [ "$1" -ge "1" ]; then
   /sbin/service avahi-daemon condrestart >/dev/null 2>&1 || :
fi

%pre autoipd
getent group avahi-autoipd >/dev/null 2>&1 || groupadd \
        -r \
        -g 170 \
        avahi-autoipd
getent passwd avahi-autoipd >/dev/null 2>&1 || useradd \
        -r -l \
        -u 170 \
        -g avahi-autoipd \
        -d %{_localstatedir}/lib/avahi-autoipd \
        -s /sbin/nologin \
        -c "Avahi IPv4LL Stack" \
        avahi-autoipd
:;

%post dnsconfd
# avahi-dnsconfd NOT run by default in any runlevel; add it
# so system-config-services can see it
/sbin/chkconfig --add avahi-dnsconfd >/dev/null 2>&1 || :

%preun dnsconfd
if [ "$1" -eq 0 ]; then
    /sbin/service avahi-dnsconfd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del avahi-dnsconfd
fi

%postun dnsconfd
if [ "$1" -ge "1" ]; then
   /sbin/service avahi-dnsconfd condrestart >/dev/null 2>&1 || :
fi

%post glib -p /sbin/ldconfig
%postun glib -p /sbin/ldconfig

%post compat-howl -p /sbin/ldconfig
%postun compat-howl -p /sbin/ldconfig

%post compat-libdns_sd -p /sbin/ldconfig
%postun compat-libdns_sd -p /sbin/ldconfig

%post qt3 -p /sbin/ldconfig
%postun qt3 -p /sbin/ldconfig

%post qt4 -p /sbin/ldconfig
%postun qt4 -p /sbin/ldconfig

%post ui -p /sbin/ldconfig
%postun ui -p /sbin/ldconfig

%post gobject -p /sbin/ldconfig
%postun gobject -p /sbin/ldconfig

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(0644,root,root,0755)
%doc docs/* avahi-daemon/example.service avahi-daemon/sftp-ssh.service
%attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/avahi-daemon
%dir %{_sysconfdir}/avahi
%dir %{_sysconfdir}/avahi/etc
%ghost %{_sysconfdir}/avahi/etc/localtime
%config(noreplace) %{_sysconfdir}/avahi/hosts
%dir %{_sysconfdir}/avahi/services
%attr(0755,avahi,avahi) %dir %{_localstatedir}/run/avahi-daemon
%config(noreplace) %{_sysconfdir}/avahi/avahi-daemon.conf
%config(noreplace) %{_sysconfdir}/avahi/services/ssh.service
%{_sysconfdir}/dbus-1/system.d/avahi-dbus.conf
%attr(0755,root,root) %{_sbindir}/avahi-daemon
%attr(0755,root,root) %{_libdir}/libavahi-core.so.*
%{_datadir}/avahi
%{_libdir}/avahi
%exclude %{_datadir}/avahi/interfaces
%{_mandir}/man5/*
%{_mandir}/man8/avahi-daemon.*

%files autoipd
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_sbindir}/avahi-autoipd
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/avahi/avahi-autoipd.action
%{_mandir}/man8/avahi-autoipd.*

%files dnsconfd
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/avahi-dnsconfd
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/avahi/avahi-dnsconfd.action
%attr(0755,root,root) %{_sbindir}/avahi-dnsconfd
%{_mandir}/man8/avahi-dnsconfd.*

%files tools
%defattr(0644, root, root, 0755)
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%exclude %{_bindir}/avahi-discover-standalone
%exclude %{_bindir}/b*
%exclude %{_bindir}/avahi-discover
%exclude %{_mandir}/man1/b*
%exclude %{_mandir}/man1/avahi-discover*

%files ui-tools
%defattr(0644, root, root, 0755)
%attr(0755,root,root) %{_bindir}/b*
%attr(0755,root,root) %{_bindir}/avahi-discover
%{_mandir}/man1/b*
%{_mandir}/man1/avahi-discover*
%{_datadir}/applications/b*.desktop
# These are .py files only, so they don't go in lib64
%{_prefix}/lib/python?.?/site-packages/*
%{_datadir}/avahi/interfaces/

%files devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-common.so
%attr(755,root,root) %{_libdir}/libavahi-core.so
%attr(755,root,root) %{_libdir}/libavahi-client.so
%{_includedir}/avahi-client
%{_includedir}/avahi-common
%{_includedir}/avahi-core
%{_libdir}/pkgconfig/avahi-core.pc
%{_libdir}/pkgconfig/avahi-client.pc

%files libs
%defattr(0644, root, root, 0755)
%attr(0755,root,root) %{_libdir}/libavahi-common.so.*
%attr(0755,root,root) %{_libdir}/libavahi-client.so.*

%files glib
%defattr(0755, root, root, 0755)
%{_libdir}/libavahi-glib.so.*

%files glib-devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-glib.so
%{_includedir}/avahi-glib
%{_libdir}/pkgconfig/avahi-glib.pc

%files gobject
%defattr(0755, root, root, 0755)
%{_libdir}/libavahi-gobject.so.*

%files gobject-devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-gobject.so
%{_includedir}/avahi-gobject
%{_libdir}/pkgconfig/avahi-gobject.pc

%files ui
%defattr(0755, root, root, 0755)
%{_libdir}/libavahi-ui.so.*

%files ui-devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-ui.so
%{_includedir}/avahi-ui
%{_libdir}/pkgconfig/avahi-ui.pc

%files qt3
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so.*

%files qt3-devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-qt3.so
%{_includedir}/avahi-qt3/
%{_libdir}/pkgconfig/avahi-qt3.pc

%files qt4
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so.*

%files qt4-devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libavahi-qt4.so
%{_includedir}/avahi-qt4/
%{_libdir}/pkgconfig/avahi-qt4.pc

%if %{WITH_MONO}
%files sharp
%defattr(0644, root, root, 0755)
%{_libdir}/mono/avahi-sharp
%{_libdir}/mono/gac/avahi-sharp
%{_libdir}/pkgconfig/avahi-sharp.pc

%files ui-sharp
%defattr(0644, root, root, 0755)
%{_libdir}/mono/avahi-ui-sharp
%{_libdir}/mono/gac/avahi-ui-sharp

%files ui-sharp-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/avahi-ui-sharp.pc
%endif

%if %{WITH_COMPAT_HOWL}
%files compat-howl
%defattr(0755, root, root, 0755)
%{_libdir}/libhowl.so.*

%files compat-howl-devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libhowl.so
%{_includedir}/avahi-compat-howl
%{_libdir}/pkgconfig/avahi-compat-howl.pc
%{_libdir}/pkgconfig/howl.pc
%endif

%if %{WITH_COMPAT_DNSSD}
%files compat-libdns_sd
%defattr(0755, root, root, 0755)
%{_libdir}/libdns_sd.so.*

%files compat-libdns_sd-devel
%defattr(0644, root, root, 0755)
%attr(755,root,root) %{_libdir}/libdns_sd.so
%{_includedir}/avahi-compat-libdns_sd
%{_includedir}/dns_sd.h
%{_libdir}/pkgconfig/avahi-compat-libdns_sd.pc
%{_libdir}/pkgconfig/libdns_sd.pc
%endif

%changelog
* Wed Jun 30 2010 Soren Sandmann <ssp@redhat.com> - 0.6.25-8
- Fix typo in the spec file: ldconfign->ldconfig
  It breaks the build roots.
- Related: #607296

* Wed Jun 30 2010 Lennart Poettering <lpoetter@redhat.com> - 0.6.25-7
- Fix for CVE-2010-2244
- Resolves: #607296
- Resolves: #594405
- Related 587761
- Related 584761
- Related 584766
- Related 596151
- Related 599435

* Mon Jan 25 2010 Lennart Poettering <lpoetter@redhat.com> - 0.6.25-6
- Move avahi-discover from avahi-tools to avahi-ui-tools
- Resolves: rhbz#554813

* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.6.25-5.1
- disable mono on RHEL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Karsten Hopp <karsten@redhat.com> 0.6.25-4
- Build *-sharp & *-ui-sharp for s390x

* Thu Jun 11 2009 Matthias Clasen <mclasen@redhat.com> - 0.6.25-4
- Use %%find_lang

* Tue May 26 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.6.25-3
- Create avahi-ui-sharp-devel package for pkgconfig dep-chain (#477308).

* Mon May 25 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.6.25-2
- Build arch ppc64 for *-sharp & *-ui-sharp.

* Mon Apr 13 2009 Lennart Poettering <lpoetter@redhat.com> - 0.6.25-1
- New upstream release

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Lennart Poettering <lpoetter@redhat.com> - 0.6.24-1
- New upstream release

* Wed Dec  3 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.22-13
- Fix libtool errors

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.22-12
- Rebuild for Python 2.6

* Wed Jun 04 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.6.22-11
- qt4 bindings (#446904)
- devel: BR: pkgconfig
- nuke rpaths

* Thu Mar 27 2008 Lennart Poettering <lpoetter@redhat.com> - 0.6.22-10
- Add release part to package dependencies (Closed #311601)

* Mon Mar 10 2008 Christopher Aillon <caillon@redhat.com> - 0.6.22-9
- The qt3 subpackage should (Build)Require: qt3

* Mon Mar 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.6.22-8
- updated (completed) German translation by Fabian Affolter (#427090)

* Thu Feb 21 2008 Adam Tkac <atkac redhat com> - 0.6.22-7
- really rebuild against new libcap

* Sun Feb 17 2008 Adam Tkac <atkac redhat com> - 0.6.22-6
- rebuild against new libcap

* Sat Feb 09 2008 Dennis Gilmore <dennis@ausil.us> - 0.6.22-5
- sparc64 does not have mono

* Tue Dec 18 2007 Lubomir Kundrak <lkundrak@redhat.com> - 0.6.22-4
- Make bvnc call vncviewer instead of xvncviewer
- Let ui-tools depend on necessary packages

* Mon Dec 17 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.22-3
- Add missing intltool dependency

* Mon Dec 17 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.22-2
- Fix mistag

* Mon Dec 17 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.22-1
- resolves #274731, #425491: New upstream version

* Tue Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.21-6
- resolves #279301: fix segfault when no domains are configured in resolv.conf (pulled from upstream SVN r1525)

* Thu Sep 6 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.21-5
- resolves #249044: Update init script to use runlevel 96
- resolves #251700: Fix assertion in libdns_sd-compat

* Thu Sep 6 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.21-4
- Ship ssh static service file by default, don't ship ssh-sftp by default
- resolves: #269741: split off avahi-ui-tools package
- resolves: #253734: add missing dependency on avahi-glib-devel to avahi-ui-devel

* Tue Aug 28 2007 Martin Bacovsky <mbacovsk@redhat.com> - 0.6.21-3
- resolves: #246875: Initscript Review

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.21-2
- Fix avahi-browse --help output

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.21-1
- New upstream release

* Thu Aug 9 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.20-7
- Fix tagging borkage

* Thu Aug 9 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.20-6
- fix avahi-autoipd corrupt packet bug
- drop dependency on python for the main package

* Wed Jul 11 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.20-5
- add two patches which are important to get RR updating work properly.
  Will be part of upstream 0.6.21

* Thu Jul  5 2007 Dan Williams <dcbw@redhat.com> - 0.6.20-4
- Add Requires(pre): shadow-utils for avahi-autoipd package

* Mon Jun 25 2007 Bill Nottingham <notting@redhat.com> - 0.6.20-3
- fix %%endif typo

* Mon Jun 25 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.20-2
- add gtk-sharp2-devel to build deps

* Fri Jun 22 2007 Lennart Poettering <lpoetter@redhat.com> - 0.6.20-1
- upgrade to new upstream 0.6.20
- fix a few rpmlint warnings
- create avahi-autoipd user
- no longer create avahi user with a static uid, move to dynamic uids
- drop a couple of patches merged upstream
- Provide "howl" and "howl-devel"
- Split off avahi-autoipd and avahi-dnsconfd
- Introduce avahi-ui packages for the first time
- Reload D-Bus config after installation using dbus-send
- add a couple of missing ldconfig invocations

* Mon Mar 12 2007 Martin Bacovsky <mbacovsk@redhat.com> - 0.6.17-1
- upgrade to new upstream 0.6.17
- redundant patches removal
- removed auto* stuff from specfile since that was no longer needed
- Resolves: #232205: 'service {avahi-dnsconfd,avahi-daemon} status'
  returns 0 when the service is stopped

* Fri Feb  2 2007 Christopher Aillon <cailloN@redhat.com> - 0.6.16-3
- Remove bogus mono-libdir patches

* Tue Jan 23 2007 Jeremy Katz <katzj@redhat.com> - 0.6.16-2
- nuke bogus avahi-sharp -> avahi-devel dep

* Mon Jan 22 2007 Martin Bacovsky <mbacovsk@redhat.com> - 0.6.16-1.fc7
- Resolves: #221763: CVE-2006-6870 Maliciously crafted packed can DoS avahi daemon
- upgrade to new upstream
- patch revision
- Resolves: #218140: avahi configuration file wants a non-existent group

* Wed Dec  6 2006 Jeremy Katz <katzj@redhat.com> - 0.6.15-4
- rebuild against python 2.5

* Mon Nov 27 2006 Martin Bacovsky <mbacovsk@redhat.com> - 0.6.15-3
- automake-1.10 required for building

* Mon Nov 27 2006 Martin Bacovsky <mbacovsk@redhat.com> - 0.6.15-2
- automake-1.9 required for building

* Thu Nov 24 2006 Martin Bacovsky <mbacovsk@redhat.com> - 0.6.15-1
- Upgrade to 0.6.15
- patches revision

* Mon Sep 18 2006 Martin Stransky <stransky@redhat.com> - 0.6.11-6
- added patch from #206445 - ia64: unaligned access errors seen
  during startup of avahi-daemon
- removed unused patches

* Thu Sep 7 2006 Dan Walsh <dwalsh@redhat.com> - 0.6.11-5
- Maintain the security context on the localtime file

* Wed Aug 23 2006 Martin Stransky <stransky@redhat.com> - 0.6.11-4
- fix for #204710 - /etc/init.d/avahi-dnsconfd missing line
  continuation slash (\) in description

* Wed Aug 23 2006 Martin Stransky <stransky@redhat.com> - 0.6.11-3
- added fix for #200767 - avahi-dnsconfd Segmentation fault
  with invalid command line argument
- added dist tag

* Tue Jul 18 2006 John (J5) Palmieri <johnp@redhat.com> - 0.6.11-2.fc6
- add BR for dbus-glib-devel
- fix deprecated functions

* Mon Jul 17 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.11-1.fc6
- Upgrade to upstream version 0.6.11
- fix bug 195674: set 'use-ipv6=yes' in avahi-daemon.conf
- fix bug 197414: avahi-compat-howl and avahi-compat-dns-sd symlinks
- fix bug 198282: avahi-compat-{howl-devel,dns-sd-devel} Requires:

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com>
- rebuild

* Tue Jun 13 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.10-3.FC6
- rebuild for broken mono deps

* Tue Jun 06 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.10-2.FC6
- fix bug 194203: fix permissions on /var/run/avahi-daemon

* Tue May 30 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.10-1.FC6
- Upgrade to upstream version 0.6.10
- fix bug 192080: split avahi-compat-libdns_sd into separate package
                  (same goes for avahi-compat-howl)

* Tue May 02 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.9-9.FC6
- fix avahi-sharp issues for banshee - patches from caillon@redhat.com

* Thu Apr 20 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.9-9.FC6
- fix bug 189427: correct avahi-resolve --help typo

* Mon Mar 20 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.9-8.FC6
- fix bug 185972: remove ellipses in initscript
- fix bug 185965: make chkconfigs unconditional

* Thu Mar 16 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.9-6
- Fix bug 185692: install avahi-sharp into %{_prefix}/lib, not %{_libdir}

* Thu Mar 09 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.9-4
- fix scriptlet error introduced by last fix:
  if user has disabled avahi-daemon, do not enable it during %post

* Wed Mar 08 2006 Bill Nottingham <notting@redhat.com> - 0.6.9-2
- fix scriplet error during installer
- move service-types* to the tools package (avoids multilib conflicts)

* Tue Mar 07 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.9-1
- Upgrade to upstream version 0.6.9

* Thu Feb 23 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.8-1
- Upgrade to upstream version 0.6.8
- fix bug 182462: +Requires(post): initscripts, chkconfig, ldconfig

* Fri Feb 17 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.7-1
- Upgrade to upstream version 0.6.7

* Fri Feb 17 2006 Karsten Hopp <karsten@redhat.de> - 0.6.6-4
- BuildRequires pygtk2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.6.6-3.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.6-3
- rebuild for new gcc (again)
- further fix for bug 178746: fix avahi-dnsconfd initscript

* Tue Feb 07 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.6-2
- rebuild for new gcc, glibc, glibc-kernheaders

* Wed Feb 01 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.6-1
- fix bug 179448: mis-alignment of input cmsghdr msg->msg_control buffer on ia64
- Upgrade to 0.6.6

* Thu Jan 26 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.5-1
- Upgrade to upstream version 0.6.5
- Make /etc/avahi/etc and /etc/avahi/etc/localtime owned by avahi
  package; copy system localtime into chroot in post

* Mon Jan 23 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.4-4
- fix bug 178689: copy localtime to chroot
- fix bug 178784: fix avahi-dnsconfd initscript

* Fri Jan 20 2006 Peter Jones <pjones@redhat.com> - 0.6.4-3
- fix subsystem locking in the initscript

* Thu Jan 19 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.4-2
- fix bug 178127: fully localize the initscript

* Mon Jan 16 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.4-1
- Upgrade to upstream version 0.6.4

* Thu Jan 12 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.3-2
- fix bug 177610: Enable mono support with new avahi-sharp package
- fix bug 177609: add gdbm / gdbm-devel Requires for avahi-browse

* Mon Jan 09 2006 Jason Vas Dias <jvdias@redhat.com> - 0.6.3-1
- Upgrade to upstream version 0.6.3
- fix bug 177148: initscript start should not fail if avahi-daemon running

* Thu Dec 22 2005 Jason Vas Dias <jvdias@redhat.com> - 0.6.1-3
- move initscripts from /etc/init.d to /etc/rc.d/init.d

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Dec 09 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6.1-2
- fix bug 175352: Do not chkconfig --add avahi-daemon
  if user has already configured it

* Wed Dec 07 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6.1-1
- Upgrade to 0.6.1

* Mon Dec 05 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6-6
- fix bug 174799 - fix .spec file \%files permissions

* Fri Dec 02 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6-5
- python-twisted has been removed from the FC-5 distribution - disable its use

* Thu Dec 01 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6-4
- Rebuild for dbus-0.6 - remove use of DBUS_NAME_FLAG_PROHIBIT_REPLACEMENT

* Wed Nov 30 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6-3
- fix bug 172047 - tools should require python-twisted
- fix bug 173985 - docs directory permissions

* Mon Nov 21 2005 Jason Vas Dias<jvdias@redhat.com> - 0.6-1
- Upgrade to upstream version 0.6 - now provides 'avahi-howl-compat'
  libraries / includes.

* Mon Nov 14 2005 Jason Vas Dias<jvdias@redhat.com> - 0.5.2-7
- fix bug 172034: fix ownership of /var/run/avahi-daemon/
- fix bug 172772: .spec file improvements from matthias@rpmforge.net

* Mon Oct 31 2005 Jason Vas Dias<jvdias@redhat.com> - 0.5.2-6
- put back avahi-devel Obsoletes: howl-devel

* Mon Oct 31 2005 Alexander Larsson <alexl@redhat.com> - 0.5.2-5
- Obsoletes howl, howl-libs, as we want to get rid of them on updates
- No provides yet, as the howl compat library is in Avahi 0.6.0.

* Sun Oct 30 2005 Florian La Roche <laroche@redhat.com>
- disable the Obsoletes: howl until the transition is complete

* Fri Oct 28 2005 Jason Vas Dias<jvdias@redhat.com> - 0.5.2-3
- change initscript to start avahi-daemon AFTER messagebus

* Wed Oct 26 2005 Karsten Hopp <karsten@redhat.de> 0.5.2-2
- add buildrequires dbus-python

* Fri Oct 21 2005 Alexander Larsson <alexl@redhat.com> - 0.5.2-1
- Initial package
