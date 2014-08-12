%define __os_install_post %{nil}
%define debug_package %{nil}
%define dsver V1R5.1

Summary:	Professional CAD system: supported file formats are DWT, DXF and DWG
Name:		draftsight
Version:	2014.3.70
Release:	2.2%{?dist}

License:	Standalone license, activation required
URL:		http://www.3ds.com/products-services/draftsight/download-draftsight
Source0:	http://dl-ak.solidworks.com/nonsecure/draftsight/%{dsver}/draftSight.rpm
Source1:	001-fix-mime-types.patch
Source2:	draftsight

BuildRequires:	desktop-file-utils

Requires:	libaudio.so.2
Requires:	libGLU.so.1
Requires:	xdg-utils
Requires:	gnome-icon-theme

Provides:   lfbmp.so.18
Provides:   lfcmp.so.18
Provides:   lffax.so.18
Provides:   lfgif.so.18
Provides:   lfj2k.so.18
Provides:   lfjb2.so.18
Provides:   lfjbg.so.18
Provides:   lfjls.so.18
Provides:   lfjxr.so.18
Provides:   lfpng.so.18
Provides:   lfpsd.so.18
Provides:   lftif.so.18
Provides:   libAcDgnLS.so.1
Provides:   libAecArchBase.so.1
Provides:   libAecArchDACHBase.so.1
Provides:   libAecAreaCalculationBase.so.1
Provides:   libAecBase.so.1
Provides:   libAecGeometry.so.1
Provides:   libAecSchedule.so.1
Provides:   libAecScheduleData.so.1
Provides:   libAecStructureBase.so.1
Provides:   libDDKERNEL.so.1
Provides:   libDGNImport.so.1
Provides:   libDwfCore.so.1
Provides:   libDwfToolkit.so.1
Provides:   libExtCommands.so.1
Provides:   libFXCommands.so.1
Provides:   libFXCommandsBase.so.1
Provides:   libFXCrashRpt.so.1
Provides:   libFXCurves.so.1
Provides:   libFXDimCommands.so.1
Provides:   libFXEvalWatcher.so.1
Provides:   libFXExport.so.1
Provides:   libFXGripPoints.so.1
Provides:   libFXLISP.so.1
Provides:   libFXProperties.so.1
Provides:   libFXRenderBase.so.1
Provides:   libFxCharMap.so.1
Provides:   libFxDesignResources.so.1
Provides:   libFxFileDialogs.so.1
Provides:   libFxImages.so.1
Provides:   libFxQtImagePlugin.so.1
Provides:   libFxStandards.so.1
Provides:   libGestureWidget.so.1
Provides:   libModelerGeometry.so.1
Provides:   libOdQtOpenGL.so.1
Provides:   libPSToolkit.so.1
Provides:   libPlotStyleServices.so.1
Provides:   libRasterProcessor.so.1
Provides:   libRecomputeDimBlock.so.1
Provides:   libRxRasterServices.so.1
Provides:   libTD_AcisBuilder.so.1
Provides:   libTD_Alloc.so.1
Provides:   libTD_Ave.so.1
Provides:   libTD_Br.so.1
Provides:   libTD_BrepRenderer.so.1
Provides:   libTD_Db.so.1
Provides:   libTD_DbRoot.so.1
Provides:   libTD_DgnImport.so.1
Provides:   libTD_DgnUnderlay.so.1
Provides:   libTD_Dwf7Export.so.1
Provides:   libTD_Dwf7Import.so.1
Provides:   libTD_DynBlocks.so.1
Provides:   libTD_FtFontEngine.so.1
Provides:   libTD_Ge.so.1
Provides:   libTD_Gi.so.1
Provides:   libTD_Gs.so.1
Provides:   libTD_PDFToolkit.so.1
Provides:   libTD_PdfExport.so.1
Provides:   libTD_Root.so.1
Provides:   libTD_STLExport.so.1
Provides:   libTD_SpatialIndex.so.1
Provides:   libTD_SvgExport.so.1
Provides:   libTG_Db.so.1
Provides:   libTG_Dgn7IO.so.1
Provides:   libTG_ModelerGeometry.so.1
Provides:   libW3dTk.so.1
Provides:   libWhipTk.so.1
Provides:   libfxsisl.so.1
Provides:   libltfil.so.18
Provides:   libltkrn.so.18

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

# Install a wrapper script for the workaround a bug with non-latin characters contained in the CAD file name and path: 
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
chmod +x %{buildroot}%{_bindir}/%{name}

# Move *.desktop file to %{_datadir}:
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/dassault-systemes_%{name}.desktop %{buildroot}%{_datadir}/applications/dassault-systemes_%{name}.desktop

# Install mime-types:
mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/dassault-systemes_%{name}-dwg.xml %{buildroot}%{_datadir}/mime/packages/dassault-systemes_%{name}-dwg.xml
mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/dassault-systemes_%{name}-dwt.xml %{buildroot}%{_datadir}/mime/packages/dassault-systemes_%{name}-dwt.xml
mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/dassault-systemes_%{name}-dxf.xml %{buildroot}%{_datadir}/mime/packages/dassault-systemes_%{name}-dxf.xml
popd

# Install pixmaps:
for SIZE in 16 32 48 64 128; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes
  mkdir -p %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/apps
  mkdir -p %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/dassault-systemes.%{name}.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/program.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/apps/dassault-systemes.%{name}.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwg.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes/application-vnd.dassault-systemes.%{name}-dwg.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwg.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes/application-vnd.dassault-systemes.%{name}-dwg.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dxf.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes/application-vnd.dassault-systemes.%{name}-dxf.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dxf.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes/application-vnd.dassault-systemes.%{name}-dxf.png
  cp %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwt.png %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/mimetypes/application-vnd.dassault-systemes.%{name}-dwt.png
  mv %{buildroot}/opt/dassault-systemes/DraftSight/Resources/pixmaps/${SIZE}x${SIZE}/file-dwt.png %{buildroot}%{_datadir}/icons/gnome/${SIZE}x${SIZE}/mimetypes/application-vnd.dassault-systemes.%{name}-dwt.png
done
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/dassault-systemes.%{name}.png %{buildroot}%{_datadir}/pixmaps/dassault-systemes.%{name}.png

# Remove unused resources:
pushd %{buildroot}
rm -rf %{buildroot}/opt/dassault-systemes/DraftSight/Resources
popd

# Fix missing genltshp.shx:
pushd %{buildroot}/opt/dassault-systemes/DraftSight/Fonts
ln -s LTypeShp.shx genltshp.shx
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

%preun
# Remove dongle preparing:
if [ /etc/udev/rules.d/ft-rockey.rules ]; then
rm /etc/udev/rules.d/ft-rockey.rules
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
%{_datadir}/applications/*.desktop
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
%{_datadir}/pixmaps/dassault-systemes.%{name}.png
%{_datadir}/mime/packages/*.xml
%{_localstatedir}/opt/dassault-systemes

%changelog
* Tue Aug 12 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2014.3.70-2.2.R
- remove some unnecessary Provides

* Sun Jul 06 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.1.R
- add a wrapper script for the workaround a bug with non-latin characters

* Sat Jul 05 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
- fix missing mime-types
- fix missing genltshp.shx
- fix %preun

* Fri Jul 04 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
#- fix missing mime-types #2 (POOR ATTEMPT!)
- change version numbering
- clean up spec file

* Wed Jul 02 2014 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 2014.3.70-2.R.4
#- fix missing mime-types #1 (POOR ATTEMPT!)
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