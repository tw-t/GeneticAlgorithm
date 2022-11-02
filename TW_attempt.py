# GA assignment my attempt

import time
import random

import Items
import Genome_tw
import g
import Pop_tw

items = Items.ItemList() # class object
items.setItems()
genT = 10  # generation count for option T
genH = 100  # generation count for option H

def optL():
    global items
    items.listItems()
    print("");

def opt1():
    global items, population, globalRand # class object items, variable population and global random number
    g.population.run1Gen()
    pass

# program for option T and H
def optT(gens):
    global items, population, globalRand
    print("Running {} times".format(gens))
    for i in range(0,gens):    # option T just runs option 1 ten times
        g.population.run1Gen()
    pass

# reset sequence
def optR():
    global items, population, globalRand
    items.setItems()
    g.population = Pop_tw.Population(g.globalRand) # why??
    g.population.popReset(g.globalRand) # resets population individuals
    g.mutations=0 # resets global mutation count
    g.generation = 0 # resets global generation count
    print("reset done")


def optP():
    print("print entire gene pool")
    for i in range(0,g.POPULATION):
        s="["+ format(i, '03d')+"]=" # 3 digit index for individual
        for j in range(0, g.NUM_OF_ITEMS):
            x=g.population.pop[i].genome[j]
            s=s+str(x) # index + full genome of this individual
        print(s)
    print()


def menu():
    opt ="loop"
    global genT, genH # set option T and H generation counts
    while (opt != "E"): # unless choose option E, print below menu options
        print()
        print("Main Menu")
        print("E - Exit")
        print("1 - Run 1 generation")
        print("T - Run generations "+str(genT)+" of them")        
        print("H - Run generations "+str(genH)+" of them")
        print("L - List all items")
#        print("G - List a gene from the gene pool (population)")        
#        print("D - List a gene from the gene pool (population) Full")
#        print("A - Analyse alleles in the gene pool")        
        print("R - reset")
        print("P - list entire gene pool")
        print("Conditions: "+" \n"+"*Triage is 31"+"; Hospital Tents are 4 and 5"+"; Petrols are 7, 8, 9, 22")

        opt=input() # take option input
        opt=opt.upper().strip()
        if (opt == "1"): opt1()
        if (opt == "L"): optL()
        if (opt == "R"): optR()        
#        if (opt == "G"): optG(False) 
#        if (opt == "D"): optG(True)        
        if (opt == "P"): optP()        
        if (opt == "T"): optT(genT)
        if (opt == "H"): optT(genH)
#        if (opt == "A"): optA()

# this is the main program
def main():
    print("GA Assignment 2022 V1.1 (30/10/2022)")
    optR()  # reset world
    menu() # runs menu program

# when run program, run the main program first
if __name__ == "__main__":
    main()
