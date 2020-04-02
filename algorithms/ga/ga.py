from Optim.algorithms.ga.init import Init
from Optim.tools import *
from Optim.solution import solution

import random
import timeit
import copy
from operator import attrgetter

####################
population = -1

Generations = -1

Cross_Rate = -1

Muta_Rate = -1
####################
best = ''
parents = None
individuals = None
solutions = None
parents = None
children = None


def Initialise():
    global best
    """
	to initialize our set of solutions which we gonna use next in our Ga.
	:return:
	"""

    global individuals
    global solutions
    global parents
    global children

    # the init initialization, go to init Class
    begin = Init(population, Generations, Cross_Rate, Muta_Rate)

    # to get the initial solutions set to use,go to init Class
    begin.Merge()

    # set the solutions variable
    solutions = begin.solutions.copy()
    parents = []
    children = []

    # the initial size of our societe
    individuals = len(solutions)
    best = min(solutions, key=attrgetter('fitness'))


def Selection():
    """
    We selection the parents that will marry ad since every 2 parents select bring 2 children
    meaning solutions.

    we use tournament methode of selection cause its the easiest and permit to select efficiently
    the parents.
    """
    global solutions
    global parents

    # Numbero of Children = the number of the newborn people in the next population  = round(Cross_Rate*population)
    Number_parents = round(Cross_Rate * population) + 2
    done = 0
    while done != Number_parents:
        luck = random.randint(1, population - 1)
        tributes = random.sample(solutions, luck)
        highest = min(tributes, key=attrgetter('fitness'))
        if highest not in parents:
            parents.append(highest)
            done = done + 1


def MPMUX(x, y, z):
    """
    Multi parents Multi point crossover.
    """
    global parents
    papa = [x, y, z]
    while True:
        c1 = []
        c2 = []
        for i in range(len(x.vector)):
            c1 = c1 + [random.choice([x.vector[i], y.vector[i], z.vector[i]])]
            c2 = c2 + [random.choice([x.vector[i], y.vector[i], z.vector[i]])]
        if c1 != c2 and c1 not in papa and c2 not in papa:
            break
    return c1, c2


def Crossover():
    """
    in this process we consider the vector as ADN full of genes and of course
    it will be crossover of genes.

    there many methodes for crossover, we will go with the uniform crossover
    where each gene has a chance to go either to the first child or the second.
    """
    global parents
    global children
    global Cross_Rate

    Num_Children = round(Cross_Rate * population)
    # parents = sorted(parents, key=lambda x: x.fitness, reverse=True)
    children_tmp = []
    done = 0
    limit = len(parents) - 3

    while done != Num_Children:
        sel_parts = random.sample(parents, 3)
        child_1, child_2 = MPMUX(sel_parts[0], sel_parts[1], sel_parts[2])
        if not (child_1 in children_tmp) and not (child_2 in children_tmp):
            if Validity(child_2) is True and Validity(child_1) is True:
                if done - Num_Children == -1:
                    done = done + 1
                    children_tmp.append(int(Fitness(child_1) > Fitness(child_2)) * child_1 + int(
                        Fitness(child_2) > Fitness(child_1)) * child_2
                        + int(Fitness(child_2) == Fitness(child_1)) * random.choice([child_1, child_2]))
                else:
                    done = done + 2
                    children_tmp.append(child_1)
                    children_tmp.append(child_2)

    for child in children_tmp:
        children.append(solution(child, Fitness(child)))


def Mutation():
    """
    this do th Mutationby replacing an arbitrary item from the solution, and replace it
    by another arbitrary from the items list.
    """

    global children

    for i in children:

        if Muta_Rate > random.random() / 10:
            s = i.vector.copy()

            s[random.randint(0, len(s) - 1)] = \
                Valid_Allocations[random.randint(
                    0, len(Valid_Allocations) - 1)]

            if Validity(s) is True:
                i.vector = s
                i.fitness = Fitness(s)


def offspring():
    global solutions
    global children

    for child in children:
        if child.vector in (i.vector for i in solutions):
            pass
        else:
            lowest = max(solutions, key=attrgetter('fitness'))
            solutions[solutions.index(lowest)] = child


def Ga(new_population, new_Generations, new_Cross_Rate, new_Muta_Rate):
    """
    well basically it is as the main, nothing just call it to lunch the process.
    the result is as follows::
    {'fitness': fitness,
            'solution': result,
            'time': the time needed for calculating the solution}
    """
    global population
    global Generations
    global Cross_Rate
    global Muta_Rate

    # attributing the values
    population, Generations, Cross_Rate, Muta_Rate = \
        new_population, new_Generations, new_Cross_Rate, new_Muta_Rate

    # check the case of the error
    if population == -1 or Generations == -1 or Cross_Rate == -1 or Muta_Rate == -1:
        raise Exception("One or all of the values has an incorrect values.")

    global individuals
    global solutions
    global best
    global parents
    global children
    global best

    start = timeit.default_timer()

    print("         INITILISING")
    Initialise()  # initializing

    for generation in range(Generations):
        #print("Iteration::", generation)

        Selection()

        Crossover()

        Mutation()

        offspring()

        parents = []
        chilren = []

        new_one = min(solutions, key=attrgetter('fitness'))
        if new_one.fitness < best.fitness:
            best = copy.deepcopy(new_one)

    return {'fitness': best.fitness, 'solution': best.vector, 'time': timeit.default_timer() - start}


if __name__ == '__main__':
    print(Ga(10, 10, 0.8, 0.1))
