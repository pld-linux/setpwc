Summary:	Utility for setting parameters of PWC-based webcams
Summary(pl):	Narz�dzie do ustawiania parametr�w kamer opartych na PWC
Name:		setpwc
Version:	1.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.vanheusden.com/setpwc/%{name}-%{version}.tgz
# Source0-md5:	acc0266534c5dc13ad1153ec890c1b8d
Patch0:		%{name}-Makefile.patch
URL:		http://www.vanheusden.com/setpwc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With setpwc you can set and list various settings of Philips (and
compatible) WebCams with the 'PWC chipset'.

%description -l pl
Przy pomocy setpwc mo�na ustawia� i odczytywa� r�ne parametry kamer
internetowych Philipsa (i kompatybilnych) opartych na uk�adzie PWC.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install setpwc $RPM_BUILD_ROOT%{_bindir}
install setpwc.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/setpwc
%{_mandir}/man1/setpwc.1*
