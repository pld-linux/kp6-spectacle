#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.3.5
%define		qtver		5.15.2
%define		kpname		spectacle

Summary:	Spectacle
Summary(pl.UTF-8):	Spectacle
Name:		kp6-%{kpname}
Version:	6.3.5
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	d6fad602653a3cce5d97b396034d72be
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kColorPicker-qt6-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.53.0
BuildRequires:	kf6-kconfig-devel >= 5.29.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.29.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.29.0
BuildRequires:	kf6-kdeclarative-devel >= 5.29.0
BuildRequires:	kf6-kdoctools-devel >= 5.29.0
BuildRequires:	kf6-ki18n-devel >= 5.29.0
BuildRequires:	kf6-kio-devel >= 5.29.0
BuildRequires:	kf6-knewstuff-devel >= 5.29.0
BuildRequires:	kf6-knotifications-devel >= 5.29.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.29.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.29.0
BuildRequires:	kf6-kxmlgui-devel >= 5.29.0
BuildRequires:	kp6-kpipewire-devel
BuildRequires:	kp6-kwayland-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= 5.6.0
BuildRequires:	shared-mime-info
BuildRequires:	xcb-util-cursor-devel
Requires(post,postun):	desktop-file-utils
Obsoletes:	ka5-spectacle < 25.04.0
Obsoletes:	ka6-spectacle < 25.04.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spectacle is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description -l pl.UTF-8
Spectacle to prosta aplikacja do robienia zrzutów ekranu. Potrafi
przechwytywać obraz całego pulpitu lub tylko pojedynczego okna. Obrazy
mogą być następnie zapisane w wielu formatach.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spectacle
%attr(755,root,root) %{_libdir}/kconf_update_bin/spectacle-24.02.0-change_placeholder_format
%attr(755,root,root) %{_libdir}/kconf_update_bin/spectacle-24.02.0-keep_old_filename_templates
%attr(755,root,root) %{_libdir}/kconf_update_bin/spectacle-24.02.0-keep_old_save_location
%attr(755,root,root) %{_libdir}/kconf_update_bin/spectacle-24.02.0-rename_settings
%attr(755,root,root) %{_libdir}/kconf_update_bin/spectacle-24.02.0-video_format
%{_datadir}/dbus-1/services/org.kde.spectacle.service
%{_desktopdir}/org.kde.spectacle.desktop
%{_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_datadir}/kconf_update/spectacle.upd
%{_datadir}/knotifications6/spectacle.notifyrc
%{_datadir}/metainfo/org.kde.spectacle.appdata.xml
%dir %{_datadir}/kglobalaccel
%{_datadir}/kglobalaccel/org.kde.spectacle.desktop
%{_datadir}/qlogging-categories6/spectacle.categories
%{systemduserunitdir}/app-org.kde.spectacle.service
%{_mandir}/ca/man1/spectacle.1*
%{_mandir}/de/man1/spectacle.1*
%{_mandir}/es/man1/spectacle.1*
%{_mandir}/it/man1/spectacle.1*
%{_mandir}/man1/spectacle.1*
%{_mandir}/nl/man1/spectacle.1*
%{_mandir}/sl/man1/spectacle.1*
%{_mandir}/sv/man1/spectacle.1*
%{_mandir}/tr/man1/spectacle.1*
%{_mandir}/uk/man1/spectacle.1*
%{_iconsdir}/hicolor/scalable/apps/spectacle.svg
