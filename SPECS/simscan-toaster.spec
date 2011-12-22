%define		name simscan
%define		pversion 1.4.0
%define 	bversion 1.3
%define		rpmrelease 8

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
# mdk = Mandrake Linux
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
%define         build_sus_111   0

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
%define         build_fedora_9  0
%define		build_fedora_964  0
%define         build_fedora_10  0
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

# Default Value (compile for RedHat9)
%define		default		1

# Command Line Overrides
%{?_with_sus100:	%{expand: %%define build_sus_100  1}}
%{?_with_sus10064:	%{expand: %%define build_sus_10064  1}}
%{?_with_sus101:	%{expand: %%define build_sus_101  1}}
%{?_with_sus10164:      %{expand: %%define build_sus_10164  1}}
%{?_with_sus111:        %{expand: %%define build_sus_111  1}}

%{?_with_mdk100:	%{expand: %%define build_mdk_100  1}}
%{?_with_mdk101:	%{expand: %%define build_mdk_101  1}}
%{?_with_mdk102:	%{expand: %%define build_mdk_102  1}}
%{?_with_mdk103:	%{expand: %%define build_mdk_103  1}}
%{?_with_mdk10364:	%{expand: %%define build_mdk_10364  1}}
%{?_with_mdr09:         %{expand: %%define build_mdr_09  1}}

%{?_with_rht90:   	%{expand: %%define build_rht_90   1}}

%{?_with_fdr10:   	%{expand: %%define build_fdr_10   1}}
%{?_with_fdr20:   	%{expand: %%define build_fdr_20   1}}
%{?_with_fdr30:   	%{expand: %%define build_fdr_30   1}}
%{?_with_fdr40:   	%{expand: %%define build_fdr_40   1}}
%{?_with_fdr4064:	%{expand: %%define build_fdr_4064   1}}
%{?_with_fdr50:   	%{expand: %%define build_fdr_50   1}}
%{?_with_fdr5064:	%{expand: %%define build_fdr_5064   1}}
%{?_with_fdr60:   	%{expand: %%define build_fdr_60   1}}
%{?_with_fdr6064:	%{expand: %%define build_fdr_6064   1}}
%{?_with_fedora_9:      %{expand: %%define build_fedora_9   1}}
%{?_with_fedora_964:    %{expand: %%define build_fedora_964   1}}
%{?_with_fedora_10:     %{expand: %%define build_fedora_10   1}}
%{?_with_fedora_1064:   %{expand: %%define build_fedora_1064   1}}
%{?_with_fedora_11:     %{expand: %%define build_fedora_11   1}}
%{?_with_fedora_1164:   %{expand: %%define build_fedora_1164   1}}

%{?_with_cnt40:   	%{expand: %%define build_cnt_40   1}}
%{?_with_cnt4064:	%{expand: %%define build_cnt_4064   1}}
%{?_with_cnt50:   	%{expand: %%define build_cnt_50   1}}
%{?_with_cnt5064:	%{expand: %%define build_cnt_5064   1}}

# Distro Statements
%if %{build_sus_100}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype RedHat 9 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 1 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 2 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 3 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%endif

############### RPM ################################

%define		debug_package %{nil}
%define         vtoaster %{pversion}
%define		builddate Fri Jun 12 2009

Name:		%{name}-toaster
Summary:	Simscan for qmail-toaster
Version:	%{vtoaster}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://www.inter7.com/vpopmail
Source0:	simscan-%{pversion}.tar.gz
Patch0:		simscan-1.4.0-clamav.3.patch.bz2
Patch1:		o_creat.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{pversion}-root
BuildPreReq:	qmail-toaster >= 1.03-1.2.4, ripmime-toaster
Requires:	qmail-toaster >= 1.03-1.2.4, clamav-toaster, ripmime-toaster
Packager:       Jake Vickers <jake@qmailtoaster.com>

%define	name simscan
%define	qdir /var/qmail
%define	qbin /var/qmail/bin
%define	qcont /var/qmail/control
%define	qtcp %{_sysconfdir}/tcprules.d/tcp.smtp

#------------------------------------------------------------------------------------
%description
#------------------------------------------------------------------------------------
SimScan is a simplified scanner for qmail similar to qmail-scanner and qscand.
It uses clamav, trophie, and/or spamassassin.  It also supports attachment
blocking by extension.  Simscan is written entirely in C to ensure maximum
speed.  There are several options to allow simscan to scan per domain, and
reject spam mail.


                Current settings
     ---------------------------------------
     user                  = clamav
     qmail directory       = /var/qmail
     work directory        = /var/qmail/simscan
     control directory     = /var/qmail/control
     qmail queue program   = /var/qmail/bin/qmail-queue
     clamdscan program     = /usr/bin/clamdscan
     clamav scan           = ON
     trophie scanning      = OFF
     attachement scan      = ON
     ripmime program       = /usr/bin/ripmime
     custom smtp reject    = ON
     drop message          = OFF
     regex scanner         = OFF
     quarantine processing = OFF
     domain based checking = ON
     add received header   = ON
     spam scanning         = ON
     spamc program         = /usr/bin/spamc
     spamc arguments       =
     spamc user            = OFF
     authenticated users scanned = OFF
     spam passthru         = OFF
     spam hits             = 40

                Current simcontrol config
     ----------------------------------------------------------
     :clam=yes,spam=yes,spam_hits=12,attach=.mp3:.src:.bat:.pif
     
     
#------------------------------------------------------------------------------------
%prep
#------------------------------------------------------------------------------------
%setup -q -n %{name}-%{pversion}
%patch0 -p1
%patch1 -p1

# Cleanup for gcc
#------------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc

echo "gcc" > %{_tmppath}/%{name}-%{pversion}-gcc


# Display compilation flags and OS with colors ;)
#------------------------------------------------------------------------------------
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


# Take care to execute and then to delete
#------------------------------------------------------------------------------------
chmod u+x %{_tmppath}/%{name}-%{pversion}-show_flags
%{_tmppath}/%{name}-%{pversion}-show_flags
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags


#----------------------------------------------------------------------------------
%build
#----------------------------------------------------------------------------------

# Run configure to create makefile
#------------------------------------------------------------------------------------
%configure \
	--enable-user=clamav \
	--enable-attach \
	--enable-ripmime=/usr/bin/ripmime \
	--enable-per-domain \
	--enable-spam \
	--enable-spam-hits=40 \
	--enable-received \
	--enable-clamavdb-path=/usr/share/clamav \
	--enable-custom-smtp-reject
%{__make}


#------------------------------------------------------------------------------------
%install
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}

# install directories
#------------------------------------------------------------------------------------
install -d -o root -g root %{buildroot}%{qdir}
install -d -o root -g root %{buildroot}%{qdir}/bin
install -d -o root -g root %{buildroot}%{qdir}/control
install -d -m750 -o clamav -g root %{buildroot}%{qdir}/simscan
install -d -o root -g root %{buildroot}%{_datadir}/doc/%{name}-%{pversion}

# install files
#------------------------------------------------------------------------------------
install -m4711 -o clamav -g root $RPM_BUILD_DIR/%{name}-%{pversion}/simscan %{buildroot}%{qdir}/bin/simscan
install -m755 -o root -g root $RPM_BUILD_DIR/%{name}-%{pversion}/simscanmk %{buildroot}%{qdir}/bin/simscanmk

# install docs
#------------------------------------------------------------------------------------
for i in AUTHORS ChangeLog INSTALL README TODO ssattach.example; do
 install -m644 -o 0 -g 0 $RPM_BUILD_DIR/%{name}-%{pversion}/$i %{buildroot}%{_datadir}/doc/%{name}-%{pversion}
done

pushd %{buildroot}%{qdir}/control
  echo ":clam=yes,spam=yes,spam_hits=12,attach=.mp3:.src:.bat:.pif" > simcontrol
popd


#------------------------------------------------------------------------------------
%post
#------------------------------------------------------------------------------------

./%{qdir}/bin/simscanmk -g 2>&1 > /dev/null

# We should not overwrite an exisiting tcp.smtp file in case it has custom items in it
if [ -f /etc/tcprules.d/tcp.smtp ] ; then
  touch /etc/tcprules.d/tcp.smtp.new
  echo '127.:allow,RELAYCLIENT="",DKSIGN="/var/qmail/control/domainkeys/%/private",RBLSMTPD="",NOP0FCHECK="1"' > /etc/tcprules.d/tcp.smtp.new
  echo ':allow,BADMIMETYPE="",BADLOADERTYPE="M",CHKUSER_RCPTLIMIT="50",CHKUSER_WRONGRCPTLIMIT="10",QMAILQUEUE="/var/qmail/bin/simscan",DKSIGN="/var/qmail/control/domainkeys/%/private",NOP0FCHECK="1"' >> /etc/tcprules.d/tcp.smtp.new
  echo ""
  echo "Your existing tcp.smtp file was *not* overwritten, but a new one was created called \"tcp.smtp.new\" that"
  echo "you should look at to ensure no new directives were added that may cause issues with your system."
  echo ""
  sleep 10

else

touch /etc/tcprules.d/tcp.smtp
echo '127.:allow,RELAYCLIENT="",DKSIGN="/var/qmail/control/domainkeys/%/private",RBLSMTPD="",NOP0FCHECK="1"' > /etc/tcprules.d/tcp.smtp
echo ':allow,BADMIMETYPE="",BADLOADERTYPE="M",CHKUSER_RCPTLIMIT="50",CHKUSER_WRONGRCPTLIMIT="10",QMAILQUEUE="/var/qmail/bin/simscan",DKSIGN="/var/qmail/control/domainkeys/%/private",NOP0FCHECK="1"' >> /etc/tcprules.d/tcp.smtp
qmailctl cdb

fi

#------------------------------------------------------------------------------------
%clean
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{pversion}
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc


#------------------------------------------------------------------------------------
%files 
#------------------------------------------------------------------------------------
%defattr(644,clamav,clamav)
%attr(0750,clamav,root) %dir %{qdir}/simscan
%attr(0755,root,root) %{qdir}/bin/simscanmk
%attr(4711,clamav,root) %{qdir}/bin/simscan
%attr(0644,root,root) %{_datadir}/doc/%{name}-%{pversion}/*
%attr(0644,clamav,root) %{qdir}/control/simcontrol


#------------------------------------------------------------------------------------
%changelog
#------------------------------------------------------------------------------------
* Thu Aug 13 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0-1.3.8
- Changed minor version number to align with version changes and scripts
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0-1.3.1
- Changed spec file so that tcp.smtp file is no longer overwritten and a tcp.smtp.new is created
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Thu Jun 11 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0-1.3.1
- Added Mandriva 2009 support
- Increased spam_hits to 40 from the original 20
* Thu Apr 23 2009 Jake Vickers <jake@qmailtoaster.com> 1.4.0-1.3.0
- Merged the fork into the main QMT trunk. Thanks to Steve for the package and testing.
- Added Suse 11.1, Fedora 9, Fedora 9 x86_64, Fedora 10, and Fedora 10 x86_64 support
- Patched simscanmk.c to compile with new distro compiler flags (O_CREAT error)
* Wed May 7 2008 Steve Huff <shuff@vecna.org> 1.4.0-1.4.0
- Updated to simscan 1.4.0
- Added John Simpson's patch to support varying ClamAV update file locations
  (http://qmail.jms1.net/simscan/)
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 1.2-1.3.6
- Added CentOS 5 i386 support
- Added CentOS 5 x86_64 support
- Removed DKVERIFY - domainkeys now only signs outgoing mail
* Sat Mar 03 2007 Erik A. Espinoza <espinoza@kabewm.com> 1.3.1-1.3.5
- Skipped RBL checks on localhost
- Modified DKVERIFY to safer defaults
* Thu Jan 11 2007 Erik A. Espinoza <espinoza@kabewm.com> 1.3.1-1.3.4
- Added fix to allow building with ClamAV 0.90rc2 and above, which doesn't use daily.cvd and main.cvd
* Mon Jan 08 2007 Erik A. Espinoza <espinoza@kabewm.com> 1.3.1-1.3.3
- Upgraded to Simscan 1.3.1
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 1.2-1.3.2
- Added Fedora Core 6 support
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 1.2-1.3.1
- Added per domain and spam hits to config
- Added SuSE 10.1 support
* Thu May 18 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 1.2-1.2.8
- Enabled simscan in configure line
- Added ripmime-toaster to Requires line
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 1.2-1.2.7
- Update to simscan-1.2
- Add Fedora Core 5 support
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 1.1-1.2.6
- Add SuSE 10.0 and Mandriva 2006.0 support
* Sat Oct 15 2005 Nick Hemmesch <nick@ndhsoft.com> 1.1-1.2.5
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 1.1-1.2.4
- Add CentOS 4 x86_64 support
* Fri Jul 01 2005 Nick Hemmesch <nick@ndhsoft.com> 1.1-1.2.3
- Add support for Fedora Core 4
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 1.1-1.2.2
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Sat May 28 2005 Nick Hemmesch <nick@ndhsoft.com> 1.1-1.2.1
- Initial simscan-toaster build
