# Note, that at the time of writing there was no proper release available,
# and also no hint from which original version the project was forked.
# That's why a specific Git commit is used instead.
%global commit0 52067f27f33e9147b46d5b21793eaca1e803d3ff
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global reponame ka9q-fec

Name:           libfec-odr
Version:        0
Release:        0.1.%{shortcommit0}%{?dist}
Summary:        Opendigitalradio's fork of KA9Q's FEC library

License:        LGPLv2+ 
Group:          System Environment/Libraries
URL:            https://github.com/Opendigitalradio/%{reponame}
Source0:        https://github.com/Opendigitalradio/%{reponame}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
#Requires:       


%description
This package provides a set of functions that implement several
popular forward error correction (FEC) algorithms and several low-level routines
useful in modems implemented with digital signal processing (DSP).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{reponame}-%{commit0}


%build
%cmake .
make %{?_smp_mflags}


%check
ctest -V %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README 
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/*


%changelog
* Thu Aug 18 2016 Christian Affolter <c.affolter@purplehaze.ch> - 0-0.1.52067f2
- Initial release
