# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/texments
# catalog-date 2009-01-03 10:55:55 +0100
# catalog-license lppl
# catalog-version 0.2.0
Name:		texlive-texments
Version:	0.2.0
Release:	1
Summary:	Using the Pygments highlighter in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texments
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texments.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texments.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texments.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package which allows to use the Pygments highlighter inside
LaTeX documents. Pygments supports syntax colouring of over 50
types of files, and ships with multiple colour schemes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texments/texments.sty
%doc %{_texmfdistdir}/doc/latex/texments/README
%doc %{_texmfdistdir}/doc/latex/texments/texments.pdf
#- source
%doc %{_texmfdistdir}/source/latex/texments/texments.dtx
%doc %{_texmfdistdir}/source/latex/texments/texments.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
