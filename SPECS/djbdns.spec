%define		name djbdns
%define		version 1.05
%define		rpmrelease 1.0.6


# INSTRUCTIONS!!! <--------------------- READ THEM!!!
#
# You can rebuild  this  package safely using Command 
# Line Overrides. For example, if you want to rebuild
# this package for RedHat just type:
# $ rpm --rebuild --with redhat package.src.rpm
# $ rpm -ba --with redhat package.spec
#
# Default values: 
# Please,  if  you have got an old RPM version, maybe
# you are  not able  to rebuild packages with Command
# Line Overrides.
# In  this case  edit  the following values: just put
# true (1) in the line of your distribution.
# So,  if  you want  to rebuild  the package for your
# RedHat 7.0 just put:
# build_rht_70 1
#
# mdk = GNU/Linux Mandrake
# rht = Linux Red-Hat
# sus = Suse Linux
# cnt = Conectiva Linux
#

%define 	build_sus_100   0
%define 	build_sus_10064   0
%define 	build_sus_101   0
%define 	build_sus_10164   0
%define		build_sus_111	0

%define		build_mdk_100  0
%define		build_mdk_101  0
%define		build_mdk_102  0
%define		build_mdk_103  0
%define		build_mdk_10364  0

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
%define         build_fedora_9  0
%define         build_fedora_10 0

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
%{?_with_sus100:   	%{expand: %%define build_sus_100   1}}
%{?_with_sus10064:   	%{expand: %%define build_sus_10064   1}}
%{?_with_sus101:   	%{expand: %%define build_sus_101   1}}
%{?_with_sus10164:   	%{expand: %%define build_sus_10164   1}}
%{?_with_sus111:        %{expand: %%define build_sus_111  1}}

%{?_with_mdk100:   	%{expand: %%define build_mdk_100  1}}
%{?_with_mdk101:   	%{expand: %%define build_mdk_101  1}}
%{?_with_mdk102:   	%{expand: %%define build_mdk_102  1}}
%{?_with_mdk103:   	%{expand: %%define build_mdk_103  1}}
%{?_with_mdk10364:   	%{expand: %%define build_mdk_10364  1}}

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
%{?_with_fedora_10:     %{expand: %%define build_fedora_10   1}}

%{?_with_cnt40:   	%{expand: %%define build_cnt_40   1}}
%{?_with_cnt4064:   	%{expand: %%define build_cnt_4064   1}}
%{?_with_cnt50:   	%{expand: %%define build_cnt_50   1}}
%{?_with_cnt5064:   	%{expand: %%define build_cnt_5064   1}}

# Distro Statements
%if %{build_sus_100}
%define		release %{rpmrelease}
%define 	ostype SuSE 10.0 Linux
Requires:	sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_sus_100   1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
Requires:	sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_sus_10064   1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{rpmrelease}
%define 	ostype SuSE 10.1 Linux
Requires:	sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_sus_101   1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
Requires:	sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_sus_10164   1
%define		default	       0
%endif

%if %{build_sus_101}
%define         release %{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
Requires:       sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:      bind, caching-nameserver, %{name}-extcache
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_sus_111   1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{rpmrelease}mdk
%define 	ostype Mandriva 2006 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{rpmrelease}mdk
%define 	ostype Mandriva 2006 x86_64 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_rht_90}
%define		release %{rpmrelease}
%define 	ostype RedHat 9 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{rpmrelease}
%define 	ostype Fedora Core 1 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{rpmrelease}
%define 	ostype Fedora Core 2 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{rpmrelease}
%define 	ostype Fedora Core 3 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{rpmrelease}
%define 	ostype Fedora Core 4 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{rpmrelease}
%define 	ostype Fedora Core 5 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{rpmrelease}
%define         ostype Fedora Core 6 Linux
Requires:       chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:      bind, caching-nameserver, %{name}-extcache
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
Requires:       chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:      bind, caching-nameserver, %{name}-extcache
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{rpmrelease}
%define         ostype Fedora 9 Linux
Requires:       chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:      bind, caching-nameserver, %{name}-extcache
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{rpmrelease}
%define         ostype Fedora 10 Linux
Requires:       chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:      bind, caching-nameserver, %{name}-extcache
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{rpmrelease}
%define 	ostype CentOS 4 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{rpmrelease}
%define 	ostype CentOS 5 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
Requires:	chkconfig, initscripts, sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	bind, caching-nameserver, %{name}-extcache
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%endif

############### RPM ################################

%define		debug_package %{nil}
%define		djbdir /var/djbdns
%define		service %{djbdir}/service
%define		_cachexlog /dnscachex/log/main
%define		_cachelog /dnscache/log/main
%define		_tinylog /tinydns/log/main
%define		_axfrlog /axfrdns/log/main
%define		_logdir /var/log/djbdns
%define		builddate Sat Apr 14 2007

Name:		%{name}
Summary:	djbdns DNS server
Version:	%{version}
Release:	%{release}
License:	D. J. Bernstein
Group:		System/Servers
URL:		http://cr.yp.to/djbdns.html
Source:		%{name}-%{version}.tar.bz2
Source1:	doc.tar.bz2
Source2:	%{name}.init
Source3:	%{name}-getdata
Source4:	ftp://ftp.innominate.org/gpa/djb/%{name}-%{version}-man.tar.bz2
Source5:	%{name}.cron
Source6:	tinydns-log.pl
Source7:	%{name}.init.suse
Patch0:		djbdns-1.05-errno.patch.bz2
Patch1:		djbdns-secpatch-03-06-09.patch.bz2
Buildprereq:	shadow-utils
Buildroot:	%{_tmppath}/%{name}-%{version}
Packager:	Jake Vickers <jake@qmailtoaster.com>


#----------------------------------------------------------------------------------
%description
#----------------------------------------------------------------------------------
djbdns is a collection of Domain Name System tools.  It includes several
components:

 * The dnscache program is a local DNS cache.  It accepts recursive DNS
   queries from local clients such as web browsers.  It collects responses
   from remote DNS servers.
 * The tinydns program is a fast, UDP-only DNS server.  It makes local DNS
   information available to the Internet.  It supports load balancing and
   client differentation.
 * The walldns program is a reverse DNS wall.  It provides matching reverse
   and forward records while hiding local host information.
 * The rbldns program is an IP-address-listing DNS server.  It uses DNS to
   publish a list of IP addresses, such as RBL or DUL.
 * The dns library handles outgoing and incoming DNS packets.  It can be
   used by clients such as web browsers to look up host addresses, hot names,
   MX records, etc.  It supports asynchronous resolution.
 * The dnsfilter program is a parallel IP-address-to-host-name converter.
 * The dnsip, dnsipq, dnsname, dnstxt, and dnsmx programs are simple
   command-line interfaces to DNS.
 * The dnsq and dnstrace programs are DNS debugging tools.

If you wish to replicate DNS information to secondary djbdns servers, you will
also need to install openssh and rsync to perform the actual replication.
This is not required unless you want to replicate to a secondary djbdns server
and is not required if your secondary is a BIND DNS server.

Patched for a security exploit discovered March 5, 2009 where the cache could become poisoned.

#----------------------------------------------------------------------------------
%package extcache
#----------------------------------------------------------------------------------
Summary:	djbdns for caching only dns servers
Group:		System/Servers
Requires:	sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	%{name}, caching-nameserver, bind, %{name}-localcache
Obsoletes:	%{name}-cache


#----------------------------------------------------------------------------------
%description extcache
#----------------------------------------------------------------------------------
This package provides djbdns caching and should only be used if you want a
caching nameserver that can be accessed by other hosts.  If you want to run a 
full DNS server, install the djbdns package instead of this one.  If you
want a local-only caching nameserver, install djbdns-localcache.  This
package includes the following components:

 * The dnscache program is a local DNS cache.  It accepts recursive DNS
   queries from local clients such as web browsers.  It collects responses
   from remote DNS servers.
 * The dnsip, dnsipq, dnsname, dnstxt, and dnsmx programs are simple
   command-line interfaces to DNS.


#----------------------------------------------------------------------------------
%package localcache
#----------------------------------------------------------------------------------
Summary:	djbdns for caching only dns servers
Group:		System/Servers
Requires:	sh-utils, daemontools-toaster, ucspi-tcp-toaster
Conflicts:	caching-nameserver, bind, %{name}-extcache
Obsoletes:	%{name}-cache


#----------------------------------------------------------------------------------
%description localcache
#----------------------------------------------------------------------------------
This package provides djbdns caching and should only be used if you want a
caching nameserver that can only be accessed by localhost.  If you want to 
run a full DNS server also, install the djbdns package as well.  If you
want a caching nameserver that can be accessed by other hosts, install 
djbdns-extcache.  This package includes the following components:

 * The dnscache program is a local DNS cache.  It accepts recursive DNS
   queries from local clients such as web browsers.  It collects responses
   from remote DNS servers.
 * The dnsip, dnsipq, dnsname, dnstxt, and dnsmx programs are simple
   command-line interfaces to DNS.


#----------------------------------------------------------------------------------
%package devel
#----------------------------------------------------------------------------------
Summary:	Development files for djbdns
Group:		Development/C
Requires:	%{name}


#----------------------------------------------------------------------------------
%description devel
#----------------------------------------------------------------------------------
These are header and library files for djbdns to be used in third-party 
programs.


#----------------------------------------------------------------------------------
%prep
#----------------------------------------------------------------------------------
%setup -q
%setup -q -T -D -c -a 4 -n %{name}-%{version}
%setup -q -T -D -c -a 1 -n %{name}-%{version}

%patch0 -p1 -b .errno
%patch1 -p0

echo "%{_prefix}" >conf-home


# Try detecting newest gcc (some distributions have got more then one compiler)
[ -f %{_tmppath}/%{name}-%{version}-gcc ] && rm -f %{_tmppath}/%{name}-%{version}-gcc

if   [ -x /usr/bin/gcc-3.2.3 ]; then
	echo "/usr/bin/gcc-3.2.3" > %{_tmppath}/%{name}-%{version}-gcc
elif   [ -x /usr/bin/gcc-3.2.2 ]; then
	echo "/usr/bin/gcc-3.2.2" > %{_tmppath}/%{name}-%{version}-gcc
elif   [ -x /usr/bin/gcc-3.2.1 ]; then
	echo "/usr/bin/gcc-3.2.1" > %{_tmppath}/%{name}-%{version}-gcc
elif [ -x /usr/bin/gcc-3.2 ]; then
        echo "/usr/bin/gcc-3.2" > %{_tmppath}/%{name}-%{version}-gcc
elif [ -x /usr/bin/gcc-3.1.1 ]; then
        echo "/usr/bin/gcc-3.1.1" > %{_tmppath}/%{name}-%{version}-gcc
else
	echo "gcc" > %{_tmppath}/%{name}-%{version}-gcc
fi

# Display compilation flags and OS with nice colors
#----------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{version}-show_flags ] && rm -f %{_tmppath}/%{name}-%{version}-show_flags
cat <<EOF >>%{_tmppath}/%{name}-%{version}-show_flags
#!/bin/sh

RPM=" RPM RELEASE: \033[40m\033[001;033m%{name}-%{version}-%{release} "
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

# Take care to execute and then to delete
#----------------------------------------------------------------------------------
chmod u+x %{_tmppath}/%{name}-%{version}-show_flags
%{_tmppath}/%{name}-%{version}-show_flags
[ -f %{_tmppath}/%{name}-%{version}-show_flags ] && rm -f %{_tmppath}/%{name}-%{version}-show_flags

# We have gcc written in a temp file
echo "`cat %{_tmppath}/%{name}-%{version}-gcc` %{ccflags}"    >conf-cc
echo "`cat %{_tmppath}/%{name}-%{version}-gcc` -s %{ldflags}" >conf-ld

# Delete gcc temp file
[ -f %{_tmppath}/%{name}-%{version}-gcc ] && rm -f %{_tmppath}/%{name}-%{version}-gcc


#----------------------------------------------------------------------------------
%build
#----------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}

make


# make docs (http://cr.yp.to/slashdoc/slashdoc-merge)
for i in packages commands cfunctions fileformats
do
  sort -f /dev/null `find doc/merge -name $i.html` > doc/$i.new
  mv doc/$i.new doc/$i.html
done


#----------------------------------------------------------------------------------
%install
#----------------------------------------------------------------------------------


#make setup check
mkdir -p %{buildroot}{%{_sysconfdir},%{_initrddir},%{_bindir}}
install -m 644 dnsroots.global %{buildroot}%{_sysconfdir}

%if %{build_sus_100} || %{build_sus_10064} || %{build_sus_101} || %{build_sus_10164} || %{build_sus_111}
  install -m 700 %{SOURCE7} %{buildroot}%{_initrddir}/djbdns
%else
  install -m 700 %{SOURCE2} %{buildroot}%{_initrddir}/djbdns
%endif

for i in axfr-get axfrdns axfrdns-conf dnscache dnscache-conf dnsfilter \
  dnsip dnsipq dnsmx dnsname dnsq dnsqr dnstrace dnstracesort dnstxt pickdns \
  pickdns-conf pickdns-data pickdns-data random-ip rbldns rbldns-conf \
  rbldns-data tinydns tinydns-conf tinydns-data tinydns-edit tinydns-get \
  walldns walldns-conf
do
  install -m 755 $i %{buildroot}%{_bindir}
done
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}

# manpages
mkdir -p %{buildroot}%{_mandir}/man{1,5,8}
install -m644 $RPM_BUILD_DIR/%{name}-%{version}/%{name}-man/*.1 %{buildroot}%{_mandir}/man1
install -m644 $RPM_BUILD_DIR/%{name}-%{version}/%{name}-man/*.5 %{buildroot}%{_mandir}/man5
install -m644 $RPM_BUILD_DIR/%{name}-%{version}/%{name}-man/*.8 %{buildroot}%{_mandir}/man8
cp $RPM_BUILD_DIR/%{name}-%{version}/%{name}-man/README \
  $RPM_BUILD_DIR/%{name}-%{version}/README.manpages
mkdir -p %{buildroot}/var/log/djbdns

# cron job
mkdir -p %{buildroot}%{_sysconfdir}/cron.daily
install -m755 %{SOURCE5} %{buildroot}%{_sysconfdir}/cron.daily/djbdns

# install other extras
install -m755 %{SOURCE6} %{buildroot}%{_bindir}

# create service directories
mkdir -p %{buildroot}%{service}
mkdir -p %{buildroot}/service
#mkdir -p %{buildroot}/service/{ dnscachex, dnscache, tinydns, axfrdns }

# stup for chaching nameserver
mkdir -p %{buildroot}%{djbdir}%{_cachexlog}
mkdir -p %{buildroot}%{djbdir}%{_cachelog}
pushd %{buildroot}%{service}
  ln -s ../dnscachex dnscachex
  ln -s ../dnscache dnscache
 cd ../../../service
  ln -s %{djbdir}/dnscachex dnscachex
  ln -s %{djbdir}/dnscache dnscache
popd

# setup for tinydns name server
mkdir -p %{buildroot}%{djbdir}%{_tinylog}
pushd %{buildroot}%{service}
  ln -s ../tinydns tinydns
 cd ../../../service
  ln -s %{djbdir}/tinydns tinydns
popd

# setup for affrdns
mkdir -p %{buildroot}%{djbdir}%{_axfrlog}
pushd %{buildroot}%{service}
  ln -s ../axfrdns axfrdns
 cd ../../../service
  ln -s %{djbdir}/axfrdns axfrdns
popd

# create log symlinks
mkdir -p %{buildroot}%{_logdir}
pushd %{buildroot}%{_logdir}
  ln -s ../../..%{djbdir}%{_cachexlog} dnscachex
  ln -s ../../..%{djbdir}%{_cachelog} dnscache
  ln -s ../../..%{djbdir}%{_tinylog} tinydns
  ln -s ../../..%{djbdir}%{_axfrlog} axfrdns
popd


# devel files
mkdir -p %{buildroot}{%{_includedir}/djbdns,%{_libdir}/djbdns}
cp -av *.h %{buildroot}%{_includedir}/djbdns
cp -av *.a %{buildroot}%{_libdir}/djbdns


#----------------------------------------------------------------------------------
%pre
#----------------------------------------------------------------------------------
### Before installation
# create groups and users
echo "Creating users and groups for djbdns..."
grep "^djbdns:" %{_sysconfdir}/group >/dev/null || groupadd -r djbdns
grep "^dnslog:" %{_sysconfdir}/passwd >/dev/null || useradd -d %{djbdir} -M -r -s /bin/true dnslog
grep "^tinydns:" %{_sysconfdir}/passwd >/dev/null || useradd -d %{djbdir} -M -r -s /bin/true tinydns
grep "^axfrdns:" %{_sysconfdir}/passwd >/dev/null || useradd -d %{djbdir} -M -r -s /bin/true axfrdns


#----------------------------------------------------------------------------------
%pre localcache
#----------------------------------------------------------------------------------
### Before installation
# create groups and users
echo "Creating users and groups for djbdns..."
grep "^djbdns:" %{_sysconfdir}/group >/dev/null || groupadd -r djbdns
grep "^dnscache:" %{_sysconfdir}/passwd >/dev/null || useradd -d %{djbdir} -M -r -s /bin/true dnscache
grep "^dnslog:" %{_sysconfdir}/passwd >/dev/null || useradd -d %{djbdir} -M -r -s /bin/true dnslog


#----------------------------------------------------------------------------------
%pre extcache
#----------------------------------------------------------------------------------
### Before installation
# create groups and users
echo "Creating users and groups for djbdns..."
grep "^djbdns:" %{_sysconfdir}/group >/dev/null || groupadd -r djbdns
grep "^dnscache:" %{_sysconfdir}/passwd >/dev/null || useradd -d %{djbdir} -M -r -s /bin/true dnscache
grep "^dnslog:" %{_sysconfdir}/passwd >/dev/null || useradd -d %{djbdir} -M -r -s /bin/true dnslog


#----------------------------------------------------------------------------------
%post
#----------------------------------------------------------------------------------
# configuration for full nameserver only if install
if [ $1 = "1" ]; then
  # get IP address for eth0
  HOST=`/sbin/ifconfig eth0|grep 'inet addr'|gawk '{print $2}'|cut -d: -f2`
  # obtain a base (x.x.x)
  BASE=`/sbin/ifconfig eth0|grep 'inet addr'|gawk '{print $2}'|cut -d: -f2|cut -d. -f1,2,3`
  echo "Making some intelligent guesses on tinydns configuration, please check"
  echo "%{djbdir}/tinydns to ensure configuration is correct."
  # tinydns-conf will not work if directory already exists so remove first
  rm -rf %{djbdir}/tinydns
  %{_bindir}/tinydns-conf tinydns dnslog %{djbdir}/tinydns $HOST
  echo ""
  echo "Making some intelligent guesses on axfrdns configuration, please check"
  echo "%{djbdir}/axfrdns to ensure configuration is correct."
  # axfrdns-conf will not work if directory already exists so remove first
  rm -rf %{djbdir}/axfrdns
  %{_bindir}/axfrdns-conf axfrdns dnslog %{djbdir}/axfrdns %{djbdir}/tinydns $HOST
  echo "$BASE.:allow" >>%{djbdir}/axfrdns/tcp
  echo ":allow,AXFR=\"\"" >>%{djbdir}/axfrdns/tcp
  echo ""
  echo "Compiling tcp database for axfrdns..."
  pushd %{djbdir}/axfrdns
    make
  popd
  echo ""
  echo "Please modify %{djbdir}/tinydns/root/Makefile to specify IP address of any"
  echo "secondary DNS servers you wish to replicate data to."
  cat << EOF >%{djbdir}/tinydns/root/Makefile
# Modify the following if you will be replicating to a secondary djbdns server
# and replace [secondary_dns] with the IP address of your secondary djbdns server
#
#remote: data.cdb
#	rsync -az -e ssh data.cdb [secondary_dns]:/var/djbdns/tinydns/root/data.cdb

it: build data.cdb

data.cdb: data
	/usr/bin/tinydns-data
build: zone*
	sort -u zone*|grep -v "#" >data
EOF
  cat << EOF >%{djbdir}/tinydns/root/data
# If this is a secondary djbdns server, data should be copied from the
# primary djbdns server using rsync and ssh and should not be modified on
# this system.  Uncomment the following line to protect data.cdb by stopping
# the make program:
#9
EOF
  echo ""
  echo "Post-install configuration completely.  Many guesses have been made to try to"
  echo "automate the setup as much as possible, however you will still need to"
  echo "fine-tune your configuration.  If you are converting to djbdns from BIND,"
  echo "please visit http://cr.yp.to/djbdns/frombind.html for further instrutions on"
  echo "how to do so."
fi
chkconfig --add djbdns


#----------------------------------------------------------------------------------
%post extcache
#----------------------------------------------------------------------------------
# configuration for caching-only nameserver only if install
if [ $1 = "1" ]; then
  # get IP address for eth0
  HOST=`/sbin/ifconfig eth0|grep 'inet addr'|gawk '{print $2}'|cut -d: -f2`
  # obtain a base (x.x.x)
  BASE=`/sbin/ifconfig eth0|grep 'inet addr'|gawk '{print $2}'|cut -d: -f2|cut -d. -f1,2,3`
  echo "Making some intelligent guesses on dnscache configuration, please check"
  echo "%{djbdir}/dnscachex to ensure configuration is correct"
  # dnscache-conf will not work if directory already exists so remove first
  rm -rf %{djbdir}/dnscachex
  %{_bindir}/dnscache-conf dnscache dnslog %{djbdir}/dnscachex $HOST
  touch %{djbdir}/dnscachex/root/ip/$BASE
fi
chkconfig --add djbdns


#----------------------------------------------------------------------------------
%post localcache
#----------------------------------------------------------------------------------
# configuration for caching-only nameserver only if install
if [ $1 = "1" ]; then
  # use localhost address
  echo "Making some intelligent guesses on dnscache configuration, please check"
  echo "%{djbdir}/dnscache to ensure configuration is correct"
  # dnscache-conf will not work if directory already exists so remove first
  rm -rf %{djbdir}/dnscache
  %{_bindir}/dnscache-conf dnscache dnslog %{djbdir}/dnscache
fi
chkconfig --add djbdns


#----------------------------------------------------------------------------------
%preun
#----------------------------------------------------------------------------------
### Before uninstallation
# Try to stop djbdns daemons for those who do not stop it first
if [ -f %{_initrddir}/djbdns ]; then
  # make sure svscan is running to prevent bad error messages
  if [ -f /var/run/djbdns-svscan.pid ]; then
    %{_initrddir}/djbdns stop
  fi
fi
if [ $1 = "0" ]; then
  # delete chkconfig entry if remove (no upgrade)
  chkconfig --del djbdns
fi


#----------------------------------------------------------------------------------
%preun extcache
#----------------------------------------------------------------------------------
### Before uninstallation
# Try to stop djbdns daemons for those who do not stop it first
if [ -f %{_initrddir}/djbdns ]; then
  # make sure svscan is running to prevent bad error messages
  if [ -f /var/run/djbdns-svscan.pid ]; then
    %{_initrddir}/djbdns stop
  fi
fi
if [ $1 = "0" ]; then
  # delete chkconfig entry if remove (no upgrade)
  chkconfig --del djbdns
fi


#----------------------------------------------------------------------------------
%preun localcache
#----------------------------------------------------------------------------------
### Before uninstallation
# Try to stop djbdns daemons for those who do not stop it first
if [ -f %{_initrddir}/djbdns ]; then
  # make sure svscan is running to prevent bad error messages
  if [ -f /var/run/djbdns-svscan.pid ]; then
    %{_initrddir}/djbdns stop
  fi
fi
if [ $1 = "0" ]; then
  # delete chkconfig entry if remove (no upgrade)
  # only if tinydns doesn't exist (means full djbdns is installed also)
  if [ ! -d %{djbdir}/tinydns ]; then
    chkconfig --del djbdns
  fi
fi


#----------------------------------------------------------------------------------
%postun
#----------------------------------------------------------------------------------
### Post uninstallation
# If djbdns is remove (no upgrade):
if [ $1 = "0" ]; then
  # this is needed for user* and group* programs
  export PATH=$PATH:/usr/sbin

  echo ""
  echo "Removing djbdns users (if they exist):"
  for i in tinydns dnslog dnscache axfrdns; do
    if  id -u $i >/dev/null 2>/dev/null ; then
      echo "  Removing $i user ..."
      userdel $i
    fi
  done

  echo ""
  echo "Removing djbdns group (if it exists):"
  if  groupmod djbdns >/dev/null 2>/dev/null ; then
    echo "  Removing djbdns group ..."
    groupdel djbdns
  fi
fi


#----------------------------------------------------------------------------------
%postun extcache
#----------------------------------------------------------------------------------
### Post uninstallation
# If djbdns is remove (no upgrade):
if [ $1 = "0" ]; then
  # this is needed for user* and group* programs
  export PATH=$PATH:/usr/sbin

  echo ""
  echo "Removing djbdns users (if they exist):"
  for i in tinydns dnslog dnscache axfrdns ; do
    if  id -u $i >/dev/null 2>/dev/null ; then
      echo "  Removing $i user ..."
      userdel $i
    fi
  done

  echo ""
  echo "Removing djbdns group (if it exists):"
  if  groupmod djbdns >/dev/null 2>/dev/null ; then
    echo "  Removing djbdns group ..."
    groupdel djbdns
  fi
fi


#----------------------------------------------------------------------------------
%postun localcache
#----------------------------------------------------------------------------------
### Post uninstallation
# If djbdns is remove (no upgrade):
if [ $1 = "0" ]; then
  # only remove users if tinydns doesn't exist (if exists, means full djbdns
  # is installed so don't remove users to break it
  if [ ! -d %{djbdir}/tinydns ]; then
    # this is needed for user* and group* programs
    export PATH=$PATH:/usr/sbin

    echo ""
    echo "Removing djbdns users (if they exist):"
    for i in tinydns dnslog dnscache axfrdns ; do
      if  id -u $i >/dev/null 2>/dev/null ; then
        echo "  Removing $i user ..."
        userdel $i
      fi
    done

    echo ""
    echo "Removing djbdns group (if it exists):"
    if  groupmod djbdns >/dev/null 2>/dev/null ; then
      echo "  Removing djbdns group ..."
      groupdel djbdns
    fi
  fi
fi


#----------------------------------------------------------------------------------
%clean
#----------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}


#----------------------------------------------------------------------------------
%files
#----------------------------------------------------------------------------------
%defattr(-,root,root)
%doc doc/*.html TINYDNS TODO CHANGES README README.manpages
%config(noreplace) %{_sysconfdir}/dnsroots.global
%config(noreplace) %{_sysconfdir}/cron.daily/djbdns
%{_initrddir}/djbdns
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%dir %{djbdir}
%dir %{service}
%dir /service
%attr(1755,root,root) %dir %{djbdir}/tinydns
%{service}/tinydns
%attr(1755,root,root) %dir %{djbdir}/axfrdns
%dir %{service}/axfrdns
%dir /var/log/djbdns
%dir /service/tinydns
%dir /service/axfrdns
%dir /var/log/djbdns/tinydns
%dir /var/log/djbdns/axfrdns


#----------------------------------------------------------------------------------
%files extcache
#----------------------------------------------------------------------------------
%defattr(-,root,root)
%doc doc/*.html TINYDNS TODO CHANGES README README.manpages
%config(noreplace) %{_sysconfdir}/dnsroots.global
%{_initrddir}/djbdns
%{_bindir}/dnscache
%{_bindir}/dnscache-conf
%{_bindir}/dnsip
%{_bindir}/dnsipq
%{_bindir}/dnsname
%{_bindir}/dnstxt
%{_bindir}/dnsmx
%{_mandir}/man8/dnscache.8*
%{_mandir}/man8/dnscache-conf.8*
%{_mandir}/man1/dnsip.1*
%{_mandir}/man1/dnsipq.1*
%{_mandir}/man1/dnsname.1*
%{_mandir}/man1/dnstxt.1*
%{_mandir}/man1/dnsmx.1*
%dir %{djbdir}
%dir %{service}
%dir /service
%attr(1755,root,root) %dir %{djbdir}/dnscachex
%{service}/dnscachex
%dir /var/log/djbdns
%dir /service/dnscachex
%dir /var/log/djbdns/dnscachex


#----------------------------------------------------------------------------------
%files localcache
#----------------------------------------------------------------------------------
%defattr(-,root,root)
%doc doc/*.html TINYDNS TODO CHANGES README README.manpages
%config(noreplace) %{_sysconfdir}/dnsroots.global
%{_initrddir}/djbdns
%{_bindir}/dnscache
%{_bindir}/dnscache-conf
%{_bindir}/dnsip
%{_bindir}/dnsipq
%{_bindir}/dnsname
%{_bindir}/dnstxt
%{_bindir}/dnsmx
%{_mandir}/man8/dnscache.8*
%{_mandir}/man8/dnscache-conf.8*
%{_mandir}/man1/dnsip.1*
%{_mandir}/man1/dnsipq.1*
%{_mandir}/man1/dnsname.1*
%{_mandir}/man1/dnstxt.1*
%{_mandir}/man1/dnsmx.1*
%dir %{djbdir}
%dir %{service}
%dir /service
%attr(1755,root,root) %dir %{djbdir}/dnscache
%dir %{service}/dnscache
%dir /var/log/djbdns
%dir /service/dnscache
%dir /var/log/djbdns/dnscache


#----------------------------------------------------------------------------------
%files devel
#----------------------------------------------------------------------------------
%defattr(-,root,root)
%dir %{_includedir}/djbdns
%{_includedir}/djbdns/*
%dir %{_libdir}/djbdns
%{_libdir}/djbdns/*


#----------------------------------------------------------------------------------
%changelog
#----------------------------------------------------------------------------------
* Fri Mar 06 2009 Jake Vickers <jake@qmailtoaster.com> 1.05-1.0.6
- Added a patch to fix a cache poisoning exploit confirmed by Bernstein
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 1.05-1.0.5
- Added CentOS 5 i386 support 
- Added CentOS 5 x86_64 support 
* Fri Mar 16 2007 Nick Hemmesch <nick@ndhsoft.com> 1.05-1.0.4
- Fix error in spec file to fix tinydns build 
- Thanks to Pritam Dutt for this fix
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 1.05-1.0.3
- Added Fedora Core 6 support
* Wed May 17 2006 Nick Hemmesch <nick@ndhsoft.com> 1.05-1.0.1
- Modify spec file and init scripts to work with all distros
* Tue Aug 02 2005 Nick Hemmesch <nick@ndhsoft.com> 1.05-1.0.1
- Modify previous build to work with QmailToaster
- Originally written by Vincent Danen <vdanen@mandrakesoft.com>
