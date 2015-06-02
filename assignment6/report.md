% BIOINF 702 Assignment 6
% Arman Bilge
% 2 June 2015

Due to genuine concerns with the stability of BEAST 2 as well as personal
preference I performed the described analysis using BEAST v1.8.2.

                      BEAST v1.8.2, 2002-2015
           Bayesian Evolutionary Analysis Sampling Trees
                     Designed and developed by
       Alexei J. Drummond, Andrew Rambaut and Marc A. Suchard

                   Department of Computer Science
                       University of Auckland
                      alexei@cs.auckland.ac.nz

                 Institute of Evolutionary Biology
                      University of Edinburgh
                         a.rambaut@ed.ac.uk

                  David Geffen School of Medicine
               University of California, Los Angeles
                         msuchard@ucla.edu

                    Downloads, Help & Resources:
                     	http://beast.bio.ed.ac.uk

    Source code distributed under the GNU Lesser General Public License:
                	http://code.google.com/p/beast-mcmc

                         BEAST developers:
    	Alex Alekseyenko, Guy Baele, Trevor Bedford, Filip Bielejec, Erik Bloomquist, Matthew Hall,
    	Joseph Heled, Sebastian Hoehna, Denise Kuehnert, Philippe Lemey, Wai Lok Sibon Li,
    	Gerton Lunter, Sidney Markowitz, Vladimir Minin, Michael Defoin Platel,
              	Oliver Pybus, Chieh-Hsi Wu, Walter Xie

                             Thanks to:
        	Roald Forsberg, Beth Shapiro and Korbinian Strimmer

    Using BEAGLE library v2.1.2 for accelerated, parallel likelihood evaluation
    2009-2013, BEAGLE Working Group - http://beagle-lib.googlecode.com/
    Citation: Ayres et al (2012) Systematic Biology 61: 170-173 | doi:10.1093/sysbio/syr100



    Random number seed: 1433233462195


    Failed to load parser: dr.inferencexml.trace.GeneralizedHarmonicMeanAnalysisParser
    line = dr.inferencexml.trace.GeneralizedHarmonicMeanAnalysisParser



    Loading additional development parsers from development_parsers.properties, which is additional set of parsers only available for development version ...

    WARNING: parser - dr.app.beagle.multidimensionalscaling.MultiDimensionalScalingLikelihood in development_parsers.properties is duplicated, which is REPLACING the same parser loaded previously.

    Parsing XML file: cats.xml
      File encoding: UTF8
    Looking for plugins in /Users/abil933/Documents/BIOINF702/assignment6/plugins
    Read alignment: alignment1
      Sequences = 35
          Sites = 381
       Datatype = nucleotide
    Read alignment: alignment2
      Sequences = 35
          Sites = 319
       Datatype = nucleotide
    Site patterns 'firsthalf.patterns' created from positions 1-381 of alignment 'alignment1'
      unique pattern count = 114
    Site patterns 'secondhalf.patterns' created from positions 1-319 of alignment 'alignment2'
      unique pattern count = 162
    Using Yule prior on tree
    Creating the tree model, 'treeModel'
      initial tree topology = (((((((((((((Catopuma badia,Herpailurus yaguarondi),Caracal caracal),Profelis aurata),Otocolobus manul),Lynx lynx),((Leopardus wiedii,Neofelis nebulosa),Lynx rufus)),(Oncifelis guigna,Uncia uncia)),((Acinonyx jubatus,Felis catus),Prionailurus viverrinus)),((((Oncifelis colocolo,Puma concolor),Felis margarita),(Felis libyca,Leptailurus serval)),Pardofelis marmorata)),(((Prionailurus bengalensis,Prionailurus planiceps),Felis silvestris),(Felis nigripes,Lynx canadensis))),((((Catopuma temminckii,Leopardus tigrinus),Prionailurus rubiginosa),Felis chaus),Oncifelis geoffroyi)),((Panthera leo,Panthera pardus),(Panthera onca,Panthera tigris))),Crocuta crocuta)
      tree height = 421.8428072152668
    Using discretized relaxed clock model.
      over sampling = 1
      parametric model = logNormalDistributionModel
       rate categories = 1
    Creating state frequencies model 'firsthalf.frequencies': Using empirical frequencies from data = {0.33787, 0.22497, 0.19921, 0.23796}
    Creating HKY substitution model. Initial kappa = 2.0
    Creating site model:
      4 category discrete gamma with initial shape = 0.5
    Creating state frequencies model 'secondhalf.frequencies': Using empirical frequencies from data = {0.3384, 0.26831, 0.07674, 0.31656}
    Creating HKY substitution model. Initial kappa = 2.0
    Creating site model:
      4 category discrete gamma with initial shape = 0.5
    Using BEAGLE TreeLikelihood
      Branch rate model used: discretizedBranchRates
      Using BEAGLE resource 0: CPU
        with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_SSE THREADING_NONE PROCESSOR_CPU FRAMEWORK_CPU
      Ignoring ambiguities in tree likelihood.
      With 114 unique site patterns.
      Using rescaling scheme : dynamic (rescaling every 100 evaluations)
    Using BEAGLE TreeLikelihood
      Branch rate model used: discretizedBranchRates
      Using BEAGLE resource 0: CPU
        with instance flags:  PRECISION_DOUBLE COMPUTATION_SYNCH EIGEN_REAL SCALING_MANUAL SCALERS_RAW VECTOR_SSE THREADING_NONE PROCESSOR_CPU FRAMEWORK_CPU
      Ignoring ambiguities in tree likelihood.
      With 162 unique site patterns.
      Using rescaling scheme : dynamic (rescaling every 100 evaluations)
    Creating swap operator for parameter branchRates.categories (weight=10.0)
    Optimization Schedule: default
    Likelihood computation is using an auto sizing thread pool.
    Creating the MCMC chain:
      chainLength=16000000
      autoOptimize=true
      autoOptimize delayed for 160000 steps
    # BEAST v1.8.2, r6692
    # Generated Tue Jun 02 20:24:23 NZST 2015 [seed=1433233462195]
    state	Posterior   	Prior       	Likelihood  	rootHeight  	ucld.mean
    0	-407944.3592	-390436.3027	-17508.0566 	421.843     	1.00000     	-
    ...
    16000000	-5213.0655  	-91.5474    	-5121.5181  	11.8928     	1.12873E-2  	0.02 hours/million states

    Operator analysis
    Operator                                          Tuning   Count      Time     Time/Op  Pr(accept)
    scale(firsthalf.kappa)                            0.487   15608      1833     0.12     0.2796
    scale(firsthalf.alpha)                            0.622   15540      1795     0.12     0.2527
    scale(secondhalf.kappa)                           0.511   15735      2283     0.15     0.2677
    scale(secondhalf.alpha)                           0.553   15608      2146     0.14     0.2602
    scale(ucld.mean)                                  0.694   469556     80257    0.17     0.246
    scale(ucld.stdev)                                 0.43    468036     79982    0.17     0.3121
    subtreeSlide(treeModel)                           1.806   2342793    116196   0.05     0.314
    Narrow Exchange(treeModel)                                2343038    93087    0.04     0.1989
    Wide Exchange(treeModel)                                  468074     12045    0.03     0.0097
    wilsonBalding(treeModel)                                  468610     21815    0.05     0.0181
    scale(treeModel.rootHeight)                       0.555   468814     14817    0.03     0.2642
    uniform(nodeHeights(treeModel))                           4688107    270319   0.06     0.4502
    scale(yule.birthRate)                             0.202   469451     8567     0.02     0.2783
    up:ucld.mean down:nodeHeights(treeModel)          0.444   468911     82755    0.18     0.2332
    swapOperator(branchRates.categories)                      1561528    94881    0.06     0.6067
    uniformInteger(branchRates.categories)                    1560591    80714    0.05     0.7204

    17.884483333333332 minutes