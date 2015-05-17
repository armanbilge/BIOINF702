% Phylogenetic Hidden Markov Models
% Arman Bilge
% 18 May 2015

In brief, a phylogenetic hidden Markov model (phylo-HMM) is an HMM which has phylogenetic models (including a tree and substitution model) as its states and emits columns of a molecular sequence alignment.
Under a phylo-HMM, the multiple sequence alignment is generated under a Markov process along the genome in addition to the standard process of molecular evolution through time.
We may consider the practical applications of this joint model from two perspectives.
In the first, phylo-HMMs relax the assumption of independence of sequences in uses of HMMs for sequence analysis;
in the second, they relax the assumption of independence of sites in phylogenetic inference.
Given our discussion of sequence analysis methods in the lectures, I will focus on the former perspective.

To complete our definition of a phylo-HMM, we require a probability distribution on emissions given the current state of the Markov chain.
This is given by the Felsenstein tree likelihood, which defines a distribution on columns of a sequence alignment given a phylogenetic tree and substitution model as well as provides an efficient algorithm with which to compute the emission probability of a given observation.
The choice of phylogenetic models as states for the phylo-HMM is dependent on the biological phenomenon being modelled.
For example, different mutation rates may model conserved and nonconserved regions,
different substitution models may model coding and noncoding regions,
and different tree toplogies may model recombination.
Notably, a phylo-HMM is special case of a standard HMM such that the Viterbi, forwards, and backwards algorithms are all applicable.
This makes working with phylo-HMMs is computationally tractable.

Siepel and Haussler demonstrated the advantages of a phylo-HMM over a normal HMM in a simple gene finder for the mamallian genome.
Their model had four states, one for each of the codon positions and one for noncoding sites.
The phylogeny and substitution model parameters for these states were based on estimates from the literature.
They predicted genes using the Viterbi algorithm and compared its accuracy to a prediction using a nonphylo-HMM (that assumes independence of sequences) for datasets of between one and eight species.
While the phylo-HMM approached 100% accuracy with each additional species, the accuracy of the nonphylo-HMM decreased.
Siepel and Haussler suggested that this discrepancy in performance was because the nonphylo-HMM considered noise in the form of random fluctuations in base composition as significant and indicative of a change of state.
The phylo-HMM was aware of the correlations between sequences and the overall substitution process so was better at distinguishing signal from noise.
Furthermore, the specific substitutions provided signal that only the phylo-HMM was sensitive to.

In their second example, Siepel and Haussler identify conserved regions of the mamallian genome.
They created a phylo-HMM with ten rate categories for a total of ten states and fitted the model to the mamallian data.
Unfortunately no details were provided with regard to how they performed the fitting.
Then they used the forward-backward algorithm on this dataset to calculate the posterior probability that a site is conserved for each site, achieving results similar to existing analyses.
The phylo-HMM approach lends several advantages over alternative methods for identifying conserved regions.
Because it does not rely on a sliding window, it can identify conserved regions of various lengths.
Additionally, it can be easily extended to consider different functional categories in addition to rate categories.

The third example given by Siepel and Haussler showed how a phylo-HMM can be extended to consider context dependent substitutions.
This was done by modelling emissions under a higher-order Markov chain coupled with a higher-order substitution model.
Specifically, they use the definition of a conditional probability to consider the probability of a column of the alignment given the preceding columns as their renormalised joint probability.
This joint probability and the normalisation term are calculated efficiently using Felsenstein's pruning algorithm.
To introduce the context-dependency, the joint probability of several columns is no longer factorised into independent terms but is instead calculated using a higher-order substitution model that provides transition probabilities between every possible configuration of states (similar to a codon model).
Fortunately, the standard HMM algorithms are unaffected by this change to the emission model.
These context-dependent phylo-HMM models fitted data much better than simpler models, particularly the third-order model (probably because codons consist of three nucleotides).
Their results show the importance (as well as the computational feasability) of using context-dependent models.

The computational feasability of phylo-HMMs is best understood when they are treated as graphical models.
A graphical model is a framework for representing analysing probabilistic models as graphs, and subsequently analysing them using graph theory.
In a graphical model, each variable in the probabilistic model is represented by a vertex in the graph and conditional dependencies between the variables are represented by directed edges.
When the graph is a tree, the marginal probabilites for a variable may be computed efficiently using dynamic programming in an elimination algorithm.
Felsenstein's pruning algorithm and the forward algorithm for HMMs are both specific cases of the elimination algorithm.
The Viterbi algorithm also takes advantage of the same properties as the elimination algorithm.
Furthermore, the elimination algorithm can be extend to calculate the posterior probability for all variables in a tree model with two passes of the graph, one to compute the conditional probabilites and a second to compute the marginals.
The forward-backward algorithm is a special case of this.
Phylo-HMMs are computationally tractable because they are trees when represented as a graphical model.
The generalised algorithms make it straightforward to perform calculations with these models.

Siepel, A. and Haussler, D. (2005).
Phylogenetic Hidden Markov Models.
In R. Nielsen (Ed.), _Statistical Methods in Molecular Evolution_ (pp. 325–351).
New York: Springer.
[`10.1007/0-387-27733-1_12`](http://doi.org/10.1007/0-387-27733-1_12)
