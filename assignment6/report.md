% BIOINF 702 Assignment 6
% Arman Bilge
% 7 June 2015

\frenchspacing

Due to genuine concerns with the stability of BEAST 2 as well as personal
preference I performed the described analysis using BEAST v1.8.2.

 1. I can tell that I ran the chain for long enough ($2 \times 10^7$ states)
    because all of the ESSs reported by Tracer are greater than 200.
    Furthermore, the trace for the TMRCA of the in-group appeared to be a
    "fuzzy caterpillar" which suggests that it was mixing well (Figure 1).

 2. The substitution model parameters were significantly different between
    the two genes.
    The mean for the posterior distribution on the transition--transversion
    ratio $\kappa$ for NADH5 was over 2.5 times greater than that for 16S.
    The mean for the posterior distribution on the gamma shape $\alpha$ for
    NADH5 was over 1.5 times greater than that for 16S.
    Notably, there was no overlap of the 95% HPD intervals for both parameters
    (Figures 2 and 3).

 3. The posterior distribution on the TMRCA for the in-group had a mean of
    10.63 Ma and a 95% HPD interval from 7.31 Ma to 14.26 Ma.
    This estimate was very similar to that made by Johnson et al. (2006), who
    reported a mean of 10.78 Ma and confidence interval from 8.38 Ma to 14.45
    Ma.

 4. Not all of the eight clades reported by Johnson et al. (2006) appeared in
    my MCC tree.
    Only the domestic cat, lynx, and ocelot lineages were monophyletic in my
    MCC tree.
    A visual analysis of the topological uncertainty in DensiTree showed that
    there was some support for the monophyleticity of the Panthera lineage.
    It also revealed substantial uncertainty with regard to the deeper
    phylogenetic relationships between the taxa.

 5. The rates across the branches of the MCC tree were fairly similar (Figure
    4).
    The posterior distribution on the coefficient of variation for the rates
    had a mean of $0.29$.
    The branches associated with *Herpailurus yaguarondi* and *Panthera onca*
    appeared to have a particularly accelerated rate, perhaps an indication of
    the inaccurate placement of these taxa in the phylogeny.

 6. I reran the above analysis using only the 16S data.
    In this analysis, the posterior distribution on the TMRCA for the in-group
    had a mean of 12.82 Ma and a 95% HPD interval from 7.78 Ma to 18.89 Ma,
    somewhat older than the previously reported dates.
    The difference indicates that there is useful signal in the additional
    NADH5 data that helps to place the TMRCA.
    Additionally, there might be some discrepancy between the substitution
    rates for the two genes: the mean rate is about twice as fast when
    considering both genes.
    The slower substitution rate of 16S would explain the older placement of
    the TMRCA.

 7. The skyline model is not appropriate for this data because it assumes that
    the samples have been taken from a panmictic population.
    This assumption does not hold when reconstructing a species phylogeny as, by
    definition, there is no gene flow between different species and therefore
    mating is not random.
    Furthermore, a grouping of individuals from different species is not a
    population.

# Figures

![MCMC trace for the TMRCA of the in-group.](trace.pdf)

![Posterior distribution on the transition--transversion ratio $\kappa$
  for 16S (black) and NADH5 (blue).](kappa.pdf)

![Posterior distribution on the gamma shape $\alpha$ for 16S (black) and
  NADH5 (blue).](alpha.pdf)

![MCC tree with branches coloured by their median clock rate with slow
  rates in blue and fast rates in red.](ratetree.pdf)

