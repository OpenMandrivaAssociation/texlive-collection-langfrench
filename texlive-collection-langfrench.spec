Name:		texlive-collection-langfrench
Epoch:		1
Version:	63147
Release:	1
Summary:	French
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langfrench.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-aeguill
Requires:	texlive-apprends-latex
Requires:	texlive-babel-basque
Requires:	texlive-babel-french
Requires:	texlive-basque-book
Requires:	texlive-basque-date
Requires:	texlive-bib-fr
Requires:	texlive-bibleref-french
Requires:	texlive-booktabs-fr
Requires:	texlive-droit-fr
Requires:	texlive-epslatex-fr
Requires:	texlive-facture
Requires:	texlive-frenchle
Requires:	texlive-frletter
Requires:	texlive-hyphen-basque
Requires:	texlive-hyphen-french
Requires:	texlive-impatient-fr
Requires:	texlive-impnattypo
Requires:	texlive-l2tabu-french
Requires:	texlive-lshort-french
Requires:	texlive-mafr
Requires:	texlive-tabvar
Requires:	texlive-tdsfrmath
Requires:	texlive-texlive-fr
Requires:	texlive-translation-array-fr
Requires:	texlive-translation-dcolumn-fr
Requires:	texlive-translation-natbib-fr
Requires:	texlive-translation-tabbing-fr
Requires:	texlive-variations

%description
Support for French and Basque.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
