# GeneticAlgorithm
Python assignment

Variation of knapsack problem.

Have a list of items that we have to send out in a fleet of 3 trucks.
Each item have a size and importance ranking.

Objective: (in order of importance)
1. Fill up the trucks (and not overload) -DONE
2. Give bias to importance -DONE
3. must include the Hospital triage unit -DONE
4-1. treat the hospital as a two truck load -DONE
4-2. must sometimes include hospital and sometimes not (depending on random seed) -DONE
5. must include at least two of the four petrol items -DONE
6. (EXTRA) Code to detect duplicated individuals, count and modify duplication -DONE

Order to look at the code:
* g.py > Items.py > Genome_tw.py > Pop_tw.py > TW_attempt.py

Scoring system: lower score is better (can go into negatives)
