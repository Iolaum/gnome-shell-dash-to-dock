%global extdir		%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global giturl		https://github.com/micheleg/dash-to-dock
%global commit 70f1db83cf6a4e83c26e6ec8b89f9a8477905406
%global commit_short 70f1db8
%global commit_date 20200323


Name:		gnome-shell-extension-dash-to-dock
Version:	67
Release:	6.%{commit_date}git%{commit_short}%{?dist}
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
Patch3: 0003-docking-Ensure-that-all-the-slider-children-are-prop.patch
Patch4: 0004-dash-Use-clutter-alignment-to-ensure-we-properly-arr.patch
Patch5: 0005-dash-Properly-respect-RTL-layout-applying-the-right-.patch
Patch6: 0006-metadata-Set-extension-compatible-with-shell-3.36-on.patch
Patch7: 0007-utils-Use-more-ES6-compliant-code-to-override-calls.patch
Patch8: 0008-windowPreview-Only-hide-the-close-button-if-no-entry.patch
Patch9: 0009-appIcons-windowPreview-Use-vfunc-instead-of-signals.patch
Patch10: 0010-docking-Remove-unused-value.patch
Patch11: 0011-dash-docking-Don-t-use-the-_delegate-pattern.patch
Patch12: 0012-dash-Reuse-as-much-as-possible-upstream-code.patch
Patch13: 0013-appIconIndicators-Make-the-count-badge-text-size-rel.patch
Patch14: 0014-dash-Sync-some-more-to-the-upstream-cleanups.patch
Patch15: 0015-docking-Properly-replace-default-dash-in-all-modes.patch
Patch16: 0016-docking-Don-t-sync-overview-s-iconSize-anymore.patch
Patch17: 0017-docking-Reset-old-dash-changes-if-something-changes-.patch
Patch18: 0018-docking-Cleanup-the-docks-destruction-code.patch
Patch19: 0019-docking-Use-parent-vfunc-results-to-get-slider-conta.patch
Patch20: 0020-docking-Add-mainDock-property-to-DockManager-and-use.patch
Patch21: 0021-docking-Don-t-pass-allDocks-to-every-child.patch
Patch22: 0022-docking-Ignore-key-repeat.patch
Patch23: 0023-fileManager1API-Use-a-cancellable-to-stop-proxy-crea.patch
Patch24: 0024-dash-Cleanup-preferred-width-height-vfuncs-reusing-u.patch
Patch25: 0025-dash-Get-content-box-from-the-themeNode.patch
Patch26: 0026-dash-Some-code-cleanups-to-match-Upstream-code-bette.patch
Patch27: 0027-appIcons-Redirect-events-from-the-showAppIcon-toggle.patch
Patch28: 0028-general-Don-t-use-Gtk-enum-definitions-for-St-widget.patch
Patch29: 0029-docking-Apply-the-height-width-dash-constraint-after.patch
Patch30: 0030-docking-Delay-toggling-to-group-multiple-requests.patch
Patch31: 0031-docking-Consider-theming-when-computing-the-sliderCo.patch
Patch32: 0032-docking-Reimplement-Clutter.BindConstraint-to-bind-t.patch
Patch33: 0033-docking-Replace-the-dashSpacer-instance-in-default-c.patch
Patch34: 0034-docking-Make-sure-we-don-t-send-the-overview-offscre.patch
Patch35: 0035-launcherAPI-Actually-keep-track-of-the-unity-bus-ID-.patch
Patch36: 0036-docking-Completely-replace-upstream-dash-spacer-only.patch

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
* Mon Apr 06 2020 Mike DePaulo <mikedep333@gmail.com> - 67-6.20200323git70f1db8
- Rebase to master branch as of 2020-03-23
- Use latest proposed patches (36 total) for GNOME 3.36 compatibility
  (rhbz: #1794889)

* Tue Mar 03 2020 Mike DePaulo <mikedep333@gmail.com> - 67-5.20200224git5658b5c
- Add 7 new addtl proposed patches for GNOME 3.36 compatibility (rhbz: #1794889)

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
