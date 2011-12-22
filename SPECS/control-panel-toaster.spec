%define		name control-panel
%define		pversion 0.5
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
%{?_with_fedora_10:	%{expand: %%define build_fedora_10   1}}
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
%define		phppaths /usr/share/php:/usr/share/php/pear:.
%define		apachedir /etc/apache2/
%define		httpdconf httpd.conf
%define		apacheuser wwwrun
%define		apachegroup www
%define		_dopasswd htpasswd2
Prereq: 	/usr/bin/perl
Requires:	apache2 >= 2.0.52, php4 >= 4.4.0
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
%define		phppaths /usr/share/php:/usr/share/php/pear:.
%define		apachedir /etc/apache2/
%define		httpdconf httpd.conf
%define		apacheuser wwwrun
%define		apachegroup www
%define		_dopasswd htpasswd2
Prereq: 	/usr/bin/perl
Requires:	apache2 >= 2.0.52, php4 >= 4.4.0
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux
%define		phppaths /usr/share/php:/usr/share/php/pear:.
%define		apachedir /etc/apache2/
%define		httpdconf httpd.conf
%define		apacheuser wwwrun
%define		apachegroup www
%define		_dopasswd htpasswd2
Prereq: 	/usr/bin/perl
Requires:	apache2 >= 2.0.52, php5 >= 5.1.2
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
%define		phppaths /usr/share/php:/usr/share/php/pear:.
%define		apachedir /etc/apache2/
%define		httpdconf httpd.conf
%define		apacheuser wwwrun
%define		apachegroup www
%define		_dopasswd htpasswd2
Prereq: 	/usr/bin/perl
Requires:	apache2 >= 2.0.52, php5 >= 5.1.2
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
%define         phppaths /usr/share/php:/usr/share/php/pear:.
%define         apachedir /etc/apache2/
%define         httpdconf httpd.conf
%define         apacheuser wwwrun
%define         apachegroup www
%define         _dopasswd htpasswd2
Prereq:         /usr/bin/perl
Requires:       apache2 >= 2.1.0, php5 >= 5.1.2
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
%define		phppaths /usr/lib/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		apacheuser apache
%define		apachegroup apache
%define		_dopasswd htpasswd
Prereq: 	/usr/bin/perl
BuildRequires:	apache-devel >= 2.0.54
Requires:	apache >= 2.0.54, libphp_common432 >= 4.3.8, apache2-mod_php, php-pear >= 4.3.8, php-mysql >= 4.3.8
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
%define		phppaths /usr/lib64/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		apacheuser apache
%define		apachegroup apache
%define		_dopasswd htpasswd
Prereq: 	/usr/bin/perl
BuildRequires:	apache-devel >= 2.0.54
Requires:	apache >= 2.0.54, lib64php_common432 >= 4.3.8, apache2-mod_php, php-pear >= 4.3.8, php-mysql >= 4.3.8
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
%define		phppaths /usr/lib/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd2.conf
%define		apacheuser apache
%define		apachegroup apache
%define		_dopasswd htpasswd2
Prereq: 	/usr/bin/perl
BuildRequires:	apache2-common >= 2.0.53
Requires:	apache2 >= 2.0.53, libphp_common432 >= 4.3.8, apache2-mod_php, php-pear >= 4.3.8, php-mysql >= 4.3.8
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
%define		phppaths /usr/lib/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd2.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
BuildRequires:	apache2-common >= 2.0.50
Requires:	apache2 >= 2.0.50, libphp_common432 >= 4.3.8, apache2-mod_php, php-pear >= 4.3.8, php-mysql >= 4.3.8
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
%define		phppaths /usr/lib/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd2.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
BuildRequires:	apache2-common >= 2.0.48
Requires:	apache2 >= 2.0.48, libphp_common432 >= 4.3.4, apache2-mod_php, php-pear >= 4.3.4, php-mysql
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
%define         phppaths /usr/lib/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         apacheuser apache
%define         apachegroup apache
%define         _dopasswd htpasswd
Prereq:         /usr/bin/perl
BuildRequires:  apache-devel >= 2.2.5
Requires:       apache >= 2.2.5, libphp5_common5 >= 4.3.8, apache-mod_php, php-pear >= 4.3.8, php-mysql >= 4.3.8
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux RedHat 9
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.40, php >= 4.2.2
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 1
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.47, php >= 4.3.3
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 2
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.49, php >= 4.3.4
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 3
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.52, php >= 4.3.10
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 4
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.54, php >= 5.0.4
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 4 x86_64
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.54, php >= 5.0.4
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 5
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.54, php >= 5.0.4
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 5 x86_64
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.54, php >= 5.0.4
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Linux Fedora Core 6
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Linux Fedora Core 6 x86_64
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
%define         phppaths /usr/share/php:/usr/share/pear:.
%define         apachedir /etc/httpd/conf/
%define         httpdconf httpd.conf
%define         _dopasswd htpasswd
%define         apacheuser apache
%define         apachegroup apache
Prereq:         /usr/bin/perl
Requires:       httpd >= 2.0.54, php >= 5.0.4
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.52, php >= 4.3.9
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
%define		phppaths /usr/lib64/php4:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.0.52, php >= 4.3.9
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.2.3, php >= 5.1.6
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
%define		phppaths /usr/lib64/php4:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.2.3, php >= 5.1.6
%define 	build_cnt_5064   1
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
%define		phppaths /usr/share/php:/usr/share/pear:.
%define		apachedir /etc/httpd/conf/
%define		httpdconf httpd.conf
%define		_dopasswd htpasswd
%define		apacheuser apache
%define		apachegroup apache
Prereq: 	/usr/bin/perl
Requires:	httpd >= 2.2.3, php >= 5.1.6
%define 	build_cnt_5064   1
%endif


############### RPM ################################

%define		debug_package %{nil}
%define         vtoaster %{pversion}
%define 	basedir %{_datadir}/toaster
%define 	htdocs %{basedir}/htdocs
%define		cgibin %{basedir}/cgi-bin
%define		hcpath %{apachedir}%{httpdconf}
%define		builddate Fri Jun 12 2009

Name: 		%{name}-toaster
Summary: 	Toaster Control Panel.
Version:	%{vtoaster}
Release:	%{release}
License: 	GNU
Group:		System/Configuration
Vendor:		Clikka!Com
URL:		http://qmailtoaster.clikka.com/
Source0:	apache-toaster-conf-%{pversion}.tar.bz2
Patch0:		apache-toaster-conf.patch.bz2
Packager:	Jake Vickers <jake@qmailtoaster.com>
BuildArchitectures: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}buildroot
Prereq: 	/usr/bin/perl
Requires:	courier-imap-toaster >= 4.1.2

#----------------------------------------------------------------------
%description
#----------------------------------------------------------------------
This package write apache directives to tune properly toaster cgi such
as qmailadmin, horde, mrtg, ezmlm.

It is written in a modular way so we can add - in the future - modules
such as isoqlog, antivirus interfaces, statistics, etc etc...


%package -n send-emails-toaster
#----------------------------------------------------------------------
Summary:	control-panel-toaster module
Group:		System/Servers
Requires:	control-panel-toaster >= %{pversion}-%{release}
Requires:	qmail-toaster >= 1.03
Requires:	vpopmail-toaster >= 5.4.17

%description -n send-emails-toaster
#----------------------------------------------------------------------
Provides a module for control-panel-toaster for sending email to all
system users.

#----------------------------------------------------------------------
%prep
#----------------------------------------------------------------------

%setup -q -n apache-toaster-conf-%{pversion}
%patch0 -p0
#----------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags
cat <<EOF >>%{_tmppath}/%{name}-%{pversion}-show_flags
#!/bin/sh

RPM=" RPM RELEASE : \033[40m\033[001;033m%{name}-toaster-%{pversion}-%{release} "
OS=" OS TYPE IS  : \033[40m\033[001;033m%{ostype} "
BLD=" BUILD DATE  : \033[40m\033[001;033m%{builddate} "
APACHEUSER=" Apache User : \033[40m\033[001;033m%{apacheuser} "
APACHEGROUP=" Apache Group: \033[40m\033[001;033m%{apachegroup} "
PHPDIRS=" PHP Dirs    : \033[40m\033[001;033m%{phppaths} "
DIR=" Apache Root : \033[40m\033[001;033m%{apachedir}%{httpdconf} "

echo
echo
echo -e "\033[40m\033[001;031m\$RPM\033[0m"
echo -e "\033[40m\033[001;031m\$OS\033[0m"
echo -e "\033[40m\033[001;031m\$BLD\033[0m"
echo -e "\033[40m\033[001;031m\$APACHEUSER\033[0m"
echo -e "\033[40m\033[001;031m\$APACHEGROUP\033[0m"
echo -e "\033[40m\033[001;031m\$PHPDIRS\033[0m"
echo -e "\033[40m\033[001;031m\$DIR\033[0m"
echo
echo

sleep 5

EOF

# Take care to execute and then to delete
#----------------------------------------------------------------------
chmod u+x %{_tmppath}/%{name}-%{pversion}-show_flags
%{_tmppath}/%{name}-%{pversion}-show_flags
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags

#----------------------------------------------------------------------
%build
#----------------------------------------------------------------------

#----------------------------------------------------------------------
%install
#----------------------------------------------------------------------
[ -n %{buildroot} ] && rm -rf %{buildroot}

[ -f %{_tmppath}/setup.sh ] && rm -f %{_tmppath}/setup.sh

cat <<EOF >>%{_tmppath}/setup.sh
#!/bin/sh

[ -d %{buildroot}%{apachedir} ] 	|| mkdir -p %{buildroot}%{apachedir}
[ -d %{buildroot}%{htdocs}/images ]	|| mkdir -p %{buildroot}%{htdocs}/images
[ -d %{buildroot}%{htdocs}/scripts ]	|| mkdir -p %{buildroot}%{htdocs}/scripts
[ -d %{buildroot}%{htdocs}/admin ]	|| mkdir -p %{buildroot}%{htdocs}/admin
[ -d %{buildroot}%{htdocs}/admin/email ]|| mkdir -p %{buildroot}%{htdocs}/admin/email
[ -d %{buildroot}%{htdocs}/mrtg ]	|| mkdir -p %{buildroot}%{htdocs}/mrtg
[ -d %{buildroot}%{cgibin} ]		|| mkdir -p %{buildroot}%{cgibin}
[ -d %{buildroot}%{cgibin}/vqadmin ]	|| mkdir -p %{buildroot}%{cgibin}/vqadmin
[ -d %{buildroot}%{basedir}/include ]	|| mkdir -p %{buildroot}%{basedir}/include

EOF

chmod u+x %{_tmppath}/setup.sh
%{_tmppath}/setup.sh
[ -f %{_tmppath}/setup.sh ] && rm -f %{_tmppath}/setup.sh


# Add Send Mail module to the Control Panel
#----------------------------------------------------------------------
cat <<EOF>%{buildroot}%{basedir}/include/email.module
<!-- horde.module -->
<tr>
	<td align="right" width="47%">Send Emails to Users</td>
	<td width="6%">&nbsp;</td>
	<td align="left" width=47%"><input type="button" value="Email Users-%{pversion}" class="inputs" onClick="location.href='/admin-toaster/email/';"></td>
</tr>
<!-- horde.module -->
EOF

# Create a configuration file for httpd.conf
#----------------------------------------------------------------------
cat <<EOF >>%{buildroot}%{apachedir}toaster.conf
<IfModule mod_alias.c>
    ScriptAlias /mail/ /usr/share/toaster/cgi-bin/
    Alias /admin-toaster /usr/share/toaster/htdocs/admin/
    Alias /stats-toaster/ /usr/share/toaster/htdocs/mrtg/
    Alias /qlogs-toaster/ /usr/share/toaster/htdocs/isoqlog/
    Alias /images-toaster/ /usr/share/toaster/htdocs/images/
    Alias /scripts/ /usr/share/toaster/htdocs/scripts/
    Alias /qmailadmin /usr/share/qmailadmin/
</IfModule>
<Directory /usr/share/qmailadmin>
    AddHandler cgi-script .cgi
    AddHandler cgi-script qmailadmin
    DirectoryIndex index.cgi qmailadmin index.html
    Options +Indexes FollowSymLinks +ExecCGI
    Order allow,deny
    Allow from all
</Directory>
<Directory /usr/share/toaster/htdocs>
    Options -Indexes FollowSymLinks MultiViews
    AllowOverride All
    Order allow,deny
    Allow from all
</Directory>
<Directory /usr/share/toaster/htdocs/admin>
    AuthType Basic
    AuthName "Qmail Toaster v. 1.3 Admin"
    AuthUserFile /usr/share/toaster/include/admin.htpasswd
    require valid-user
</Directory>
<Directory /usr/share/toaster/htdocs/mrtg>
    AllowOverride All
    Order allow,deny
    Allow from all
    AuthType Basic
    AuthName "Qmail Toaster v. 1.3 Admin"
    AuthUserFile /usr/share/toaster/include/admin.htpasswd
    require valid-user
</Directory>
<Directory /usr/share/toaster/htdocs/isoqlog>
    AllowOverride All
    Order allow,deny
    Allow from all
    AuthType Basic
    AuthName "Qmail Toaster v. 1.3 Admin"
    AuthUserFile /usr/share/toaster/include/admin.htpasswd
    require valid-user
</Directory>
<Directory /usr/share/toaster/cgi-bin/vqadmin>
    AllowOverride All
    Options ExecCGI
    Order allow,deny
    Allow from all
    AuthType Basic
    AuthName "Qmail Toaster v. 1.3 Admin"
    AuthUserFile /usr/share/toaster/include/admin.htpasswd
    require valid-user
</Directory>
<Directory /usr/share/toaster/cgi-bin>
    AllowOverride All
    Options ExecCGI
    Order allow,deny
    Allow from all
</Directory>

EOF
#"

install -m644 index.php %{buildroot}%{htdocs}/admin/index.php
install -m644 admin.inc.php %{buildroot}%{basedir}/include/admin.inc.php
install -m644 ./*.gif %{buildroot}%{htdocs}/images/
install -m644 ./javascripts.js %{buildroot}%{htdocs}/scripts/
install -m644 ./styles.css %{buildroot}%{htdocs}/scripts/
install -m644 ./email.php %{buildroot}%{htdocs}/admin/email/index.php

%{_dopasswd} -bc %{buildroot}%{basedir}/include/admin.htpasswd admin toaster >/dev/null 2>&1

[ -f %{buildroot}%{basedir}/include/admin.pass ] || echo "toaster" > %{buildroot}%{basedir}/include/admin.pass

chown %{apacheuser}:%{apachegroup} %{buildroot}%{basedir}/include/*

#----------------------------------------------------------------------
%clean
#----------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/apache-toaster-conf-%{pversion} ] && rm -rf $RPM_BUILD_DIR/apache-toaster-conf-%{pversion}


#----------------------------------------------------------------------
%preun
#----------------------------------------------------------------------
if [ "$1" = 0 ]; then
   # Remove toaster.conf
   grep -v 'Include %{apachedir}toaster.conf' %{hcpath} > %{hcpath}.new
   mv -f %{hcpath}.new %{hcpath}
fi


#----------------------------------------------------------------------
%post
#----------------------------------------------------------------------
if [ $1 = "1" ]; then

[ -f %{basedir}/include/htpasswd ] 	|| ln -s `which %{_dopasswd}` %{basedir}/include/htpasswd


grep -i 'Include.*toaster.conf$' %{apachedir}%{httpdconf} >/dev/null 2>&1

if [ $? -eq 0 ]; then
	perl -pi -e 's/^#+// if (/Include.*toaster.conf$/i);' %{apachedir}%{httpdconf}
else
	echo "Include %{apachedir}toaster.conf" >>%{apachedir}%{httpdconf}
fi

echo ""
echo "Take a look at your %{httpdconf}"
echo ""
echo "A new include directive was added:"
echo "%{apachedir}toaster.conf"
echo ""
echo " Configuration,"
echo " If you plan to use it in a VirtualDomain please delete"
echo " the include directive from %{httpdconf} and  add it  in"
echo " your VirtualDomain"
echo ""
echo " If you plan to use it without VirtualDomain just leave"
echo " it as is (but be sure about cgi and alias)"
echo ""
echo " To make changes taking effect you need to reload httpd"
echo ""

fi

#----------------------------------------------------------------------
%files
#----------------------------------------------------------------------
%defattr(-,root,root)
%config %{apachedir}/toaster.conf
%attr(755,%{apacheuser},%{apachegroup}) %dir %{htdocs}/admin
%attr(755,%{apacheuser},%{apachegroup}) %dir %{htdocs}/images
%attr(755,%{apacheuser},%{apachegroup}) %dir %{basedir}/include
%attr(644,root,%{apachegroup}) %{htdocs}/admin/*.php
%attr(644,root,%{apachegroup}) %{htdocs}/admin/*.php
%attr(644,%{apacheuser},%{apachegroup}) %{htdocs}/images/*.gif
%attr(644,%{apacheuser},%{apachegroup}) %{htdocs}/scripts/*
%attr(644,root,%{apachegroup}) %{basedir}/include/*.php
%attr(644,%{apacheuser},%{apachegroup}) %config(noreplace) %{basedir}/include/admin.htpasswd
%attr(644,%{apacheuser},%{apachegroup}) %config(noreplace) %{basedir}/include/admin.pass

%files -n send-emails-toaster
%attr(750,%{apacheuser},%{apachegroup}) %dir %{htdocs}/admin/email
%attr(750,%{apacheuser},%{apachegroup}) %dir %{basedir}/include
%attr(644,root,%{apachegroup}) %{htdocs}/admin/email/*.php
%attr(644,%{apacheuser},%{apachegroup}) %{basedir}/include/email.module

#----------------------------------------------------------------------
%changelog
#----------------------------------------------------------------------
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 0.5-1.3.7
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Wed Jun 10 2009 Jake Vickers <jake@qmailtoaster.com> 0.5-1.3.7
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 0.5-1.3.6
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 0.5-1.3.5
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 0.5-1.3.5
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.3.4
- Add CentOS 5 i386 support
- Add CentOS 5 x86_64 support
* Sat Jan 13 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.5-1.3.3
- Included xspace patch for proper password changing
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.5-1.3.2
- Added Fedora Core 6 support
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.3.1
- Add SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.9
- Add Fedora Core 5 support
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.8
- Add SuSE 10.0 and Mandriva 2006.0 support
* Sat Oct 15 2005 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.7
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.6
- Add CentOS 4 x86_64 support
* Wed Jun 29 2005 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.5
- Add Fedora Core 4 support
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.5-1.2.4
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
- Change owner on .php scrips to fix php safe mode rights for le2005
* Mon Mar 21 2005 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.3
- Remove Horde includes
- Add password protection to qlogs-toaster
* Sun Feb 27 2005 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.3
- Add Fedora Core 3 support
- Add CentOS 4 support
* Thu Jun 03 2004 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.2
- Add Fedora Core 2 support
* Thu May 13 2004 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.2.1
- Make changes for Control Panel to work with 1.2.1 packages
- The toaster.conf is a mess and send emails doesn't work if
- the domain name has a dash.  I will fix them at a later date
* Mon Dec 29 2003 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.0.5
- Add Fedora Core 1 support
* Tue Nov 25 2003 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.0.4
- Add new toaster.conf for Horde with many apps
* Sun Nov 23 2003 Nick Hemmesch <nick@ndhsoft.com> 0.5-1.0.3
- Add Trustix 2.0 support
- Change images to images-toaster
* Thu May 15 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.5-1.0.2
- Red Hat Linux 9.0 support (nick@ndhsoft.com)
- Gnu/Linux Mandrake 9.2 support
* Sun Mar 30 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.5-1.0.1
- Support for Conectiva Linux 7.0
- Better managing of apache user (related to distro)
- Added Alias for isoqlog
* Sun Feb 18 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.4-1.0.1
- Antivirus, httpd2.conf for Mandrake
* Sun Feb 16 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.3-1.0.4
- Support for apache2 in Mandrake 9.1
* Sat Feb 15 2003 Nick Hemmesch <nick@ndhsoft.com> 0.3-1.0.3
- Support for Red Hat 8.0
* Sat Feb 01 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.3-1.0.2
- Redo Macros to prepare supporting larger RPM OS.
  We could be able to compile (and use) packages under every RPM based
  distribution: we just need to write right requirements.
* Sat Jan 25 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.3-1.0.1
- Added MDK 9.1 support
- Added very little patch to compile with newest GLIBC
- Support dor new RPM-4.0.4
* Thu Oct 10 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3-0.9.2
- Fixed little macro problem in rebuilding under RedHat
* Sun Oct 06 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3-0.9.1
- New Module: send-emails-toaster for sending administrative emails to
  all systen users
* Sun Sep 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.2-0.9.1
- RPM macros to detect Mandrake, RedHat, Trustix are OK again. They are
  very basic but they should work.
* Fri Sep 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.8.0.2-1
- Rebuilded under 0.8 tree.
- Important comments translated from Italian to English.
- Written rpm rebuilds instruction at the top of the file (in english).
- Added noreplace on htpasswd (for upgrades)
* Fri Sep 06 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.2-1
- Renamed the package in control-panel-toaster (now version 0.2)
- Css are external
- Blocks (vqadmin, qmailadmin, horde, mrtg) are modularized
* Thu Aug 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.1-3
- Deleted Mandrake Release Autodetection (creates problems)
- Fixed RedHat compatibility
* Wed Aug 28 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.1-2
- Added mrtg toaster support
* Fri Aug 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.1-1
- First release
- Apache directives make vqadmin working correctly (need htaccess)
- Toaster Control Panel (Release 0.1)
