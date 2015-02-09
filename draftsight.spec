%define __os_install_post %{nil}
%define debug_package %{nil}
%define dsver V1R6.1
%define developer dassaultsystemes

Summary:	Professional CAD system: supported file formats are DWT, DXF and DWG
Name:		draftsight
Version:	2015.1.0.60
Release:	1.1%{?dist}

License:	Standalone license, activation required
URL:		http://www.3ds.com/products-services/%{name}/download-%{name}
Source0:	http://dl-ak.solidworks.com/nonsecure/%{name}/%{dsver}/draftSight.rpm
Source1:	%{name}
Source2:	%{developer}-%{name}.desktop
Source3:	vnd.%{developer}.%{name}.dwg.xml
Source4:	vnd.%{developer}.%{name}.dwt.xml
Source5:	vnd.%{developer}.%{name}.dxf.xml
Source6:	ft-rockey.rules

BuildRequires:	desktop-file-utils

Requires:	libaudio.so.2
Requires:	libGLU.so.1
Requires:	xdg-utils
Requires:	gnome-icon-theme

#Provides:   lfbmp.so.18
#Provides:   lfcmp.so.18
#Provides:   lffax.so.18
#Provides:   lfgif.so.18
#Provides:   lfj2k.so.18
#Provides:   lfjb2.so.18
#Provides:   lfjbg.so.18
#Provides:   lfjls.so.18
#Provides:   lfjxr.so.18
#Provides:   lfpng.so.18
#Provides:   lfpsd.so.18
#Provides:   lftif.so.18
#Provides:   libAcDgnLS.so.1
#Provides:   libAecArchBase.so.1
#Provides:   libAecArchDACHBase.so.1
#Provides:   libAecAreaCalculationBase.so.1
#Provides:   libAecBase.so.1
Provides:   libAecGeometry.so()(64bit)
#Provides:   libAecSchedule.so.1
#Provides:   libAecScheduleData.so.1
#Provides:   libAecStructureBase.so.1
Provides:   libDDKERNEL.so.1()(64bit)
Provides:   libDGNImport.so.1()(64bit)
Provides:   libDwfCore.so()(64bit)
#Provides:   libDwfToolkit.so.1
Provides:   libExtCommands.so.1()(64bit)
Provides:   libFxCharMap.so.1()(64bit)
Provides:   libFXCommands.so.1()(64bit)
Provides:   libFXCommandsBase.so.1()(64bit)
Provides:   libFXCrashRpt.so.1()(64bit)
Provides:   libFXCurves.so.1()(64bit)
Provides:   libFXDimCommands.so.1()(64bit)
Provides:   libFXEvalWatcher.so.1()(64bit)
Provides:   libFXExport.so.1()(64bit)
Provides:   libFXGripPoints.so.1()(64bit)
Provides:   libFXLISP.so.1()(64bit)
Provides:   libFXProperties.so.1()(64bit)
Provides:   libFXRenderBase.so.1()(64bit)
#Provides:   libFxCharMap.so.1
Provides:   libFxDesignResources.so.1()(64bit)
Provides:   libFxFileDialogs.so.1()(64bit)
Provides:   libFxImages.so.1()(64bit)
#Provides:   libFxQtImagePlugin.so.1
Provides:   libFxStandards.so.1()(64bit)
Provides:   libGestureWidget.so.1()(64bit)
#Provides:   libModelerGeometry.so.1
Provides:   libOdQtOpenGL.so.1()(64bit)
#Provides:   libPSToolkit.so.1
#Provides:   libPlotStyleServices.so.1
#Provides:   libRasterProcessor.so.1
#Provides:   libRecomputeDimBlock.so.1
Provides:   libRxRasterServices.so.1()(64bit)
#Provides:   libTD_AcisBuilder.so.1
Provides:   libTD_Alloc.so()(64bit)
#Provides:   libTD_Ave.so.1
#Provides:   libTD_Br.so.1
#Provides:   libTD_BrepRenderer.so.1
Provides:   libTD_Db.so()(64bit)
Provides:   libTD_DbRoot.so()(64bit)
#Provides:   libTD_DgnImport.so.1
#Provides:   libTD_DgnUnderlay.so.1
#Provides:   libTD_Dwf7Export.so.1
#Provides:   libTD_Dwf7Import.so.1
#Provides:   libTD_DynBlocks.so.1
#Provides:   libTD_FtFontEngine.so.1
Provides:   libTD_Ge.so()(64bit)
Provides:   libTD_Gi.so()(64bit)
Provides:   libTD_Gs.so()(64bit)
#Provides:   libTD_PDFToolkit.so.1
#Provides:   libTD_PdfExport.so.1
Provides:   libTD_Root.so()(64bit)
#Provides:   libTD_STLExport.so.1
#Provides:   libTD_SpatialIndex.so.1
#Provides:   libTD_SvgExport.so.1
#Provides:   libTG_Db.so.1
#Provides:   libTG_Dgn7IO.so.1
#Provides:   libTG_ModelerGeometry.so.1
#Provides:   libW3dTk.so.1
#Provides:   libWhipTk.so.1
Provides:   libdsApi.so.1()(64bit)
#Provides:   libdsApi_LIB.so.1()(64bit)
#Provides:   libdsInterface.so.1()(64bit)
#Provides:   libdsJServerAddin.so.1()(64bit)
Provides:   libdsLibrary.so.1()(64bit)
#Provides:   libfxsisl.so.1
Provides:   libicudata.so.48()(64bit)
Provides:   libicui18n.so.48()(64bit)
Provides:   libicuuc.so.48()(64bit)
Provides:   libltbar.so.18()(64bit)
Provides:   libltimgclr.so.18()(64bit)
Provides:   libltimgcor.so.18()(64bit)
Provides:   libltimgefx.so.18()(64bit)
Provides:   libltimgutl.so.18()(64bit)
Provides:   libltdic.so.18()(64bit)
Provides:   libltdis.so.18()(64bit)
Provides:   libltfil.so.18()(64bit)
Provides:   libltkrn.so.18()(64bit)

ExclusiveArch:	x86_64

%description
Free CAD software for your DWG files by Dassault Systèmes (standalone license).
DraftSight lets professional CAD users, students and educators create, edit and
view DWG files. DraftSight runs on Windows®, Mac® and Linux.

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

# Remove broken link:
rm %{buildroot}/opt/dassault-systemes/DraftSight/Linux/K2GestureWidget.tx

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

#Workaround the rpath errors:
export QA_RPATHS=$[ 0x0004|0x0010 ]

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

%changelog
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