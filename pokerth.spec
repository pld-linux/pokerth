Summary:	The Open Source Texas-Holdem Poker Engine
Summary(pl.UTF-8):	Silnik gry Texas-Holdem poker
Name:		pokerth
Version:	0.8.1
Release:	3
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/pokerth/PokerTH-%{version}-src.tar.bz2
# Source0-md5:	990b2b7dcb48028c0e963161ddea5806
URL:		http://www.pokerth.net/
BuildRequires:	QtCore-devel >= 4.3.1
BuildRequires:	QtGui-devel >= 4.3.1
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	boost-devel >= 1.37.0-3
BuildRequires:	curl-devel >= 7.16
BuildRequires:	gnutls-devel
BuildRequires:	gsasl-devel
BuildRequires:	qt4-build >= 4.3.1
BuildRequires:	qt4-qmake >= 4.3.1
BuildRequires:	zlib-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PokerTH is a poker game written in C++/QT4. You can play the popular
"Texas Hold'em" poker variant against up to six computer-opponents or
play network games with people all over the world. This poker engine
is available for Linux, Windows, and MacOSX.

%description -l pl.UTF-8
PokerTH to komputerowa gra w pokera napisana w C++/QT4. Umożliwia ona
grę w popularny wariant "Texas Hold'em" przeciwko maksymalnie sześciu
komputerowym przeciwnikom lub sieciową grę z innymi zawodnikami.
Silnik gry dostępny jest na platformy Linux, Windows oraz MacOSX.

%prep
%setup -q -n PokerTH-%{version}-src

%build
qmake-qt4 pokerth.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install pokerth bin/pokerth_server $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog TODO
%attr(755,root,root) %{_bindir}/pokerth*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/%{name}
