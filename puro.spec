%define __os_install_post %{nil}

Name:           puro
Version:        1.2.5
Release:        1%{?dist}
Summary:        Puro is a powerful tool for installing and upgrading Flutter versions

License:        BSD
URL:            https://puro.dev/

Source0:        https://puro.dev/builds/%{version}/linux-x64/puro

ExclusiveArch:  x86_64

%description
Puro is a powerful tool for installing and upgrading Flutter versions, it is essential for developers that work on multiple projects or have slower internet.

%install
install -dp %{buildroot}%{_bindir}
install -Dm 0755 %{SOURCE0} %{buildroot}%{_bindir}


%files
%{_bindir}/puro

%changelog
* Sun Apr 30 2023 Alberto Pedron <albertop2197@gmail.com> - 1.2.5-1
- Initial release
