Summary:	FUSE-based file system backed by Amazon S3
Name:		s3fs-fuse
Version:	1.76
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/System
Source0:	http://github.com/s3fs-fuse/s3fs-fuse/tarball/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1f1db900f083aa0b07f66bfa8fc9063a
URL:		http://code.google.com/p/s3fs/wiki/FuseOverAmazon
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
Obsoletes:	s3fs < 1:1.75
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
s3fs is a fuse filesystem that allows you to mount an Amazon S3 bucket
as a local filesystem. It stores files natively and transparently in
S3 (i.e., you can use other programs to access the same files).
Maximum file size=5G.

s3fs is stable and is being used in number of production environments,
e.g., rsync backup to s3.

%prep
%setup -qc
mv s3fs-fuse-s3fs-fuse-*/* .
%{__rm} -r s3fs-fuse-s3fs-fuse-*

%build
%{__aclocal}
%{__autoconf}
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/s3fs.1*
