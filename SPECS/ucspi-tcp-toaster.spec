%define 	name ucspi-tcp
%define 	pversion 0.88
%define		bversion 1.3
%define 	rpmrelease 9

# INSTRUCTIONS!!! <--------------------- READ THEM!!!
#
# You can rebuild  this  package safely using Command
# Line Overrides. For example, if you want to rebuild
# this package for RedHat just type:
# $ rpmbuild --rebuild --with rht90 package.src.rpm
# $ rpmbuild -ba --with rht90 package.spec
#
# Redhat 9 Linux is the "default" installation
#
# Default values:
# Please,  if  you have got an old RPM version, maybe
# you are  not able  to rebuild packages with Command
# Line Overrides.
#
# mdk = Linux Mandrake Linux
# rht = RedHat Linux
# fdr = Fedora Core Linux
# fedora = Fedora Linux
# sus = Suse Linux
# cnt = CentOS Linux
#

%define		build_sus_100  0
%define		build_sus_10064  0
%define		build_sus_101  0
%define		build_sus_10164  0
%define		build_sus_111	0

%define		build_mdk_100  0
%define		build_mdk_101  0
%define		build_mdk_102  0
%define		build_mdk_103  0
%define		build_mdk_10364  0
%define		build_mdr_09	0

%define 	build_rht_90   0

%define 	build_fdr_10   0
%define 	build_fdr_20   0
%define 	build_fdr_30   0
%define 	build_fdr_40   0
%define 	build_fdr_4064   0
%define 	build_fdr_50   0
%define 	build_fdr_5064   0
%define 	build_fdr_60   0
%define 	build_fdr_6064   0
%define		build_fedora_9	0
%define		build_fedora_964  0
%define		build_fedora_10	0
%define		build_fedora_1064  0
%define		build_fedora_11	0
%define		build_fedora_1164  0

%define 	build_cnt_40   0
%define 	build_cnt_4064   0
%define 	build_cnt_50   0
%define 	build_cnt_5064   0

#####################################################
#                                                   #
#      Do not touch anything below this line        #
#                                                   #
#####################################################

# Default Value (compile for RedHat 9)
%define		default		1

# Command Line Overrides
%{?_with_sus100:   	%{expand: %%define build_sus_100  1}}
%{?_with_sus10064:   	%{expand: %%define build_sus_10064  1}}
%{?_with_sus101:   	%{expand: %%define build_sus_101  1}}
%{?_with_sus10164:   	%{expand: %%define build_sus_10164  1}}
%{?_with_sus111:        %{expand: %%define build_sus_111  1}}

%{?_with_mdk100:   	%{expand: %%define build_mdk_100  1}}
%{?_with_mdk101:   	%{expand: %%define build_mdk_101  1}}
%{?_with_mdk102:   	%{expand: %%define build_mdk_102  1}}
%{?_with_mdk103:   	%{expand: %%define build_mdk_103  1}}
%{?_with_mdk10364:   	%{expand: %%define build_mdk_10364  1}}
%{?_with_mdr09:         %{expand: %%define build_mdr_09  1}}

%{?_with_rht90:   	%{expand: %%define build_rht_90   1}}

%{?_with_fdr10:   	%{expand: %%define build_fdr_10   1}}
%{?_with_fdr20:   	%{expand: %%define build_fdr_20   1}}
%{?_with_fdr30:   	%{expand: %%define build_fdr_30   1}}
%{?_with_fdr40:   	%{expand: %%define build_fdr_40   1}}
%{?_with_fdr4064:   	%{expand: %%define build_fdr_4064   1}}
%{?_with_fdr50:   	%{expand: %%define build_fdr_50   1}}
%{?_with_fdr5064:   	%{expand: %%define build_fdr_5064   1}}
%{?_with_fdr60:   	%{expand: %%define build_fdr_60   1}}
%{?_with_fdr6064:   	%{expand: %%define build_fdr_6064   1}}
%{?_with_fedora_9:      %{expand: %%define build_fedora_9   1}}
%{?_with_fedora_964:    %{expand: %%define build_fedora_964   1}}
%{?_with_fedora_10:     %{expand: %%define build_fedora_10   1}}
%{?_with_fedora_1064:   %{expand: %%define build_fedora_1064   1}}
%{?_with_fedora_11:     %{expand: %%define build_fedora_11   1}}
%{?_with_fedora_1164:   %{expand: %%define build_fedora_1164   1}}

%{?_with_cnt40:   	%{expand: %%define build_cnt_40   1}}
%{?_with_cnt4064:   	%{expand: %%define build_cnt_4064   1}}
%{?_with_cnt50:   	%{expand: %%define build_cnt_50   1}}
%{?_with_cnt5064:   	%{expand: %%define build_cnt_5064   1}}

# Distro Statements
%if %{build_sus_100}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 Linux
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13, zlib-devel >= 1.2.3
Requires:	mysql >= 4.1.13, zlib >= 1.2.3
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13, zlib-devel >= 1.2.3
Requires:	mysql >= 4.1.13, zlib >= 1.2.3
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13, zlib-devel >= 1.2.3
Requires:	mysql >= 4.1.13, zlib >= 1.2.3
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13, zlib-devel >= 1.2.3
Requires:	mysql >= 4.1.13, zlib >= 1.2.3
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
BuildRequires:  libmysqlclient-devel >= 5.0.49, mysql >= 5.0.49, libopenssl-devel >= 0.9.0, zlib-devel >= 1.2.3
Requires:       mysql >= 5.0.49, zlib >= 1.2.3
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
BuildRequires:	libmysql14-devel >= 4.1.11, libmysql14 >= 4.1.11, zlib1-devel >= 1.2.2.2
Requires:	libmysql14 >= 4.1.11, zlib1 >= 1.2.2.2
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
BuildRequires:	lib64mysql14-devel >= 4.1.11, lib64mysql14 >= 4.1.11, zlib1-devel >= 1.2.2.2
Requires:	lib64mysql14 >= 4.1.11, zlib1 >= 1.2.2.2
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
BuildRequires:	libmysql14-devel >= 4.1.11, libmysql14 >= 4.1.11, zlib1-devel >= 1.2.2.2
Requires:	libmysql14 >= 4.1.11, zlib1 >= 1.2.2.2
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
BuildRequires:	libmysql12-devel >= 4.0.20, libmysql12 >= 4.0.20, zlib1-devel >= 1.2.1.1
Requires:	libmysql12 >= 4.0.20, zlib1 >= 1.2.1.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
BuildRequires:	libmysql12-devel >= 4.0.12, libmysql12 >= 4.0.12, zlib1-devel >= 1.2.1
Requires:	libmysql12 >= 4.0.12, zlib1 >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
BuildRequires:  libmysql14-devel >= 4.1.11, libmysql14 >= 4.1.11, zlib1-devel >= 1.2.2.2
Requires:       libmysql14 >= 4.1.11, zlib1 >= 1.2.2.2
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype RedHat 9 Linux
BuildRequires:	zlib-devel >= 1.1.4
Requires:	zlib >= 1.1.4
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 1 Linux
BuildRequires:	zlib-devel >= 1.2.0
Requires:	zlib >= 1.2.0
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 2 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 3 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 Linux
BuildRequires:  zlib-devel >= 1.2.1
Requires:       zlib >= 1.2.1
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
BuildRequires:  zlib-devel >= 1.2.1
Requires:       zlib >= 1.2.1
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
BuildRequires:  zlib-devel >= 1.2.1
Requires:       zlib >= 1.2.1
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
BuildRequires:  zlib-devel >= 1.2.1
Requires:       zlib >= 1.2.1
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
BuildRequires:  zlib-devel >= 1.2.1
Requires:       zlib >= 1.2.1
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
BuildRequires:  zlib-devel >= 1.2.1
Requires:       zlib >= 1.2.1
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
BuildRequires:  zlib-devel >= 1.2.3
Requires:       zlib >= 1.2.3
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
BuildRequires:  zlib-devel >= 1.2.3
Requires:       zlib >= 1.2.3
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%endif

############### RPM ################################


%define		debug_package %{nil}
%define 	vtoaster %{pversion}
%define		qdir /var/qmail/
%define		builddate Fri Jun 12 2009

Name:		%{name}-toaster
Summary:	tcpserver and tcpclient for building TCP client-server apps
Version:	%{vtoaster}
Release:	%{release}
License:	GNU
Group:		System/Servers
URL:		http://cr.yp.to/ucspi-tcp.html
Source:		ucspi-tcp-%{pversion}.tar.bz2
Source1:	ucspi-tcp-%{pversion}-man.tar.bz2
Patch0:		ucspi-tcp-toaster-04182004.patch.bz2
Patch1:		ucspi-tcp-rbltimeout.patch.bz2
Patch2:		ucspi-tcp-limits.patch.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}
Requires:	daemontools-toaster >= 0.76-1.2.2
Obsoletes:	ucspi-tcp-toaster-doc
Packager:	Jake Vickers <jake@qmailtoaster.com>


#----------------------------------------------------------------------------------
%description
#----------------------------------------------------------------------------------
Tcpserver and tcpclient are easy-to-use command-line tools for building TCP
client-server applications.

Tcpserver waits for incoming connections  and, for each  connection, runs a
program  of  your  choice.  Your  program  receives  environment  variables
showing the local and remote host names, IP addresses, and port numbers.

Tcpserver offers a concurrency  limit to  protect  you from  running out of
processes and memory.   When you  are handling 40 (by default) simultaneous
connections, tcpserver smoothly defers acceptance of new connections.

Tcpserver   also   provides   TCP  access  control   features,  similar  to
tcp-wrappers/tcpd's hosts.allow but much faster.  It's access control rules
are compiled into a  hashed format  with cdb,  so it  can easily  deal with
thousands of different hosts.

This package  includes  a  recordio  tool  that  monitors all the input and
output of a server.

Tcpclient makes a TCP connection and runs a program of your choice. It sets
up the same environment variables as tcpserver.

This package includes several sample clients built on top of tcpclient:
who@, date@, finger@, http@, tcpcat, and mconnect.

Tcpserver  and tcpclient  conform to  UCSPI, the UNIX Client-Server Program
Interface, using the TCP protocol.  UCSPI  tools are  available for several
different networks.


#----------------------------------------------------------------------------------
%prep
#----------------------------------------------------------------------------------

%define name ucspi-tcp
%setup -q -n ucspi-tcp-%{pversion}
%patch0 -p0
%patch1 -p0
%patch2 -p1

# Cleanup for gcc
#----------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc

echo "gcc" > %{_tmppath}/%{name}-%{pversion}-gcc


# Display compilation flags and OS with colors ;)
#----------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags
cat <<EOF >>%{_tmppath}/%{name}-%{pversion}-show_flags
#!/bin/sh

RPM=" RPM RELEASE: \033[40m\033[001;033m%{name}-toaster-%{pversion}-%{release} "
OS=" OS TYPE IS : \033[40m\033[001;033m%{ostype} "
BLD=" BUILD DATE : \033[40m\033[001;033m%{builddate} "
CCF=" CCFLAGS    : \033[40m\033[001;033m%{ccflags} "
LDF=" LDFLAGS    : \033[40m\033[001;033m%{ldflags} "

echo
echo
echo -e "\033[40m\033[001;031m\$RPM\033[0m"
echo -e "\033[40m\033[001;031m\$OS\033[0m"
echo -e "\033[40m\033[001;031m\$BLD\033[0m"
echo -e "\033[40m\033[001;031m\$CCF\033[0m"
echo -e "\033[40m\033[001;031m\$LDF\033[0m"
echo
echo

sleep 5

EOF

# Delete show_flags temp files
chmod u+x %{_tmppath}/%{name}-%{pversion}-show_flags
%{_tmppath}/%{name}-%{pversion}-show_flags
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags


#----------------------------------------------------------------------------------
%build
#----------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

mkdir -p %{buildroot}

# We have gcc written in a temp file
echo "`cat %{_tmppath}/%{name}-%{pversion}-gcc` %{ccflags}"    >conf-cc
echo "`cat %{_tmppath}/%{name}-%{pversion}-gcc` -s %{ldflags}" >conf-ld

# Delete gcc temp file
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc

echo "%{_prefix}" >conf-home

make


#----------------------------------------------------------------------------------
%install
#----------------------------------------------------------------------------------
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/{man5,man8}
install -m 755 addcr argv0 date@ delcr finger@ fixcrio http@ mconnect \
  mconnect-io rblsmtpd recordio tcpcat tcpclient tcprules tcprulescheck \
  tcpserver who@ %{buildroot}%{_bindir}
cd $RPM_BUILD_DIR
tar xvfj %{SOURCE1}
cd ucspi-tcp-%{pversion}-man
install -m 644 *.5 %{buildroot}%{_mandir}/man5
install -m 644 *.8 %{buildroot}%{_mandir}/man8


#----------------------------------------------------------------------------------
%clean
#----------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{pversion}


#----------------------------------------------------------------------------------
%files
#----------------------------------------------------------------------------------
%defattr (-,root,root)
%doc CHANGES README TODO VERSION
%attr(0755,root,root) %{_bindir}/addcr
%attr(0755,root,root) %{_bindir}/argv0
%attr(0755,root,root) %{_bindir}/date@
%attr(0755,root,root) %{_bindir}/delcr
%attr(0755,root,root) %{_bindir}/finger@
%attr(0755,root,root) %{_bindir}/fixcrio
%attr(0755,root,root) %{_bindir}/http@
%attr(0755,root,root) %{_bindir}/mconnect
%attr(0755,root,root) %{_bindir}/mconnect-io
%attr(0755,root,root) %{_bindir}/rblsmtpd
%attr(0755,root,root) %{_bindir}/recordio
%attr(0755,root,root) %{_bindir}/tcpcat
%attr(0755,root,root) %{_bindir}/tcpclient
%attr(0755,root,root) %{_bindir}/tcprules
%attr(0755,root,root) %{_bindir}/tcprulescheck
%attr(0755,root,root) %{_bindir}/tcpserver
%attr(0755,root,root) %{_bindir}/who@

%attr(0644,root,root) %{_mandir}/man5/tcp-qualify.5*
%attr(0644,root,root) %{_mandir}/man8/addcr.8*
%attr(0644,root,root) %{_mandir}/man8/argv0.8*
%attr(0644,root,root) %{_mandir}/man8/date@.8*
%attr(0644,root,root) %{_mandir}/man8/delcr.8*
%attr(0644,root,root) %{_mandir}/man8/finger@.8*
%attr(0644,root,root) %{_mandir}/man8/fixcrio.8*
%attr(0644,root,root) %{_mandir}/man8/http@.8*
%attr(0644,root,root) %{_mandir}/man8/mconnect.8*
%attr(0644,root,root) %{_mandir}/man8/rblsmtpd.8*
%attr(0644,root,root) %{_mandir}/man8/recordio.8*
%attr(0644,root,root) %{_mandir}/man8/tcpcat.8*
%attr(0644,root,root) %{_mandir}/man8/tcpclient.8*
%attr(0644,root,root) %{_mandir}/man8/tcprules.8*
%attr(0644,root,root) %{_mandir}/man8/tcprulescheck.8*
%attr(0644,root,root) %{_mandir}/man8/tcpserver.8*
%attr(0644,root,root) %{_mandir}/man8/who@.8*


#----------------------------------------------------------------------------------
%changelog
#----------------------------------------------------------------------------------
* Sun Aug 23 2009 Eric Shubert <ejs@shubes.net> 0.88-1.3.9
- Fixed cleanup to work with async i/o on COS4 with unionfs
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.8
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Tue Jun 02 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.8
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.7
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.6
- Added Suse 11.1 support
* Sun Feb 08 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.6
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.3.5
- Add CentOS 5 i386 support
- Add CentOS 5 x86_64 support
* Wed Jan 24 2007 JP van de Plasse <jeanpaul@i-serve.nl> 0.88-1.3.4
- Included tcpserver limit patch from http://linux.voyager.hr/ucspi-tcp/
* Sun Jan 14 2007 JP van de Plasse <jeanpaul@i-serve.nl> 0.88-1.3.3
- Included a patch for rblsmtpd so a overall timeout can be set.
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88-1.3.2
- Added Fedora Core 6 support
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.3.1
- Add SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.11
- Add Fedora Core 5 support
* Fri Apr 28 2006 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.10
- Cleanup spec file - No major changes
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.9
- Add SuSE 10.0 and Mandriva 2006.0 support
* Fri Oct 14 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.8
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.7
- Add CentOS 4 x86_64 support
* Wed Jun 29 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.6
- Add Fedora Core 4 support
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.88-1.2.5
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Sun May 22 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.4
- Make everyuthing into a single rpm
* Sun Feb 27 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.3
- Add Fedora Core 3 support
- Add CentOS 4 support
* Wed Jun 02 2004 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.2
- Add Fedora Core 2 support
* Sun Apr 18 2004 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.1
- Remove Mysql patch and add ucspi-tcp-toaster-20040123.patch
- This version is required by qmail-toaster-1.03-1.2.1 and higher
* Thu Jan 08 2004 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.10
- Fix Trustix 2.0 support
* Sat Dec 27 2003 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.9
- Add Fedora Core 1 support
* Tue Nov 25 2003 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.8
- Add Trustix 2.0 support
* Thu May 15 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.7
- Clean-ups on SPEC  compilation banner, better gcc detects
- Detect gcc-3.2.3
- Red Hat Linux 9.0 support (nick@ndhsoft.com)
- Gnu/Linux Mandrake 9.2 support
* Wed Apr 02 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.6
- Conectiva Linux 7.0 support
- Clean-ups
- Better dependencies for all distros
* Mon Mar 31 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.5
- Conectiva Linux 7.0 support
* Sun Feb 15 2003 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.4
- Support for Red Hat 8.0
* Wed Feb 05 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.3
- Support for Red Hat 8.0 thanks to Andrew.J.Kay
* Sat Feb 01 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.2
- Redo Macros to prepare supporting larger RPM OS.
  We could be able to compile (and use) packages under every RPM based
  distribution: we just need to write right requirements.
* Sat Jan 25 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.1
- Added MDK 9.1 support
- Try to use gcc-3.2.1
- Added very little patch to compile with newest GLIBC
- Support dor new RPM-4.0.4
* Sun Oct 06 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-0.9.2
- Little clean-ups
* Sun Sep 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-0.9.1
- RPM macros to detect Mandrake, RedHat, Trustix are OK again. They are
  very basic but they should work.
- Packages are named with their proper releases and bversion is from now
  part of the rpm release: we will continue upgrading safely.
* Mon Sep 23 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.8.0.88-1
- Rebuilded under 0.8 tree.
- Important comments translated from Italian to English.
- Written rpm rebuilds instruction at the top of the file (in english).
- Clean-ups
* Sun Sep 22 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.88-3
- Clean-ups on patches
* Thu Aug 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.88-2
- Deleted Mandrake Release Autodetection (creates problems)
* Fri Aug 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.88-1
- New version: 0.7 toaster.
- Clean-ups on compiler detecting (now it works again)
- Better macros to detect Mandrake Release
* Thu Aug 13 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.6.0.88-1
- New version: 0.6 toaster.
* Mon Aug 12 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.5.0.88-1
- Doc package is standalone (someone does not ask for man pages)
- Checks for gcc-3.2 (default compiler from now)
- New version: 0.5 toaster.
* Tue Aug 08 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.4.0.88-1
- Rebuild agains 0.4 toaster
* Thu Aug 06 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.0.88-3
- Better dependencies for RedHat
* Tue Jul 30 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.0.88-2
- Now packages have got 'no sex': you can rebuild them with command line
  flags for specifics targets that are: RedHat, Trustix, and of course
  Mandrake (that is default)
- Fixed the Makefile patch (now it works again): tnx to Carlo Borelli.
* Sun Jul 28 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3-0.88.1mdk
- toaster v. 0.3: now it is possible upgrading safely because of 'pversion'
  that is package version and 'version' that is toaster version
* Thu Jul 25 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.2-0.88.1mdk
- toaster v. 0.2
- added files attributes
* Thu Jul 18 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.1-0.88.3mdk
- Added tests for gcc-3.1.1
- Added toaster version (we will need to mantain it too): is vtoaster 0.1
- Very soft clean-ups.
* Thu Jul 11 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-2mdk
- Renamed the package in toaster (we are building toaster packages with
  toaster patches).
* Mon Jul 01 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1mdk
- First RPM.
