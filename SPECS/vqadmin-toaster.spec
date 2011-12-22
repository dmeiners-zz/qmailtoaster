%define		name vqadmin
%define		pversion 2.3.4
%define 	bversion 1.3
%define		rpmrelease 6 

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
%define         build_fdr_60   0
%define         build_fdr_6064   0
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
%{?_with_fdr60:         %{expand: %%define build_fdr_60   1}}
%{?_with_fdr6064:       %{expand: %%define build_fdr_6064   1}}
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
%define		apacheuser wwwrun
%define		apachegroup www
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux
%define		apacheuser wwwrun
%define		apachegroup www
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux
%define		apacheuser wwwrun
%define		apachegroup www
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux
%define		apacheuser wwwrun
%define		apachegroup www
BuildRequires:	mysql-devel >= 4.1.13, mysql >= 4.1.13
Requires:	mysql >= 4.1.13
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
%define         apacheuser wwwrun
%define         apachegroup www
BuildRequires:  libmysqlclient-devel >= 5.0.49, mysql >= 5.0.49
Requires:       mysql >= 5.0.49
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	libmysql14-devel >= 4.1.12, libmysql14 >= 4.1.12, zlib1-devel >= 1.2.3
Requires:	libmysql14 >= 4.1.12, zlib1 >= 1.2.3
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	lib64mysql14-devel >= 4.1.12, lib64mysql14 >= 4.1.12, zlib1-devel >= 1.2.3
Requires:	lib64mysql14 >= 4.1.12, zlib1 >= 1.2.3
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
%define		apacheuser apache
%define		apachegroup apache
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
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	lib64mysql12-devel >= 4.0.20, lib64mysql12 >= 4.0.20, zlib1-devel >= 1.2.1.1
Requires:	lib64mysql12 >= 4.0.20, zlib1 >= 1.2.1.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	libmysql12-devel >= 4.0.18, libmysql12 >= 4.0.18, zlib1-devel >= 1.2.1
Requires:	libmysql12 >= 4.0.18, zlib1 >= 1.2.1
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  libmysql-devel >= 5.0.0, libmysql15 >= 5.0.0, zlib1-devel >= 1.2.3
Requires:       libmysql15 >= 5.0.0, zlib1 >= 1.2.3
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux RedHat 9
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 3.23.54, mysql >= 3.23.54
Requires:	mysql >= 3.23.54
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 1
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 3.23.58, mysql >= 3.23.58
Requires:	mysql >= 3.23.58
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 2
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 3.23.58, mysql >= 3.23.58
Requires:	mysql >= 3.23.58
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 3
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 3.23.58, mysql >= 3.23.58
Requires:	mysql >= 3.23.58
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 4
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Linux Fedora Core 5
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:	mysql >= 4.1.11
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Linux Fedora Core 6
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 4.1.11, mysql >= 4.1.11
Requires:       mysql >= 4.1.11
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 5.1.0, mysql >= 5.1.0
Requires:       mysql >= 5.1.0
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
%define         apacheuser apache
%define         apachegroup apache
BuildRequires:  mysql-devel >= 5.1.0, mysql >= 5.1.0
Requires:       mysql >= 5.1.0
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 4.1.7, mysql >= 4.1.7
Requires:	mysql >= 4.1.7
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 4.1.10, mysql >= 4.1.10
Requires:	mysql >= 4.1.10
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 5.0.22, mysql >= 5.0.22
Requires:	mysql >= 5.0.22
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 5.0.22, mysql >= 5.0.22
Requires:	mysql >= 5.0.22
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux
%define		apacheuser apache
%define		apachegroup apache
BuildRequires:	mysql-devel >= 5.0.22, mysql >= 5.0.22
Requires:	mysql >= 5.0.22
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%endif

############### RPM ################################

%define		debug_package %{nil}
%define         vtoaster %{pversion}
%define 	basedir %{_datadir}/toaster
%define 	vqadmdir %{basedir}/vqadmin
%define		builddate Fri Jun 12 2009

Name:           %{name}-toaster
Summary:	Web Administration for qmail-toaster
Version:	%{vtoaster}
Release:	%{release}
License:	GPL
Group:		Networking/Other
URL:		http://www.inter7.com/qmailadmin
Source:		vqadmin-%{pversion}.tar.bz2
Source1:	html.tar.bz2
Patch0:		vqadmin.template.patch.bz2
Patch1:		vqadmin.valias.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}buildroot
BuildRequires:	vpopmail-toaster >= 5.4.17
Requires:	vpopmail-toaster >= 5.4.17
Requires:	control-panel-toaster >= 0.2
Packager:       Jake Vickers <jake@qmailtoaster.com>

#------------------------------------------------------------------------------------
%description
#------------------------------------------------------------------------------------
Vqadmin description

#------------------------------------------------------------------------------------
%prep
#------------------------------------------------------------------------------------

%define name vqadmin
%setup -q -n %{name}-%{pversion}
%patch0 -p0
%patch1 -p0
tar fvxj %{SOURCE1}

# Cleanup fpr gcc
#------------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc

echo "gcc" > %{_tmppath}/%{name}-%{pversion}-gcc


# Display compilation flags and OS with colors ;)
#------------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags
cat <<EOF >>%{_tmppath}/%{name}-%{pversion}-show_flags
#!/bin/sh

RPM=" RPM RELEASE : \033[40m\033[001;033m%{name}-toaster-%{pversion}-%{release} "
OS=" OS TYPE IS  : \033[40m\033[001;033m%{ostype} "
BLD=" BUILD DATE  : \033[40m\033[001;033m%{builddate} "
CCF=" CCFLAGS     : \033[40m\033[001;033m%{ccflags} "
LDF=" LDFLAGS     : \033[40m\033[001;033m%{ldflags} "
APACHEUSER=" Apache User : \033[40m\033[001;033m%{apacheuser} "
APACHEGROUP=" Apache Group: \033[40m\033[001;033m%{apachegroup} "

echo
echo
echo -e "\033[40m\033[001;031m\$RPM\033[0m"
echo -e "\033[40m\033[001;031m\$OS\033[0m"
echo -e "\033[40m\033[001;031m\$BLD\033[0m"
echo -e "\033[40m\033[001;031m\$CCF\033[0m"
echo -e "\033[40m\033[001;031m\$LDF\033[0m"
echo -e "\033[40m\033[001;031m\$APACHEUSER\033[0m"
echo -e "\033[40m\033[001;031m\$APACHEGROUP\033[0m"
echo
echo

sleep 5

EOF

# Take care to execute and then to delete
#------------------------------------------------------------------------------------
chmod u+x %{_tmppath}/%{name}-%{pversion}-show_flags
%{_tmppath}/%{name}-%{pversion}-show_flags
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags

# Patch th templates
#------------------------------------------------------------------------------------
[ -f %{_tmppath}/patch_templates ] && rm -f %{_tmppath}/patch_templates
#
cat <<EOF >>%{_tmppath}/patch_templates
#!/bin/sh
ls $RPM_BUILD_DIR/%{name}-%{pversion}/*.c >  %{_tmppath}/c.list
ls $RPM_BUILD_DIR/%{name}-%{pversion}/*.h >> %{_tmppath}/c.list
ls $RPM_BUILD_DIR/%{name}-%{pversion}/html/*.html > %{_tmppath}/html.list
# Correggo i path nei riferimenti c
for i in \`cat %{_tmppath}/c.list\`; do

perl -pi -e 's|html/|%{vqadmdir}/html/|g' \$i

done;

for i in \`cat %{_tmppath}/html.list\`; do

perl -pi -e 's|/mail/toaster.vqadmin|/mail/vqadmin/toaster.vqadmin|g' \$i

done;

[ -f %{_tmppath}/c.list ] && rm -f %{_tmppath}/c.list
[ -f %{_tmppath}/html.list ] && rm -f %{_tmppath}/html.list

EOF

# Setto il piccolo file bash eseguibile, lo eseguo, e lo cancello
chmod u+x %{_tmppath}/patch_templates
%{_tmppath}/patch_templates
[ -f %{_tmppath}/patch_templates ] && rm -f %{_tmppath}/patch_templates

# Scrivo il modlulo per il control panel
cat <<EOF >>$RPM_BUILD_DIR/%{name}-%{pversion}/vqadmin.module


<!-- vqadmin.module -->
<tr>
	<td align="right" width="47%">Add and edit Virtual domains</td>
	<td width="6%">&nbsp;</td>
	<td align="left" width="47%"><input type="button" value="%{name}-%{pversion}" class="inputs" onClick="location.href='/mail/vqadmin/toaster.vqadmin';"></td>
</tr>
<!-- vqadmin.module -->


EOF

# We have gcc written in a temp file
#------------------------------------------------------------------------------------
export CC="`cat %{_tmppath}/%{name}-%{pversion}-gcc` %{ccflags}"


#------------------------------------------------------------------------------------
%build
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}

%configure \
	--enable-qmaildir=/var/qmail \
	--enable-vpopuser=vpopmail \
	--enable-vpopgroup=vchkpw \
	--enable-cgibindir=%{basedir}/cgi-bin/ \
	--enable-htmldir=%{vqadmdir}/html

make


#------------------------------------------------------------------------------------
%install
#------------------------------------------------------------------------------------

[ -d %{buildroot}%{vqadmdir} ] 			|| mkdir -p %{buildroot}%{vqadmdir}
[ -d %{buildroot}%{vqadmdir}/html ] 		|| mkdir -p %{buildroot}%{vqadmdir}/html
[ -d %{buildroot}%{vqadmdir}/docs ] 		|| mkdir -p %{buildroot}%{vqadmdir}/docs
[ -d %{buildroot}%{basedir}/include ] 		|| mkdir -p %{buildroot}%{basedir}/include
[ -d %{buildroot}%{basedir}/cgi-bin/vqadmin ]	|| mkdir -p %{buildroot}%{basedir}/cgi-bin/vqadmin

install -m755 vqadmin %{buildroot}%{basedir}/cgi-bin/vqadmin/toaster.vqadmin
install -m644 html/* %{buildroot}%{vqadmdir}/html/
install -m644 html/en %{buildroot}%{vqadmdir}/html/en-us
install -m644 vqadmin.acl %{buildroot}%{basedir}/cgi-bin/vqadmin/vqadmin.acl
install -m644 vqadmin.module %{buildroot}%{basedir}/include

#------------------------------------------------------------------------------------
%clean
#------------------------------------------------------------------------------------
[ -n %{buildroot} -a %{buildroot} ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{pversion}
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc

#------------------------------------------------------------------------------------
%files
#------------------------------------------------------------------------------------
%attr(0755,root,root) %dir %{basedir}
%attr(0755,root,root) %dir %{vqadmdir}
%attr(0755,root,root) %dir %{vqadmdir}/docs
%attr(0755,root,root) %dir %{vqadmdir}/html

%attr(0755,root,root) %dir %{basedir}/cgi-bin/vqadmin

%attr(6755,root,root) %{basedir}/cgi-bin/vqadmin/toaster.vqadmin
%attr(0644,root,root) %{vqadmdir}/html/*
%attr(0644,%{apacheuser},%{apachegroup}) %{basedir}/include/*
%attr(0444,%{apacheuser},%{apachegroup}) %{basedir}/cgi-bin/vqadmin/vqadmin.acl

#------------------------------------------------------------------------------------
%changelog
#------------------------------------------------------------------------------------
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 2.3.4-1.3.6
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Wed Jun 10 2009 Jake Vickers <jake@qmailtoaster.com> 2.3.4-1.3.6
- Added Mandriva 2009 support
* Thu Apr 23 2009 Jake Vickers <jake@qmailtoaster.com> 2.3.4-1.3.5
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
- Fixed type in PHP code that could cause a table to display incorrectly
* Mon Feb 16 2009 Jake Vickers <jake@qmailtoaster.com> 2.3.4-1.3.4
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 2.3.4-1.3.4
- Added Fedora Core 6 support, as well as Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.3.3
- Add CentOS 5 i386 support
- Add CentOS 5 x86_64 support
* Tue Jul 18 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 2.3.4-1.3.2
- Lame attempt at adding valias support
- Fixed typo in template patch (QVADMIN to VQADMIN)
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.3.1
- Add SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.13
- Add Fedora Core 5 support
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.12
- Add SuSE 10.0 and Mandriva 2006.0 support
* Sat Oct 15 2005 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.11
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.10
- Add CentOS 4 x86_64 support
* Wed Sep 28 2005 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.9
- Revert back to vqadmin-2.3.4 account stability problems
* Fri Sep 22 2005 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.5a
- Fixed panel scripts to allow mail user account control
* Fri Jul 01 2005 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.5
- Add Fedora Core 4 support
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 2.3.4-1.2.4
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Sun Feb 27 2005 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.3
- Add Fedora Core 3 support
- Add CentOS support
* Thu Jun 03 2004 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.2
- Add Fedora Core 2 support
* Sun May 09 2004 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.2.1
- Update for qmailtoaster 1.2.1
* Mon Dec 29 2003 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.0.8
- Add Fedora Core 1 support
* Sun Nov 23 2003 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.0.7
- Add Trustix 2.0 support
- Fix images to images-toaster
* Thu May 15 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.3.4-1.0.6
- Red Hat Linux 9.0 support (nick@ndhsoft.com)
- Gnu/Linux Mandrake 9.2 support
- Clean-ups on SPEC: compilation banner, better gcc detects
- Detect gcc-3.2.3
* Mon Mar 31 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.3.4-1.0.5
- Conectiva Linux 7.0 support
- Better managing of apache user (related to distro)
* Sun Feb 15 2003 Nick Hemmesch <nick@ndhsoft.com> 2.3.4-1.0.4
- Support for Red Hat 8.0
* Wed Feb 05 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.3.4-1.0.3
- Support for Red Hat 8.0 thanks to Andrew.J.Kay
* Sat Feb 01 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.3.4-1.0.2
- Redo Macros to prepare supporting larger RPM OS.
  We could be able to compile (and use) packages under every RPM based
  distribution: we just need to write right requirements.
* Sat Jan 25 2003 Miguel Beccari <miguel.beccari@clikka.com> 2.3.4-1.0.1
- Added MDK 9.1 support
- Try to use gcc-3.2.1
- Added very little patch to compile with newest GLIBC
- Support dor new RPM-4.0.4
* Sat Oct 05 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.3.2-0.9.2
- Soft clean-ups
* Sun Sep 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 2.3.2-0.9.1
- RPM macros to detect Mandrake, RedHat, Trustix are OK again. They are
  very basic but they should work.
* Fri Sep 27 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.8.2.3.2-1
- Rebuilded under 0.8 tree.
- Important comments translated from Italian to English.
- Written rpm rebuilds instruction at the top of the file (in english).
- Finished JavaScript controls.
* Sun Sep 22 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.2.3.2-3
- External CSS
- JavaScripts controls (have to finish them)
- Clean-ups
* Thu Aug 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.2.3.2-2
- Deleted Mandrake Release Autodetection (creates problems)
* Fri Aug 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.2.3.2-1
- First RPM release. It comes with toaster templates, toaster layout,
  toaster dependencies: seems to work.

