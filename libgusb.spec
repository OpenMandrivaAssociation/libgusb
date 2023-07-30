%define api 1.0
%define major 2
%define libname %mklibname gusb %{major}
%define girname %mklibname gusb-gir %{api}
%define devname %mklibname gusb -d
%bcond_without vala

Summary:	GLib wrapper around libusb1
Name:		libgusb
Version:	0.4.6
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://gitorious.org/gusb/
Source0:	https://github.com/hughsie/libgusb/releases/download/%{version}/libgusb-%{version}.tar.xz
# Old source
#Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
Patch0:		libgusb-0.4.5-fix-symbol-versioning.patch
BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(umockdev-1.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(gi-docgen)
%if %{with vala}
BuildRequires:	vala-devel
BuildRequires:	vala-tools
%endif
BuildRequires:	gtk-doc

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
%autosetup -p1

%build
%meson \
%if %{with vala}
	-Dvapi=true
%else
	-Dvapi=false
%endif
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libgusb.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GUsb-%{api}.typelib

%files -n %{devname}
%doc AUTHORS NEWS
%doc %{_datadir}/doc/libgusb/
%{_includedir}/gusb-1
%{_bindir}/gusbcmd
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/gusb.pc
%{_datadir}/gir-1.0/GUsb-1.0.gir
%if %{with vala}
%{_datadir}/vala/vapi/gusb.*
%endif
