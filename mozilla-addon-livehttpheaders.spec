%define		_realname	livehttpheaders
Summary:	Show information about the HTTP headers
Summary(pl):	Pokazywanie informacji o nag³ówkach HTTP
Name:		mozilla-addon-%{_realname}
Version:	0.9
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.mozdev.org/%{_realname}/%{_realname}-%{version}.xpi
# Source0-md5:	156444d6a43d9d6ed1785e4f92f6fc9c
Source1:	%{_realname}-installed-chrome.txt
URL:		http://livehttpheaders.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _chromedir      %{_datadir}/mozilla/chrome

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
Celem tego projektu jest dodanie informacji o nag³ówkach HTTP na dwa
sposoby:

- po pierwsze przez dodanie panelu "Headers" w opcji "Poka¿ informacje
  o stronie"

- po drugie przez dodanie narzêdzia w menu "Narzêdzia->Narzêdzia
  programistyczne", umo¿liwiaj±cego wy¶wietlanie nag³ówków HTTP w
  czasie rzeczywistym (podczas ¶ci±gania stron z Internetu)

- po trzecie przez pozwolenie na edycjê nag³ówków ¿±dañ i ponowne
  otworzenie URL-a (w stadium beta). Przycisk Replay mo¿na znale¼æ w
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
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%doc $RPM_BUILD_ROOT%{_chromedir}/TODO.txt
%{_chromedir}/*
