%global debug_package %{nil}
%define _build_id_links none
%define __os_install_post %{nil}

Name:           puro
Version:        1.4.0
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
* Sun Oct 08 2023 Github Actions <github-actions@users.noreply.github.com> - 1.4.0-1
- Update Puro

* Thu Oct 05 2023 Github Actions <github-actions@users.noreply.github.com> - 1.3.8-1
- Update Puro

* Tue Sep 26 2023 Github Actions <github-actions@users.noreply.github.com> - 1.3.7-1
- Update Puro

* Sat Sep 23 2023 Github Actions <github-actions@users.noreply.github.com> - 1.3.6-1
- Update Puro

* Wed Aug 23 2023 Github Actions <github-actions@users.noreply.github.com> - 1.3.5-1
- Update Puro

* Sun Aug 06 2023 Alberto Pedron <albertop2197@gmail.com> - 1.3.4-1
- Update to v1.3.4

* Wed Jul 19 2023 Alberto Pedron <albertop2197@gmail.com> - 1.3.2-1
- Update to v1.3.2

* Sat Jun 17 2023 Alberto Pedron <albertop2197@gmail.com> - 1.3.1-1
- Update Puro

* Wed May 17 2023 Alberto Pedron <albertop2197@gmail.com> - 1.2.5-2
- v1.2.6

* Sun Apr 30 2023 Alberto Pedron <albertop2197@gmail.com> - 1.2.5-1
- Initial release
