%define libname %mklibname sgp4
%define devname %mklibname sgp4 -d
%define sourcedate 20260122
%define gitcommit d176906

Name:		sgp4
Version:	1.0^%{sourcedate}git%{gitcommit}
Release:	1
Summary:	SGP4 is a satellite tracking library
URL:		https://github.com/dnwrnr/sgp4
License:	GPL
Group:		System/Libraries
#Source0:	https://github.com/dnwrnr/sgp4/archive/%%{version}/%%{name}-%%{version}.tar.gz
Source0:	%{name}-%{sourcedate}-%{gitcommit}.tar.zst
# Fixes hardcoded lib dir path
Patch0:	sgp4-20260122-d176906-fix-cmakelists-libdir.patch

BuildRequires:	cmake
BuildRequires:	glibc-devel
BuildRequires:	ninja

%description
SGP4 is mathematical model used to calculate orbital state vectors of
satellites and space debris relative to the Earth-centered inertial
coordinate system.

%package -n %{libname}
Summary:	%{libname} is a satellite tracking library
Group:		System/Libraries
Provides:	sgp4 = %{version}-%{release}

%description -n %{libname}
%{libname} is a satellite tracking library.

%package -n %{devname}
Summary:	Development files for %{libname}
Group:		Development/C
Provides:	sgp4-devel = %{version}-%{release}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{libname}.

%prep
%autosetup -n %{name}-%{sourcedate}-%{gitcommit} -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
	-DCMAKE_BUILD_TYPE="RelWithDebInfo" \
	-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=OFF \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libsgp4s.so

%files -n %{devname}
%{_includedir}/libsgp4/*
