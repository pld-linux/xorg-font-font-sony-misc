Summary:	Sony fixed bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe Sony o stałej szerokości
Name:		xorg-font-font-sony-misc
Version:	1.0.1
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-sony-misc-%{version}.tar.bz2
# Source0-md5:	7b6f5117814599b86ed3470de6c62aa3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.3
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
	--build=%{_host} \
	--host=%{_host} \
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
%doc COPYING ChangeLog README
%{_fontsdir}/misc/8x16*.pcf.gz
%{_fontsdir}/misc/12x24*.pcf.gz
