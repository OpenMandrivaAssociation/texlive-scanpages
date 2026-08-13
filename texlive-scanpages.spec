%global tl_name scanpages
%global tl_revision 42633
%global tl_version 1.05a

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Support importing and embellishing scanned documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scanpages
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scanpages.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scanpages.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The bundle provides support for the process of creating documents based
on pre-TeX-era material that is available as scanned pages, only.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from scanpages:
Map scanpages.map
TL_DROPIN_EOF
