% BIOINF 702 Assignment 6
% Arman Bilge
% 2 June 2015

Due to genuine concerns with the stability of BEAST 2 as well as personal
preference I performed the described analysis using BEAST v1.8.2.

 1. I can tell that I ran the chain for long enough ($64 \times 10^6$ states)
    because all of the ESSs reported by Tracer are greater than 200.
    Furthermore, the trace for the TMRCA of the in-group appeared to be a
    "fuzzy caterpillar" which suggests that it was mixing well (Figure 1).
    Although the ESS for every parameter is greater than 200, the trace of the
    likelihood (and therefore the posterior) looked more like a "bumpy
    caterpillar" due to a bimodal tree distribution.

    ![MCMC trace for the TMRCA of the in-group.](trace.pdf)

 2. The substitution model parameters are significantly different between
    the two genes.
    The mean for the posterior distribution on the transition--transversion
    ratio $\kappa$ for NADH5 is over 2.5 times greater than that for 16S.
    The mean for the posterior distribution on the gamma shape $\alpha$ for
    NADH5 is nearly twice as great as that for 16S.
    Notably, there is no overlap of the 95% HPD intervals for both parameters
    (Figures 2 and 3).

    ![Posterior distribution on the transition--transversion ratio $\kappa$
      for 16S (black) and NADH5 (blue).](kappa.pdf)

    ![Posterior distribution on the gamma shape $\alpha$ for 16S (black) and
      NADH5 (blue).](alpha.pdf)

 3. The posterior distribution on the TMRCA for the in-group has a mean of
    10.48 Ma and a 95% HPD interval of 7.14 to 13.95 Ma.
    This estimate is very similar to that made by Johnson et al. (2006), who
    reported a mean of 10.78 Ma and confidence interval from 8.38 to 14.45 Ma.

 4. Not all of the eight clades reported by Johnson et al. (2006) appear in
    my MCC tree.
    This tree contains the Panthera clade,

 6. I reran the above analysis using only the 16S data.


 7. The skyline model is not appropriate for this data because it assumes that
    the samples have been taken from a panmictic population.
    This assumption does not hold when reconstructing a species phylogeny as, by
    definition, there is no gene flow between different species and therefore
    mating is not random.
    Furthermore, a grouping of individuals from different species is not a
    population.
