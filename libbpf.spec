%global githubname   libbpf
%global githubver    0.0.5
%global githubfull   %{githubname}-%{githubver}

Name:           %{githubname}
Version:        %{githubver}
Release:        1%{?dist}
Summary:        Libbpf library

License:        LGPLv2 or BSD
URL:            https://github.com/%{githubname}/%{githubname}
Source:         https://github.com/%{githubname}/%{githubname}/archive/v%{githubver}.tar.gz
BuildRequires:  gcc elfutils-libelf-devel elfutils-devel

# This package supersedes libbpf from kernel-tools,
# which has default Epoch: 0. By having Epoch: 1
# this libbpf will take over smoothly
Epoch:          1

%description
A mirror of bpf-next linux tree bpf-next/tools/lib/bpf directory plus its
supporting header files. The version of the package reflects the version of
ABI.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = 1:%{version}-%{release}

%description devel
The %{name}-devel package contains libraries header files for
developing applications that use %{name}

%package static
Summary: Static library for libbpf development
Requires: %{name}-devel = 1:%{version}-%{release}

%description static
The %{name}-static package contains static library for
developing applications that use %{name}

%global make_flags DESTDIR=%{buildroot} OBJDIR=%{_builddir} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags} -Wl,--no-as-needed" LIBDIR=/%{_libdir} NO_PKG_CONFIG=1

%prep
%autosetup -n %{githubfull}

%build
%make_build -C ./src %{make_flags}

%install
%make_install -C ./src %{make_flags}

%files
%{_libdir}/libbpf.so.%{version}
%{_libdir}/libbpf.so.0

%files devel
%{_libdir}/libbpf.so
%{_includedir}/bpf/
%{_libdir}/pkgconfig/libbpf.pc

%files static
%{_libdir}/libbpf.a

%changelog
* Thu Oct 03 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.5-1
- release 0.0.5

* Wed Sep 25 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-2
- Fix libelf linking (BZ#1755317)

* Fri Sep 13 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-1
- Initial release
