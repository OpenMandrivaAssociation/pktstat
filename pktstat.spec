Summary: 	Displays a live list of active connections and what files are being transferred
Name: 		pktstat
Version:	1.8.4
Release:	%mkrel 5
Group: 		Monitoring
Url:		http://www.adaptive-enterprises.com.au/~d/software/pktstat/
License: 	BSD
Source: 	http://www.adaptive-enterprises.com.au/~d/software/pktstat/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libpcap-devel ncurses-devel

%description
Display a real-time list of active connections seen on a network interface, 
and how much bandwidth is being used by what. Partially decodes HTTP and FTP
protocols to show what filename is being transferred. X11 application names 
are also shown. Entries hang around on the screen for a few seconds so you
can see what just happened. Also accepts filter expressions.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_bindir}/pktstat
%{_mandir}/man1/pktstat*
