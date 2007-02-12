Summary:	MPEG-I video player for KDE
Summary(pl.UTF-8):	Odtwarzacz wideo MPEG-I dla KDE
Name:		zzplayer
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/zzplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	27403fb96630b4ab42cc9fad66604b4b
URL:		http://zzplayer.sourceforge.net/
BuildRequires:	smpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
ZZplayer is a MPEG-I video player for the KDE environment. He is based
on SMPEG library.

%description -l pl.UTF-8
ZZplayer jest odtwarzaczem MPEG-1 dla KDE. Jest oparty na bibliotece SMPEG.

%prep
%setup -q -n ZZplayer-%{version}

%build
CXXFLAGS="%{rpmcflags}"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{name}
echo "%docdir $KDEDIR/doc/kde" >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
%defattr(644,root,root,755)
