import sys
#sys.path.append("/media/fares/code/Python")

from Optim.algorithms.bbo.init import Init
from Optim.tools import *
from Optim.solution import solution

import random
import timeit
import copy
from operator import attrgetter


# tha max immigration value
immigration = -1

# the max emigration value
emigration = -1

# tha max mutation value
mutation = -1

# the bbo iterations
iterations = -1

# the initial population solutions set
population = -1

# the initial size of our echosystem
habitats = 0

# the list of the solutions working on
solutions = []

# the best solution
best = ''

###
def Initialise():
	"""
	to initialize our set of solutions which we gonna use next in our
	Bbo method.
	"""
	global habitats
	global solutions
	global best

	# the init initialization, go to init Class
	begin = Init(population, iterations, mutation, emigration, immigration)


	# to get the initial solutions set to use,go to init Class
	begin.Merge()

	# set the solutions variable
	solutions = begin.solutions.copy()

	# the initial size of our echosystem
	habitats = len(solutions)

	# intiliase the solution
	best = min(solutions, key=attrgetter('fitness'))

	SetMigrationRates()


def SetMigrationRates() :
	"""
	to set the immigration and migration rates of the function,it depends on the formula.
	please see the research paper to understand.
	"""
	k=habitats
	for i in solutions:
		i.immigration = immigration*(1 - k/habitats)
		i.emigration = emigration*(k/habitats)
		k -= 1


def Migrate():
	"""
	this is the Migration method, that does the double work of both
	migration and of course immigration.
	because when an item immigrates from a solution, it migrate to another.
	"""
	global solutions
	global habitats

	for i in solutions:
		copy_i = i.vector.copy()

		if i.immigration > random.uniform(0, MAX_IMMIGRATION):
			for j in solutions:
				# from here to bottom down we used a copied version to work on
				# bcz we need to check the validity of the solution
				# so check the temporary var 's ,& we insert or not after

				if (j.emigration > random.uniform(0, MAX_EMIGRATION)) and (i != j):

					ss = j.vector[random.randint(0, len(j.vector)-1)]
					copy_i[random.randint(0, len(i.vector)-1)] = ss  # we should use only this one

					if Validity(copy_i) is True:
						i.vector = copy_i

					break


def Mutation():
	"""
	as the one just above does the Migration, this do th Mutation
	by replacing an arbitrary item from the solution, and replace it
	by another arbitrary from the items list.
	Please go back to the paper that talks about the BBO.
	"""
	global solutions

	for i in solutions:
		if mutation > random.random()/10:
			s = i.vector.copy()
			# the cause as migration

			s[random.randint(0, len(s)-1)] = \
				Valid_Allocations[random.randint(0, len(Valid_Allocations)-1)]

			if Validity(s) is True:
				i.vector = s


def bbo(new_immigration, new_emigration, new_mutation, new_iterations, new_population):
	"""
	well basically it is as the main, nothing just call it to lunch the process.
	the result is as follows::
	{'fitness': fitness,
		'solution': result,
		'time': the time needed for calculating the solution}
	"""

	global immigration
	global emigration
	global mutation
	global iterations
	global population

	# attributing the values
	immigration, emigration, mutation, iterations, population =\
		new_immigration, new_emigration, new_mutation, new_iterations, new_population

	# check the case of the error
	if immigration == -1 or emigration == -1 or \
			mutation == -1 or iterations == -1 or population == -1:

		raise Exception("One or all of the values has an incorrect values.")

	global habitats
	global solutions
	global best

	start = timeit.default_timer()

	print("         INITILISING\n")
	Initialise()  # initializing

	for iteration in range(iterations):
		#print("Iteration::", iteration, "\n")

		Migrate()

		Mutation()

		habitats = len(solutions)  # the habitats changes

		# in this scope we gonna calculate the fitness after the end of the execution
		for sol in solutions:
			sol.fitness = Fitness(sol.vector)

		SetMigrationRates()

		new_one = min(solutions, key=attrgetter('fitness'))
		if new_one.fitness < best.fitness:
			best = copy.deepcopy(new_one)


	# send the results
	fit = best.fitness
	result = best.vector

	return {'fitness': fit, 'solution': result, 'time': timeit.default_timer() - start}



def bboCheck(new_immigration, new_emigration, new_mutation, new_iterations, new_population, check):
	"""
	well basically it is as the main, nothing just call it to lunch the process.
	the result is as follows::
	{'fitness': fitness,
		'solution': result,
		'time': the time needed for calculating the solution}
	"""
	check_values = []

	global immigration
	global emigration
	global mutation
	global iterations
	global population
	global habitats
	global solutions
	global best

	# attributing the values
	immigration, emigration, mutation, iterations, population =\
		new_immigration, new_emigration, new_mutation, new_iterations, new_population


	start = timeit.default_timer()

	print("         INITILISING\n")
	Initialise()  # initializing

	for iteration in range(1, iterations+1):
		#print("Iteration::", iteration, "\n")

		Migrate()

		Mutation()

		habitats = len(solutions)  # the habitats changes

		# in this scope we gonna calculate the fitness after the end of the execution
		for sol in solutions:
			sol.fitness = Fitness(sol.vector)

		SetMigrationRates()

		new_one = min(solutions, key=attrgetter('fitness'))
		if new_one.fitness < best.fitness:
			best = copy.deepcopy(new_one)

		if iteration % check == 0 and iteration >= check:
			print(iteration)
			check_values.append(round(best.fitness, 3))

	file = open('/home/fares/Desktop/time.txt', 'a+')
	file.write(str(timeit.default_timer() - start) + "\n")
	file.close()

	return check_values



if __name__ == '__main__':
	print(bbo(1, 1, 0.1, 150, 100))