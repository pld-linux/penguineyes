Summary:	You are watched!
Summary(pl):	Jeste¶ obserwowany!
Name:		penguineyes
Version:	0.10
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://ftp.debian.org/debian/pool/main/p/penguineyes/%{name}_%{version}.orig.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-bilgejc.tar.gz
Patch0:		%{name}-time.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	imlib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
aclocal
%{__autoconf}
automake -a -f
%{configure} \
	--disable-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Amusements}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install bilgejc* $RPM_BUILD_ROOT%{_datadir}/penguineyes/Default
cat penguineyesrc >> $RPM_BUILD_ROOT%{_datadir}/penguineyes/Config/penguineyesrc

gzip -9nf NEWS README TODO THEMES

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install penguinize.png $RPM_BUILD_ROOT%{_pixmapsdir}/penguineyes.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/penguineyes
%{_pixmapsdir}/*
%{_applnkdir}/Amusements/*
