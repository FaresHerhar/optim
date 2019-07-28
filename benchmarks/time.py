"""
to represent the possible allocations by rank
{rank: [(row, rank),......]}
"""
Rank_Allocations = {1: []}


"""
the Valid_Allocations is a constant that simulates the current status
of the bay, it is represented as:: (row, container rank).
"""
Valid_Allocations = [
            (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
            (3, 2), (3, 3), (3, 4), (3, 5),
            (4, 2), (4, 3), (4, 4), (4, 5),
            (5, 2), (5, 3), (5, 4), (5, 5),
                            (6, 4), (6, 5),
    (7, 1), (7, 2), (7, 3), (7, 4), (7, 5),
    (8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
                                    (9, 5),
            (10, 2), (10, 3), (10, 4), (10, 5),
    (11, 1), (11, 2), (11, 3), (11, 4), (11, 5),
                                (12, 4), (12, 5)
]


"""
the empty cells in each row, we need it to generate the allocations
"""
EmptyCells = {1: 2, 2: 1, 3: 2, 4: 3, 5: 4, 6: 4, 7: 3, 8: 4, 9: 3, 10: 3, 11: 3, 12: 3}

"""
IncomingContainers[index] container of || index=rank

in the example:
---------------
1 container of rank 1
1 container of rank 2
1 container of rank 3
1 container of rank 4
1 container of rank 5
"""
IncommingContainers = [4, 5, 5, 5, 7]


"""
the time unit for horizontal displacement
"""
TimeUnit1 = 1.0
TimeUnit11 = 0.4*TimeUnit1


"""
the times needed for horizontal displacement for reach row
"""
MoveTimes = {
    1: TimeUnit1,
    2: TimeUnit1+TimeUnit11,
    3: TimeUnit1+TimeUnit11*2,
    4: TimeUnit1+TimeUnit11*3,
    5: TimeUnit1*2,
    6: TimeUnit1*2+TimeUnit11,
    7: TimeUnit1*2+TimeUnit11*2,
    8: TimeUnit1*2+TimeUnit11*3,
    9: TimeUnit1*3,
    10: TimeUnit1*3+TimeUnit11,
    11: TimeUnit1*3+TimeUnit11*2,
    12: TimeUnit1*3+TimeUnit11*3
}


"""
the time unit for vertical displacement
"""
TimeUnit2 = 70 / 60


"""
the times needed for vertical displacement for reach row
"""
ShiftTimes = {
    1: TimeUnit2,
    2: TimeUnit2*2,
    3: TimeUnit2*3,
    4: TimeUnit2*4,
    5: TimeUnit2*5,
}

################
# for Bbo
MAX_EMIGRATION = 1
MAX_IMMIGRATION = 1

MAX_MUTATION = 0.1
MIN_MUTATION = 0.01

#################
# for Ga
MAX_GA_MUTATION = 0.1
MIN_GA_MUTATION = 0.01

MAX_GA_CROSS_OVER = 0.97
MIN_GA_CROSS_OVER = 0.3
