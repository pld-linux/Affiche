Summary:	Application allowing to "stick little notes" on desktop
Summary(pl):	Aplikacja pozwalaj±ca przyklejaæ ma³e notatki na pulpicie
Name:		Affiche
Version:	0.6.0
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://www.collaboration-world.com/affiche.data/releases/Stable/%{name}-%{version}.tar.gz
# Source0-md5:	6c7ad52544579594b20ca7c86954042e
URL:		http://www.collaboration-world.com/affiche/
BuildRequires:	gnustep-gui-devel
Requires:	gnustep-gui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
Affiche is a little application that allows people to 'stick little
notes' on your desktop.

%description -l pl
Affiche to ma³a aplikacja pozwalaj±ca u¿ytkownikom przyklejaæ ma³e
notatki na pulpicie.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%dir %{_prefix}/System/Applications/Affiche.app
%attr(755,root,root) %{_prefix}/System/Applications/Affiche.app/Affiche
%dir %{_prefix}/System/Applications/Affiche.app/Resources
%{_prefix}/System/Applications/Affiche.app/Resources/*.desktop
%{_prefix}/System/Applications/Affiche.app/Resources/*.plist
%{_prefix}/System/Applications/Affiche.app/Resources/*.tiff
%{_prefix}/System/Applications/Affiche.app/Resources/English.lproj
%lang(fr) %{_prefix}/System/Applications/Affiche.app/Resources/French.lproj
%lang(de) %{_prefix}/System/Applications/Affiche.app/Resources/German.lproj
# ISO-639-2 (not in 639-1)
%lang(art-lojban) %{_prefix}/System/Applications/Affiche.app/Resources/Lojban.lproj
%lang(es) %{_prefix}/System/Applications/Affiche.app/Resources/Spanish.lproj
%lang(sv) %{_prefix}/System/Applications/Affiche.app/Resources/Swedish.lproj
%dir %{_prefix}/System/Applications/Affiche.app/%{gscpu}
%dir %{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}/%{libcombo}/Affiche
%{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
