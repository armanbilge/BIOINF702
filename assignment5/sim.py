"""
sim.py

The MIT License (MIT)

Copyright (c) 2015 Arman Bilge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from argparse import ArgumentParser
import itertools as it
import numpy as np
from numpy import linalg as LA
from numpy import random
import string
from Tree import Tree
from Node import Node

BASES = ('A', 'C', 'G', 'T')

def yule_origin(n, lambd):
    return - np.log(1 - np.power(random.random(), 1/n)) / lambd

def yule_speciations(n, lambd):
    tor = yule_origin(n, lambd)
    s = - np.log(1 - (1 - np.exp(-lambd * tor)) * random.random(n-1)) / lambd
    s.sort()
    return s

def coal_intervals(n, theta):
    for k in reversed(range(2, n+1)):
        yield random.exponential(4 * theta / (k * (k-1)))

def coal_coalescents(n, theta):
    return it.accumulate(coal_intervals(n, theta))

TREE_MODELS = {'yule': yule_speciations, 'coal': coal_coalescents}

def simulate_tree(n, p, model):
    nodes = []
    for i in map(str, range(n)):
        node = Node(i)
        node.set_height(0)
        nodes.append(node)
    for s in model(n, p):
        node = Node()
        i, j = random.choice(nodes, replace=False, size=2)
        node.set_height(s)
        node.add_child(i)
        node.add_child(j)
        nodes.remove(i)
        nodes.remove(j)
        nodes.append(node)
    return Tree(nodes[0])

class SubstitutionModel:
    def __init__(self, mu, abcdef, pi):
        self.mu = mu
        self.pi = pi
        Q = SubstitutionModel.create_Q(abcdef, pi)
        self.L, self.T = LA.eig(Q)
        self.Tinv = LA.inv(self.T)

    def transition_matrix(self, t):
        return self.T * np.diag(np.exp(t * self.mu * self.L)) * self.Tinv

    def random_sequence(self, L):
        return ''.join(random.choice(BASES, size=L, p=self.pi))

    def mutate_sequence(self, S, t):
        T = self.transition_matrix(t)
        P = {}
        for i,b in enumerate(BASES):
            e = np.matrix(np.eye(1, 4, i)).getT()
            P[b] = np.squeeze(np.asarray(T * e))
            P[b] /= P[b].sum() # Deal with numerical imprecision
        return ''.join(random.choice(BASES, p=P[x]) for x in S)

    def create_Q(abcdef, pi):
        a, b, c, d, e, f = abcdef
        A, C, G, T = pi
        Q = np.matrix([[0.0] * 4 for _ in range(4)])
        Q[0,1] = a * C
        Q[1,0] = a * A
        Q[0,2] = b * G
        Q[2,0] = b * A
        Q[0,3] = c * T
        Q[3,0] = c * A
        Q[1,2] = d * G
        Q[2,1] = d * C
        Q[3,1] = e * T
        Q[1,3] = e * C
        Q[2,3] = f * T
        Q[3,2] = f * G
        for i in range(4):
            Q[i,i] = - Q[i,:].sum()
        beta = 1 / (2 * (a * A * C
                          + b * A * G
                          + c * A * T
                          + d * C * G
                          + e * C * T
                          + f * G * T))
        Q *= beta
        return Q

def simulate_sequences(node, model, length=None):
    if length:
        node = node.get_root()
        node.set_sequence(model.random_sequence(length))
    if not node.is_root():
        parent = node.get_parent()
        s = model.mutate_sequence(parent.get_sequence(),
                                  parent.get_height() - node.get_height())
        node.set_sequence(s)
    if not node.is_leaf():
        for child in node.get_children():
            simulate_sequences(child, model)

parser = ArgumentParser(description='Simulate a tree and sequences.')
parser.add_argument('-n', '--taxa', metavar='N', type=int, required=True,
                    help='the number of taxa')
parser.add_argument('-t', '--tree-model',
                    metavar='{' + ','.join(TREE_MODELS.keys()) + '}',
                    type=lambda x: TREE_MODELS[x],
                    choices=TREE_MODELS.values(),
                    required=True, help='the tree model')
parser.add_argument('-r', '--theta', '--lambda', metavar='R', type=float,
                    required=True, help='the parameter for the tree model')
parser.add_argument('-l', '--length', metavar='L', type=int, required=True,
                    help='the length of the sequence')
parser.add_argument('-f', '--frequencies', metavar=BASES,
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

tree = simulate_tree(args.taxa, args.theta, args.tree_model)

with open('{}.tree'.format(args.filename), 'w') as f:
    print(tree.get_newick(), file=f)

sm = SubstitutionModel(args.mutation_rate, args.rate_matrix, args.frequencies)
simulate_sequences(tree, sm, args.length)

with open('{}.nex'.format(args.filename), 'w') as f:
    print('#NEXUS', file=f)
    print('Begin data;', file=f)
    print('Dimensions ntax={} nchar={};'.format(tree.get_leaf_count(),
          args.length), file=f)
    print('Format datatype=dna missing=? gap=-;', file=f)
    print('Matrix', file=f)
    for leaf in sorted(tree.get_leaves(), key=lambda n: int(n.get_label())):
        print('{}    {}'.format(leaf.get_label(), leaf.get_sequence()), file=f)
    print(';', file=f)
    print('End;', file=f)
