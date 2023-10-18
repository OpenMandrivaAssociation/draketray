%global gb_ver %(rpm -q --qf '%%{version}' gambas-devel)

Summary:	Icon tray for dnfdrake and flatdrake
Name:		draketray
Version:	3.0.3
Release:	1
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		https://mib.pianetalinux.org
#URL:		https://github.com/astrgl/draketray
Source0:	https://github.com/astrgl/draketray/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gambas-devel
BuildRequires:	gambas-gb.dbus
BuildRequires:	gambas-gb.form
BuildRequires:	gambas-gb.form.stock
BuildRequires:	gambas-gb.gui
BuildRequires:	gambas-gb.image
BuildRequires:	gambas-gui-backend

Requires:	sudo
Requires:	createrepo_c
Requires:	dnf-utils
Requires:	gambas-runtime = %{gb_ver}
Requires:	gambas-gb.dbus = %{gb_ver}
Requires:	gambas-gb.form = %{gb_ver}
Requires:	gambas-gb.form.stock = %{gb_ver}
Requires:	gambas-gb.gui = %{gb_ver}
Requires:	gambas-gb.image = %{gb_ver}
Requires:	gambas-gui-backend = %{gb_ver}
Requires:	lsb-release
Requires:	python-dnf-plugin-versionlock
Requires:	xrandr

Suggests:	dnfdrake

BuildArch: noarch

%rename dnfdraketray
#Obsoletes:	dnfdraketray < %{version}

%description
Icon tray for dnfdrake.

%files
%license FILE-EXTRA/license
%{_bindir}/%{name}.gambas
%{_datadir}/%{name}/%{name}.desktop

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
gbc3 -e -a -g -t -f public-module -f public-control -j%{?_smp_mflags}
gba3

# unversion binary
mv %{name}-%{version}.gambas %{name}.gambas

%install
# binary
install -Dm 0755 %{name}.gambas -t %{buildroot}/%{_bindir}/

#.desktop used by dnfdrake
install -Dm 0755 FILE-EXTRA/%{name}.desktop -t %{buildroot}/%{_datadir}/%{name}/

