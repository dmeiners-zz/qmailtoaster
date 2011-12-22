%define		name spamassassin
%define		pversion 3.2.5
%define 	bversion 1.3
%define		rpmrelease 17

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
BuildRequires:	perl >= 5.8.7, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_100  1
%define		default	       0
%endif

%if %{build_sus_10064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.0 x86_64 Linux 
BuildRequires:	perl >= 5.8.7, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10064  1
%define		default	       0
%endif

%if %{build_sus_101}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 Linux 
BuildRequires:	perl >= 5.8.7, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_101  1
%define		default	       0
%endif

%if %{build_sus_10164}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype SuSE 10.1 x86_64 Linux 
BuildRequires:	perl >= 5.8.7, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_sus_10164  1
%define		default	       0
%endif

%if %{build_sus_111}
%define         release %{bversion}.%{rpmrelease}
%define         ostype OpenSuSE 11.1 Linux
BuildRequires:  perl >= 5.8.7, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_sus_111  1
%define         default        0
%endif

%if %{build_mdk_103}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 Linux
BuildRequires:	perl-devel >= 5.8.7, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_103  1
%define		default	       0
%endif

%if %{build_mdk_10364}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2006.0 x86_64 Linux
BuildRequires:	perl-devel >= 5.8.7, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags} I /usr/lib/rpm/macros
%define		build_mdk_10364  1
%define		default	       0
%endif

%if %{build_mdk_102}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandriva 2005 Linux
BuildRequires:	perl-devel >= 5.8.6, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_102  1
%define		default	       0
%endif

%if %{build_mdk_101}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.1 Linux
BuildRequires:	perl-devel >= 5.8.5, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_101  1
%define		default	       0
%endif

%if %{build_mdk_100}
%define		release %{bversion}.%{rpmrelease}mdk
%define 	ostype Mandrake 10.0 Linux
BuildRequires:	perl-devel >= 5.8.3, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define		build_mdk_100  1
%define		default	       0
%endif

%if %{build_mdr_09}
%define         release %{bversion}.%{rpmrelease}mdk
%define         ostype Mandriva 2009 Linux
BuildRequires:  perl-devel >= 5.10.8, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_mdr_09  1
%define         default        0
%endif

%if %{build_rht_90}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype RedHat 9 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel, perl-forward-compat 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail, 
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_rht_90   1
%define		default	       0
%endif

%if %{build_fdr_10}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 1 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_10   1
%define		default	       0
%endif

%if %{build_fdr_20}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 2 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_20   1
%define		default	       0
%endif

%if %{build_fdr_30}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 3 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_30   1
%define		default	       0
%endif

%if %{build_fdr_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_40   1
%define		default	       0
%endif

%if %{build_fdr_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 4 x86_64 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_4064   1
%define		default	       0
%endif

%if %{build_fdr_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_50   1
%define		default	       0
%endif

%if %{build_fdr_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype Fedora Core 5 x86_64 Linux
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_fdr_5064   1
%define		default	       0
%endif

%if %{build_fdr_60}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_60   1
%define         default        0
%endif

%if %{build_fdr_6064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora Core 6 x86_64 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fdr_6064   1
%define         default        0
%endif

%if %{build_fedora_9}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_9   1
%define         default        0
%endif

%if %{build_fedora_964}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 9 x86_64 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_964   1
%define         default        0
%endif

%if %{build_fedora_10}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_10   1
%define         default        0
%endif

%if %{build_fedora_1064}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 10 x86_64 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1064   1
%define         default        0
%endif

%if %{build_fedora_11}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_11   1
%define         default        0
%endif

%if %{build_fedora_1164}
%define         release %{bversion}.%{rpmrelease}
%define         ostype Fedora 11 x86_64 Linux
BuildRequires:  perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel
Requires:       perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define         ccflags %{optflags}
%define         ldflags %{optflags}
%define         build_fedora_1164   1
%define         default        0
%endif

%if %{build_cnt_40}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 Linux 
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_40   1
%define		default	       0
%endif

%if %{build_cnt_4064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 4 x86_64 Linux 
BuildRequires:	perl >= 5.8.0, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_4064   1
%define		default	       0
%endif

%if %{build_cnt_50}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 Linux 
BuildRequires:	perl >= 5.8.8, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_50   1
%define		default	       0
%endif

%if %{build_cnt_5064}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux 
BuildRequires:	perl >= 5.8.8, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%define		default	       0
%endif

%if %{default}
%define		release %{bversion}.%{rpmrelease}
%define 	ostype CentOS 5 x86_64 Linux 
BuildRequires:	perl >= 5.8.8, perl(Digest::SHA1), perl(HTML::Parser), openssl-devel 
Requires:	perl(Digest::SHA1), perl(HTML::Parser), perl(Pod::Usage), procmail
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
%define		ccflags %{optflags}
%define		ldflags %{optflags}
%define 	build_cnt_5064   1
%endif

############### RPM ################################

%define		debug_package %{nil}
%define         vtoaster %{pversion}
%define		_use_internal_dependency_generator 0
%define		real_name Mail-SpamAssassin
%define		krb5backcompat %([ -a /usr/kerberos/include/krb5.h ] && echo 1 || echo 0)

%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

%define		builddate Fri Jun 12 2009

Name:		%{name}-toaster
Summary:	Spam filter for email which can be invoked from mail delivery agents.
Version:	%{vtoaster}
Release:	%{release}
License:	Apache License
Group:		Applications/Internet
URL:		http://spamassassin.apache.org/
Source0:	%{name}/%{real_name}-%{version}.tar.bz2
Source1:	qmailtoaster.local.cf.bz2
Source2:	supervise.spamd.run.bz2
Source3:	supervise.spamd.log.run.bz2
Source4:	qmailtoaster.v310.pre.bz2
Source99:	filter-requires-spamassassin.sh
Buildroot:	%{_tmppath}/%{name}-root
Prefix:		%{_prefix}
Requires:	vpopmail-toaster >= 5.4.17, qmail-toaster
Obsoletes:	perl-Mail-SpamAssassin, spamassassin, perl-spamassassin
Packager:       Jake Vickers <jake@qmailtoaster.com>

%define		name spamassassin
%define		__find_requires %{SOURCE99}
%define		qdir /var/qmail

#------------------------------------------------------------------------------------
%description
#------------------------------------------------------------------------------------
SpamAssassin provides you with a way to reduce if not completely eliminate
Unsolicited Commercial Email (SPAM) from your incoming email.  It can
be invoked by a MDA such as sendmail or postfix, or can be called from
a procmail script, .forward file, etc.  It uses a genetic-algorithm
evolved scoring system to identify messages which look spammy, then
adds headers to the message so they can be filtered by the user's mail
reading software.  This distribution includes the spamd/spamc components
which create a server that considerably speeds processing of mail.

v310.pre settings
-----------------------------------------------------------
loadplugin Mail::SpamAssassin::Plugin::Pyzor
loadplugin Mail::SpamAssassin::Plugin::AWL
loadplugin Mail::SpamAssassin::Plugin::AutoLearnThreshold
loadplugin Mail::SpamAssassin::Plugin::WhiteListSubject
loadplugin Mail::SpamAssassin::Plugin::MIMEHeader
loadplugin Mail::SpamAssassin::Plugin::ReplaceTags

The custom local.cf for spamassassin-toaster is as follows:
-----------------------------------------------------------
ok_locales all
skip_rbl_checks 1

required_score 5
report_safe 0
rewrite_header Subject ***SPAM***

use_pyzor 1

use_auto_whitelist 1

use_bayes 1
use_bayes_rules 1
bayes_auto_learn 1


#------------------------------------------------------------------------------------
%prep
#------------------------------------------------------------------------------------

%setup -q -n Mail-SpamAssassin-%{version}

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


#------------------------------------------------------------------------------------
%build
#------------------------------------------------------------------------------------
%{__perl} Makefile.PL DESTDIR=$RPM_BUILD_ROOT/ SYSCONFDIR=%{_sysconfdir} INSTALLDIRS=vendor ENABLE_SSL=yes < /dev/null

%{__make} %{?krb5backcompat:SSLCFLAGS=-DSPAMC_SSL\ -I/usr/kerberos/include} OPTIMIZE="$RPM_OPT_FLAGS"


#------------------------------------------------------------------------------------
%install
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall PREFIX=%{buildroot}%{prefix} \
	INSTALLMAN1DIR=%{buildroot}%{_mandir}/man1 \
	INSTALLMAN3DIR=%{buildroot}%{_mandir}/man3 \
	LOCAL_RULES_DIR=%{buildroot}/etc/mail/spamassassin
chmod 755 %{buildroot}%{_bindir}/* # allow stripping


[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -v {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

find $RPM_BUILD_ROOT/usr -type f -print |
        sed "s@^$RPM_BUILD_ROOT@@g" |
        grep -v perllocal.pod |
        grep -v "\.packlist" > %{name}-%{version}-filelist
if [ "$(cat %{name}-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit -1
fi
find $RPM_BUILD_ROOT%{perl_vendorlib}/* -type d -print |
        sed "s@^$RPM_BUILD_ROOT@%dir @g" >> %{name}-%{version}-filelist


rm -f %{buildroot}%{_sysconfdir}/mail/spamassassin/local.cf
rm -f %{buildroot}%{_sysconfdir}/mail/spamassassin/init.pre

	
# Dirs
#------------------------------------------------------------------------------------
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}/etc/cron.hourly
install -d %{buildroot}/etc/mail/spamassassin
install -d %{buildroot}%{qdir}/supervise/spamd
install -d %{buildroot}%{qdir}/supervise/spamd/log
install -d %{buildroot}%{qdir}/supervise/spamd/supervise
install -d %{buildroot}/var/log/qmail
install -d %{buildroot}/var/log/qmail/spamd

#files
#------------------------------------------------------------------------------------
rm -f %{buildroot}%{_sysconfdir}/mail/spamassassin/local.cf
rm -f %{buildroot}%{_sysconfdir}/mail/spamassassin/v310.pre
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mail/spamassassin/local.cf.bz2
bunzip2 %{buildroot}%{_sysconfdir}/mail/spamassassin/local.cf.bz2
install -m 0644 %{SOURCE2} %{buildroot}%{qdir}/supervise/spamd/run.bz2
bunzip2 %{buildroot}%{qdir}/supervise/spamd/run.bz2
install -m 0644 %{SOURCE3} %{buildroot}%{qdir}/supervise/spamd/log/run.bz2
bunzip2 %{buildroot}%{qdir}/supervise/spamd/log/run.bz2
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/mail/spamassassin/v310.pre.bz2
bunzip2 %{buildroot}%{_sysconfdir}/mail/spamassassin/v310.pre.bz2
install -m 0644 $RPM_BUILD_DIR/%{real_name}-%{pversion}/rules/v312.pre %{buildroot}%{_sysconfdir}/mail/spamassassin/v312.pre
install -m 0644 $RPM_BUILD_DIR/%{real_name}-%{pversion}/rules/v320.pre %{buildroot}%{_sysconfdir}/mail/spamassassin/v320.pre
 

%if %{build_mdk_103} || %{build_mdk_10364}
   %{__perl} -pi -e "s|gz|bz2|g" $RPM_BUILD_DIR/%{real_name}-%{pversion}/spamassassin-%{pversion}-filelist
%endif

%if %{build_mdr_09}
   %{__perl} -pi -e "s|gz|lzma|g" $RPM_BUILD_DIR/%{real_name}-%{pversion}/spamassassin-%{pversion}-filelist
%endif

#------------------------------------------------------------------------------------
%post
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
%postun
#------------------------------------------------------------------------------------

if [ $1 = "0" ]; then
  rm -fR /var/qmail/supervise/spamd/
  rm -fR /var/log/qmail/spamd/
fi
#------------------------------------------------------------------------------------
%preun
#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
%clean
#------------------------------------------------------------------------------------
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{real_name}-%{pversion} ] && rm -rf $RPM_BUILD_DIR/%{real_name}-%{pversion}
[ -f %{_tmppath}/%{name}-%{pversion}-gcc ] && rm -f %{_tmppath}/%{name}-%{pversion}-gcc


#------------------------------------------------------------------------------------
%files -f %{name}-%{version}-filelist
#------------------------------------------------------------------------------------
%defattr(-,root,root)

# Docs
%doc LICENSE CREDITS Changes README TRADEMARK UPGRADE
%doc USAGE sample-nonspam.txt sample-spam.txt

# Dirs
%attr(0755,root,root) %dir %{_sysconfdir}/mail/spamassassin
%attr(1700,qmaill,qmail) %dir %{qdir}/supervise/spamd
%attr(0700,qmaill,qmail) %dir %{qdir}/supervise/spamd/log
%attr(0755,qmaill,qmail) %dir %{qdir}/supervise/spamd/supervise
%attr(0700,qmaill,qmail) %dir /var/log/qmail
%attr(0755,qmaill,qmail) %dir /var/log/qmail/spamd

# Files
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/mail/spamassassin/local.cf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/mail/spamassassin/v310.pre
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/mail/spamassassin/v312.pre
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/mail/spamassassin/v320.pre
%attr(0751,qmaill,qmail) %{qdir}/supervise/spamd/run
%attr(0751,qmaill,qmail) %{qdir}/supervise/spamd/log/run

#------------------------------------------------------------------------------------
%changelog
#------------------------------------------------------------------------------------
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 3.2.5-1.3.17
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Wed Jun 10 2009 Jake Vickers <jake@qmailtoaster.com> 3.2.5-1.3.17
- Added Mandriva 2009 support
* Thu Apr 23 2009 Jake Vickers <jake@qmailtoaster.com> 3.2.5-1.3.16
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
- Fixed a bug in installation of /etc/mail/spamassassin files that may have
- caused it to no build/install on certain systems
* Mon Feb 16 2009 Jake Vickers <jake@qmailtoaster.com> 3.2.5-1.3.15
- Added Suse 11.1 support
* Mon Feb 09 2009 Jake Vickers <jake@qmailtoaster.com> 3.2.5-1.3.15
- Added Fedora 9 and 10 support
* Fri Jul 11 2008 Erik A. Espinoza <espinoza@kabewm.com> 3.2.5-1.3.14
- Upgraded to SpamAssassin 3.2.5
* Sun Feb 04 2008 Erik A. Espinoza <espinoza@kabewm.com> 3.2.4-1.3.13
- Upgraded to SpamAssassin 3.2.4
* Thu Aug 09 2007 Erik A. Espinoza <espinoza@kabewm.com> 3.2.3-1.3.12
- Upgraded to SpamAssassin 3.2.3
* Tue Aug 07 2007 Erik A. Espinoza <espinoza@kabewm.com> 3.2.2-1.3.11
- Upgraded to SpamAssassin 3.2.2
* Mon Jun 18 2007 Erik A. Espinoza <espinoza@kabewm.com> 3.2.1-1.3.10
- Upgraded to SpamAssassin 3.2.1
* Mon May 21 2007 Erik A. Espinoza <espinoza@kabewm.com> 3.2.0-1.3.9
- Upgraded to SpamAssassin 3.2.0
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 3.1.8-1.3.8
- Added CentOS 5 i386 support
- Added CentOS 5 x86_64 support
* Sat Feb 24 2007 Erik A. Espinoza <espinoza@kabewm.com> 3.1.8-1.3.7
- Upgraded to SpamAssassin 3.1.8
- Made local.cf, v310.pre and v312.pre into config for easier upgrades
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.7-1.3.6
- Added Fedora Core 6 support
- Changed "required_hits" to "required_score" as the old option has been deprecated
* Sat Oct 14 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.7-1.3.5
- Upgraded to SpamAssassin 3.1.7
* Sat Oct 07 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.6-1.3.4
- Upgraded to SpamAssassin 3.1.6
- Removed "-L", local checks only setting
* Sun Sep 10 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.5-1.3.3
- Upgraded to SpamAssassin 3.1.5
* Sat Aug 05 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.4-1.3.2
- Upgraded to SpamAssassin 3.1.4
* Tue Jun 06 2006 John Li <jli@jlisbz.com> 3.1.3-1.3.1
- Upgraded to SpamAssassin 3.1.3
- Ticked branch to 1.3
* Sun May 28 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.2-1.2.16
- Upgraded to spamassassin 3.1.2
* Tue May 16 2006 Nick Hemmesch <nick@ndhsoft.com> 3.1.1-1.2.15
- Added SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 3.1.1-1.2.14
- Added Fedora Core 5 support
* Sun Apr 30 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.1-1.2.13
- Fixed spec file to clean build root properly
- Reoved spam-sync cron job
* Tue Apr 10 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.1-1.2.12
- Updated to spamassassin 3.1.1
* Tue Dec 06 2005 Nick Hemmesch <nick@ndhsoft.com> 3.1.0-1.2.11
- Fix bayes_auto_learn and sa-learn functions
- Update local.cf and v310.pre
- Add sa-learn --sync call to cron.hourly
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 3.1.0-1.2.10
- Add SuSE 10.0 and Mandriva 2006.0 support
* Sat Oct 15 2005 Nick Hemmesch <nick@ndhsoft.com> 3.0.4-1.2.9
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 3.0.4-1.2.8
- Add CentOS 4 x86_64 support
* Mon Sep 26 2005 Nick Hemmesch <nick@ndhsoft.com> 3.1.0-1.2.7
- Update local.cf and dirs for spamassassin 3.1.0
* Tue Sep 20 2005 Erik A. Espinoza <espinoza@forcenetworks.com> 3.1.0-1.2.6
- Upgraded to spamassassin 3.1.0
* Thu Jul 28 2005 Nick Hemmesch <nick@ndhsoft.com> 3.0.4-1.2.5
- Fix auto-whitelist - change from a dir to a file
* Mon Jul 04 2005 Nick Hemmesch <nick@ndhsoft.com> 3.0.4-1.2.4
- Fix perl-forward-compat problem with rht90 
* Fri Jul 01 2005 Nick Hemmesch <nick@ndhsoft.com> 3.0.4-1.2.4
- Add support for Fedora Core 4
* Sun Jun 19 2005 Nick Hemmesch <nick@ndhsoft.com> 3.0.4-1.2.3
- Update to spamassassin-3.0.4
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 3.0.1-1.2.2
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Mon May 30 2005 Nick Hemmesch <nick@ndhsoft.com> - 3.0.1-1.2.1
- Intitial build to work with qmail-toaster and simscan-toaster
