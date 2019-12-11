Name:		texlive-scanpages
Version:	1.05a
Release:	2
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
%{_texmfdistdir}/tex/latex/scanpages
%doc %{_texmfdistdir}/doc/latex/scanpages

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
