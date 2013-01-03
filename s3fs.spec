Summary:	FUSE-based file system backed by Amazon S3
Name:		s3fs
Version:	1.61
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/System
Source0:	http://s3fs.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	0dd7b7e9b1c58312cde19894488c5072
Patch0:		%{name}-x-amz-meta.patch
Patch1:		%{name}-missing_mode.patch
Patch2:		%{name}-cache_check.patch
URL:		http://code.google.com/p/s3fs/wiki/FuseOverAmazon
BuildRequires:	curl-devel
BuildRequires:	libfuse-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
s3fs is a fuse filesystem that allows you to mount an Amazon S3 bucket
as a local filesystem. It stores files natively and transparently in
S3 (i.e., you can use other programs to access the same files).
Maximum file size=5G.

s3fs is stable and is being used in number of production environments,
e.g., rsync backup to s3.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
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
