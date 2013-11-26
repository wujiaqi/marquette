##########################################
#
# Jiaqi Wu
# MSCS 5600 Programming Assignment 4
# Python Baysian Net implementation
# inspired by Berkeley CS department AIMA 
# http://aima.cs.berkeley.edu/
# bayesnet.py
#
##########################################

from random import random

class BayesNet:
  def __init__(self, nodes=[]):
    #modified here to remove dependency from a utils module
    self.vars=[]
    self.nodes=[]
    for node in nodes:
      self.add(node)

  def add(self, node):
    self.nodes.append(node)
    self.vars.append(node.variable)

  def observe(self, var, val):
    self.evidence[var] = val

class BayesNode:
  def __init__(self, variable, parents, cpt):
    if isinstance(parents, str): parents = parents.split()
    #modified here to remove dependency from a utils module
    self.variable=variable
    self.parents=parents
    self.cpt=cpt

  def sample(self, x):
    cptKey = ()
    for parent in self.parents:
      cptKey += (x[parent],)
    prob = 0
    if len(self.parents) == 0:
      prob = self.cpt
    else:
      prob = self.cpt[cptKey]
    if random() < prob:
      return True
    else:
      return False

def prior_sample(bn):
  x = {}
  for xi in bn.nodes:
    x[xi.variable] = xi.sample(x)
  return x

#tests if sample is consistent with conditions
def consistent(sample, conditions):
  for cond in conditions.keys():
    if sample[cond] != conditions[cond]:
      return False
  return True

#normalizes all values in dictionary x
def normalize(x):
  sum = 0
  x_keys = x.keys()
  for key in x_keys:
    sum += x[key]
  normalized_x = {}
  for key in x_keys:
    normalized_x[key] = float(x[key])/float(sum)
  return normalized_x

def rejection_sampling(x, e, bn, n):
  counts = {True: 0, False: 0}
  for i in xrange(1,n):
    sample = prior_sample(bn)
    if consistent(sample, e):
      counts[sample[x]] += 1
  return normalize(counts)

node = BayesNode

T, F = True, False

