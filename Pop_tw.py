# population my attempt

import g
import Genome_tw

class Population:

    pop = []  # the individuals of the population

    def __init__(self,rng):
        self.popReset(rng)

    def popReset(self,rng):
        self.pop = [None] * g.POPULATION # initialise an array with the chosen population size

        # adding in an individual to each slot of the population (collection of 35 genomes makes an individual)
        for i in range(0, g.POPULATION):
            self.pop[i]= Genome_tw.Genome(g.globalRand)

    def calcScore(self):
        # returns the number of the best individual
        global bestScore, best # need this line???
        retv = 0
        self.pop[0].calcScoreG() # calculate score of first individual
        g.bestScore = self.pop[0].score # initialise with score of first individual
        for i in range(1, g.POPULATION): # looping through each individual in population
            self.pop[i].calcScoreG() # finding score of 'the next' individual
            if (self.pop[i].score < g.bestScore): # if the score of 'the next' individual is better (lower) than current, then replace
                retv = i;
                g.best=i # finds and sets the best performing individual id
                g.bestScore =self.pop[i].score; # finds and sets the score of best performing individual
        return retv; # returns ID of best individual


    def mate(self, killMe, mum, dad, rng):

        self.pop[killMe].score = g.marker # setting the score of the individual to become child as marker (reset)

        # mutation strategy 1: mixing mum and dad to create child
        for  i in range(0, g.NUM_OF_ITEMS): # looping through each genome (which defined with number of items)
            if (rng.random() < 0.5):  # at 50% chance
                self.pop[killMe].genome[i] = self.pop[mum].genome[i]; # swap the genome with mum's genome
            else:
                self.pop[killMe].genome[i] = self.pop[dad].genome[i]; # otherwise, swap with dad's genome
           
        self.pop[killMe].generation = max(self.pop[dad].generation, self.pop[mum].generation) + 1; # generation is counted as plus one to max of mum's or dad's
        self.pop[killMe].mutations = max(self.pop[dad].mutations, self.pop[mum].mutations); # mutation is counted as max of mum's or dad's
        
        # suprise twist- random mutations
        if (rng.random() * 100 < g.MUTATIONPERCENT): # if random number is less than preset mutationPercent
            g.mutations = g.mutations + 1 # add one to global mutation marker
            self.pop[killMe].mutations = self.pop[killMe].mutations + 1; # add one to individual mutation marker

            if (rng.random() < 0.5) : # decide large or small mutation (50% chance each)
                # mutation case 1 (large mutation)
                self.pop[killMe] = Genome_tw.Genome(g.globalRand) # chosen individual to replace with random genome

            else:
                # mutation case 2 (small mutation)
                for k in range(0,g.rndInt(rng, 1, 8)): # repeat swap for 1 to 8 times
                    Smut = g.rndInt(rng, 0, g.NUM_OF_ITEMS -1) # choosing the item to re-allocate
                    self.pop[killMe].genome[Smut] = g.rndInt(g.globalRand, 0, g.NUM_OF_TRUCKS) # randomly re-allocate selected item again


    def breed(self, rng):
        #// picks 3 from this generation - kills the weakest and breeds from the other two
        # choose 3 random individuals
        c1 = g.rndInt(rng, 0, g.POPULATION -1)
        c2 = g.rndInt(rng, 0, g.POPULATION -1)
        c3 = g.rndInt(rng, 0, g.POPULATION -1)
        # condition to choose again if any of the random individual id are the same, or if chose the child
        while (c2 == c1 or c3 == c1 or c2 == c3 or
            self.pop[c1].score == g.marker or self.pop[c2].score == g.marker or self.pop[c3].score == g.marker):
            c1 = g.rndInt(rng, 0, g.POPULATION -1)
            c2 = g.rndInt(rng, 0, g.POPULATION -1)
            c3 = g.rndInt(rng, 0, g.POPULATION -1)
        #// at this time c1, c2 , c3 are legit
        if (self.pop[c1].score >= self.pop[c2].score and self.pop[c1].score >= self.pop[c3].score): # if c1 performs the worst out of three
            self.mate(c1, c2, c3, rng)
            return c1; ## set c1 as child of c2 and c3
 
        if (self.pop[c2].score >= self.pop[c1].score and self.pop[c2].score >= self.pop[c3].score): # if c2 performs the worst
            self.mate(c2, c1, c3, rng)
            return c2;  ## set c2 as child

        if (self.pop[c3].score >= self.pop[c2].score and self.pop[c3].score >= self.pop[c1].score): # if c3 performs the worst
            self.mate(c3, c2, c1, rng)
            return c3;  ## set c3 as child
        return -1; #// should never happen


    def find_duplicates(self):
        # finds id of duplicated individuals
        self.temp=[]
        self.uniqlist=[]
        self.duplist=[]
        self.dup_ind=[]

        # transforming individuals from list to one string
        for i in range(0, g.POPULATION):
            s=""
            for j in range(0, g.NUM_OF_ITEMS):
                x=g.population.pop[i].genome[j]
                s=s+str(x) # index + full genome of this individual
            self.temp.append(s)

        # converting string to number
        for i,v in enumerate(self.temp):
            self.temp[i] = int(self.temp[i])

        # checking for duplicates and treating
        self.q=0
        for i in self.temp:

            if i not in self.uniqlist:
                self.uniqlist.append(i)
            else:
                g.dup_count = g.dup_count + 1
                self.dup_ind.append(self.q)
#                self.pop[self.q] = Genome_tw.Genome(g.globalRand) # replace duplicates with random genome  ##UNCOMMENT THIS LINE FOR HD EXPERIMENT

            self.q=self.q+1

        return len(self.dup_ind)




    def run1Generation(self):
        global globalRand
        gg = int(g.POPULATION / 2) # half of population number (50 in our case)
        for i in range(0, gg):
            self.breed(g.globalRand); # performing breed function 50 times
        g.best = self.calcScore(); # find the best individual ID through the calcScore() above
        g.generation = g.generation +1 # add one to global generation count

    def show(self, num):
        # creates a string do describe the population member, will work with function of same name in Genom.py
        retv = "Best individual details: "+ " \n"
        retv = retv + "ID: "+ str(g.best) + " " + self.pop[num].showG() + " \n"

        # display if duplicates exist
        if (self.find_duplicates() == 0):
            retv = retv + "No duplicates"
        else:
            retv = retv + "There are " + str(self.find_duplicates()) + " duplicates in this population. (UNtreated)"  ## COMMENT THIS LINE OUT FOR HD EXP
#            pass  ##UNCOMMENT THIS LINE FOR HD EXPERIMENT
       
        return retv

    def showBest(self):
        print("=======================================================")
        print(self.show(g.best))  # runs show() above
        print("Global details: generations="+str(g.generation)+"  mutations="+str(g.mutations)+" duplication treatment count="+str(g.dup_count)) # prints global gen and mut count (mutation count only have global count, gen have individual count)
        print("Random seed number: " + str(g.seed_no))
        print("=======================================================")

    def run1Gen(self):
        global globalRand, population
        self.run1Generation()
        self.showBest()
