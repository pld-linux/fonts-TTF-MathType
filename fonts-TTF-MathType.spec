Summary:	MathType Fonts
Name:		fonts-TTF-MathType
Version:	1.0
Release:	1
License:	looks like free
Group:		Fonts
Source0:	http://www.dessci.com/en/dl/MathTypeTrueTypeFonts.asp
# Source0-md5:	f3522c4ca9b4be08252848c1933d021e
URL:		http://www.dessci.com/en/dl/fonts/
BuildRequires:	cabextract
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         ttffontsdir     %{_fontsdir}/TTF

%description

%prep
%setup -qcT
cabextract %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}
cp -a *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/*.ttf
