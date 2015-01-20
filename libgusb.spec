%define api 1.0
%define major 2
%define libname %mklibname gusb %{major}
%define girname %mklibname gusb-gir %{api}
%define devname %mklibname gusb -d

Summary:	GLib wrapper around libusb1
Name:		libgusb
Version:	0.2.4
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://gitorious.org/gusb/
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
BuildRequires:	libtool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libusb-1.0)

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package -n %{libname}
Summary:	GLib wrapper around libusb1
Group:		System/Libraries

%description -n %{libname}
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Libraries and headers for gusb
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{devname}
GLib headers and libraries for gusb.

%prep
%setup -q

%build
%configure \
        --disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgusb.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GUsb-%{api}.typelib

%files -n %{devname}
%doc README AUTHORS NEWS COPYING
%{_includedir}/gusb-1
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/gusb.pc
%{_datadir}/gir-1.0/GUsb-1.0.gir
%doc %{_datadir}/gtk-doc/html/gusb

