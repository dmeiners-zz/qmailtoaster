%define		name vpopmail
%define		pversion 5.4.17
%define 	bversion 1.3
%define		rpmrelease 7

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
%define 	build_fedora_1164  0

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
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
BuildPreReq:	perl
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
BuildPreReq:	perl
%define		ccflags %{optflags} -fPIC
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
BuildPreReq:	perl
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
BuildPreReq:	perl
%define		ccflags %{optflags} -fPIC
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
BuildRequires:  libmysqlclient-devel >= 5.0.49, mysql >= 5.0.49
Requires:       mysql >= 5.0.49
BuildPreReq:    perl
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib/mysql
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006 Linux
BuildRequires:	libmysql14-devel >= 4.1.11, libmysql14 >= 4.1.11, zlib1-devel >= 1.2.2.2, pam-devel >= 0.77
Requires:	libmysql14 >= 4.1.11, zlib1 >= 1.2.2.2, shadow-utils, vixie-cron
BuildPreReq:	perl, shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
BuildRequires:	lib64mysql14-devel >= 4.1.11, lib64mysql14 >= 4.1.11, zlib1-devel >= 1.2.2.2, pam-devel >= 0.77
Requires:	lib64mysql14 >= 4.1.11, zlib1 >= 1.2.2.2, shadow-utils, vixie-cron
BuildPreReq:	perl, shadow-utils
%define		ccflags %{optflags} -fPIC
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
BuildRequires:	libmysql14-devel >= 4.1.11, libmysql14 >= 4.1.11, zlib1-devel >= 1.2.2.2, pam-devel >= 0.77
Requires:	libmysql14 >= 4.1.11, zlib1 >= 1.2.2.2, shadow-utils, vixie-cron
BuildPreReq:	perl, shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
BuildRequires:	libmysql12-devel >= 4.0.20, libmysql12 >= 4.0.20, zlib1-devel >= 1.2.1.1, pam-devel >= 0.77
Requires:	libmysql12 >= 4.0.20, zlib1 >= 1.2.1.1, shadow-utils, vixie-cron
BuildPreReq:	perl, shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
BuildRequires:	libmysql12-devel >= 4.0.18, libmysql12 >= 4.0.18, zlib1-devel >= 1.2.1, pam-devel >= 0.77
Requires:	libmysql12 >= 4.0.18, zlib1 >= 1.2.1, shadow-utils, vixie-cron
BuildPreReq:	perl, shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
BuildRequires:  libmysql15-devel >= 5.0.0, libmysql15 >= 5.0.0, zlib1-devel >= 1.2.2.2, pam-devel >= 0.77
Requires:       libmysql15 >= 5.0.0, zlib1 >= 1.2.2.2, shadow-utils, vixie-cron
BuildPreReq:    perl, shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype RedHat 9 Linux
BuildRequires:	mysql-devel >= 3.23.54, mysql >= 3.23.54, pam-devel >= 0.75
Requires:	mysql >= 3.23.54, shadow-utils, vixie-cron
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 1 Linux
BuildRequires:	mysql-devel >= 3.23.58, mysql >= 3.23.58
Requires:	mysql >= 3.23.58
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 2 Linux
BuildRequires:	mysql-devel >= 3.23.58, mysql >= 3.23.58
Requires:	mysql >= 3.23.58
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 3 Linux
BuildRequires:	mysql-devel >= 3.23.58, mysql >= 3.23.58
Requires:	mysql >= 3.23.58
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 Linux
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
BuildPreReq:	shadow-utils
%define		ccflags %{optflags} -fPIC
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 Linux
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
BuildPreReq:	shadow-utils
%define		ccflags %{optflags} -fPIC
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 Linux
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
BuildPreReq:    shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib/mysql
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
BuildPreReq:    shadow-utils
%define         ccflags %{optflags} -fPIC
%define         ldflags %{optflags}
%define         mylibdir /usr/lib64/mysql
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
BuildPreReq:    shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib/mysql
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
BuildPreReq:    shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib64/mysql
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
BuildPreReq:    shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib/mysql
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
BuildPreReq:    shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib64/mysql
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
BuildRequires:  mysql-devel >= 5.1.0, mysql >= 5.1.0
Requires:       mysql >= 5.1.0
BuildPreReq:    shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib/mysql
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
BuildRequires:  mysql-devel >= 5.1.0, mysql >= 5.1.0
Requires:       mysql >= 5.1.0
BuildPreReq:    shadow-utils
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         mylibdir /usr/lib64/mysql
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux
BuildRequires:	mysql-devel >= 4.1.7, mysql >= 4.1.7
Requires:	mysql >= 4.1.7
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
BuildRequires:	mysql-devel >= 4.1.10, mysql >= 4.1.10
Requires:	mysql >= 4.1.10
BuildPreReq:	shadow-utils
%define		ccflags %{optflags} -fPIC
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux
BuildRequires:	mysql-devel >= 5.0.22, mysql >= 5.0.22
Requires:	mysql >= 5.0.22
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib/mysql
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
BuildRequires:	mysql-devel >= 5.0.22, mysql >= 5.0.22
Requires:	mysql >= 5.0.22
BuildPreReq:	shadow-utils
%define		ccflags %{optflags} -fPIC
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
BuildRequires:	mysql-devel >= 5.0.22, mysql >= 5.0.22
Requires:	mysql >= 5.0.22
BuildPreReq:	shadow-utils
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		mylibdir /usr/lib64/mysql
%define 	build_cnt_5064   1
%endif

############### RPM ################################

%define		debug_package %{nil}
%define         vtoaster %{pversion}
%define 	vdir /home/vpopmail
%define		builddate Fri Jun 12 2009

Name:		%{name}-toaster
Summary:	Vpopmail for qmail-toaster
Version:	%{vtoaster}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://www.inter7.com/vpopmail
Source0:	vpopmail-%{pversion}.tar.bz2
Patch0:		vpopmail-5.4.17.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{pversion}-root
Obsoletes:	vpopmail-toaster-doc
Conflicts:      set-toaster, checkpassword, vpopmail, postfix
Packager:       Jake Vickers <jake@qmailtoaster.com>

%define	name vpopmail
%define	vdir /home/vpopmail
%define	tempdir="0"


#------------------------------------------------------------------------------------
%description
#------------------------------------------------------------------------------------
vpopmail (vchkpw)  is a collection  of programs  and a library to automate
the creation and maintence of virtual domain email for qmail installations
using either a single UID/GID, or any valid  UID/GID in /etc/passwd with a
home directory. All the  features  are  provided  in the library for other
applications which need to maintain virtual domain email accounts.

It supports named or IP based domains.  It works with vqadmin, qmailadmin,
vqregister, sqwebmail, and courier-imap.

It supports MySQL,  Sybase,  Oracle,  LDAP,  and  file-based (DJB constant
database) authentication.

It handles 10 to 10 million users, and over 500K domains.

 
           vpopmail 5.4.17
            Current settings
---------------------------------------

vpopmail directory = /home/vpopmail
               uid = 89
               gid = 89
     roaming users = OFF --disable-roaming-users (default)
 password learning = OFF --disable-learn-passwords (default)
     md5 passwords = ON  --enable-md5-passwords (default)
      file locking = ON  --enable-file-locking (default)
vdelivermail fsync = OFF --disable-file-sync (default)
     make seekable = ON  --enable-make-seekable (default)
      clear passwd = ON  --enable-clear-passwd (default)
 user dir hashing  = OFF --disable-users-big-dir
address extensions = ON  --enable-qmail-ext
          ip alias = OFF --disable-ip-alias-domains (default)
       auth module = mysql --enable-auth-module=mysql
 mysql replication = OFF --disable-mysql-replication (default)
       sql logging = OFF --disable-sql-logging (default)
      mysql limits = OFF --disable-mysql-limits (default)
      MySQL valias = ON  --enable-valias
          auth inc = -I/usr/include/mysql
          auth lib = -L/usr/lib64/mysql  -lmysqlclient -lz -lm
  system passwords = OFF --disable-passwd (default)
        pop syslog = log success and errors including passwords
                     --enable-logging=v
      auth logging = ON  --enable-auth-logging (default)
one domain per SQL table     = --disable-many-domains



#------------------------------------------------------------------------------------
%prep
#------------------------------------------------------------------------------------
%setup -q -n %{name}-%{pversion}

%patch0 -p0

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
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}

# Trick vpopmail so we don't install qmail twice to have chkuser
#------------------------------------------------------------------------------------
if [ -f /var/qmail/bin/vpopfake ] ; then
	rm -fR /var/qmail ;
fi

if [ -f /var/qmail/bin/qmail-newu ] ; then
	tempdir="1" ;
else
	mkdir /var/qmail ;
	mkdir /var/qmail/bin ;
	touch /var/qmail/bin/qmail-newu ;
	touch /var/qmail/bin/qmail-inject ;
	touch /var/qmail/bin/qmail-newmrh ;
	touch /var/qmail/bin/vpopfake ;
fi


# Create group and user for build if they don't exist
#------------------------------------------------------------------------------------
if [ -z "`/usr/bin/id -g vchkpw 2>/dev/null`" ]; then
	/usr/sbin/groupadd -g 89 -r vchkpw 2>&1 || :
fi

if [ -z "`/usr/bin/id -u vpopmail 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 89 -r -M -d %{vdir}  -s /sbin/nologin -c "Vpopmail User" -g vchkpw vpopmail 2>&1 || :
fi


# Run configure to create makefile
#------------------------------------------------------------------------------------

./configure --prefix=%{vdir} \
	--enable-vpopuser=vpopmail \
	--enable-vpopgroup=vchkpw \
	--enable-libdir=%{mylibdir} \
	--disable-roaming-users \
	--enable-tcprules-prog=/usr/bin/tcprules \
	--enable-tcpserver-file=/etc/tcprules.d/tcp.smtp \
	--enable-make-seekable \
	--enable-clear-passwd \
	--disable-users-big-dir \
	--enable-qmail-ext \
	--disable-ip-alias-domains \
	--enable-auth-module=mysql \
	--disable-passwd \
	--enable-logging=v \
	--enable-log-name=vpopmail \
	--disable-mysql-limits \
	--enable-valias \
	--disable-many-domains
make

# Delete gcc temp file
#------------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc


#------------------------------------------------------------------------------------
%install
#------------------------------------------------------------------------------------
make DESTDIR=%{buildroot} install-strip


# Set defaults for vpopmail mysql
#------------------------------------------------------------------------------------
mv %{buildroot}%{vdir}/etc/vpopmail.mysql %{buildroot}%{vdir}/etc/vpopmail.mysql.dist
echo "localhost|0|vpopmail|SsEeCcRrEeTt|vpopmail" > %{buildroot}%{vdir}/etc/vpopmail.mysql


# Install domain quota messages
#------------------------------------------------------------------------------------
for i in overquota.msg quotawarn.msg; do
 install $i %{buildroot}%{vdir}/domains
done

mv %{buildroot}%{vdir}/domains/overquota.msg %{buildroot}%{vdir}/domains/.overquota.msg
mv %{buildroot}%{vdir}/domains/quotawarn.msg %{buildroot}%{vdir}/domains/.quotawarn.msg


#------------------------------------------------------------------------------------
%pre
#------------------------------------------------------------------------------------
# Create group and user if they don't exist
#------------------------------------------------------------------------------------
if [ -z "`/usr/bin/id -g vchkpw 2>/dev/null`" ]; then
	/usr/sbin/groupadd -g 89 -r vchkpw 2>&1 || :
fi

if [ -z "`/usr/bin/id -u vpopmail 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 89 -r -M -d %{vdir}  -s /sbin/nologin -c "Vpopmail User" -g vchkpw vpopmail 2>&1 || :
fi


#------------------------------------------------------------------------------------
%preun
#------------------------------------------------------------------------------------
if [ "$1" = 0 ]; then
	userdel vpopmail 2> /dev/null
	groupdel vchkpw 2> /dev/null
fi


#------------------------------------------------------------------------------------
%post
#------------------------------------------------------------------------------------
if [ -f /var/qmail/bin/vpopfake ]; then
	rm -Rf /var/qmail ;
fi


#------------------------------------------------------------------------------------
%clean
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{pversion}
if [ -f /var/qmail/bin/vpopfake ]; then
	rm -Rf /var/qmail ;
fi


#------------------------------------------------------------------------------------
%files
#------------------------------------------------------------------------------------
%defattr (-,vpopmail,vchkpw)
%attr(0700,vpopmail,vchkpw) %dir %{vdir}
%attr(0755,vpopmail,vchkpw) %dir %{vdir}/bin
%attr(0755,vpopmail,vchkpw) %dir %{vdir}/etc
%attr(0755,vpopmail,vchkpw) %dir %{vdir}/include
%attr(0755,vpopmail,vchkpw) %dir %{vdir}/lib
%attr(0700,vpopmail,vchkpw) %dir %{vdir}/domains

%attr(0751,vpopmail,vchkpw) %{vdir}/bin/*
%attr(0644,vpopmail,vchkpw) %{vdir}/domains/.quotawarn.msg
%attr(0644,vpopmail,vchkpw) %{vdir}/domains/.overquota.msg
%attr(0644,vpopmail,vchkpw) %{vdir}/etc/inc_deps
%attr(0644,vpopmail,vchkpw) %{vdir}/etc/lib_deps
%attr(0644,vpopmail,vchkpw) %config(noreplace) %{vdir}/etc/vlimits.default
%attr(0644,vpopmail,vchkpw) %config(noreplace) %{vdir}/etc/vpopmail.mysql
%attr(0644,vpopmail,vchkpw) %{vdir}/etc/vpopmail.mysql.dist
%attr(0444,vpopmail,vchkpw) %{vdir}/include/*
%attr(0600,vpopmail,vchkpw) %{vdir}/lib/*

%attr(0755,vpopmail,vchkpw) %dir %{vdir}/doc
%attr(0755,vpopmail,vchkpw) %dir %{vdir}/doc/doc_html
%attr(0755,vpopmail,vchkpw) %dir %{vdir}/doc/man_html
%attr(0444,vpopmail,vchkpw) %{vdir}/doc/doc_html/*
%attr(0444,vpopmail,vchkpw) %{vdir}/doc/man_html/*


#------------------------------------------------------------------------------------
%changelog
#------------------------------------------------------------------------------------
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 5.4.17-1.3.7
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Tue Jun 02 2009 Jake Vickers <jake@qmailtoaster.com> 5.4.17-1.3.7
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 5.4.17-1.3.6
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 5.4.17-1.3.5
- Added Suse 11.1 support
* Sun Feb 08 2009 Jake Vickers <jake@qmailtoaster.com> 5.4.17-1.3.5
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@qmailtoaster.com> 5.4.17-1.3.4
- Update to vpopmail-5.4.17
- Added CentOS 5 i386 support
- Added CentOS 5 x86_64 support
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 5.4.13-1.3.3
- Added Fedora Core 6 support
* Fri Jul 14 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 5.4.13-1.3.2
- Added vpopmail-5.4.13-mysql patch, fixes mysql's gone away error
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 5.4.13-1.3.1
- Add SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 5.4.13-1.2.12
- Add Fedora Core 5 support
* Fri Apr 28 2006 Nick Hemmesch <nick@ndhsoft.com> 5.4.13-1.2.11
- Update to vpopmail-5.4.13
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 5.4.10-1.2.10
- Add SuSE 10.0 and Mandriva 2006.0 support
* Fri Oct 14 2005 Nick Hemmesch <nick@ndhsoft.com> 5.4.10-1.2.9
- Add Fedora Core 4 x86_64 support
- Make vlimits.default and vpopmail.mysql no replace config files
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 5.4.10-1.2.8
- Add CentOS 4 x86_64 support
* Wed Jun 29 2005 Nick Hemmesch <nick@ndhsoft.com> 5.4.10-1.2.7
- Add Fedora Core 4 support
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 5.4.10-1.2.6
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Fri May 20 2005 Nick Hemmesch <nick@ndhsoft.com> 5.4.10-1.2.5
- Update to vpopmail-5.4.10
- Create group and user
* Tue Mar 15 2005 Nick Hemmesch <nick@ndhsoft.com> 5.4.4-1.2.4
- Add patch to build vpopmail before qmail
- Fix domainquotas
* Sun Feb 27 2005 Nick Hemmesch <nick@ndhsoft.com> 5.4.4-1.2.3
- Add Fedora Core 3 support
- Add CentOS suport
* Wed Jun 02 2004 Nick Hemmesch <nick@ndhsoft.com> 5.4.4-1.2.2
- Update to vpopmail-5.4.4
- Add Fedora Core 2 support
* Tue May 04 2004 Nick Hemmesch <nick@ndhsoft.com> 5.4.3-1.2.1
- Major rebuild of spec file
- Update to vpopmail-5.4.3
- Make rpm patch and config patch
* Sun Feb 22 2004 Nick Hemmesch <nick@ndhsoft.com> 5.3.8-1.0.12
- By popular demand, make no roaming users the default install
- Allow roaming users with "roaming" switch
* Sun Feb 15 2004 Nick Hemmesch <nick@ndhsoft.com> 5.3.8-1.0.11
- Set roaming user clear time to 15 minutes
* Mon Jan 12 2004 Nick Hemmesch <nick@ndhsoft.com> 5.3.8-1.0.10
- Fix for Trustix 2.0 by Christian Dietrich
* Sat Jan 10 2004 Nick Hemmesch <nick@ndhsoft.com> 5.3.8-1.0.9
- Add Fedora Core 1 support
- Fix Trustix 2.0 - change dependency
- Add no roaming-users as an option
- Add 15 minute expiration for roaming users
* Sun Nov 23 2003 Nick Hemmesch <nick@ndhsoft.com> 5.3.8-1.0.8
- Add Trustix 2.0
- Fix cdb function
- New patch to fix vmysql.h configure and to allow rpm build
* Sat Apr 26 2003 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-1.0.7
- Clean-ups on SPEC file: compilation banner, better gcc detects
- Detect gcc-3.2.3
- Red Hat Linux 9.0 support (nick@ndhsoft.com)
- Gnu/Linux Mandrake 9.2 support
* Wed Apr 02 2003 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-1.0.6
- Clean-ups
* Mon Mar 31 2003 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-1.0.5
- Conectiva Linux 7.0 support
* Sun Feb 15 2003 Nick Hemmesch <nick@ndhsoft.com> 5.3.8-1.0.4
- Support for Red Hat 8.0
* Wed Feb 05 2003 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-1.0.3
- Support for Red Hat 8.0 thanks to Andrew.J.Kay
* Sat Feb 01 2003 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-1.0.2
- Redo Macros to prepare supporting larger RPM OS.
  We could be able to compile (and use) packages under every RPM based
  distribution: we just need to write right requirements.
* Sat Jan 25 2003 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-1.0.1
- Added MDK 9.1 support
- Try to use gcc-3.2.1
- Added very little patch to compile with newest GLIBC
- Support dor new RPM-4.0.4
* Sat Oct 05 2002 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-0.9.2
- Soft clean-ups
* Sun Sep 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 5.3.8-0.9.1
- RPM macros to detect Mandrake, RedHat, Trustix are OK again. They are
  very basic but they should work.
- Packages are named with their proper releases and bversion is from now
  part of the rpm release: we will continue upgrading safely.
* Mon Sep 23 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.8.5.3.8-1
- Rebuilded under 0.8 tree.
- Important comments translated from Italian to English.
- Written rpm rebuilds instruction at the top of the file (in english).
- Clean-ups
* Sun Sep 22 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.5.3.8-3
- Now cron-job works 100%!!!
* Thu Aug 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.5.3.8-2
- Deleted Mandrake Release Autodetection (creates problems)
* Fri Aug 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.5.3.8-1
- New version: 0.7 toaster.
- Better macros to detect Mandrake Release
- Minor clean-ups.
* Thu Aug 13 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.6.5.3.8-1
- New version: 0.6 toaster.
* Mon Aug 12 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.5.5.3.8-1
- Doc package is standalone (someone does not ask for man pages)
- Checks for gcc-3.2 (default compiler from now)
- New version: 0.5 toaster.
* Tue Aug 08 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.4.5.3.8-1
* Rebuild agains 0.4 toaster
- new version 5.3.8
* Thu Aug 06 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.5.3.5-4
- Deleted userdel and groupdel in uninstallation (safe): if the user
  wants to delete he has to do it manually (more safe)
* Wed Jul 31 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.5.3.5-3
- Written a patch that makes vpopmail constantly reading from sql:
  in this way tou can change on the fly sql values and we could build
  binaries version of packages (because passwords are out of the code)
* Tue Jul 30 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.5.3.5-2
- Now packages have got 'no sex': you can rebuild them with command line
  flags for specifics targets that are: RedHat, Trustix, and of course
  Mandrake (that is default)
* Sun Jul 28 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.2.5.3.5.1mdk
- toaster v. 0.3: now it is possible upgrading safely because of 'pversion'
  that is package version and 'version' that is toaster version
* Thu Jul 25 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.2-5.3.5.1mdk
- toaster v. 0.2: Very soft clean-ups.
* Mon Jul 22 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.1-5.3.5.4mdk
- Added useradd -r flag to create systems account. That is, an user with an
  UID  lower  than  value  of UID_MIN defined in /etc/login.defs
* Thu Jul 18 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.1-5.3.5.3mdk
- Added toaster version (we will need to mantain it too): is vtoaster 0.1
- Added cron.d files
- Added tests to make gcc to be 3.1.1
- Very soft clean-ups.
* Wed Jul 10 2002 Miguel Beccari <mighi@clikka.com> 5.3.5 2mdk
- Better dependecings (with ucspi-tcp)
- Changed the name in vpopmail-toaster beacuse we are going
  building *-toaster packages.
* Mon Jul 08 2002 Miguel Beccari <mighi@clikka.com> 5.3.5 1mdk
- First package (needs a lot of work).
- However the package is able to:
  * detect if user vpopmail exists (if not it creates)
  * detect if group exists (if not it creates)
  * apply a light patch stuff for 'make install' operations
  * read /var/qmail/control/sql and patch vmysql.h
