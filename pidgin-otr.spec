Summary:	Off-The-Record Messaging plugin for pidgin
Name:		pidgin-otr
Version:	3.2.0
Release:	1
Source0:	http://otr.cypherpunks.ca/%{name}-%{version}.tar.gz
License:	GPL
Group:		Applications/Networking
URL:		http://otr.cypherpunks.ca/
BuildRequires:	glib2-devel
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libgpg-error-devel
BuildRequires:	pidgin-devel >= 2.0.0
BuildRequires:	libotr-devel >= 3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a pidgin plugin which implements Off-the-Record (OTR)
Messaging. It is known to work (at least) under the Linux and Windows
versions of pidgin (2.x).

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

# libtool insists on creating this
rm $RPM_BUILD_ROOT%{_libdir}/pidgin/pidgin-otr.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README COPYING
%{_libdir}/pidgin/pidgin-otr.so
