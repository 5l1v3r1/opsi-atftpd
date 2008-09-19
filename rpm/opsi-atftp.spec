Name:           opsi-atftp
Summary:        advanced TFTP server - opsi version with pcre, fifo and max-blksize patches
License:        GPL v2 or later
Group:          Productivity/Networking/Opsi
AutoReqProv:    on
Version:        0.7
Release:        1
Summary:        OPSI linux bootimage
%define tarname opsi-linux-bootimage
Source:         %{tarname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# ===[ description ]================================
%description
Multi-threaded TFTP server implementing all options (option extension and
multicast) as specified in RFC1350, RFC2090, RFC2347, RFC2348 and RFC2349.
Atftpd also supports multicast protocol known as mtftp, defined in the PXE
specification. The server supports being started from inetd(8) as well as
in daemon mode using init scripts.
This version of atftpd is patched to support reading from named pipes and
blksize limits. 

%package client
Summary: Advanced Trivial File Transfer Protocol (ATFTP) - TFTP client
Group: Applications/Internet

%description client
Advanced Trivial File Transfer Protocol client program for requesting
files using the TFTP protocol.

# ===[ debug_package ]==============================
%debug_package

# ===[ prep ]=======================================
%prep

# ===[ setup ]======================================
%setup

# ===[ build ]======================================
%build
%configure
make

# ===[ install ]====================================
%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != '/' ] && rm -rf $RPM_BUILD_ROOT
%makeinstall

# ===[ clean ]======================================
%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != '/' ] && rm -rf $RPM_BUILD_ROOT

# ===[ post ]=======================================
%post

# ===[ preun ]======================================
%preun
%stop_on_removal opsipxeconfd

# ===[ postun ]=====================================
%postun
%restart_on_update opsipxeconfd
%insserv_cleanup

# ===[ files ]======================================
%files
%{_mandir}/man8/atftpd.8.gz
%{_sbindir}/atftpd
%{_mandir}/man8/in.tftpd.8.gz
%{_sbindir}/in.tftpd

%files client
%{_mandir}/man1/atftp.1.gz
%{_bindir}/atftp

# ===[ changelog ]==================================
%changelog
* Fri Sep 19 2008 - j.schneider@uib.de
- created new package

