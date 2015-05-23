# CYGNuS

A simulator of Coalescent and Yule trees and GTR Nucleotide Sequences.

To run the example, try `./example.sh`.

```
usage: cygnus.py [-h] -n N -t {coal,yule} -b B -l L -f A C G T -q a b c d e f
                 -m mu
                 filename

A simulator of Coalescent and Yule trees and GTR Nucleotide Sequences.

positional arguments:
  filename              the filename stem

optional arguments:
  -h, --help            show this help message and exit
  -n N, --taxa N        the number of taxa
  -t {coal,yule}, --tree-model {coal,yule}
                        the tree model
  -b B, --theta B, --lambda B
                        the parameter for the tree model
  -l L, --length L      the length of the sequence
  -f A C G T, --frequencies A C G T
                        the stationary distribution for the bases
  -q a b c d e f, --rate-matrix a b c d e f
                        the relative substitution rates
  -m mu, --mutation-rate mu
                        the mutation rate
```
