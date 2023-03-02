Summary:	Sony fixed bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe Sony o stałej szerokości
Name:		xorg-font-font-sony-misc
Version:	1.0.4
Release:	1
License:	MIT
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-sony-misc-%{version}.tar.xz
# Source0-md5:	ed9d0215f66b622457cd6ecef29a71ec
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sony fixed bitmap fonts in ISO-8859-1 (Latin) and JISX 0201.1976
(Japanese) encodings.

%description -l pl.UTF-8
Fonty bitmapowe Sony o stałej szerokości znaków w kodowaniach
ISO-8859-1 (łacińskim) i JISX 0201.1976 (japońskim).

%prep
%setup -q -n font-sony-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/misc/8x16*.pcf.gz
%{_fontsdir}/misc/12x24*.pcf.gz
