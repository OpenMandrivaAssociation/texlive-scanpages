# revision 32673
# category Package
# catalog-ctan /macros/latex/contrib/scanpages
# catalog-date 2014-01-11 00:28:51 +0100
# catalog-license lppl1.3
# catalog-version 1.01
Name:		texlive-scanpages
Version:	1.01
Release:	4
Summary:	Support importing and embellishing scanned documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scanpages
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scanpages.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scanpages.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides support for the process of creating
documents based on pre-TeX-era material that is available as
scanned pages, only.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/scanpages/scanpages.sty
%doc %{_texmfdistdir}/doc/latex/scanpages/README
%doc %{_texmfdistdir}/doc/latex/scanpages/replicate.plist
%doc %{_texmfdistdir}/doc/latex/scanpages/replicate.py
%doc %{_texmfdistdir}/doc/latex/scanpages/scanpages-doc.pdf
%doc %{_texmfdistdir}/doc/latex/scanpages/scanpages-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
