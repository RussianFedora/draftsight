%define __os_install_post %{nil}
%define debug_package %{nil}
%define dsver V1R5.1

Summary:	Professional CAD system: supported file formats are DWT, DXF and DWG
Name:		draftsight
Version:	2014.3.70
Release:	2.1%{?dist}

License:	Standalone license, activation required
URL:		http://www.3ds.com/products-services/draftsight/download-draftsight
Source0:	http://dl-ak.solidworks.com/nonsecure/draftsight/%{dsver}/draftSight.rpm
Source1:	001-fix-mime-types.patch

BuildRequires:	desktop-file-utils

Requires:	libaudio.so.2
Requires:	libGLU.so.1
Requires:	xdg-utils
Requires:	gnome-icon-theme

Provides:	lfbmp.so.18  
Provides:	lfcmp.so.18  
Provides:	lffax.so.18  
Provides:	lfgif.so.18  
Provides:	lfj2k.so.18  
Provides:	lfjb2.so.18  
Provides:	lfjbg.so.18  
Provides:	lfjls.so.18  
Provides:	lfjxr.so.18  
Provides:	lfpng.so.18  
Provides:	lfpsd.so.18  
Provides:	lftif.so.18  
Provides:	libAcDgnLS.so.1  
Provides:	libAecArchBase.so.1  
Provides:	libAecArchDACHBase.so.1  
Provides:	libAecAreaCalculationBase.so.1  
Provides:	libAecBase.so.1  
Provides:	libAecGeometry.so.1  
Provides:	libAecSchedule.so.1  
Provides:	libAecScheduleData.so.1  
Provides:	libAecStructureBase.so.1  
Provides:	libDDKERNEL.so.1  
Provides:	libDGNImport.so.1  
Provides:	libDwfCore.so.1  
Provides:	libDwfToolkit.so.1  
Provides:	libExtCommands.so.1  
Provides:	libFXCommands.so.1  
Provides:	libFXCommandsBase.so.1  
Provides:	libFXCrashRpt.so.1  
Provides:	libFXCurves.so.1  
Provides:	libFXDimCommands.so.1  
Provides:	libFXEvalWatcher.so.1  
Provides:	libFXExport.so.1  
Provides:	libFXGripPoints.so.1  
Provides:	libFXLISP.so.1  
Provides:	libFXProperties.so.1  
Provides:	libFXRenderBase.so.1  
Provides:	libFxCharMap.so.1  
Provides:	libFxDesignResources.so.1  
Provides:	libFxFileDialogs.so.1  
Provides:	libFxImages.so.1  
Provides:	libFxQtImagePlugin.so.1  
Provides:	libFxStandards.so.1  
Provides:	libGestureWidget.so.1  
Provides:	libModelerGeometry.so.1  
Provides:	libOdQtOpenGL.so.1  
Provides:	libPSToolkit.so.1  
Provides:	libPlotStyleServices.so.1  
Provides:	libQtCLucene.so.4  
Provides:	libQtCore.so.4  
Provides:	libQtDBus.so.4  
Provides:	libQtGui.so.4  
Provides:	libQtHelp.so.4  
Provides:	libQtMultimedia.so.4  
Provides:	libQtNetwork.so.4  
Provides:	libQtOpenGL.so.4  
Provides:	libQtSql.so.4  
Provides:	libQtSvg.so.4  
Provides:	libQtWebKit.so.4  
Provides:	libQtXml.so.4  
Provides:	libQtXmlPatterns.so.4  
Provides:	libRasterProcessor.so.1  
Provides:	libRecomputeDimBlock.so.1  
Provides:	libRxRasterServices.so.1  
Provides:	libTD_AcisBuilder.so.1  
Provides:	libTD_Alloc.so.1  
Provides:	libTD_Ave.so.1  
Provides:	libTD_Br.so.1  
Provides:	libTD_BrepRenderer.so.1  
Provides:	libTD_Db.so.1  
Provides:	libTD_DbRoot.so.1  
Provides:	libTD_DgnImport.so.1  
Provides:	libTD_DgnUnderlay.so.1  
Provides:	libTD_Dwf7Export.so.1  
Provides:	libTD_Dwf7Import.so.1  
Provides:	libTD_DynBlocks.so.1  
Provides:	libTD_FtFontEngine.so.1  
Provides:	libTD_Ge.so.1  
Provides:	libTD_Gi.so.1  
Provides:	libTD_Gs.so.1  
Provides:	libTD_PDFToolkit.so.1  
Provides:	libTD_PdfExport.so.1  
Provides:	libTD_Root.so.1  
Provides:	libTD_STLExport.so.1  
Provides:	libTD_SpatialIndex.so.1  
Provides:	libTD_SvgExport.so.1  
Provides:	libTG_Db.so.1  
Provides:	libTG_Dgn7IO.so.1  
Provides:	libTG_ModelerGeometry.so.1  
Provides:	libW3dTk.so.1  
Provides:	libWhipTk.so.1  
Provides:	libfreetype.so.6  
Provides:	libfxsisl.so.1  
Provides:	libltfil.so.18  
Provides:	libltkrn.so.18  
Provides:	libphonon.so.4  
Provides:	libqcncodecs.so  
Provides:	libqgif.so  
Provides:	libqico.so  
Provides:	libqjpcodecs.so  
Provides:	libqjpeg.so  
Provides:	libqkrcodecs.so  
Provides:	libqmng.so  
Provides:	libqsqlite.so  
Provides:	libqsvg.so  
Provides:	libqtiff.so  
Provides:	libqtwcodecs.so  

ExclusiveArch:	i686

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

# Remove broken link:
rm %{buildroot}/opt/dassault-systemes/DraftSight/Linux/K2GestureWidget.tx

# Fix *.desktop file and mime-types:
patch -p1 < %{SOURCE1}

# Move *.desktop file to %{_datadir}:
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/dassault-systemes_draftsight.desktop %{buildroot}%{_datadir}/applications/dassault-systemes_draftsight.desktop

# Install mime-types:
mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/dassault-systemes_draftsight-dwg.xml %{buildroot}%{_datadir}/mime/packages/dassault-systemes_draftsight.xml
popd

# Create the link at %{_bindir} pointing to the executable binary: 
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s ../../../opt/dassault-systemes/DraftSight/Linux/DraftSight draftsight
popd

# Install pixmaps:
for SIZE in 16 32 48 64 128; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes
  mkdir -p %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/apps
  mkdir -p %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/dassault-systemes_draftsight.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes/dassault-systemes_draftsight.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/apps/dassault-systemes_draftsight.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes/dassault-systemes_draftsight.png
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/dassault-systemes_draftsight.png %{buildroot}%{_datadir}/pixmaps/dassault-systemes_draftsight.png

pushd %{buildroot}
rm -rf %{buildroot}/opt/dassault-systemes/DraftSight/Resources
popd

%post
# Prepare for dongle:
if [ /etc/udev/rules.d/ ]; then
  echo "BUS==\"usb\", SYSFS{idVendor}==\"096e\", MODE==\"0666\"" > /etc/udev/rules.d/ft-rockey.rules
fi

if [ -x /usr/bin/touch ]; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{_datadir}/icons/gnome &> /dev/null || :
fi

#if [ -x "`which update-menus 2>/dev/null`" ]; then
#  update-menus || :
#fi

if [ -x /usr/bin/update-desktop-database ]; then
/usr/bin/update-desktop-database %{_datadir}/applications/ || :
#&> /dev/null || :
fi

if [ -x /usr/bin/update-mime-database ]; then
/usr/bin/update-mime-database %{_datadir}/mime/ || :
#&> /dev/null || :
fi

if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &> /dev/null || :
fi

if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/gnome &> /dev/null || :
fi

%preun
# Remove dongle preparing:
[ /etc/udev/rules.d/ ] && rm /etc/udev/rules.d/ft-rockey.rules

%postun
if [ -x /usr/bin/touch ]; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{_datadir}/icons/gnome &> /dev/null || :
fi

#if [ -x "`which update-menus 2>/dev/null`" ]; then
#  update-menus || :
#fi

if [ -x /usr/bin/update-desktop-database ]; then
/usr/bin/update-desktop-database %{_datadir}/applications/ || :
#&> /dev/null || :
fi

if [ -x /usr/bin/update-mime-database ]; then
/usr/bin/update-mime-database %{_datadir}/mime/ || :
#&> /dev/null || :
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
%{_bindir}/draftsight
%{_datadir}/applications/dassault-systemes_draftsight.desktop
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
%{_datadir}/pixmaps/dassault-systemes_draftsight.png
%{_datadir}/mime/packages/dassault-systemes_draftsight.xml
%{_localstatedir}/opt/dassault-systemes

%changelog
* Fri Jul 04 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.1.R
- fix missing mime-types
- change version numbering
- clean up spec file

* Wed Jul 02 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.4
#- fix missing mime-types (POOR ATTEMPT!)
- add some dependences
- clean up spec file

* Mon Jun 30 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.3
- remove some useless "Provides" strings
- clean up spec file

* Sun Jun 29 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.2
- remove the most "Requires" strings
- add dependence on libaudio.so.2
- clean up spec file

* Sun Jun 01 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.1
- initial build for Fedora