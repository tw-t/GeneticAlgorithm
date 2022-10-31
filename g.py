#globals my attempt

import random

NUM_OF_TRUCKS = 3
NUM_OF_ITEMS = 35
TRUCK_CAPACITY = 19

POPULATION = 100;
MUTATIONPERCENT=3 

generation=0;  
maxGeneration =20;
marker = -99999;
mutations = 0;
best = -1; # best individual's ID
bestScore = -99991 # score of best individual

globalRand=random.Random() # use globalRand.random
random.seed(102) #comment in for fixed seed for repeatability

population = None # will initialise later dont worry

# Below are Random Number Generators (RNG)

def rnd (rng, lo, hi):
    #never actually get high value
    retv = (hi - lo) * rng.random() + lo;
    return retv

def rndInt (rng, lo, hi):
    # note this is inclusive of lo and Hi val
    retv = (hi - lo+0.999) * rng.random() + lo;
    return int(retv)

def rnd0or1 (rng):
    # 0 or 1 50% chance
    retv = 0
    if (rng.random() <0.5): retv=1
    return retv





