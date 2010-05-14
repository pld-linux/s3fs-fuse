Summary:	FUSE-based file system backed by Amazon S3
Name:		s3fs
Version:	r191
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://s3fs.googlecode.com/files/%{name}-%{version}-source.tar.gz
# Source0-md5:	59754b68a5601ddeaf66cd6460301a47
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
%setup -q -n %{name}

%build
%{__cxx} %{rpmcxxflags} %{rpmldflags} -Wall  s3fs.cpp -o s3fs \
	`pkg-config fuse --cflags --libs` `pkg-config libcurl --cflags --libs` \
	`xml2-config --cflags --libs` -lcrypto

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install s3fs $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
