Name:           perl-GD
Version:        2.76
Release:        1
Summary:        A perl5 interface to Thomas Boutell's gd library
License:        GPL+ or Artistic 2.0
URL:            https://metacpan.org/release/GD
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/GD-%{version}.tar.gz

BuildRequires:  coreutils findutils gcc gd-devel make perl-devel perl-ExtUtils-PkgConfig
BuildRequires:  perl-generators perl-interpreter perl(ExtUtils::MakeMaker)

#Test
BuildRequires:  perl(Test::More) perl(lib)
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | cut -d"'" -f 2))
Requires:       gd

%{?perl_default_filter}

%description
This is a autoloadable interface module for libgd, a popular library
for creating and manipulating PNG files.  With this library you can
create PNG images on the fly or modify existing files.  Features
include:

a.  lines, polygons, rectangles and arcs, both filled and unfilled
b.  flood fills
c.  the use of arbitrary images as brushes and as tiled fill patterns
d.  line styling (dashed lines and the like)
e.  horizontal and vertical text rendering
f.  support for transparency and interlacing
g.  support for TrueType font rendering, via libfreetype.
h.  support for spline curves, via GD::Polyline
i.  support for symbolic font names, such as "helvetica:italic"
j.  support for symbolic color names, such as "green", via GD::Simple
k.  produces output in png, gif, jpeg and xbm format
l.  produces output in svg format via GD::SVG.

%package_help

%prep
%autosetup -n GD-%{version} -p1

perl -pi -e 's|/usr/local/bin/perl\b|%{__perl}|' \
      demos/{*.{pl,cgi},truetype_test}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc ChangeLog README README.QUICKDRAW demos/
%{_bindir}/bdf2gdfont.pl
%{perl_vendorarch}/GD/
%{perl_vendorarch}/auto/GD/
%{perl_vendorarch}/GD.pm

%files help
%{_mandir}/man*/*

%changelog
* Fri Apr 29 2022 hkgy <kaguyahatu@outlook.com> - 2.76-1
* Upgrade version to 2.76

* Thu Jan 28 2021 liudabo <liudabo1@huawei.com> - 2.73-1
- upgrade version to 2.73

* Thu Jul 30 2020 wenzhanli<wenzhanli2@huawei.com> - 2.72-1
- Type:NA
- ID:NA
- SUG:NA
- DESC:update version 2.72

* Mon Feb 10 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.71-1
- Package init
