import gambit as gb
import string as st
import numpy as np
import numpy.random as rng
class GroupAgent:
    """ A group agent. The list of agents is from most preferred to least prferred option """
    agents
    aggregator
    preferences
    game
    def __init__(self, agents, aggregator, preferences):
        self.agents = agents
        self.aggregator = aggregator
        self.preferences = aggregator(preferences)

def generate_agents(n_agents, n_options):
    return [rng.permutation(n_options) for i in range(n_agents)]

def dictator(A):
    return A[0]
class first_past_post:
    

def first_past_post(A, votes):
    vote_tally = [np.sum([x[0]==i for x in A]) for i in range(len(A[0]))]
    
    return 
def average(A):
A = generate_agents(10,3)
dictator(A)


import gambit

g = gb.Game.new_tree()
nplayers = len(A)
players = [g.players.add(x) for x in string.ascii_lowercase[0:nplayers]]
g = g.new_table([len(x) for x in A])
g.players[0]



import torch as t
import kymatio as km
from kymatio.torch import Scattering2D

t.random
k=2
x = t.randn(10, 2**5,2)
N = x.shape[-2]
x.view()

xp = x.view(x.shape[:-2] + (k, N // k, 2))
