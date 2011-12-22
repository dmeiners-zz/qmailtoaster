%define		name courier-authlib
%define		pversion 0.59.2
%define 	bversion 1.3
%define		rpmrelease 10
#courier-authlib-0.62.2.tar.bz2
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
# sus = Suse Line
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

# Default Value (compile for RedHat9)
%define		default		1

# Command Line Overrides
%{?_with_sus100:	%{expand: %%define build_sus_100  1}}
%{?_with_sus10064:	%{expand: %%define build_sus_10064  1}}
%{?_with_sus101:	%{expand: %%define build_sus_101  1}}
%{?_with_sus10164:	%{expand: %%define build_sus_10164  1}}
%{?_with_sus111:        %{expand: %%define build_sus_111  1}}

%{?_with_mdk100:	%{expand: %%define build_mdk_100  1}}
%{?_with_mdk101:	%{expand: %%define build_mdk_101  1}}
%{?_with_mdk102:	%{expand: %%define build_mdk_102  1}}
%{?_with_mdk103:	%{expand: %%define build_mdk_103  1}}
%{?_with_mdk10364:	%{expand: %%define build_mdk_10364  1}}
%{?_with_mdr09:         %{expand: %%define build_mdr_09  1}}

%{?_with_rht90:		%{expand: %%define build_rht_90   1}}

%{?_with_fdr10:		%{expand: %%define build_fdr_10   1}}
%{?_with_fdr20:		%{expand: %%define build_fdr_20   1}}
%{?_with_fdr30:		%{expand: %%define build_fdr_30   1}}
%{?_with_fdr40:		%{expand: %%define build_fdr_40   1}}
%{?_with_fdr4064:	%{expand: %%define build_fdr_4064   1}}
%{?_with_fdr50:		%{expand: %%define build_fdr_50   1}}
%{?_with_fdr5064:	%{expand: %%define build_fdr_5064   1}}
%{?_with_fdr60:		%{expand: %%define build_fdr_60   1}}
%{?_with_fdr6064:	%{expand: %%define build_fdr_6064   1}}
%{?_with_fedora_9:	%{expand: %%define build_fedora_9   1}}
%{?_with_fedora_964:    %{expand: %%define build_fedora_964   1}}
%{?_with_fedora_10:	%{expand: %%define build_fedora_10   1}}
%{?_with_fedora_1064:   %{expand: %%define build_fedora_1064   1}}
%{?_with_fedora_11:     %{expand: %%define build_fedora_11   1}}
%{?_with_fedora_1164:   %{expand: %%define build_fedora_1164   1}}

%{?_with_cnt40:		%{expand: %%define build_cnt_40   1}}
%{?_with_cnt4064:	%{expand: %%define build_cnt_4064   1}}
%{?_with_cnt50:		%{expand: %%define build_cnt_50   1}}
%{?_with_cnt5064:	%{expand: %%define build_cnt_5064   1}}

# Distro Statements
%if %{build_sus_100}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_100  1
%define		default	0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10064  1
%define		default	0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_101  1
%define		default	0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10164  1
%define		default	0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_sus_111  1
%define         default 0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_10364  1
%define		default	0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_102  1
%define		default	0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_mdr_09  1
%define         default 0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype RedHat 9 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_rht_90   1
%define		default	0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 1 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_10   1
%define		default	0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 2 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_20   1
%define		default	0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 3 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_30   1
%define		default	0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_40   1
%define		default	0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_4064   1
%define		default	0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_50   1
%define		default	0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_5064   1
%define		default	0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_60   1
%define         default 0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_6064   1
%define         default 0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_9   1
%define         default 0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_964   1
%define         default 0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_10   1
%define         default 0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1064   1
%define         default 0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_11   1
%define         default 0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
BuildRequires:  automake, autoconf
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1164   1
%define         default 0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_40   1
%define		default	0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_4064   1
%define		default	0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_50   1
%define		default	0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
BuildRequires:	automake, autoconf
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%define		default	0
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
%define         _qdir /var/qmail
%define		_spath %{_qdir}/supervise
%define		_qtlogdir /var/log/qmail
%define		builddate Tue Jun 16 2009

Name:		%{name}-toaster
Summary:	courier-authlib for qmail-toaster
Version:	%{vtoaster}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://www.courier-mta.org/
Source0:	courier-authlib-%{pversion}.tar.bz2
Source1:	supervise-authlib.run.bz2
Source2:	supervise-authlib-log.run.bz2
Source3:	authdaemonrc.bz2
BuildRoot:	%{_tmppath}/%{name}-%{pversion}-root
BuildPreReq:    %{_includedir}/ltdl.h
BuildPreReq:	libtool, mysql-devel, zlib-devel, gdbm-devel, expect, gcc-c++
BuildPreReq:	qmail-toaster >= 1.03-1.3.15
Requires:	qmail-toaster >= 1.03-1.3.15
Obsoletes:	courier-imap-toaster < 4
Packager:       Jake Vickers <jake@qmailtoaster.com>

%define	name courier-authlib


#------------------------------------------------------------------------------------
%description
#------------------------------------------------------------------------------------
This package, courier-authlib, allows the new courier imap to use vpopmail for authentication.


#------------------------------------------------------------------------------------
%prep
#------------------------------------------------------------------------------------
%setup -q -n %{name}-%{pversion}


# Cleanup for the compiler
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
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}

# Run configure to create makefile
#------------------------------------------------------------------------------------
%if %{build_rht_90} || %{build_fdr_10} || %{build_fdr_20} || %{build_fdr_30} || %{build_fdr_40} || %{build_fdr_50} ||  %{build_fdr_60} || %{build_fedora_9} || %{build_fedora_10} || %{build_cnt_50} || %{build_cnt_5064} || %{build_cnt_40} || %{build_cnt_4064} || %{build_fdr_4064} || %{build_fdr_5064} || %{build_fdr_6064} || %{build_fedora_964} || %{build_fedora_1064} || %{build_fedora_11} || %{build_fedora_1164}

%configure \
    --with-mailuser=vpopmail \
    --with-mailgroup=vchkpw \
    --sysconfdir=%{_sysconfdir}/courier \
    --with-authvchkpw \
    --without-authuserdb \
    --without-authpam \
    --without-authldap \
    --without-authpwd \
    --with-authshadow \
    --without-authpgsql \
    --without-authmysql \
    --without-authcustom \
    --without-authpipe \
    --enable-ltdl-install=no \
    --with-ssl \
    --with-redhat

%else

%configure \
    --with-mailuser=vpopmail \
    --with-mailgroup=vchkpw \
    --sysconfdir=%{_sysconfdir}/courier \
    --with-authvchkpw \
    --without-authuserdb \
    --without-authpam \
    --without-authldap \
    --without-authpwd \
    --with-authshadow \
    --without-authpgsql \
    --without-authmysql \
    --without-authcustom \
    --without-authpipe \
    --enable-ltdl-install=no \
    --with-ssl
%endif

%{__make}

# Delete gcc temp file
#------------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc


#------------------------------------------------------------------------------------
%install
#------------------------------------------------------------------------------------

# Install into buildroot
#-----------------------------------------------------------------------------
        make DESTDIR=%{buildroot} install


# Install default config
#-----------------------------------------------------------------------------
mkdir -p %{buildroot}%{_sysconfdir}/courier
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/courier/authlib/authdaemonrc.bz2
bunzip2 %{buildroot}%{_sysconfdir}/courier/authlib/authdaemonrc.bz2 

# Supervise
#-----------------------------------------------------------------------------
mkdir -p %{buildroot}%{_spath}/authlib/log
mkdir -p %{buildroot}%{_spath}/authlib/env
mkdir -p %{buildroot}%{_spath}/authlib/supervise
mkdir -p %{buildroot}%{_qtlogdir}/authlib

install -m700 %{SOURCE1} %{buildroot}%{_spath}/authlib/run.bz2
bunzip2 %{buildroot}%{_spath}/authlib/run.bz2
install -m700 %{SOURCE2} %{buildroot}%{_spath}/authlib/log/run.bz2
bunzip2 %{buildroot}%{_spath}/authlib/log/run.bz2

%if %{build_sus_10064} || %{build_sus_10164} || %{build_mdk_10364}
   %{__perl} -pi -e "s|libexec|lib64|g" %{buildroot}%{_spath}/authlib/run
%endif

%if %{build_sus_100} || %{build_sus_101} || %{build_sus_111} || %{build_mdk_100} || %{build_mdk_101} || %{build_mdk_102} || %{build_mdk_103} || %{build_mdr_09}
   %{__perl} -pi -e "s|libexec|lib|g" %{buildroot}%{_spath}/authlib/run
%endif


#------------------------------------------------------------------------------------
%postun
#------------------------------------------------------------------------------------
if [ $1 = "0" ]; then
  rm -fR %{_spath}/authlib/
  rm -fR %{_qtlogdir}/authlib/
fi


#------------------------------------------------------------------------------------
%clean
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{pversion}


#------------------------------------------------------------------------------------
%files 
#------------------------------------------------------------------------------------
%defattr(-,root,root)
%doc README READM*html README.ldap INSTALL INSTALL.html NEWS NEWS.html auth*.html 
%attr(0755,root,root) %dir %{_libexecdir}/courier-authlib
%attr(0755,root,root) %dir %{_sysconfdir}/courier
%attr(0750,qmaill,qmail) %dir %{_qtlogdir}/authlib
%attr(0755,root,root) %dir %{_localstatedir}/spool/authdaemon
%attr(1700,qmaill,qmail) %dir %{_spath}/authlib
%attr(0700,qmaill,qmail) %dir %{_spath}/authlib/log
%attr(0700,qmaill,qmail) %dir %{_spath}/authlib/env
%attr(0700,qmaill,qmail) %dir %{_spath}/authlib/supervise
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{_sbindir}/*
%attr(0644,root,root) %{_includedir}/*
%attr(0755,root,root) %{_libdir}/*
%attr(0755,root,root) %{_libexecdir}/courier-authlib/*
%attr(0644,root,root) %{_sysconfdir}/courier/*
%attr(0751,qmaill,qmail) %{_spath}/authlib/run
%attr(0751,qmaill,qmail) %{_spath}/authlib/log/run
%attr(0644,root,root) %{_mandir}/man1/*
%attr(0644,root,root) %{_mandir}/man3/*
%attr(0644,root,root) %{_mandir}/man8/*


#------------------------------------------------------------------------------------
%changelog
#------------------------------------------------------------------------------------
* Tue Jun 16 2009 Jake Vickers <jake@qmailtoaster.com> 0.59.2-1.3.10
- Rolled the courier-authlib package back to 0.59.2 since the new version does not have the 
- required vpopmail patches to function with Qmail. Sorry!
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 0.62.2-1.3.9
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Wed Jun 10 2009 Jake Vickers <jake@qmailtoaster.com> 0.62.2-1.3.9
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 0.59.2-1.3.8
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 0.59.2-1.3.7
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 0.59.2-1.3.7
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch 0.59.2-1.3.6
- Upgraded to courier-authlib 0.59.2
- Added CentOS 5 i386 support
- Added CentOS 5 x86_64 support
* Thu Feb 01 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.59.1-1.3.5
- Upgraded to courier-authlib 0.59.1
* Tue Jan 02 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.59-1.3.4
- Upgraded to courier-authlib 0.59
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.58-1.3.3
- Added Fedora Core 6 support
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.58-1.3.2
- Fixed libtool-ltdl conflict on FC4
* Mon Jun 05 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.58-1.3.1
- Initial Package
- Add SuSE 10.1 support
