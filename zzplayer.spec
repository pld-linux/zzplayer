# Note that this is NOT a relocatable package
%define ver      0.4
%define rel      1
%define prefix   /usr

Summary:   MPEG-I video player for KDE
Name:      ZZplayer
Version:   %ver
Release:   %rel
Copyright: GPL
Group:     X11/KDE/Multimedia
Source0:   zzplayer-%{PACKAGE_VERSION}.tar.gz
URL:       http://www.chez.com/tsc/zzplayer/zzplayer.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Packager:  Nicolas Vignal <nicolas.vignal@fnac.net>
Docdir: %{prefix}/doc

%description
ZZplayer is a MPEG-I video player for the KDE environment.
He is based on SMPEG library.

%prep
rm -rf %{builddir}

%setup
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
make

%install
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
rm -rf $RPM_BUILD_ROOT
make install-strip

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
rm -rf %{builddir}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
