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
        for i, v in enumerate(self.genome):
            # left out list
            if (v == 0):
                self.s0 = self.s0 + items.lst[i].size # calculates total sum for left out list

            # truck 1
            if (v == 1):
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
            if (v == 2):
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
            if (v == 3):
                self.s3 = self.s3 + items.lst[i].size # calculates total sum for truck 3
                if (items.lst[i].importance == "N"):
                    self.score = self.score -0
                if (items.lst[i].importance == "I"):
                    self.score = self.score -1
                if (items.lst[i].importance == "V"):
                    self.score = self.score -2
                if (items.lst[i].importance == "C"):
                    self.score = self.score -3

        # condition to penalise overloading (strongly penalise)
        for s in [self.s1, self.s2, self.s3]: # note s0 does not affect score
            if (s > g.TRUCK_CAPACITY):
                self.score = self.score + abs(g.TRUCK_CAPACITY - s)
                self.score = self.score + 20
            else:
                self.score = self.score + g.TRUCK_CAPACITY - s

        # condition to bring Triage (strongly incentivise)
        if (self.genome[31] != 0):
            self.score = self.score -5

        # condition to treat two part hospital tents as one (strongly penalise)
        if (self.genome[4] != 0 and self.genome[5] == 0):
            self.score = self.score + 10
        if (self.genome[5] != 0 and self.genome[4] == 0):
            self.score = self.score + 10

        # condition to bring 2 out of 4 petrol items
        petrol_items = [self.genome[7], self.genome[8], self.genome[9], self.genome[22]]
        if (petrol_items.count(0) > 2): # 3 or 4 petrol items assigned to leftout list (strong penalty)
            self.score = self.score + 10
        if (petrol_items.count(0) <= 2): # at least 2 petrol items brought  (strongly incentivise)
            self.score = self.score -5

           
        return self.score
