Summary:	FUSE-based file system backed by Amazon S3
Summary(pl.UTF-8):	Oparty na FUSE system plików wykorzystujący usługę Amazon S3
Name:		s3fs-fuse
Version:	1.80
Release:	2
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/s3fs-fuse/s3fs-fuse/releases
Source0:	https://github.com/s3fs-fuse/s3fs-fuse/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1ecb93611245a82d6f07b77ec71dfef2
URL:		https://github.com/s3fs-fuse/s3fs-fuse/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.0
BuildRequires:	libfuse-devel >= 2.8.4
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 1:2.6
# alternatively nettle >= 2.7.1+gnutls >= 2.12 or nss
BuildRequires:	openssl-devel >= 0.9
BuildRequires:	pkgconfig
Requires:	libfuse >= 2.8.4
Requires:	libxml2 >= 1:2.6
Obsoletes:	s3fs < 1:1.75
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
s3fs is a FUSE filesystem that allows you to mount an Amazon S3 bucket
as a local filesystem. It stores files natively and transparently in
S3 (i.e., you can use other programs to access the same files).
Maximum file size=5G.

s3fs is stable and is being used in number of production environments,
e.g., rsync backup to s3.

%description -l pl.UTF-8
s3fs to oparty na FUSE system plików, pozwalający na montowanie zasobu
Amazon S3 jako lokalnego systemu plików. Przechowuje pliki natywnie i
w sposób przezroczysty w S3 (czyli można używać innych programów do
dostępu do tych samych plików). Maksymalny rozmiar pliku to 5G.

s3fs jest stabilny, używany w wielu środowiskach produkcyjnych, np.
synchronizacja kopii zapasowych na s3.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/s3fs
%{_mandir}/man1/s3fs.1*
