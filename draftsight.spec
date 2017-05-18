%define __os_install_post %{nil}
%define debug_package %{nil}
%define dsver 2017SP02
%define developer dassaultsystemes
%global fix_rpath_errors 1
%global manual_deps 1

Summary:	Professional CAD system: supported file formats are DWT, DXF and DWG
Summary(ru): 	Профессиональная САПР: поддерживаются форматы файлов DWT, DXF и DWG
Name:		draftsight
Version:	2017.2.0.3085
%if 0%{?fedora} >= 25
Release:	1.1%{?dist}.R
%else
Release:	1.1%{?dist}
%endif

License:	Standalone license, activation required
URL:		http://www.3ds.com/products-services/%{name}-cad-software/

Source0:	http://dl-ak.solidworks.com/nonsecure/%{name}/%{dsver}/draftSight.rpm
Source1:	%{name}
Source2:	%{developer}-%{name}.desktop
Source3:	vnd.%{developer}.%{name}.dwg.xml
Source4:	vnd.%{developer}.%{name}.dwt.xml
Source5:	vnd.%{developer}.%{name}.dxf.xml
Source6:	ft-rockey.rules
Source7:	%{developer}-%{name}.appdata.xml

BuildRequires:	desktop-file-utils
%if 0%{?fix_rpath_errors}
BuildRequires:	chrpath
%endif
%if 0%{?fedora} >= 20
BuildRequires:  libappstream-glib
%endif

%if 0%{?manual_deps}
AutoReq:	no

Requires:	/bin/bash
Requires:	gnome-icon-theme
Requires:	libGLU.so.1()(64bit)
Requires:	libaudio.so.2()(64bit)
Requires:	xdg-utils

Requires:	ld-linux-x86-64.so.2()(64bit)
Requires:	ld-linux-x86-64.so.2(GLIBC_2.3)(64bit)
Requires:	libX11.so.6()(64bit)
Requires:	libc.so.6()(64bit)
Requires:	libc.so.6(GLIBC_2.14)(64bit)
Requires:	libc.so.6(GLIBC_2.15)(64bit)
Requires:	libc.so.6(GLIBC_2.2.5)(64bit)
Requires:	libc.so.6(GLIBC_2.3)(64bit)
Requires:	libc.so.6(GLIBC_2.3.2)(64bit)
Requires:	libc.so.6(GLIBC_2.3.4)(64bit)
Requires:	libc.so.6(GLIBC_2.4)(64bit)
Requires:	libdl.so.2()(64bit)
Requires:	libdl.so.2(GLIBC_2.2.5)(64bit)
Requires:	libgcc_s.so.1()(64bit)
Requires:	libgcc_s.so.1(GCC_3.0)(64bit)
Requires:	libgcc_s.so.1(GCC_3.3)(64bit)
Requires:	libgcc_s.so.1(GCC_4.2.0)(64bit)
Requires:	libm.so.6()(64bit)
Requires:	libm.so.6(GLIBC_2.2.5)(64bit)
Requires:	libpthread.so.0()(64bit)
Requires:	libpthread.so.0(GLIBC_2.2.5)(64bit)
Requires:	libstdc++.so.6()(64bit)
Requires:	libstdc++.so.6(CXXABI_1.3)(64bit)
Requires:	libstdc++.so.6(GLIBCXX_3.4)(64bit)
Requires:	libstdc++.so.6(GLIBCXX_3.4.11)(64bit)
Requires:	libstdc++.so.6(GLIBCXX_3.4.15)(64bit)
Requires:	libstdc++.so.6(GLIBCXX_3.4.9)(64bit)
Requires:	libuuid.so.1()(64bit)
Requires:	libuuid.so.1(UUID_1.0)(64bit)
Requires:	rtld(GNU_HASH)
%endif

ExclusiveArch:	x86_64

%description
Free CAD software for your DWG files by Dassault Systèmes (standalone license).
DraftSight lets professional CAD users, students and educators create, edit and
view DWG files. DraftSight runs on Windows®, Mac® and Linux.

%description -l ru
Бесплатная САПР с поддержкой формата DWG от Dassault Systèmes (индивидуальная
лицензия). DraftSight позволяет профессиональным пользователям, студентам и
преподавателям создавать, редактировать и просматривать файлы DWG. DraftSight
работает на платформах Windows®, Mac® and Linux.

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

pushd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -idV --quiet
popd

# Fix missing genltshp.shx:
pushd %{buildroot}/opt/dassault-systemes/DraftSight/Fonts
ln -s LTypeShp.shx genltshp.shx
popd

# Remove broken links:
rm $(find %{buildroot}/opt/dassault-systemes/DraftSight/ -type l -! -exec test -e {} \; -print)

# Install launch script:
mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Install *.desktop file and mime-types:
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mime/packages
install -pm 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{developer}-%{name}.desktop
install -pm 644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/vnd.%{developer}.%{name}.dwg.xml
install -pm 644 %{SOURCE4} %{buildroot}%{_datadir}/mime/packages/vnd.%{developer}.%{name}.dwt.xml
install -pm 644 %{SOURCE5} %{buildroot}%{_datadir}/mime/packages/vnd.%{developer}.%{name}.dxf.xml

# Install pixmaps:
for SIZE in 16 32 48 64 128; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes
  mkdir -p %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/apps
  mkdir -p %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/%{developer}-%{name}.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/apps/%{developer}-%{name}.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwg.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes/application-vnd.%{developer}.%{name}.dwg.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwg.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes/application-vnd.%{developer}.%{name}.dwg.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dxf.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes/application-vnd.%{developer}.%{name}.dxf.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dxf.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes/application-vnd.%{developer}.%{name}.dxf.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwt.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes/application-vnd.%{developer}.%{name}.dwt.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwt.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes/application-vnd.%{developer}.%{name}.dwt.png
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{developer}-%{name}.png %{buildroot}%{_datadir}/pixmaps/%{developer}-%{name}.png

# Remove unused resources:
pushd %{buildroot}
rm -rf %{buildroot}/opt/dassault-systemes/DraftSight/Resources
popd

# Install udev rule (prepare for dongle):
if [ %{_sysconfdir}/udev/rules.d/ ]; then
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/udev/rules.d/ft-rockey.rules
fi

# Fix RPATH errors:
%if 0%{?fix_rpath_errors}
    for BROKEN_RPATH_FILES in \
        %{buildroot}/opt/dassault-systemes/DraftSight/Linux/RecentDocumentBrowser.tx \
        %{buildroot}/opt/dassault-systemes/DraftSight/Linux/dsHttpApiService \
        %{buildroot}/opt/dassault-systemes/DraftSight/Linux/dsHttpApiController \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltbar.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libK2CrashReportSendService.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfjbg.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libK2TaskPane.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfjls.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltdic.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libK2AVCommand.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfcmp.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltimgutl.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfjxr.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfj2k.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lffax.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltfil.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltimgefx.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfbmp.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libdsJServerAddin.so.1 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltimgclr.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltkrn.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfpng.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfgif.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libExtCommands.so.1 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltimgcor.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/libltdis.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfpsd.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lfjb2.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/Libraries/lftif.so.18.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsInterface.so.1 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsInterface.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsLibrary.so.1.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsInterface.so \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsLibrary.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsInterface.so.1.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsLibrary.so \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/lib/cpp/libdsLibrary.so.1 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/Windows/_lib/release64/libWindows.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/DockWidget/_lib/release64/libDockWidget.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/DictionaryXDataDemo/_lib/release64/libDictionaryXDataDemo.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/DrawingToImage/_lib/release64/libDrawingToImage.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/EntityPreviewDemo/_lib/release64/libEntityPreviewDemo.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/ContextMenu/_lib/release64/libContextMenu.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/DrawTableCommand/_lib/release64/libDrawTableCommand.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/MyPrint/_lib/release64/libMyPrint.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/DrawCircleCommand/_lib/release64/libDrawCircleCommand.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/Reactors/_lib/release64/libReactors.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/Selection/_lib/release64/libSelection.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Simple/Menu/_lib/release64/libMenu.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Complex/BlockLibraryManager/_lib/release64/libBlockLibraryManager.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Complex/Lisp/_lib/release64/libLispSample.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Complex/BlockCustomData/_lib/release64/libBlockCustomData.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Complex/PropertyWidgets/_lib/release64/libPropertyWidgets.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Complex/PostEvent/_lib/release64/libPostEvent.so.1.0.0 \
        %{buildroot}/opt/dassault-systemes/DraftSight/APISDK/Samples/C++/Complex/BlockTrackerDemo/_lib/release64/libBlockTrackerDemo.so.1.0.0; do
            if [ ! -w ${BROKEN_RPATH_FILES} ]; then
                chmod +w ${BROKEN_RPATH_FILES}
                chrpath --delete ${BROKEN_RPATH_FILES}
                chmod -w ${BROKEN_RPATH_FILES}
            else
                chrpath --delete ${BROKEN_RPATH_FILES}
            fi
        done
%endif

# Workaround the RPATH errors:
# export QA_RPATHS=$[ 0x0004|0x0010 ]

# Install appstream data
%if 0%{?fedora} >= 20
    mkdir -p %{buildroot}%{_datadir}/appdata
    install -pm 644 %{SOURCE7} %{buildroot}%{_datadir}/appdata/%{developer}-%{name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{developer}-%{name}.appdata.xml
%endif

%post
if [ -x /usr/bin/touch ]; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{_datadir}/icons/gnome &> /dev/null || :
fi

if [ -x /usr/bin/update-desktop-database ]; then
/usr/bin/update-desktop-database %{_datadir}/applications/ &> /dev/null || :
fi

if [ -x /usr/bin/update-mime-database ]; then
/usr/bin/update-mime-database %{_datadir}/mime/ &> /dev/null || :
fi

if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &> /dev/null || :
fi

if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/gnome &> /dev/null || :
fi

%postun
if [ -x /usr/bin/touch ]; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{_datadir}/icons/gnome &> /dev/null || :
fi

if [ -x /usr/bin/update-desktop-database ]; then
/usr/bin/update-desktop-database %{_datadir}/applications/ &> /dev/null || :
fi

if [ -x /usr/bin/update-mime-database ]; then
/usr/bin/update-mime-database %{_datadir}/mime/ &> /dev/null || :
fi

if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &> /dev/null || :
fi

if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/gnome &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%clean
rm -rf %{buildroot}

%files
/opt/dassault-systemes
%{_bindir}/%{name}
%{_datadir}/Dassault*
%{_datadir}/applications/%{developer}-%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/16x16/mimetypes/*.png
%{_datadir}/icons/gnome/16x16/apps/*.png
%{_datadir}/icons/gnome/16x16/mimetypes/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/icons/gnome/32x32/apps/*.png
%{_datadir}/icons/gnome/32x32/mimetypes/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/48x48/mimetypes/*.png
%{_datadir}/icons/gnome/48x48/apps/*.png
%{_datadir}/icons/gnome/48x48/mimetypes/*.png
%{_datadir}/icons/hicolor/64x64/apps/*.png
%{_datadir}/icons/hicolor/64x64/mimetypes/*.png
%{_datadir}/icons/gnome/64x64/apps/*.png
%{_datadir}/icons/gnome/64x64/mimetypes/*.png
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/128x128/mimetypes/*.png
%{_datadir}/icons/gnome/128x128/apps/*.png
%{_datadir}/icons/gnome/128x128/mimetypes/*.png
%{_datadir}/pixmaps/%{developer}-%{name}.png
%{_datadir}/mime/packages/*.xml
%{_localstatedir}/opt/dassault-systemes
%config %{_sysconfdir}/udev/rules.d/ft-rockey.rules
%if 0%{?fedora} >= 20
%{_datadir}/appdata/%{developer}-%{name}.appdata.xml
%endif

%changelog
* Thu May 18 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2017.2.0.3085-1.1.R
- update to 2017SP02

* Mon Jan 02 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2017.0.0.1197-1.1.R
- update to 2017SP0

* Fri Jul 08 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2016.3.0.4050-1.1.R
- update to 2016SP2

* Sun Apr 17 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2016.2.0.3034-1.1.R
- update to 2016SP1

* Sun Feb 28 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2016.1.0.2021-1.3.R
- remove Requires: config(draftsight)

* Sun Feb 28 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2016.1.0.2021-1.2.R
- add BR: libappstream-glib

* Sat Feb 27 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2016.1.0.2021-1.1.R
- update to 2016SP0
- add *.appdata.xml for Fedora >=20
- clean up spec file

* Wed Sep 09 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2015.3.0.3020-1.2.R
- update to V1R6.3-2

* Sun Aug 23 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2015.3.0.3020-1.1.R
- update to V1R6.3-1

* Tue Jun 23 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2015.3.0.3019-1.1.R
- update to V1R6.3

* Tue Apr 07 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2015.2.0.2052-1.1.R
- update to V1R6.2

* Mon Feb 09 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2015.1.0.60-1.1.R
- update to V1R6.1

* Thu Oct 23 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.7.495-1.1.R
- fix mime-types and *.desktop file
- create launch script

* Mon Oct 20 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
- update to V1R6.0: migrated to Qt5; DraftSight for GNU/Linux is x86_64 only now!

* Sun Aug 24 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.5.60-2.3.1.R
- bump version for RFR20

* Sun Aug 24 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.5.60-2.3.R
- ft-rockey.rules (udev rule) is created at <install> section now, not at <post> section
- remove <preun> section

* Fri Aug 22 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.5.60-2.2.R
- hot fix: DraftSight doesn't open files with spaces in names
- remove wrapper script <SOURCE0>

* Fri Aug 22 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.5.60-2.1.R
- update to V1R5.2
- replace old wrapper script with new one (pushd into DraftSight working directory
  is required now); see https://swym.3ds.com/#post:31853
  "767690 The file name saved with Russian characters shows error when opening it"

* Tue Aug 12 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2014.3.70-2.2.R
- remove some unnecessary <Provides>

* Sun Jul 06 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.1.R
- add a wrapper script for the workaround a bug with non-latin characters

* Sat Jul 05 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
- fix missing mime-types
- fix missing genltshp.shx
- fix <preun>

* Fri Jul 04 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
#- fix missing mime-types #2 (POOR ATTEMPT!)
- change version numbering
- clean up spec file

* Wed Jul 02 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.4
#- fix missing mime-types #1 (POOR ATTEMPT!)
- add some dependences
- clean up spec file

* Mon Jun 30 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.3
- remove some useless <Provides> strings
- clean up spec file

* Sun Jun 29 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.2
- remove the most <Requires> strings
- add dependence on libaudio.so.2
- clean up spec file

* Sun Jun 01 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.1
- initial build for Fedora
