%define		_realname	livehttpheaders
Summary:	Show information about the HTTP headers
Summary(pl):	Pokazywanie informacji o nag��wkach HTTP
Name:		mozilla-addon-%{_realname}
Version:	0.10
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.mozdev.org/livehttpheaders/%{_realname}-%{version}.xpi
# Source0-md5:	f86f03ed6098c4581412f312b5a18ccf
Source1:	%{_realname}-installed-chrome.txt
URL:		http://livehttpheaders.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
The goal of this project is to adds information about the HTTP headers
in two ways:

* First by adding a 'Headers' tab in 'View Page Info' of a web page.

* Second by adding a tool in the 'Tools->Web Development' menu to
  be able to display HTTP headers in real time (while pages are being
  downloaded from the Internet.

* Third by letting you edit request headers and replay an URL (beta).
  Look for the Replay button in the live window!

%description -l pl
Celem tego projektu jest dodanie informacji o nag��wkach HTTP na dwa
sposoby:

- po pierwsze przez dodanie panelu "Headers" w opcji "Poka� informacje
  o stronie"

- po drugie przez dodanie narz�dzia w menu "Narz�dzia->Narz�dzia
  programistyczne", umo�liwiaj�cego wy�wietlanie nag��wk�w HTTP w
  czasie rzeczywistym (podczas �ci�gania stron z Internetu)

- po trzecie przez pozwolenie na edycj� nag��wk�w ��da� i ponowne
  otworzenie URL-a (w stadium beta). Przycisk Replay mo�na znale�� w
  okienku.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%doc $RPM_BUILD_ROOT%{_chromedir}/TODO.txt
%{_chromedir}/*
