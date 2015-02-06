Summary: 	Displays a live list of active connections and what files are being transferred
Name: 		pktstat
Version:	1.8.5
Release:	2
Group: 		Monitoring
Url:		http://www.adaptive-enterprises.com.au/~d/software/pktstat/
License: 	BSD
Source0: 	http://www.adaptive-enterprises.com.au/~d/software/pktstat/%{name}-%{version}.tar.gz
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
%configure2_5x
%make

%install
%makeinstall

%files
%doc COPYING NEWS README
%{_bindir}/pktstat
%{_mandir}/man1/pktstat*


%changelog
* Mon Mar 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.8.5-1
+ Revision: 782176
- version update  1.8.5

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.4-7mdv2011.0
+ Revision: 614562
- the mass rebuild of 2010.1 packages

* Tue Feb 09 2010 Antoine Ginies <aginies@mandriva.com> 1.8.4-6mdv2010.1
+ Revision: 502741
- fix format string pb

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.4-5mdv2009.1
+ Revision: 298350
- rebuilt against libpcap-1.0.0

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.8.4-4mdv2009.0
+ Revision: 259081
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.8.4-3mdv2009.0
+ Revision: 246990
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.4-1mdv2008.1
+ Revision: 111154
- update to new version 1.8.4

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 1.8.3-1mdv2008.0
+ Revision: 29467
- add ncurses-devel buildrequires
- release 1.8.3
- Import pktstat

