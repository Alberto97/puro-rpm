%global debug_package %{nil}
%define _build_id_links none
%define __os_install_post %{nil}

Name:           puro
Version:        1.2.6
Release:        1%{?dist}
Summary:        Puro is a powerful tool for installing and upgrading Flutter versions

License:        BSD
URL:            https://puro.dev/

Source0:        https://github.com/PixelToast/puro/archive/refs/tags/%{version}.zip

BuildRequires:  dart

%description
Puro is a powerful tool for installing and upgrading Flutter versions, it is essential for developers that work on multiple projects or have slower internet.

%prep
%autosetup -p1

%build
cd puro
dart pub get
dart compile exe bin/puro.dart -o bin/puro "--define=puro_version=%{version}"
cd ..

%install
install -dp %{buildroot}%{_bindir}
install -Dm 0755 puro/bin/puro %{buildroot}%{_bindir}


%files
%license puro/LICENSE
%{_bindir}/puro

%changelog
* Wed May 17 2023 Alberto Pedron <albertop2197@gmail.com> - 1.2.5-2
- v1.2.6

* Sun Apr 30 2023 Alberto Pedron <albertop2197@gmail.com> - 1.2.5-1
- Initial release