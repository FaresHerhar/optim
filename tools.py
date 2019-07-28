from math import factorial
from benchmarks.time import *

def MaxPossibleTuples(n,k):
	"""
	the max number of the solutions with no repetition and no order switching
	"""

	if n < k:
		print('error', '\n')
		exit(1)

	return factorial(n)/(factorial(k)*factorial(n-k))

def MaxPossibleIterations():
	"""
	the maximum number of possible Solutions.
	usually the number of Solutions found is less than the returned value of this function
	"""
	count = 1
	MaxIterations = 1
	for rank in IncommingContainers:
		MaxIterations *= MaxPossibleTuples(len(Rank_Allocations[count]), rank)
		count += 1
	return int(MaxIterations)


def Fitness(list):
	"""
	to calculate the Fitness or the evaluation value of the solution
	the formula as it is was given to us by the research paper author.
	to understand why check the Pdf, that describes the problem.
	"""
	rows = []  # it contains the already placed in rows
	value = 0

	for element in list:
		zero = element[0]  # to get the row number
		value += (2*MoveTimes[zero])+(ShiftTimes[EmptyCells[zero]-rows.count(zero)]/element[1])

		#  in the case where the solution is not valid
		#  we get ShiftTimes[EmptyCells[zero]-rows.count(zero)==0
		#  in this the solution is not valid
		rows.append(zero)

	return value


def Validity(list_):
	"""
	some solutions are correct when talking about a list of items
	but it is not necessarily true as a solution to the problem.
	therefore we check if it is Valid or not, based on our critics.
	"""

	# if the len(solution) is larger then the len(IncommingContainers)
	if len(list_) != sum(IncommingContainers):
		return False

	# to check the number of priority per container
	s = [0 for i in range(0, len(IncommingContainers))]
	for i in list_:
		s[i[1]-1] += 1  # to accesses the the i[1]-1 element,the occurrence number
	if s != IncommingContainers:
		return False

	# in the case where the solution is not valid
	# we get EmptyCells[zero]-rows.count(zero)==0
	# in this the solution is not valid
	rows = []
	for element in list_:
		zero = element[0]
		if EmptyCells[zero]-rows.count(zero) == 0:
			return False
		else:
			rows.append(zero)

	return True



def SetRankAllocations():
	"""
	when we get the Valid_Allocations list,we need to attribute the valid for each rank
	we can,not use it,but by doing it it becomes much easier
	"""

	# if it Exists we append
	# else we should create 'define' the dictionary element first,
	# bcz it can support many types in once

	for item in Valid_Allocations:
		i=item[1]
		if i in Rank_Allocations.keys():
			if item not in Rank_Allocations[i]:
				Rank_Allocations[i].append(item)
		else:
			Rank_Allocations[i] = []
			Rank_Allocations[i].append(item)
