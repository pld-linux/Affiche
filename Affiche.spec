Summary:	Application allowing to "stick little notes" on desktop
Summary(pl):	Aplikacja pozwalaj±ca przyklejaæ ma³e notatki na pulpicie
Name:		Affiche
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnustep.org/pub/gnustep/usr-apps/%{name}-%{version}.tar.gz
# Source0-md5:	5052e59981e7f1df3e8e6d995f74110c
URL:		http://www.collaboration-world.com/affiche/
BuildRequires:	gnustep-extensions-devel
BuildRequires:	gnustep-gui-devel
Requires:	gnustep-gui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
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
%dir %{_prefix}/System/Applications/Affiche.app/%{gscpu}
%dir %{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}/%{libcombo}/Affiche
%{_prefix}/System/Applications/Affiche.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
