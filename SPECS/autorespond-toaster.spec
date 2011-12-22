%define 	name autorespond
%define 	pversion 2.0.4
%define 	bversion 1.3
%define 	rpmrelease 6

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
%define		build_fedora_10  0
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
%{?_with_fedora_9:	%{expand: %%define build_fedora_9   1}}
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
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux RedHat 9
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 2
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 3
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 4
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core x86_64 4
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 5
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 5 x86_64
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Linux Fedora Core 6
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Linux Fedora Core 6 x86_64
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%endif

############### RPM ################################
%define		debug_package %{nil}
%define         vtoaster %{pversion}
%define		builddate Fri Jun 12 2009

Name:		%{name}-toaster
Summary:	Simple autoresponder for qmail
Version:	%{vtoaster}
Release:	%{release}
License:	GPL
Group:		System/Servers
URL:		http://www.inter7.com
Source:		autorespond-%{pversion}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}
Packager:	Jake Vickers <jake@qmailtoaster.com>


#------------------------------------------------------------------------------------
%description
#------------------------------------------------------------------------------------
Mail is sent to help@my-company.com.   An automatically generated response
is sent back to the user  with an  address  of "help@my-company.com".  You
can set the  envelope  sender  to an empty string.  However, some programs
will parse the  message  for  the  "From:"  field and send an autoresponse
back to it.  It is received at your autoresponder, and you now have a mail
loop. 

This autoresponder  also catches some other simple situations such as mail
from a mailer-daemon, empty envelope sender, bulk precedence headers, etc.

#------------------------------------------------------------------------------------
%prep
#------------------------------------------------------------------------------------

%define name autorespond
%setup -q -n autorespond-%{pversion}


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


#------------------------------------------------------------------------------------
%build
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}

# We have gcc written in a temp file
export CC="`cat %{_tmppath}/%{name}-%{pversion}-gcc` %{ccflags}"

$CC -Wall -o autorespond autorespond.c


#------------------------------------------------------------------------------------
%install
#------------------------------------------------------------------------------------
install -d %{buildroot}/%{_bindir}
install -m755 autorespond %{buildroot}/%{_bindir}/autorespond


#------------------------------------------------------------------------------------
%clean
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{pversion}
rm -rf %{_tmppath}/%{name}-%{pversion}-gcc


#------------------------------------------------------------------------------------
%files
#------------------------------------------------------------------------------------
%defattr(-,-,root)
%attr(0755,root,root) %{_bindir}/autorespond


#------------------------------------------------------------------------------------
%changelog
#------------------------------------------------------------------------------------
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.6
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Wed Jun 10 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.6
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.5
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.4
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 2.0.4-1.3.4
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.3.3
- Add CentOS 5 i386 support
- Add CentOS 5 x86_64 support
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 2.0.4-1.3.2
- Add Fedora Core 6 support
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.3.1
- Add SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.9
- Add Fedora Core 5 support
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.8
- Add SuSE 10.0 and Mandriva 2006.0 support
* Sat Oct 15 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.7
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.6
- Add CentOS 4 x86_64 support
* Wed Jun 29 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.5
- Add Fedora Core 4 support
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 2.0.4-1.2.4
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Sun Feb 27 2005 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.3
- Add Fedora Core 3 support
- Add CentOS 4 support
* Fri Jun 04 2004 Nick Hemmesch <nick@ndhsoft.com> 2.0.4-1.2.2
- Udpate to autorespond 2.0.4
* Thu Jun 03 2004 Nick Hemmesch <nick@ndhsoft.com> 2.0.2-1.0.8
- Add Fedora Core 2 support
* Mon Dec 29 2003 Nick Hemmesch <nick@ndhsoft.com> 2.0.2-1.0.7
- Add Fedora Core 1 support
* Sun Nov 23 2003 Nick Hemmesch <nick@ndhsoft.com> 2.0.2-1.0.6
- Add Trustix 2.0 support
* Thu May 15 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.5
- Clean-ups on SPEC file: compilation banner, better gcc detects
- Detect gcc-3.2.3
- Red Hat Linux 9.0 support (nick@ndhsoft.com)
- Gnu/Linux Mandrake 9.2 support
* Wed Apr 02 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.4
- Clean-ups
* Mon Mar 31 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.3
- Conectiva Linux 7.0 support
* Sat Feb 01 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0.2
- Redo Macros to prepare supporting larger RPM OS.
  We could be able to compile (and use) packages under every RPM based
  distribution: we just need to write right requirements.
* Sat Jan 25 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1.0-1
- Added MDK 9.1 support
- Try to use gcc-3.2.1
- Added very little patch to compile with newest GLIBC
- Support dor new RPM-4.0.4
* Sat Oct 05 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-0.9.2
- Soft clean-ups
* Sun Sep 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-0.9.1
- RPM macros to detect Mandrake, RedHat, Trustix are OK again. They are
  very basic but they should work.
* Fri Sep 27 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.8.2.0.2-1
- Rebuilded under 0.8 tree.
- Important comments translated from Italian to English.
- Written rpm rebuilds instruction at the top of the file (in english).
* Thu Aug 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.2.0.2-2
- Deleted Mandrake Release Autodetection (creates problems)
* Fri Aug 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.2.0.2-1
- New version: 0.7 toaster (rebuild with 0.7 spec)
* Thu Aug 13 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.6.2.0.2-1
- New version: 0.6 toaster.
* Mon Aug 12 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.5.2.0.2-1
- Checks for gcc-3.2 (default compiler from now)
- New version: 0.5 toaster.
* Tue Aug 08 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.4.2.0.2-1
- Rebuild against 0.4 toaster
* Thu Jul 30 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.2.0.2-2
- Now packages have got 'no sex': you can rebuild them with command line
  flags for specifics targets that are: RedHat, Trustix, and of course
  Mandrake (that is default)
* Sun Jul 28 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.2.0.2.1mdk
- toaster v. 0.3: now it is possible upgrading safely because of 'pversion'
  that is package version and 'version' that is toaster version
* Thu Jul 25 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.2-2.0.2.1mdk
- toaster v. 0.2
* Thu Jul 18 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.1-2.0.2.2mdk
- Added tests for gcc-3.1.1
- Added toaster version (we will need to mantain it too): is vtoaster 0.1
* Mon Jul 15 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.0.2-1mdk
- First RPM package.
