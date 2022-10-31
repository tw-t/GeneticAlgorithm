# Genome my attempt

import random
import Items
import g

items = Items.ItemList() # class object
items.setItems()

class Genome(object):

    genome = [] # array of 35 items, with truck number as each gene (0=leftout, 1=truck1, 2=truck2, 3=truck3)
    s0 = 0
    s1 = 0
    s2 = 0
    s3 = 0
    score=0 # lower score is better
    generation=0
    mutations=0


    def __init__(self,rng):

        self.genome = [None] * g.NUM_OF_ITEMS  # set up the size of genome according to number of items

        for i in range(0, g.NUM_OF_ITEMS):
            self.genome[i] = g.rndInt(g.globalRand, 0, g.NUM_OF_TRUCKS) # rng, randomly assign truck number (1,2,3) or left out (0) to gene

        self.score = g.marker
        self.generation = 0
        self.mutations = 0
        self.s0 = 0
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.calcScoreG()

    # display sequence for an individual
    def showG(self):
        retv = ""
        leftout = ""
        truck1 = ""
        truck2 = ""
        truck3 = ""

        retv="Score: {score}, generations: {gen}, mutations: {mut}".format(score=self.score, gen=self.generation, mut=self.mutations) + " \n"
        
        for i in range(0, g.NUM_OF_ITEMS):  # this is the list genomes
            # left out list
            if (self.genome[i] == 0):
                leftout = leftout + str(i) + ", "
            # truck 1 list
            if (self.genome[i] == 1):
                truck1 = truck1 + str(i) + ", "
            # truck 2 list
            if (self.genome[i] == 2):
                truck2 = truck2 + str(i) + ", "
            # truck 3 list
            if (self.genome[i] == 3):
                truck3 = truck3 + str(i) + ", "

        retv = retv + "Truck 1: " + str(truck1) + " \n" + "Total size: " + str(self.s1) + "/" + str(g.TRUCK_CAPACITY) + " \n"
        retv = retv + "Truck 2: " + str(truck2) + " \n" + "Total size: " + str(self.s2) + "/" + str(g.TRUCK_CAPACITY) + " \n"
        retv = retv + "Truck 3: " + str(truck3) + " \n" + "Total size: " + str(self.s3) + "/" + str(g.TRUCK_CAPACITY) + " \n"
        retv = retv + "Left out: " + str(leftout) + " \n" + "Remaining size: " + str(self.s0)

        return retv


    def calcScoreG(self):
        global globalRand
        global POPULATION
        global TRUCK_CAPACITY
        global NUM_OF_ITEMS
        global NUM_OF_TRUCKS

        self.score=0
        self.s0 = 0
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0


        # sequence to add up weight of items in each truck of one individual
        # condition to give bias according to importance (incetivising)
        for i in range(0, g.NUM_OF_ITEMS):
            # left out list
            if (self.genome[i] == 0):
                self.s0 = self.s0 + items.lst[i].size # calculates total sum for left out list

            # truck 1
            if (self.genome[i] == 1):
                self.s1 = self.s1 + items.lst[i].size # calculates total sum for truck 1
                if (items.lst[i].importance == "N"):
                    self.score = self.score -0
                if (items.lst[i].importance == "I"):
                    self.score = self.score -1
                if (items.lst[i].importance == "V"):
                    self.score = self.score -2
                if (items.lst[i].importance == "C"):
                    self.score = self.score -3

            # truck 2
            if (self.genome[i] == 2):
                self.s2 = self.s2 + items.lst[i].size # calculates total sum for truck 2
                if (items.lst[i].importance == "N"):
                    self.score = self.score -0
                if (items.lst[i].importance == "I"):
                    self.score = self.score -1
                if (items.lst[i].importance == "V"):
                    self.score = self.score -2
                if (items.lst[i].importance == "C"):
                    self.score = self.score -3

            # truck 3
            if (self.genome[i] == 3):
                self.s3 = self.s3 + items.lst[i].size # calculates total sum for truck 3
                if (items.lst[i].importance == "N"):
                    self.score = self.score -0
                if (items.lst[i].importance == "I"):
                    self.score = self.score -1
                if (items.lst[i].importance == "V"):
                    self.score = self.score -2
                if (items.lst[i].importance == "C"):
                    self.score = self.score -3

        # condition to penalise overloading
        for s in [self.s1, self.s2, self.s3]: # note s0 does not affect score
            if (s > g.TRUCK_CAPACITY):
                self.score = self.score + abs(g.TRUCK_CAPACITY - s)
                self.score = self.score + 20

            else:
                self.score = self.score + g.TRUCK_CAPACITY - s
           
        return self.score
