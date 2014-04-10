#Rahul Ramakrishnan
#Stochastic Optimization
#Algorithmic Trading Script
'''
        ------------------ To Do: -------------------
	0. Print out equation, fitness, best ----DONE
        1. Add more diversity preserving
                a. Roullette Wheel --------------DONE
                b. Tournament Selection ---------DONE
        2. Graph the evolution of the different methods
        3. Add more terminal nodes (data from nasdaq)
        4. Add more functional nodes
        5. Convert for loops to map & reduce
        6. Use filter when you can 
        7. Convert map and reduce to HADOOP Fast Code
        8. Become more memory efficient  
	9. Create training data -----------------DONE
	10. Separate the Genetic_Program.py into separate modules in a package __init__.py
	11. Switch to list object with average fitness methods that gets passed around
	12. Avoid having a list
'''

import genetic_program as GP
import config
import test_program as TP

#Initialize objects and literals
population = GP.initializePopulation(config.population_size)
size = len(population)

for generation in xrange(0, config.generations):		
	print "----------Generation: %d----------" %(generation)
	for tree in xrange(0, size):			
		GP.performMutation(population)
		GP.performCrossover(population)
	GP.generateFitnesses(population)
	TP.printEquationPopulation(population)	
	GP.tournamentParentSelection(population)
	GP.calculateAverageFitness(population)	

print "============= After genetic program ===================="
TP.printEquationPopulation(population)

