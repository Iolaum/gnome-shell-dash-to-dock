%global extdir		%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global giturl		https://github.com/micheleg/dash-to-dock


Name:		gnome-shell-extension-dash-to-dock
Version:	61
Release:	2%{?dist}
Summary:	Dock for the Gnome Shell by micxgx.gmail.com

License:	GPLv2+
URL:		https://micheleg.github.io/dash-to-dock
Source0:	%{giturl}/archive/extensions.gnome.org-v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	%{_bindir}/glib-compile-schemas

Requires:	gnome-shell-extension-common

%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications
and a faster switching between windows and desktops without having
to leave the desktop view.


%prep
%autosetup -n dash-to-dock-extensions.gnome.org-v%{version} -p 1


%build
%make_build


%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name


# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
	%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi


%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 61-1
- Initial import (rhbz#1520149)

* Fri Dec 01 2017 Björn Esser <besser82@fedoraproject.org> - 61-0.1
- Initial rpm release (rhbz#1520149)
