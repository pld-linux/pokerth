Summary:	The Open Source Texas-Holdem Poker Engine
Summary(pl.UTF-8):	Silnik gry Texas-Holdem poker
Name:		pokerth
Version:	1.1.2
Release:	10
License:	AGPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/pokerth/pokerth-%{version}.tar.gz
# Source0-md5:	8fd7d7fc7ece17315e58aa3240dd4586
Patch0:		x32.patch
Patch1:		system-qtsingleapp.patch
Patch2:		moc.patch
Patch3:		%{name}-protobuf.patch
Patch4:		%{name}-boost.patch
# from https://github.com/zaphoyd/websocketpp/pull/814/commits/c769c9238ad62178f506038178714a1c35aa2769.patch
Patch5:		%{name}-websocketpp-boost.patch
URL:		http://www.pokerth.net/
BuildRequires:	QtCore-devel >= 4.4.3
BuildRequires:	QtGui-devel >= 4.4.3
BuildRequires:	QtNetwork-devel >= 4.4.3
BuildRequires:	QtSingleApplication-devel
BuildRequires:	QtSql-devel >= 4.4.3
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	boost-devel >= 1.49
BuildRequires:	curl-devel >= 7.16
BuildRequires:	gnutls-devel
BuildRequires:	gsasl-devel >= 1.4
BuildRequires:	libircclient-devel >= 1.3
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	protobuf-devel >= 2.3.0
BuildRequires:	qt4-build >= 4.3.1
BuildRequires:	qt4-qmake >= 4.3.1
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tinyxml-devel
BuildRequires:	zlib-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PokerTH is a poker game written in C++/Qt4. You can play the popular
"Texas Hold'em" poker variant against up to six computer-opponents or
play network games with people all over the world. This poker engine
is available for Linux, Windows, and MacOS X.

%description -l pl.UTF-8
PokerTH to komputerowa gra w pokera napisana w C++/Qt4. Umożliwia ona
grę w popularny wariant "Texas Hold'em" przeciwko maksymalnie sześciu
komputerowym przeciwnikom lub sieciową grę z innymi zawodnikami.
Silnik gry dostępny jest na platformy Linux, Windows oraz MacOS X.

%prep
%setup -q -n pokerth-%{version}-rc
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%{__rm} -r src/third_party/qtsingleapplication

%build
install -d build-client build-server
cd build-server
qmake-qt4 ../pokerth.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
%{__make}

cd ../build-client
qmake-qt4 ../pokerth.pro \
	CONFIG+=client \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -C build-client install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install build-client/pokerth build-server/bin/pokerth_server $RPM_BUILD_ROOT%{_bindir}
cp -p docs/pokerth.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog TODO
%attr(755,root,root) %{_bindir}/pokerth
%attr(755,root,root) %{_bindir}/pokerth_server
%{_desktopdir}/pokerth.desktop
%{_pixmapsdir}/pokerth.png
%{_datadir}/pokerth
%{_mandir}/man1/pokerth.1*
