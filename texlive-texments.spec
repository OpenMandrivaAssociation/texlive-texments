Name:		texlive-texments
Version:	15878
Release:	2
Summary:	Using the Pygments highlighter in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texments
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texments.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texments.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texments.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package which allows to use the Pygments highlighter inside
LaTeX documents. Pygments supports syntax colouring of over 50
types of files, and ships with multiple colour schemes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texments/texments.sty
%doc %{_texmfdistdir}/doc/latex/texments/README
%doc %{_texmfdistdir}/doc/latex/texments/texments.pdf
#- source
%doc %{_texmfdistdir}/source/latex/texments/texments.dtx
%doc %{_texmfdistdir}/source/latex/texments/texments.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
