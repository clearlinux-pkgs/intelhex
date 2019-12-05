#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intelhex
Version  : 2.2.1
Release  : 5
URL      : https://github.com/bialix/intelhex/archive/2.2.1.tar.gz
Source0  : https://github.com/bialix/intelhex/archive/2.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: intelhex-bin = %{version}-%{release}
Requires: intelhex-license = %{version}-%{release}
Requires: intelhex-python = %{version}-%{release}
Requires: intelhex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Python IntelHex library
***********************
Introduction
------------
The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard
for representation of code to be programmed into microelectronic devices.

%package bin
Summary: bin components for the intelhex package.
Group: Binaries
Requires: intelhex-license = %{version}-%{release}

%description bin
bin components for the intelhex package.


%package license
Summary: license components for the intelhex package.
Group: Default

%description license
license components for the intelhex package.


%package python
Summary: python components for the intelhex package.
Group: Default
Requires: intelhex-python3 = %{version}-%{release}

%description python
python components for the intelhex package.


%package python3
Summary: python3 components for the intelhex package.
Group: Default
Requires: python3-core

%description python3
python3 components for the intelhex package.


%prep
%setup -q -n intelhex-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539723666
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intelhex
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/intelhex/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bin2hex.py
/usr/bin/hex2bin.py
/usr/bin/hex2dump.py
/usr/bin/hexdiff.py
/usr/bin/hexinfo.py
/usr/bin/hexmerge.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intelhex/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
