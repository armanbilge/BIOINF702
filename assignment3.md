---
title: '[Is the protein folding problem still beyond us?]'
author: Arman Bilge
date: Friday 8 May 2015
csl: apa.csl
references:
- id: Fis09
  type: chapter
  author:
  - given: Andr\'as
    family: Fiser
  issued:
    year: 2009
  title: Comparative Protein Structure Modelling
  container-title: From Protein Structure to Function with Bioinformatics
  editor:
  - given: Daniel John
    family: Rigden
  publisher: Springer
  publisher-place: Netherlands
  page: 57--90
  DOI: 10.1007/978-1-4020-9058-5_3
- id: Her+14
  type: article-journal
  author:
  - given: Joseph L.
    family: Herman
  - given: Christopher J.
    family: Challis
  - given: \'Ad\'am
    family: Nov\'ak
  - given: Jotun
    family: Hein
  - given: Scott C.
    family: Schmidler
  issued:
    year: 2014
  title: Simultaneous Bayesian Estimation of Alignment and Phylogeny under a Joint Model of Protein Sequence and Structure
  container-title: Mol Biol Evol
  volume: 31
  issue: 9
  page: 2251--2266
  DOI: 10.1093/molbev/msu184
- id: Lup08
  type: article-journal
  author:
  - given: Andrei N.
    family: Lupas
  issued:
    year: 2008
  title: The long coming of computational structural biology
  container-title: Journal of Structural Biology
  volume: 163
  issue: 3
  page: 254--257
  DOI: 10.1016/j.jsb.2008.02.006
- id: LWZ09
  type: chapter
  author:
  - given: Jooyoung
    family: Lee
  - given: Sitao
    family: Wu
  - given: Yang
    family: Zhang
  issued:
    year: 2009
  title: "*Ab Initio* Protein Structure Prediction"
  container-title: From Protein Structure to Function with Bioinformatics
  editor:
  - given: Daniel John
    family: Rigden
  publisher: Springer
  publisher-place: Netherlands
  page: 3-25
  DOI: 10.1007/978-1-4020-9058-5_3
- id: Mou+14
  type: article-journal
  author:
  - given: John
    family: Moult
  - given: Krzysztof
    family: Fidelis
  - given: Andriy
    family: Kryshtafovych
  - given: Torsten
    family: Schwede
  - given: Anna
    family: Tramontano
  issued:
    year: 2014
  title: Critical assessment of methods of protein structure prediction (CASP) --- round x
  container-title: Proteins
  volume: 82
  issue: Suppl 2
  page: 1--6
  DOI: 10.1002/prot.24452
...

\frenchspacing

# Introduction

Proteins play a fundamental role in effectively all metabolic pathways and thus
are at the heart of molecular biology and biochemistry.
The structure of a protein is directly related to its function,
Knowledge of protein structure also has important implications for evolutionary
biology.
Specifically, because structure is conserved more strongly than molecular
sequence [@Fis09], structural information makes it possible to accurately
determine the evolutionary relationships between distantly related species
[@Her+14].
However, the technical difficulties in determining experimentally the structure
of a protein have created a rapidly growing gap between the number of sequenced
proteins and those with a known structure [@LWZ09].


@Fis09 summarised the approaches to protein structure prediction as using
either the laws of physics (*ab initio*) or the theory of evolution
(comparative, template-based methods).
However, @Lup08 emphasised that the true solution to this problem is *ab
initio* given the limited usefulness of comparative methods to make accurate
predictions, especially in the absence of substantial prior information.

The dichotomy described by @Fis09 is less clear-cut in practice: many otherwise
*ab inito* methods take advantage of knowledge in databases [@LWZ09] and
template-based methods still need physics-based energy functions for
refinement as it is impossible to make accurate predictions solely based on
homology [@Fis09].

# Concluding Remarks

It is clear that no matter what approach is taken to the protein structure
prediction problem,

Furthermore, it is difficult to establish how much of the recent advances in
template-based approaches are due to actual improvements in methodology versus


# References
