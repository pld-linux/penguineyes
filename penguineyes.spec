Summary:	You are watched!
Summary(pl):	Jeste¶ obserwowany!
Name:		penguineyes
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Amusements
# for 0.10
#Source0:	http://ftp.debian.org/debian/pool/main/p/penguineyes/%{name}_%{version}.orig.tar.gz
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	imlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libungif-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
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
#%setup -q -n %{name}-%{version}.orig
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -f
%{configure}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Amusements}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
cp data/robopenguin.png data/tux_colour.xpm data/tux_mask.png data/tux_pupil.png $RPM_BUILD_ROOT%{_datadir}/penguineyes/Default

gzip -9nf NEWS README TODO

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/penguineyes
%{_pixmapsdir}/*
%{_applnkdir}/Amusements/*
