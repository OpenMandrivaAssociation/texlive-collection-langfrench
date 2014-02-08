# revision 27049
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langfrench
Epoch:		1
Version:	20120810
Release:	2
Summary:	French
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langfrench.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-aeguill
Requires:	texlive-basque-book
Requires:	texlive-basque-date
Requires:	texlive-bib-fr
Requires:	texlive-bibleref-french
Requires:	texlive-booktabs-fr
Requires:	texlive-droit-fr
Requires:	texlive-facture
Requires:	texlive-frenchle
Requires:	texlive-frletter
Requires:	texlive-impnattypo
Requires:	texlive-mafr
Requires:	texlive-tabvar
Requires:	texlive-tdsfrmath
Requires:	texlive-variations
Requires:	texlive-hyphen-basque
Requires:	texlive-hyphen-french
Requires:	texlive-collection-basic

%description
Support for typesetting French and Basque.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813925
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780407
- Update to latest release.
- Import texlive-collection-langfrench
- Import texlive-collection-langfrench

