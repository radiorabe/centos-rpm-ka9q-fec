#
# spec file for package libfec-odr
#
# Copyright (c) 2016 Radio Bern RaBe
#                    http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-libfec-odr
#

%global reponame ka9q-fec
%global upstream_version 3.0.1-odr1


Name:           libfec-odr
Version:        3.0.1.odr1
Release:        0%{?dist}
Summary:        Opendigitalradio's fork of KA9Q's FEC library

License:        LGPLv2+ 
Group:          System Environment/Libraries
URL:            https://github.com/Opendigitalradio/%{reponame}
Source0:        https://github.com/Opendigitalradio/%{reponame}/archive/v%{upstream_version}.tar.gz#/%{name}-%{version}.tar.gz

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
%autosetup -n %{reponame}-%{upstream_version}


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
* Fri Aug 19 2016 Christian Affolter <c.affolter@purplehaze.ch> - 3.0.1.odr1-0
- Switched from Git to first upstream release

* Thu Aug 18 2016 Christian Affolter <c.affolter@purplehaze.ch> - 0-0.1.52067f2
- Initial release
