Summary:	Application allowing to "stick little notes" on desktop
Summary(pl.UTF-8):	Aplikacja pozwalająca przyklejać małe notatki na pulpicie
Name:		Affiche
Version:	0.6.0
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://www.collaboration-world.com/affiche.data/releases/Stable/%{name}-%{version}.tar.gz
# Source0-md5:	6c7ad52544579594b20ca7c86954042e
URL:		http://www.collaboration-world.com/affiche/
BuildRequires:	gnustep-gui-devel
Requires:	gnustep-gui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Affiche is a little application that allows people to 'stick little
notes' on your desktop.

%description -l pl.UTF-8
Affiche to mała aplikacja pozwalająca użytkownikom przyklejać małe
notatki na pulpicie.

%prep
%setup -q -n %{name}

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	DESTDIR=$RPM_BUILD_ROOT 

for f in Affiche ; do
	ln -sf %{_libdir}/GNUstep/Applications/$f.app/$f $RPM_BUILD_ROOT/%{_bindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/GNUstep/Applications/Affiche.app
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Affiche.app/Affiche
%dir %{_libdir}/GNUstep/Applications/Affiche.app/Resources
%{_libdir}/GNUstep/Applications/Affiche.app/Resources/*.desktop
%{_libdir}/GNUstep/Applications/Affiche.app/Resources/*.plist
%{_libdir}/GNUstep/Applications/Affiche.app/Resources/*.tiff
%{_libdir}/GNUstep/Applications/Affiche.app/Resources/English.lproj
%lang(fr) %{_libdir}/GNUstep/Applications/Affiche.app/Resources/French.lproj
%lang(de) %{_libdir}/GNUstep/Applications/Affiche.app/Resources/German.lproj
# ISO-639-2 (not in 639-1)
%lang(art-lojban) %{_libdir}/GNUstep/Applications/Affiche.app/Resources/Lojban.lproj
%lang(es) %{_libdir}/GNUstep/Applications/Affiche.app/Resources/Spanish.lproj
%lang(sv) %{_libdir}/GNUstep/Applications/Affiche.app/Resources/Swedish.lproj
