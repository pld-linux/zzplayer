Summary:	MPEG-I video player for KDE
Name:		zzplayer
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://www.chez.com/tsc/zzplayer/%{name}-%{version}.tar.gz
URL:		http://www.chez.com/tsc/zzplayer/zzplayer.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ZZplayer is a MPEG-I video player for the KDE environment. He is based
on SMPEG library.

%prep
%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS"
LFLAGS="-s"
export CXXFLAGS LFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
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
