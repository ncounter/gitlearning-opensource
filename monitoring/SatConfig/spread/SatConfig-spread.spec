Name:         SatConfig-spread
Version:      1.1.1
Release:      1%{?dist}
Summary:      Spread configuration for Spacewalk
# This src.rpm is cannonical upstream
# You can obtain it using this set of commands
# git clone git://git.fedorahosted.org/git/spacewalk.git/
# cd monitoring/SatConfig/spread
# make srpm
URL:          https://fedorahosted.org/spacewalk
Source:	      %{name}-%{version}.tar.gz
BuildArch:    noarch
Group:        Applications/System
License:      GPLv2
Buildroot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Defines how Spacewalk spread configurations should look.

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 getSpreadConfig $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(-,root,root,-)
%{_bindir}/getSpreadConfig
%doc README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Oct 20 2008 Miroslav Suchý <msuchy@redhat.com>
- 467441 - fix namespace

* Wed Sep 24 2008 Miroslav Suchý <msuchy@redhat.com> 1.1.1-1
- spec cleanup for Fedora
