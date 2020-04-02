import random

from Optim.tools import *
from Optim.solution import solution


class Init:
    # population, Generations, Cross_Rate, Muta_Rate
    # the values above are the maximum values of each of them as in definition
    def __init__(self, population, Generations, Cross_Rate, Muta_Rate):
        self.Generations = Generations
        self.population = population
        self.Muta_Rate = Muta_Rate
        self.Cross_Rate = Cross_Rate
        # it is a list that will contain the solutions
        # i mean the initial solutions to work on
        self.solutions = []

        # i put it as an automatic one
        SetRankAllocations()

    # to check if a solution Exists or not
    def Exist(self, list_):
        size_ = len(list_)
        for data in self.solutions:
            if len(set(data.vector) & set(list_)) == size_:
                return True
        return False

    def Merge(self):
        limit = MaxPossibleIterations()

        if self.population > limit:
            print(self.population, limit)
            print(
                "ATTENTION::: the the population wanted is bigger then MaxPossibleIterations")

        else:
            limit = self.population

        # i think that the third of MaxPossibleIterations might be enough
        # to stop the it when it equals to population
        done = 0
        while done != limit:
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
            if self.Exist(list_) is False:
                try:
                    # as we did the last time if the Fitness method
                    # generates an exception it means that it is not valid
                    k = solution(list_, Fitness(list_))

                    # i append the solutions list
                    self.solutions.append(k)
                    done = done + 1
                except:
                    pass
