%define major     2
%define libname   %mklibname gusb %{major}
%define develname %mklibname gusb -d

Summary:   GLib wrapper around libusb1
Name:      libgusb
Version:   0.1.3
Release:   1
License:   LGPLv2+
Group:     System/Libraries
URL:       https://gitorious.org/gusb/
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel >= 2.16.1
BuildRequires: libtool
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: libusb1-devel

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package -n %{libname}
Summary:   GLib wrapper around libusb1
Group:     System/Libraries

%description -n %{libname}
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package -n %{develname}
Summary: Libraries and headers for gusb
Group: Development/C
Provides: %{name}-devel = %{EVRD}
Requires: %{libname} = %{version}

%description -n %{develname}
GLib headers and libraries for gusb.

%prep
%setup -q

%build
%configure \
        --disable-static \
        --disable-dependency-tracking

%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/libgusb.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libgusb.so.%{major}
%{_libdir}/libgusb.so.%{major}.0.*

%files -n %{develname}
%doc README AUTHORS NEWS COPYING
%{_includedir}/gusb-1
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/gusb.pc
%{_datadir}/gtk-doc/html/gusb


%changelog
* Mon Dec 26 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.1.3-1
+ Revision: 745418
- imported package libgusb

