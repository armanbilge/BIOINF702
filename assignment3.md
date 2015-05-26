---
title: '[Is the protein folding problem still beyond us?]'
author: Arman Bilge
date: Friday 8 May 2015
csl: apa.csl
references:
- id: Fis09
  type: chapter
  author:
  - given: András
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
  page: 57–90
  DOI: 10.1007/978-1-4020-9058-5_3
- id: Her+14
  type: article-journal
  author:
  - given: Joseph L.
    family: Herman
  - given: Christopher J.
    family: Challis
  - given: Ádám
    family: Novák
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
  page: 2251–2266
  DOI: 10.1093/molbev/msu184
- id: Kav+98
  author:
  - given: Jeffrey S.
    family: Kavanaugh
  - given: Jamie A.
    family: Weydert
  - given: Paul H.
    family: Rogers
  - given: Arthur
    family: Arnone
  type: article-journal
  issued:
    year: 1998
  title: "High-Resolution Crystal Structures of Human Hemoglobin with Mutations at Tryptophan 37beta: Structural Basis for a High-Affinity T-State"
  container-title: Biochemistry
  volume: 37
  issue: 13
  page: 4358–4373
  DOI: 10.1021/bi9708702
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
  page: 254–257
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
  DOI: 10.1007/978-1-4020-9058-5_1
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
  page: 1–6
  DOI: 10.1002/prot.24452
- id: XZ12
  type: article-journal
  author:
  - given: Dong
    family: Xu
  - given: Yang
    family: Zhang
  issued:
    year: 2012
  title: "*Ab initio* protein structure assembly using continuous structure fragments and optimized knowledge-based force field"
  container-title: Proteins
  volume: 80
  issue: 7
  page: 1715–1735
  DOI: 10.1002/prot.24065
...

\frenchspacing

# Introduction

Proteins play a fundamental role in effectively all metabolic pathways and thus
are at the heart of molecular biology and biochemistry.
The function of a protein is directly related to its structure, the series of
folds that occur along the sequence of amino acids comprising the protein
[@Fis09].
Knowledge of protein structure also has important implications for evolutionary
biology.
Specifically, because structure is conserved more strongly than molecular
sequence [@Fis09], structural information makes it possible to accurately
determine the evolutionary relationships between distantly related species
[@Her+14].
However, the technical difficulties in experimentally determining the structure
of a protein have created a rapidly growing gap between the total number of
sequenced proteins and those with a known structure [@LWZ09].
@LWZ09 suggested that structural prediction *in silico* is the only way to
close this gap.

@Fis09 summarised the computational approaches to protein structure prediction
as using either the laws of physics (*ab initio* methods) or the theory of
evolution (comparative, template-based methods).
However, @Lup08 emphasised that the true solution to this problem is *ab
initio* given the limited usefulness of comparative methods to make accurate
predictions, especially in the absence of substantial prior information.
Furthermore, the *ab initio* methods that actually simulate the folding of a
protein may yield important insights into this process.
It is worth nothing that the dichotomy described by @Fis09 is less clear-cut in
practice: many otherwise *ab inito* methods do take advantage of the knowledge
in databases [@Fis09; @LWZ09] and template-based methods still rely on physics
for refinement as it is impossible to make accurate predictions solely based on
homology [@Fis09].

From a computer science perspective, the protein structure prediction problem
is an optimisation problem.
The key challenges are then (1) deriving a scoring function that gives the best
score to the true structure and (2) developing a search algorithm that can find
this structure with the optimal score.
I will consider both of these aspects.

# Scoring Functions

In *ab initio* modelling, the correct structure is assumed to be the most
thermodynamically stable one and thus structures are scored according to an
energy function.
Both physics- and knowledge-based energy functions are used in this context.

# Search Algorithms

The total search space for any reasonably-sized protein is immense.
Proteins are generally modelled on the atomic level, where each atom is
represented by three coordinates (either using the Cartesian system or the
torsion-angle system), such that a protein consisting of $n$ atoms has
$3\left(n-1\right)$ degrees of freedom [@XZ12].
The beta subunit of haemoglobin consists of nearly 5000 atoms for some 15000
degrees of freedom [@Kav+98].



It comes as no surprise that template-based methods have been successful given
their ability to aggressively reduce the search space by applying the concept
that a small change in sequence should cause only a small change in structure
[@Fis09].
The first steps for these methods involve searching through the PDB for
homologous structures and deciding which parts of these to use, if any
[@Fis09].



# Concluding Remarks

It is clear that no matter what approach is taken to the protein structure
prediction problem,

Furthermore, it is difficult to establish how much of the recent advances in
template-based approaches are due to actual improvements in methodology versus


# References
