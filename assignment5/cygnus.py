"""
cygnus.py
A simulator of Coalescent and Yule trees and GTR Nucleotide Sequences.
"""

# The MIT License (MIT)
#
# Copyright (c) 2015 Arman Bilge
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from argparse import ArgumentParser
import itertools as it
import numpy as np
from numpy import linalg as LA
from numpy import random
import string
from Tree import Tree
from Node import Node

# References:
#   Felsenstein, Joseph (2004). Inferring Phylogenies. Sinaur Associates.
#   Gernhard, Tanja (2008). On the conditioned reconstructed process.
#       Journal of Theoretical Biology 253(4). doi:10.1016/j.jtbi.2008.04.005

def yule_origin(n, lambd):
    """Sample time of origin for a Yule tree on n taxa with rate lambda."""
    # Gernhard (2008) Corollary 3.3
    return - np.log(1 - np.power(random.random(), 1/n)) / lambd

def yule_speciations(n, lambd):
    """Sample speciation times for a Yule tree on n taxa with rate lambda."""
    # Gernhard (2008) Section 2.1.1
    t = yule_origin(n, lambd)
    s = - np.log(1 - (1 - np.exp(-lambd * t)) * random.random(n-1)) / lambd
    s.sort() # Most recent to oldest
    return s

def coal_intervals(n, theta):
    """Sample coalescent intervals for n taxa from population of size theta."""
    # Algorithm given by Felsenstein (2004) Chapter 26 pp. 456
    for k in range(n, 1, -1):
        # Using scale = 1/lambda parameterisation
        yield random.exponential(2 * theta / (k * (k-1)))

def coal_coalescents(n, theta):
    """Sample coalescent times for n taxa from population of size theta."""
    # Running sum of intervals
    return it.accumulate(coal_intervals(n, theta))

# Short names of the tree models
TREE_MODELS = {'yule': yule_speciations, 'coal': coal_coalescents}

def simulate_tree(n, p, model):
    """Simulate a tree on n taxa according to the model with parameter p."""

    nodes = [] # Active nodes

    # Create leaf nodes with integer labels
    for i in map(str, range(n)):
        node = Node(i)
        node.set_height(0)
        nodes.append(node)

    for s in model(n, p):
        # Create parent
        node = Node()
        node.set_height(s)

        # Choose children
        i, j = random.choice(nodes, replace=False, size=2)
        nodes.remove(i)
        nodes.remove(j)

        # Set children
        node.add_child(i)
        node.add_child(j)

        # Add to active nodes
        nodes.append(node)

    # Last node is root
    return Tree(nodes[0])

class SubstModel:
    """Represents a nucleotide substitution model."""
    # The genetic code
    BASES = ('A', 'C', 'G', 'T')
    # Standard basis vectors for 4-dimensional space
    E = tuple(np.matrix(np.eye(1, 4, i)).getT() for i in range(4))

    def __init__(self, mu, abcdef, pi):
        self.mu = mu # mutation rate
        self.pi = pi # equilibrium frequencies
        Q = SubstModel.create_Q(abcdef, pi)
        # Eigenvalue decomposition Q = T L T^-1
        # Felsenstein (2004) eq. 13.17
        self.L, self.T = LA.eig(Q)
        self.Tinv = LA.inv(self.T)

    def transition_matrix(self, t):
        """Computes the finite time transition matrix."""
        # Matrix exponential by diagonalisation
        # Felsenstein (2004) Chapter 13 pp. 206
        return self.T * np.diag(np.exp(t * self.mu * self.L)) * self.Tinv

    def random_sequence(self, L):
        """Draw a random sequence under model."""
        # Draw bases according to equilibrium frequencies
        return ''.join(random.choice(SubstModel.BASES, size=L, p=self.pi))

    def mutate_sequence(self, S, t):
        """Simulates mutations on a sequence for time t under model."""
        P = self.transition_matrix(t)
        # Precompute transition probabilities conditioning on ancestral base
        p = {}
        for b, e in zip(SubstModel.BASES, SubstModel.E):
            p[b] = np.squeeze(np.asarray(P * e))
        # Draw bases according to conditional transition probabilities
        return ''.join(random.choice(SubstModel.BASES, p=p[x]) for x in S)

    def create_Q(abcdef, pi):
        """Creates the normalised rate matrix for GTR model."""

        a, b, c, d, e, f = abcdef
        A, C, G, T = pi

        # Felsenstein (2004) eq. 13.15
        Q = np.matrix([[0.0] * 4 for _ in range(4)])
        Q[0,1] = a * A
        Q[0,2] = b * A
        Q[0,3] = c * A
        Q[1,2] = d * C
        Q[1,3] = e * C
        Q[2,3] = f * G
        Q[1,0] = a * C
        Q[2,0] = b * G
        Q[3,0] = c * T
        Q[2,1] = d * G
        Q[3,1] = e * T
        Q[3,2] = f * T

        # Set diagonals so columns sum to 0
        for i in range(4):
            Q[i,i] = - Q[:,i].sum()

        # Felsenstein (2004) eq. 13.14
        beta = 1 / (2 * (a * A * C
                          + b * A * G
                          + c * A * T
                          + d * C * G
                          + e * C * T
                          + f * G * T))
        # Renormalise Q
        Q *= beta

        return Q

def simulate_sequences(node, model, length=None):
    """Simulates a sequence alignment for a tree under a substition model."""
    if length: # First call in recursion
        node = node.get_root()
        # Draw root sequence from equilibrium frequencies
        node.set_sequence(model.random_sequence(length))
    if not node.is_root(): # Simulate mutations during time since parent
        parent = node.get_parent()
        s = model.mutate_sequence(parent.get_sequence(),
                                  parent.get_height() - node.get_height())
        node.set_sequence(s)
    if not node.is_leaf(): # Recurse on children
        for child in node.get_children():
            simulate_sequences(child, model)

# Setup command line options
parser = ArgumentParser(description='A simulator of Coalescent and Yule trees'
                                             + ' and GTR Nucleotide Sequences.')
parser.add_argument('-n', '--taxa', metavar='N', type=int, required=True,
                    help='the number of taxa')
parser.add_argument('-t', '--tree-model',
                    metavar='{' + ','.join(TREE_MODELS.keys()) + '}',
                    type=lambda x: TREE_MODELS[x],
                    choices=TREE_MODELS.values(),
                    required=True, help='the tree model')
parser.add_argument('-b', '--theta', '--lambda', metavar='B', type=float,
                    required=True, help='the parameter for the tree model')
parser.add_argument('-l', '--length', metavar='L', type=int, required=True,
                    help='the length of the sequence')
parser.add_argument('-f', '--frequencies', metavar=SubstModel.BASES,
                    type=float, nargs=4, required=True,
                    help='the stationary distribution for the bases')
parser.add_argument('-q', '--rate-matrix',
                    metavar=tuple(string.ascii_lowercase[:6]), type=float,
                    nargs=6, required=True,
                    help='the relative substitution rates')
parser.add_argument('-m', '--mutation-rate', metavar='mu', type=float,
                    required=True, help='the mutation rate')
parser.add_argument('filename', help='the filename stem')

args = parser.parse_args()

# Simulate the tree
tree = simulate_tree(args.taxa, args.theta, args.tree_model)

# Write the tree to a file
with open('{}.tree'.format(args.filename), 'w') as f:
    print(tree.get_newick(), file=f)

# Create the substitution model
sm = SubstModel(args.mutation_rate, args.rate_matrix, args.frequencies)
# Simulate the sequence alignment
simulate_sequences(tree, sm, args.length)

# Write the alignment to a NEXUS file
with open('{}.nex'.format(args.filename), 'w') as f:
    print('#NEXUS', file=f)
    print('Begin data;', file=f)
    print('Dimensions ntax={} nchar={};'.format(tree.get_leaf_count(),
          args.length), file=f)
    print('Format datatype=dna missing=? gap=-;', file=f)
    print('Matrix', file=f)
    # Iterate over leaves in order
    for leaf in sorted(tree.get_leaves(), key=lambda n: int(n.get_label())):
        print('{}    {}'.format(leaf.get_label(), leaf.get_sequence()), file=f)
    print(';', file=f)
    print('End;', file=f)
