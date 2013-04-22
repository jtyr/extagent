%define		pkgprefix extagent
%define		main_version 20130405-r1

Name:		%{pkgprefix}-daemon
Summary:	Daemon for SNMP Extension Agents
Version:	1.14
Release:	1%{?dist}
License:	GPL3
URL:		http://snmp-extagent.googlecode.com
Group:		Application/Monitoring
Source:		%{pkgprefix}-%{main_version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{main_version}-%{release}-root

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl >= 1:5.6.1
Requires:	logrotate

%description
This is a daemon which executes individual agents.


%package -n %{pkgprefix}-logparser-statuscode
Summary:	HTTP Status Code agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl

%description -n %{pkgprefix}-logparser-statuscode
This is SNMP extension agent for HTTP status code monitoring.


%package -n %{pkgprefix}-cert-expiry
Summary:	SSL certificate expiry agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl
Requires:	openssl

%description -n %{pkgprefix}-cert-expiry
This is SNMP extension agent for SSL certificate expiry monitoring.


%package -n %{pkgprefix}-sendmail-stats
Summary:	Sendmail stats agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl
Requires:	sendmail

%description -n %{pkgprefix}-sendmail-stats
This is SNMP extension agent for Sendmail stats monitoring.


%package -n %{pkgprefix}-file-size
Summary:	File size agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl

%description -n %{pkgprefix}-file-size
This is SNMP extension agent for file size monitoring.


%package -n %{pkgprefix}-javaapp-status
Summary:	Java application status agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl

%description -n %{pkgprefix}-javaapp-status
This is SNMP extension agent for Java application status monitoring.


%package -n %{pkgprefix}-javaapp-elogging
Summary:	JMX eLogging agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl
Requires:	perl-libwww-perl

%description -n %{pkgprefix}-javaapp-elogging
This is SNMP extension agent for JMX eLogging monitoring.


%package -n %{pkgprefix}-cpu-summary
Summary:	CPU summary agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl
Requires:	/usr/sbin/dmidecode

%description -n %{pkgprefix}-cpu-summary
This is SNMP extension agent for CPU summary monitoring.


%package -n %{pkgprefix}-javaapp-gc
Summary:	Java GC agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl
Requires:	perl-libwww-perl

%description -n %{pkgprefix}-javaapp-gc
This is SNMP extension agent for Java Garbage Collector monitoring.


%package -n %{pkgprefix}-mysql-status
Summary:	MySQL Status agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl
Requires:	perl-libwww-perl
Requires:	perl-DBD-MySQL

%description -n %{pkgprefix}-mysql-status
This is SNMP extension agent for MySQL status monitoring.


%package -n %{pkgprefix}-dummy-simple
Summary:	Dummy simple agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl

%description -n %{pkgprefix}-dummy-simple
This is SNMP extension agent demonstrating simple SNMP structure.


%package -n %{pkgprefix}-table-maker
Summary:	Table maker agent
Version:	1.14
Release:	1%{?dist}
Group:		Application/Monitoring
Requires:	%{pkgprefix}-daemon >= 1.14
Requires:	net-snmp-perl

%description -n %{pkgprefix}-table-maker
This is SNMP extension agent aggregates other extagents into a table.


%prep
%setup -q -n %{pkgprefix}-%{main_version}


%install
[ "%{buildroot}" != / ] && %{__rm} -rf "%{buildroot}"
%{__make} install DESTDIR=%{buildroot}
%{__chmod} -R u+w %{buildroot}/*


%clean
[ "%{buildroot}" != / ] && %{__rm} -rf "%{buildroot}"


%files
%defattr(-,root,root,-)
%doc Changes README
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/%{pkgprefix}.conf
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-daemon.conf
%config %{_sysconfdir}/sysconfig/%{pkgprefix}d
%config %{_sysconfdir}/logrotate.d/%{pkgprefix}
%config %{_sysconfdir}/init.d/%{pkgprefix}d
%{_bindir}/%{pkgprefix}d
%{_var}/log/%{pkgprefix}/%{pkgprefix}d.log

%files -n %{pkgprefix}-logparser-statuscode
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-logparser-statuscode.conf
%{_bindir}/%{pkgprefix}-logparser-statuscode

%files -n %{pkgprefix}-cert-expiry
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-cert-expiry.conf
%{_bindir}/%{pkgprefix}-cert-expiry

%files -n %{pkgprefix}-sendmail-stats
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-sendmail-stats.conf
%{_bindir}/%{pkgprefix}-sendmail-stats

%files -n %{pkgprefix}-file-size
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-file-size.conf
%{_bindir}/%{pkgprefix}-file-size

%files -n %{pkgprefix}-javaapp-status
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-javaapp-status.conf
%{_bindir}/%{pkgprefix}-javaapp-status

%files -n %{pkgprefix}-javaapp-elogging
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-javaapp-elogging.conf
%{_bindir}/%{pkgprefix}-javaapp-elogging

%files -n %{pkgprefix}-cpu-summary
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-cpu-summary.conf
%{_bindir}/%{pkgprefix}-cpu-summary

%files -n %{pkgprefix}-javaapp-gc
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-javaapp-gc.conf
%{_bindir}/%{pkgprefix}-javaapp-gc

%files -n %{pkgprefix}-mysql-status
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-mysql-status.conf
%{_bindir}/%{pkgprefix}-mysql-status

%files -n %{pkgprefix}-dummy-simple
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-dummy-simple.conf
%{_bindir}/%{pkgprefix}-dummy-simple

%files -n %{pkgprefix}-table-maker
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{pkgprefix}/default/%{pkgprefix}-table-maker.conf
%{_bindir}/%{pkgprefix}-table-maker


%changelog
* Wed Apr 3 2013 Jiri Tyr <jiri.tyr at gmail.com>
- Replacing underscroles by hyphens.

* Tue Apr 2 2013 Jiri Tyr <jiri.tyr at gmail.com>
- Added version for each extagent.

* Thu Mar 14 2013 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-table-maker package.

* Mon Mar 11 2013 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-dummy-simple package.

* Thu Sep 13 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added noreplace to the config macro for all extagent config files.

* Wed Aug 22 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-mysql-status package.

* Mon Jun 18 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-javaapp-gc package.

* Tue May 29 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-cpu-summary package.

* Wed Mar 21 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-javaapp-elogging package.

* Wed Feb 29 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-javaapp-status package.

* Tue Feb 28 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-sendmail-stats and extagent-file-size package.

* Mon Feb 27 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added dist variable into the release number.

* Mon Feb 27 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added dist variable into the release number.

* Mon Feb 24 2012 Jiri Tyr <jiri.tyr at gmail.com>
- Added extagent-cert-expiry package.

* Wed Feb 15 2012 Jiri Tyr <jiri.tyr at gmail.com>
- First build.
