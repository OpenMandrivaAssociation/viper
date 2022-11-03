%define snapshot 20220831

Name: viper
Version: 0.9.1
Release: %{?snapshot:1.%{snapshot}.}1
Source0: https://github.com/LeFroid/Viper-Browser/archive/refs/heads/master.tar.gz
Summary: Lightweight web browser
URL: https://github.com/viper/viper
License: GPLv3
Group: Networking/WWW
BuildRequires: cmake ninja
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6QmlIntegration)
BuildRequires: cmake(Qt6QmlModels)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(xkbcommon)

%description
A powerful yet lightweight web browser built with the Qt framework

%prep
%autosetup -p1 -n Viper-Browser-master
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/viper-browser
%{_datadir}/applications/viper-browser.desktop
%{_datadir}/icons/hicolor/64x64/apps/viper-browser.png
