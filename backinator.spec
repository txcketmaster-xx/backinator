Summary: Backinator Backup Program
Name: backinator
Version: 1.0.0
Release: 1
License: GPLv3
Group: System
URL: http://code.ticketmaster.com
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: perl, perl(Config::Simple)
BuildArch: noarch

%description
Backinator Backup Program

%prep
%setup -q

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0755 backinator %{buildroot}%{_bindir}/backinator
%{__install} -D -m 0640 backinator.conf %{buildroot}%{_sysconfdir}/backinator.conf

%files
%defattr(-,root,root)
%{_bindir}/backinator
%config(noreplace) %{_sysconfdir}/backinator.conf

%changelog
* Wed Jun 30 2010 Chet Burgess <cfb@liquidreality.org> 1.0.0-1
- Initial spec file
