%global extdir		%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global giturl		https://github.com/micheleg/dash-to-dock
%global commit 5658b5c2217ab3b7a036d51b62b357ea99e8fedc
%global commit_short 5658b5c
%global commit_date 20200224


Name:		gnome-shell-extension-dash-to-dock
Version:	67
Release:	4.%{commit_date}git%{commit_short}%{?dist}
Summary:	Dock for the Gnome Shell by micxgx.gmail.com

License:	GPLv2+
URL:		https://micheleg.github.io/dash-to-dock
%if 0%{?commit:1}
Source0:	%{giturl}/archive/%{commit}.tar.gz
%else
Source0:	%{giturl}/archive/extensions.gnome.org-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

# GNOME 3.36 support
# https://github.com/micheleg/dash-to-dock/pull/1097
Patch1: 0001-general-Update-to-gnome-shell-3.36-code-with-more-ac.patch
Patch2: 0002-general-Use-Clutter.ActorAlign-to-set-alignments.patch
Patch3: 0003-metadata-Set-extension-compatible-with-shell-3.36-on.patch
Patch4: 0004-utils-Use-more-ES6-compliant-code-to-override-calls.patch
Patch5: 0005-windowPreview-Only-hide-the-close-button-if-no-entry.patch
Patch6: 0006-appIcons-windowPreview-Use-vfunc-instead-of-signals.patch

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
%if 0%{?commit:1}
%autosetup -n dash-to-dock-%{commit} -p 1
%else
%autosetup -n dash-to-dock-extensions.gnome.org-v%{version} -p 1
%endif


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
* Thu Feb 27 2020 Mike DePaulo <mikedep333@gmail.com> - 67-4.20200224git5658b5c
- Add new addtl proposed patch for GNOME 3.36 compatibility (rhbz: #1794889)

* Tue Feb 25 2020 Mike DePaulo <mikedep333@gmail.com> - 67-3
- Upgrade to latest master branch
- Add proposed PR/patches for GNOME 3.36 compatibility

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Mike DePaulo <mikedep333@gmail.com> - 67-1
- Upgrade to 67 for GNOME 3.34 (f31) compatibility (rhbz#1753665)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Björn Esser <besser82@fedoraproject.org> - 66-1
- Upgrade to 66 for GNOME 3.32 (f30) compatibility (rhbz#1700690)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Mike DePaulo <mikedep333@gmail.com> - 64-1
- Upgrade to 64 for GNOME 3.30 (f29) compatibility as well as formal
  GNOME 3.28 (f28 & EPEL 7.6) compatibility. (resolves #1634447)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 61-1
- Initial import (rhbz#1520149)

* Fri Dec 01 2017 Björn Esser <besser82@fedoraproject.org> - 61-0.1
- Initial rpm release (rhbz#1520149)
