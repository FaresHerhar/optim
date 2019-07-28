import random
import timeit

from tools import *

###
# the initial population solutions set
population = -1

# the best solution
# check the benchmark file
THE_BEST_ESTIMATED = 10000
best = [[], THE_BEST_ESTIMATED]

# the solutions found so far
solutions = []

###
def Exist(list_):
	"""
	we may find the same solution over and over, this just to prevent that.
	a boolean output.
	"""
	size_ = len(list_)
	for data in solutions:
		if len(set(data) & set(list_)) == size_:
			return True

	return False


def Merge():
	limit = MaxPossibleIterations()

	if population > limit:
		print(population, limit)
		print("ATTENTION::: the the population wanted is bigger then MaxPossibleIterations")

	else:
		limit = population



	global best
	done = 0

	while done != limit:
		#print("Iterating:: ", done, "of", population)

		list_ = []
		count = 1

		for container in IncommingContainers:

			# in case the number of containers to insert is zero
			# it may generate an exception so we skip it this way :)
			if container == 0:
				pass
			else:
				# the sample method to generate a solution in a random way
				list_ += random.sample(Rank_Allocations[count], container)

			count += 1

		# to avoid the redefinitions of the Solutions, & then
		# we write the solution 'list' in a binary file after each solution generations
		if Exist(list_) is False and Validity(list_) is True:
			done += 1
			solutions.append(list_)
			fit = Fitness(list_)

			if best[1] > fit:
				best[0] = list_
				best[1] = fit


###
def normal(new_population):
	"""
	well basically it is as the main, nothing just call it to lunch the process.
	the result is as follows::
	{'fitness': fitness,
		'solution': result,
		'time': the time needed for calculating the solution}
	"""
	# because in the API  i ll add this option
	# he choices the number of population he want to work on

	global population
	population = new_population

	if population == -1:
		print("Error,no population set in.")
		exit(1)

	start = timeit.default_timer()
	SetRankAllocations()
	Merge()

	# send the results
	fit = best[1]
	result = best[0]

	return {'fitness': fit, 'solution': result, 'time': timeit.default_timer() - start}


if __name__ == '__main__':
	print(normal(100))