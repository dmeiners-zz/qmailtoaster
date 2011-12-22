%define		name clamav
%define		pversion 0.97.3
%define 	bversion 1.3
%define		rpmrelease 44

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
%define		build_mdr_0964	0
%define		build_mdr_10	0
%define		build_mdr_1064	0

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
%define         build_fedora_12 0
%define         build_fedora_1264  0

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
%{?_with_mdr0964:       %{expand: %%define build_mdr_0964  1}}
%{?_with_mdr10:         %{expand: %%define build_mdr_10  1}}
%{?_with_mdr1064:       %{expand: %%define build_mdr_1064  1}}

%{?_with_rht90:		%{expand: %%define build_rht_90   1}}

%{?_with_fdr10:		%{expand: %%define build_fdr_10   1}}
%{?_with_fdr20:   	%{expand: %%define build_fdr_20   1}}
%{?_with_fdr30:   	%{expand: %%define build_fdr_30   1}}
%{?_with_fdr40:   	%{expand: %%define build_fdr_40   1}}
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
%{?_with_fedora_12:     %{expand: %%define build_fedora_12   1}}
%{?_with_fedora_1264:   %{expand: %%define build_fedora_1264   1}}

%{?_with_cnt40:		%{expand: %%define build_cnt_40   1}}
%{?_with_cnt4064:	%{expand: %%define build_cnt_4064   1}}
%{?_with_cnt50:		%{expand: %%define build_cnt_50   1}}
%{?_with_cnt5064:	%{expand: %%define build_cnt_5064   1}}

# Distro Statements
%if %{build_sus_100}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 Linux 
BuildRequires:	bzip2, gtkzip, perl-Archive-Zip, gmp, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2, gtkzip, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/init.d
%define		_initdist suse
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux 
BuildRequires:	bzip2, gtkzip, perl-Archive-Zip, gmp-32bit, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2, gtkzip, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/init.d
%define		_initdist suse
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux 
BuildRequires:	bzip2, perl-Archive-Zip, gmp, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/init.d
%define		_initdist suse
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux 
BuildRequires:	bzip2, perl-Archive-Zip, gmp-32bit, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/init.d
%define		_initdist suse
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
BuildRequires:  bzip2, perl-Archive-Zip, gmp, zlib-devel, libcurl4, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/init.d
%define         _initdist suse
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
BuildRequires:	bzip2-devel, libgmp3-devel, zlib-devel, curl-devel, libidn11-devel, autoconf2.5, automake1.7, ncurses, ncurses-devel
BuildRequires:	multiarch-utils >= 1.0.3
Obsoletes:	clamav, clamav-db, libclamav1, klamav
Requires:	libbzip2_1, libgmp3, zlib, curl, libidn11
PreReq:		rpm-helper
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
BuildRequires:	bzip2-devel, lib64gmp3-devel, zlib-devel, curl-devel, lib64idn11-devel, autoconf2.5, automake1.7, ncurses, ncurses-devel
BuildRequires:	multiarch-utils >= 1.0.3
Obsoletes:	clamav, clamav-db, lib64clamav1, klamav
Requires:	lib64bzip2_1, lib64gmp3, zlib, curl, lib64idn11
PreReq:		rpm-helper
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
BuildRequires:	bzip2-devel, libgmp3-devel, zlib-devel, curl-devel, libidn11-devel, autoconf2.5, automake1.7, ncurses, ncurses-devel
BuildRequires:	multiarch-utils >= 1.0.3
Requires:	libbzip2_1, libgmp3, zlib, curl, libidn11
PreReq:		rpm-helper
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
%define 	ostype Mandriva 2005 Linux
BuildRequires:	bzip2-devel, libgmp3-devel, zlib-devel, curl-devel, libidn11-devel, autoconf2.5, automake1.7, ncurses, ncurses-devel
Requires:	libbzip2_1, libgmp3, zlib, curl, libidn11
PreReq:		rpm-helper
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
BuildRequires:	bzip2-devel, libgmp3-devel, zlib-devel, curl-devel, libidn11-devel, autoconf2.5, automake1.7, ncurses, ncurses-devel 
Requires:	libbzip2_1, libgmp3, zlib, curl, libidn11
PreReq:		rpm-helper
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
BuildRequires:  libbzip2-devel, libgmp-devel, zlib1-devel, libcurl-devel, libidn-devel, autoconf, automake1.7, ncurses, libncurses-devel
BuildRequires:  multiarch-utils >= 1.0.9
Obsoletes:      clamav, clamav-db, libclamav1, klamav
Requires:       libbzip2_1, libgmp3, zlib1, curl, libidn11
PreReq:         rpm-helper
%define         ccflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         ldflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_mdr_0964}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 x86_64 Linux
BuildRequires:  libbzip2-devel, libgmp-devel, zlib1-devel, libcurl-devel, libidn-devel, autoconf, automake1.7, ncurses, libncurses-devel
BuildRequires:  multiarch-utils >= 1.0.9
Obsoletes:      clamav, clamav-db, libclamav1, klamav
Requires:       libbzip2_1, libgmp3, zlib1, curl, libidn11
PreReq:         rpm-helper
%define         ccflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         ldflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_mdr_0964  1
%define         default        0
%endif

%if %{build_mdr_10}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2010 Linux
BuildRequires:  libbzip2-devel, libgmp-devel, zlib1-devel, libcurl-devel, libidn-devel, autoconf, automake1.7, ncurses, libncurses-devel
BuildRequires:  multiarch-utils >= 1.0.9
Obsoletes:      clamav, clamav-db, libclamav1, klamav
Requires:       libbzip2_1, libgmp3, zlib1, curl, libidn11
PreReq:         rpm-helper
%define         ccflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         ldflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_mdr_10  1
%define         default        0
%endif

%if %{build_mdr_1064}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2010 x86_64 Linux
BuildRequires:  libbzip2-devel, libgmp-devel, zlib1-devel, libcurl-devel, libidn-devel, autoconf, automake1.7, ncurses, libncurses-devel
BuildRequires:  multiarch-utils >= 1.0.9
Obsoletes:      clamav, clamav-db, libclamav1, klamav
Requires:       libbzip2_1, libgmp3, zlib1, curl, libidn11
PreReq:         rpm-helper
%define         ccflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         ldflags -O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -fomit-frame-pointer -march=i586 -mtune=generic
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_mdr_1064  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype RedHat 9 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 1 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 2 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 3 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_fedora_12}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 12 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_12   1
%define         default        0
%endif

%if %{build_fedora_1264}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 12 x86_64 Linux
BuildRequires:  bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:       bzip2-libs, gmp, zlib, curl, libidn
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         crontab /etc/crontab
%define         _initpath /etc/rc.d/init.d
%define         _initdist notsuse
%define         build_fedora_1264   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux 
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel 
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux 
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux 
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux 
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux 
BuildRequires:	bzip2-devel, gmp-devel, zlib-devel, curl-devel, libidn-devel, autoconf, automake, ncurses, ncurses-devel
Requires:	bzip2-libs, gmp, zlib, curl, libidn
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		crontab	/etc/crontab
%define		_initpath /etc/rc.d/init.d
%define		_initdist notsuse
%define 	build_cnt_5064   1
%endif

############### RPM ################################

%define		debug_package %{nil}
%define         vtoaster %{pversion}
%define		_qdir /var/qmail
%define		_spath %{_qdir}/supervice
%define		_qtlogdir /var/log/qmail
%define		real_name clamav

%define		builddate Tue Nov 08 2011

Name:		%{name}-toaster
Summary:	ClamAV for qmail-toaster
Version:	%{vtoaster}
Release:	%{release}
License:	GPL
Group:		System Enviroment/Daemons
URL:		http://www.clamav.net
Source0:	clamav-%{pversion}.tar.bz2
Source1:	freshclam.logrotate.bz2
#Source2:	freshclam.daily.bz2
Source3:	freshclam.bz2
Source4:	supervise-clamd.run.bz2
Source5:	supervise-clamd-log.run.bz2
Source6:	freshclam.sus.bz2
Patch0:		clamav-0.9x-qmailtoaster.patch.bz2
#Patch1:		freshclam.conf-0.96.0.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{pversion}-root
Requires:	zlib >= 1.2.3
Packager:	Jake Vickers <jake@qmailtoaster.com>

%define	name clamav


#-------------------------------------------------------------------------------
%description
#-------------------------------------------------------------------------------
Clam AntiVirus is a GPL anti-virus toolkit for UNIX. The main purpose of this
software is the integration with mail servers (attachment scanning).
The package provides a flexible and scalable multi-threaded daemon,
a command line scanner, and a tool for automatic updating via Internet.
The programs are based on a shared library distributed with package,
which you can use with your own software.
Most importantly, the virus database is kept up to date .


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -q -n %{name}-%{pversion}

# Patch the config files
%patch0 -p1
#%patch1 -p1

# 6-10-09 Rename the configure.in file for Mandriva 2009 or it will not compile
%if %{build_mdr_09} || %{build_mdr_10} || %{build_mdr_0964} || %{build_mdr_1064}
mv configure.in configure.in.mandriva
%endif


# Cleanup for the compiler
#-------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc

echo "gcc" > %{_tmppath}/%{name}-%{pversion}-gcc


# Display compilation flags and OS with colors ;)
#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------
chmod u+x %{_tmppath}/%{name}-%{pversion}-show_flags
%{_tmppath}/%{name}-%{pversion}-show_flags
[ -f %{_tmppath}/%{name}-%{pversion}-show_flags ] && rm -f %{_tmppath}/%{name}-%{pversion}-show_flags


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

# Make clamav user and group for build
#-------------------------------------------------------------------------------
if [ -z "`/usr/bin/id -g clamav 2>/dev/null`" ]; then
	/usr/sbin/groupadd -g 46 -r clamav 2>&1 || :
fi
if [ -z "`/usr/bin/id -u clamav 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 46 -r -M -d /tmp  -s /sbin/nologin -c "Clam AntiVirus" -g clamav clamav 2>&1 || :
fi


# Run configure to create makefile
#-------------------------------------------------------------------------------
#%{__aclocal}
#%{__autoconf}
#%{__automake}
%configure
%{__make}

# Delete gcc temp file
#-------------------------------------------------------------------------------
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d %{buildroot}/%{name}-%{pversion} ] && rm -rf %{buildroot}/%{name}-%{pversion}

install -d %{buildroot}%{_initpath}/
install -d %{buildroot}%{_sysconfdir}/cron.daily
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -d %{buildroot}/var/log/clamav
install -d %{buildroot}/var/run/clamav
install -d %{buildroot}/var/spool/clamav

%{__make} DESTDIR=%{buildroot} install

install -d %{buildroot}%{_qdir}
install -d %{buildroot}%{_qdir}/supervise
install -d %{buildroot}%{_qdir}/supervise/clamd
install -d %{buildroot}%{_qdir}/supervise/clamd/log
install -d %{buildroot}%{_qdir}/supervise/clamd/supervise
install -d %{buildroot}/var/log/qmail
install -d %{buildroot}/var/log/qmail/clamd

rm -rf %{buildroot}%{_mandir}/man8/clamav-milter.8*
install etc/clamd.conf %{buildroot}%{_sysconfdir}/clamd.conf
install etc/freshclam.conf %{buildroot}%{_sysconfdir}/freshclam.conf
install %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/freshclam.bz2
bunzip2 %{buildroot}%{_sysconfdir}/logrotate.d/freshclam.bz2
#install %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.daily/freshclam.bz2
#bunzip2 %{buildroot}%{_sysconfdir}/cron.daily/freshclam.bz2
%if %{build_sus_100} || %{build_sus_10064} || %{build_sus_101} || %{build_sus_10164} || %{build_sus_111}
   install %{SOURCE6} %{buildroot}%{_initpath}/freshclam.bz2
   bunzip2 %{buildroot}%{_initpath}/freshclam.bz2
%else
   install %{SOURCE3} %{buildroot}%{_initpath}/freshclam.bz2
   bunzip2 %{buildroot}%{_initpath}/freshclam.bz2
%endif
install %{SOURCE4} %{buildroot}%{_qdir}/supervise/clamd/run.bz2
bunzip2 %{buildroot}%{_qdir}/supervise/clamd/run.bz2
install %{SOURCE5} %{buildroot}%{_qdir}/supervise/clamd/log/run.bz2
bunzip2 %{buildroot}%{_qdir}/supervise/clamd/log/run.bz2
touch %{buildroot}/var/log/clamav/freshclam.log

# Make freshclam sym link
#-------------------------------------------------------------------------------
pushd %{buildroot}%{_bindir}
  ln -s ../..%{_initpath}/freshclam fclamctl
popd


%if %{build_mdk_102}
%multiarch_binaries %{buildroot}%{_bindir}/clamav-config
%endif

# Remove old daily.cld file if it exists
if [ -e /usr/share/clamav/daily.cld ]; then
 rm  -f /usr/share/clamav/daily.cld
fi

#Remove old main.cld file if it exists
if [ -e /usr/share/clamav/main.cld ]; then
 rm -f /usr/share/clamav/main.cld
fi

#-------------------------------------------------------------------------------
%pre
#-------------------------------------------------------------------------------
if [ -z "`/usr/bin/id -g clamav 2>/dev/null`" ]; then
	/usr/sbin/groupadd -g 46 -r clamav 2>&1 || :
fi
if [ -z "`/usr/bin/id -u clamav 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 46 -r -M -d /tmp  -s /sbin/nologin -c "Clam AntiVirus" -g clamav clamav 2>&1 || :
fi


#-------------------------------------------------------------------------------
%post
#-------------------------------------------------------------------------------
# Use country mirror for virus DB
ZONES="/usr/share/zoneinfo/zone.tab"
CONFIG="/etc/sysconfig/clock"
FRESHCFG=`/bin/mktemp /tmp/freshclam.XXXXXX`

if [ -r "$CONFIG" -a -r "$ZONES" ]; then
	source "$CONFIG"
	export CODE="$(grep -E "\b$ZONE\b" "$ZONES" | head -1 | cut -f1 | tr [A-Z] [a-z])"
fi

if [ -z "$CODE" ]; then
	export CODE="local"
fi

sed -e "s%^#DatabaseMirror .*%DatabaseMirror db.$CODE.clamav.net%" \
	%{_sysconfdir}/freshclam.conf > $FRESHCFG
mv $FRESHCFG %{_sysconfdir}/freshclam.conf

if [ -f %{_sysconfdir}/freshclam.conf.rpmnew ]; then
   sed -e "s%^#DatabaseMirror .*%DatabaseMirror db.$CODE.clamav.net%" \
   %{_sysconfdir}/freshclam.conf.rpmnew > $FRESHCFG
   mv $FRESHCFG %{_sysconfdir}/freshclam.conf.rpmnew
fi

chmod 0640 %{_sysconfdir}/freshclam.conf*

#if [ %{_initdist} = "suse" ]; then
  /sbin/chkconfig --add freshclam  
  /sbin/chkconfig freshclam on
#fi


%if %{build_mdk_102}
   %create_ghostfile /var/log/%{name}/freshclam.log %{name} %{name} 0644
%endif

# only start freshclam if we're not installing in a sandbox.
# fuse-unionfs doesn't appear to support opening (the log) in append mode.
if [ ! -f /boot/.qtp-sandbox ]; then
  /sbin/service freshclam start > /dev/null 2>&1
fi

#-------------------------------------------------------------------------------
%preun
#-------------------------------------------------------------------------------
killall -TERM freshclam > /dev/null 2>&1
if [ $1 -eq 0 ]; then
  userdel clamav

  /sbin/chkconfig --del freshclam 

  if [ %{_initdist} = "notsuse" ]; then
    # Remove runlevel links
    rm -f %{_sysconfdir}/rc0.d/K30freshclam 2>&1 > /dev/null
    rm -f %{_sysconfdir}/rc1.d/K30freshclam 2>&1 > /dev/null
    rm -f %{_sysconfdir}/rc2.d/S80freshclam 2>&1 > /dev/null
    rm -f %{_sysconfdir}/rc3.d/S80freshclam 2>&1 > /dev/null
    rm -f %{_sysconfdir}/rc4.d/S80freshclam 2>&1 > /dev/null
    rm -f %{_sysconfdir}/rc5.d/S80freshclam 2>&1 > /dev/null
    rm -f %{_sysconfdir}/rc6.d/K30freshclam 2>&1 > /dev/null
  fi
fi


#-------------------------------------------------------------------------------
%postun
#-------------------------------------------------------------------------------
if [ $1 = "0" ]; then
  rm -fR %{_spath}/clamd/
  rm -fR %{_qtlogdir}/clamd/
fi


#-------------------------------------------------------------------------------
%clean
#-------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{real_name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{real_name}-%{pversion}
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc


#-------------------------------------------------------------------------------
%files 
#-------------------------------------------------------------------------------
%defattr(0644,root,root,0755)

# Dirs
%attr(0755,clamav,clamav) %dir /var/log/clamav
%attr(0755,clamav,clamav) %dir /var/run/clamav
%attr(0755,root,qmail) %dir %{_qdir}
%attr(0755,qmaill,qmail) %dir %{_qdir}/supervise
%attr(1700,qmaill,qmail) %dir %{_qdir}/supervise/clamd
%attr(0700,qmaill,qmail) %dir %{_qdir}/supervise/clamd/log
%attr(0755,qmaill,qmail) %dir %{_qdir}/supervise/clamd/supervise
%attr(0700,qmaill,qmail) %dir /var/log/qmail
%attr(0755,qmaill,qmail) %dir /var/log/qmail/clamd
%attr(0755,clamav,clamav) %dir %{_datadir}/clamav

# Binaries
%attr(0755,root,root) %{_bindir}/clamscan
%attr(0755,root,root) %{_bindir}/clamdscan
%attr(0755,root,root) %{_bindir}/freshclam
%attr(0755,root,root) %{_bindir}/clamdtop
%if %{build_mdk_102}
%multiarch %{multiarch_bindir}/clamav-config
%endif
%attr(0755,root,root) %{_bindir}/clamav-config
%attr(0755,root,root) %{_bindir}/clamconf
%attr(0755,root,root) %{_bindir}/sigtool
%attr(0755,root,root) %{_bindir}/clambc
%attr(0755,root,root) %{_sbindir}/clamd

# Sym Link
%attr(-,root,root) %{_bindir}/fclamctl

# Configuration
%attr(0755,root,root) %{_initpath}/freshclam
#%attr(0755,root,root) %{_sysconfdir}/cron.daily/freshclam
%attr(0644,root,clamav) %config(noreplace) %{_sysconfdir}/clamd.conf
%attr(0640,root,clamav) %config(noreplace) %{_sysconfdir}/freshclam.conf
%attr(0644,root,root) %{_sysconfdir}/logrotate.d/freshclam
%attr(0644,clamav,clamav) %config(noreplace) %{_datadir}/clamav/main.cvd
%attr(0644,clamav,clamav) %config(noreplace) %{_datadir}/clamav/daily.cvd
%attr(0640,clamav,clamav) %ghost /var/log/clamav/freshclam.log
%attr(0751,qmaill,qmail) %{_qdir}/supervise/clamd/run
%attr(0751,qmaill,qmail) %{_qdir}/supervise/clamd/log/run

# Devel
%attr(0644,root,root) %{_includedir}/clamav.h
%attr(0755,root,root) %{_libdir}/libclamav.so.*
%attr(0755,root,root) %{_libdir}/libclamav.so
#%attr(0755,root,root) %{_libdir}/libclamav.a
%attr(0755,root,root) %{_libdir}/libclamav.la
%attr(0755,root,root) %{_libdir}/libclamunrar*
%attr(0644,root,root) %{_libdir}/pkgconfig/libclamav.pc

# Documents
%doc AUTHORS BUGS COPYING ChangeLog FAQ INSTALL NEWS README
%doc docs/*.pdf test/

# Man pages
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/clamd.8*


#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Tue Nov 08 2011 Jake Vickers <jake@qmailtoaster.com> 0.97.3-1.3.44
- Updated clamav sources to 0.97.3
* Fri Jul 29 2011 Jake Vickers <jake@qmailtoaster.com> 0.97.2-1.3.43
- updated clamav sources to 0.97.2
* Sun Jun 12 2011 Jake Vickers <jake@qmailtoaster.com> 0.97.1-1.3.42
- Updated clamav sources to 0.97.1
* Sat Feb 12 2011 Jake Vickers <jake@qmailtoaster.com> 0.97.0-1.3.41
- Updated clamav to 0.97.0
- Added a routine to remove old .cld file if it exists
* Fri Dec 03 2010 Jake Vickers <jake@qmailtoaster.com> 0.96.5-1.3.40
- Updated clamav to 0.96.5
- Re-diff'ed the patch file and renamed to mark a demarcation point
- Merged the freshclam patch into the clamav-qmailtoaster patch
* Tue Oct 26 2010 Jake Vickers <jake@qmailtoaster.com> 0.96.4-1.3.39
- Updated clamav to 0.96.4
- Version numbers for packaging got messed up at some point in the spec
- file comments - went back and changed the last couple of releases,
- but not going back past the 0.96 mark
* Tue Sep 21 2010 Jake Vickers <jake@qmailtoaster.com> 0.96.3-1.3.38
- Updated clamav to 0.96.3
* Sat Aug 14 2010 Jake Vickers <jake@qmailtoaster.com> 0.96.2-1.3.37
- Updated clamav to 0.96.2
* Fri May 28 2010 Jake Vickers <jake@qmailtoaster.com> 0.96.1-1.3.36
- Updated clamav to 0.96.1
* Sat Apr 10 2010 Jake Vickers <jake@qmailtoaster.com> 0.96.0-1.3.35
- Added patch file to adjust the freshclam.conf file settings
* Tue Apr 06 2010 Jake Vickers <jake@qmailtoaster.com> 0.96.0-1.3.33
- Updated clamav source to 0.96 (added .0 to align with current numbering)
- clambc added to 0.96.0
- libclamav.a removed from 0.96.0
- Updated patch file for clamd.conf to enable new settings and generally freshen up
* Sun Dec 06 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.3-1.3.32
- Added Fedora 12 and Fedora 12 x86_64 support
* Mon Nov 16 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.3-1.3.32
- Changed spec file to require libgmp-devel instead of libgmp3-devel
- for Mandriva 2009 and 2010 support
- Added Mandriva 2010 support
* Wed Oct 28 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.3-1.3.31
- Updated clamav to 0.95.3 - bugfix release
* Tue Aug 18 2009 Eric Shubert <ejs@shubes.net> 0.95.2-1.3.30
- Modified %post to not do freshclam processing when installing in sandbox
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.2-1.3.29
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Wed Jun 10 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.2-1.3.29
- Updated ClamAV to 0.95.2
- Added Mandriva 2009 support
* Thu Apr 23 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.1-1.3.28
- Added Fedora 9 x86_64 and Fedors 10 x86_64 support
- Fixed typo that may have caused Fedora 10 to incorrectly build
* Thu Apr 16 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.1-1.3.27
- Upgraded to ClamAV 0.95.1
* Wed Apr 01 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.0-1.3.26
- Added clamdtop to the spec file and ncurses-devel dependency
* Tue Mar 31 2009 Jake Vickers <jake@qmailtoaster.com> 0.95.0-1.3.25
- Updated clamav to 0.95
* Mon Feb 16 2009 Jake Vickers <jake@qmailtoaster.com> 0.94.2-1.3.24
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 0.94.2-1.3.24
- Added Fedora 9 and 10 support
* Thu Dec 04 2008 Jake Vickers <jake@v2gnu.com> 0.94.2-1.3.23
- Upgraded to ClamAV 0.94.2
* Wed Nov 12 2008 Erik A. Espinoza <espinoza@kabewm.com> 0.94.1-1.3.22
- Upgraded to ClamAV 0.94.1
* Wed Sep 03 2008 Erik A. Espinoza <espinoza@kabewm.com> 0.94-1.3.21
- Upgraded to ClamAV 0.94
* Fri Jul 11 2008 Erik A. Espinoza <espinoza@kabewm.com> 0.93.3-1.3.20
- Upgraded to ClamAV 0.93.3
* Sun Jul 06 2008 Erik A. Espinoza <espinoza@kabewm.com> 0.93.1-1.3.19
- Upgraded to ClamAV 0.93.1
* Sun Apr 19 2008 Erik A. Espinoza <espinoza@kabewm.com> 0.93-1.3.18
- Upgraded to ClamAV 0.93
* Thu Feb 20 2008 Erik A. Espinoza <espinoza@kabewm.com> 0.92.1-1.3.17
- Upgraded to ClamAv 0.92.1
* Tue Dec 25 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.92-1.3.16
- Upgraded to ClamAV 0.92
* Sun Aug 26 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.91.2-1.3.15
- Upgraded to ClamAV 0.91.2
* Tue Jul 17 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.91.1-1.3.14
- Upgraded to ClamAV 0.91.1
* Sun Jun 03 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.90.3-1.3.13
- Upgraded to ClamAV 0.90.3
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 0.90.2-1.3.12
- Upgraded to ClamAV 0.90.2
- Added CentOS 5 i386 support
- Added CentOS 5 x86_64 support
* Fri Mar 02 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.90.1-1.3.11
- Upgraded to ClamAV 0.90.1
- Removed stderr patch
- Removed logging configuration from default config
* Wed Feb 14 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.90-1.3.10
- Updated to ClamAV 0.90 release
* Thu Feb 01 2007 Erik A. Espinoza <espinoza@kabewm.com> 0.90rc3-1.3.9
- Updated to ClamAV 0.90rc3
- Set FixStaleSocket to yes in clamd.conf default
* Sun Nov 05 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.90rc2-1.3.8
- Removed freshclam cron, as it breaks new ClamAV
* Thu Nov 02 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.90rc2-1.3.7
- Added Fedora Core 6 support
* Mon Oct 30 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.90rc2-1.3.6
- Upgraded to ClamAV 0.90rc2 w/ Experimental settings enabled
* Sun Oct 21 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.90RC1.1-1.3.5
- Upgraded to ClamAV 0.90RC1.1 w/ Experimental settings enabled
* Sun Oct 15 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88.5-1.3.4
- Upgraded to ClamAV 0.88.5
* Mon Aug 07 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88.4-1.3.3
- Upgraded to ClamAV 0.88.4
* Sun Jul 02 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88.3-1.3.2
- Upgraded to ClamAV 0.88.3
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 0.87.1-1.3.1
- Added SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 0.87.1-1.2.15
- Added Fedora Core 5 support
* Wed May 03 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88.2-1.2.14
- Fixed freshclam logrotate
- Add new freshclam init script 
- Upgraded to ClamAV 0.88.2
* Sun Apr 30 2006 Nick Hemmesch <nick@ndhsoft.com> 0.87.1-1.2.13
- Fixed freshclam logrotate thanks to xspace
* Thu Apr 06 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88.1-1.2.12
- Upgraded to ClamAV 0.88.1
* Thu Jan 12 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88-1.2.11
- Upgraded to ClamAV 0.88
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 0.87.1-1.2.10
- Add SuSE 10.0 and Mandriva 2006.0 support
* Thu Nov 10 2005 Erik A. Espinoza <espinoza@forcenetworks.com> 0.87.1-1.2.9
- Upgraded to 0.87.1
* Sat Oct 15 2005 Nick Hemmesch <nick@ndhsoft.com> 0.87-1.2.8
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 0.87-1.2.7
- Add CentOS 4 x86_64 support
* Tue Sep 20 2005 Erik A. Espinoza <espinoza@forcenetworks.com> 0.87-1.2.6
- Upgraded to clamav 0.87
- Changed zlib to require 1.2.3
* Mon Jul 25 2005 Erik A. Espinoza <espinoza@forcenetworks.com> 0.86.2-1.2.5
- Upgraded to clamav 0.86.2
* Fri Jul 01 2005 Nick Hemmesch <nick@ndhsoft.com> 0.86.1-1.2.4
- Add support for Fedora Core 4
* Sun Jun 26 2005 Nick Hemmesch <nick@ndhsoft.com> 0.86.1-1.2.3
- Update to clamav-0.86.1
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.85-1.2.2
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
- fix deps and conditional %%multiarch for 10.2
* Sun May 22 2005 Nick Hemmesch <nick@ndhsoft.com> 0.85.1-1.2.1
- Adapt ClamAV for QmailToaster
- Initial build
