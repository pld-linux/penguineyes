Summary:	You are watched!
Summary(pl):	Jeste¶ obserwowany!
Name:		penguineyes
Version:	0.10
Release:	3
License:	GPL
Group:		X11/Amusements
Source0:	http://ftp.debian.org/debian/pool/main/p/penguineyes/%{name}_%{version}.orig.tar.gz
# Source0-md5:	f17906b904b5e640f06427b81df53f4a
Source1:	%{name}.desktop
Source2:	%{name}-bilgejc.tar.gz
# Source2-md5:	c3c0c4a3dc68e088d76f86dad2f0abfb
Patch0:		%{name}-time.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	imlib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PenguinEyes is clone of xeyes. It shows penguin (or something else),
which will be looking at your cursor.

%description -l pl
PenguinEyes jest klonem xeyes. Pokazuje pingwina (lub co¶ innego),
który bêdzie obserwowa³ twój kursor.

%prep
%setup -q -a2 -n %{name}-%{version}.orig
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{configure} \
	--disable-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install bilgejc* $RPM_BUILD_ROOT%{_datadir}/penguineyes/Default
cat penguineyesrc >> $RPM_BUILD_ROOT%{_datadir}/penguineyes/Config/penguineyesrc

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install penguinize.png $RPM_BUILD_ROOT%{_pixmapsdir}/penguineyes.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO THEMES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/penguineyes
%{_pixmapsdir}/*
%{_desktopdir}/*
