Name:      systemd-ci-environment
Version:   0
Release:   4%{?dist}
Summary:   Metapackage for systemd CI

Group:     Development/System
License:   GPLv2+

Requires:  util-linux >= 2.32
Requires:  libcap-devel
Requires:  libmount-devel
Requires:  pam-devel
Requires:  libselinux-devel
Requires:  audit-libs-devel
Requires:  cryptsetup-devel
Requires:  dbus-devel
Requires:  libacl-devel
Requires:  gobject-introspection-devel
Requires:  libblkid-devel
Requires:  xz-devel
Requires:  bzip2-devel
Requires:  libidn-devel
Requires:  libcurl-devel >= 7.32.0
Requires:  kmod-devel
Requires:  elfutils-devel
Requires:  libgcrypt-devel
Requires:  gnutls-devel
Requires:  qrencode-devel
Requires:  libmicrohttpd-devel
Requires:  iptables-devel
Requires:  libxslt
Requires:  docbook-style-xsl
Requires:  pkgconfig
Requires:  intltool
Requires:  gperf
Requires:  gawk
Requires:  tree
Requires:  libseccomp-devel
Requires:  automake
Requires:  autoconf
Requires:  libtool
Requires:  git
Requires:  lz4-devel
Requires:  libxkbcommon-devel

#FIXME
#not present on centos
#Requires:  python3-devel
#Requires:  python3-lxml
#Requires:  firewalld-filesystem

%description
Metapackage with dependencies needed
for building upstream systemd on top of el7.

%files

%changelog
* Wed Dec 05 2018 Frantisek Sumsal <fsumsal@redhat.com> - 0-4
- add lz4-devel and libxkbcommon-devel packages

* Tue Oct 16 2018 Frantisek Sumsal <fsumsal@redhat.com> - 0-3
- bump util-linux version

* Thu Feb 18 2016 Lukáš Nykrýn <lnykryn@redhat.com> - 0-2
- bump libcurl version

* Thu Feb 18 2016 Lukáš Nykrýn <lnykryn@redhat.com> - 0-1
- initial version
