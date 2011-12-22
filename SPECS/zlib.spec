%define debug_package %{nil}

Summary: The zlib compression and decompression library.
Name: zlib
Version: 1.2.3
Release: 1.0.3
Group: System Environment/Libraries
Source: ftp://ftp.info-zip.org/pub/infozip/zlib/zlib-%{version}.tar.bz2
Patch0: zlib-1.1.4-make-test.patch
URL: http://www.gzip.org/zlib/
License: BSD
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Zlib is a general-purpose, patent-free, lossless data compression
library which is used by many different programs.

%package devel
Summary: Header files and libraries for Zlib development.
Group: Development/Libraries
Requires: zlib = %{version}

%description devel
The zlib-devel package contains the header files and libraries needed
to develop programs that use the zlib compression and decompression
library.

%prep
%setup -q
%patch0 -p1 -b .make-test

%build

CFLAGS="$RPM_OPT_FLAGS -fPIC" ./configure --shared --prefix=%{_prefix}

# now build the static lib
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man3

CFLAGS="$RPM_OPT_FLAGS -fPIC" ./configure --shared --prefix=%{_prefix}
make install prefix=${RPM_BUILD_ROOT}%{_prefix}

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}
make install prefix=${RPM_BUILD_ROOT}%{_prefix}

install -m644 zutil.h ${RPM_BUILD_ROOT}%{_includedir}/zutil.h

if [ "%{_prefix}/lib" != "%{_libdir}" ]; then
    mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
    mv ${RPM_BUILD_ROOT}%{_prefix}/lib/* ${RPM_BUILD_ROOT}%{_libdir}
    rmdir ${RPM_BUILD_ROOT}%{_prefix}/lib
fi

%check
make %{?_smp_mflags} test

%clean
[ -d /usr/src/redhat/BUILD/zlib-1.2.3 ] && rm -rf /usr/src/redhat/BUILD/zlib-1.2.3
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README
%{_libdir}/libz.so.*

%files devel
%defattr(-,root,root)
%doc ChangeLog algorithm.txt minigzip.c example.c
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/zlib.3*

%changelog
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 1.2.3-1.0.3
- Change compile options

* Wed Jul 27 2005 Erik A. Espinoza <espinoza@forcenetworks.com> 1.2.3-1.0.2
- Upgraded to 1.2.3 due to various security fixes

* Tue Jan 18 2005 Petr Kritof <Petr|Kristof_CZ> 1.2.2.2-0
- Backport to  FC1 and FC2 and FC3

* Sat Jan  1 2005 Jeff Johnson <jbj@jbj.org> 1.2.2.2-1
- upgrade to 1.2.2.2.

* Fri Nov 12 2004 Jeff Johnson <jbj@jbj.org> 1.2.2.1-1
- upgrade to 1.2.2.1.

* Sun Sep 12 2004 Jeff Johnson <jbj@redhat.com> 1.2.1.2-1
- update to 1.2.1.2 to fix 2 DoS problems (#131385).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Jan 18 2004 Jeff Johnson <jbj@jbj.org> 1.2.1.1-1
- upgrade to zlib-1.2.1.1.

* Sun Nov 30 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.2.1 release

* Mon Oct 13 2003 Jeff Johnson <jbj@jbj.org> 1.2.0.7-3
- unrevert zlib.h include constants (#106291), rejected upstream.

* Wed Oct  8 2003 Jeff Johnson <jbj@jbj.org> 1.2.0.7-2
- fix: gzeof not set when reading compressed file (#106424).
- fix: revert zlib.h include constants for now (#106291).

* Tue Sep 23 2003 Jeff Johnson <jbj@redhat.com> 1.2.0.7-1
- update to 1.2.0.7, penultimate 1.2.1 release candidate.

* Tue Jul 22 2003 Jeff Johnson <jbj@redhat.com> 1.2.0.3-0.1
- update to release candidate.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 19 2003 Jeff Johnson <jbj@redhat.com> 1.1.4-9
- rebuild, revert from 1.2.0.1.

* Mon Feb 24 2003 Jeff Johnson <jbj@redhat.com> 1.1.4-8
- fix gzprintf buffer overrun (#84961).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.1.4-7
- rebuilt

* Thu Nov 21 2002 Elliot Lee <sopwith@redhat.com> 1.1.4-6
- Make ./configure use $CC to ease cross-compilation

* Tue Nov 12 2002 Jeff Johnson <jbj@redhat.com> 1.1.4-5
- rebuild from cvs.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 26 2002 Jakub Jelinek <jakub@redhat.com> 1.1.4-2
- remove glibc patch, it is no longer needed (zlib uses gcc -shared
  as it should)
- run tests and only build the package if they succeed

* Thu Apr 25 2002 Trond Eivind Glomsrd <teg@redhat.com> 1.1.4-1
- 1.1.4

* Wed Jan 30 2002 Trond Eivind Glomsrd <teg@redhat.com> 1.1.3-25.7
- Fix double free

* Sun Aug 26 2001 Trond Eivind Glomsrd <teg@redhat.com> 1.1.3-24
- Add example.c and minigzip.c to the doc files, as
  they are listed as examples in the README (#52574)

* Mon Jun 18 2001 Trond Eivind Glomsrd <teg@redhat.com>
- Updated URL
- Add version dependency for zlib-devel
- s/Copyright/License/

* Wed Feb 14 2001 Trond Eivind Glomsrd <teg@redhat.com>
- bumped version number - this is the old version without the performance enhancements

* Fri Sep 15 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add -fPIC for shared libs (patch by Fritz Elfert)

* Thu Sep  7 2000 Jeff Johnson <jbj@redhat.com>
- on 64bit systems, make sure libraries are located correctly.

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 02 2000 Trond Eivind Glomsrd <teg@redhat.com>
- rebuild

* Tue Jun 13 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging to build on solaris2.5.1.

* Wed Jun 07 2000 Trond Eivind Glomsrd <teg@redhat.com>
- use %%{_mandir} and %%{_tmppath}

* Fri May 12 2000 Trond Eivind Glomsrd <teg@redhat.com>
- updated URL and source location
- moved README to main package

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man page.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- link against glibc

* Mon Jul 27 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 1.1.3

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.2
- buildroot

* Tue Oct 07 1997 Donnie Barnes <djb@redhat.com>
- added URL tag (down at the moment so it may not be correct)
- made zlib-devel require zlib

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
