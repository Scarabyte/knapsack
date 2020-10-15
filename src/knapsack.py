# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:52:21 2020

@author: scara
"""
from random import getrandbits, choice
# The Knapsack Problem as described in https://youtu.be/MacVqujSXWE
#
# Steps:
# 1. Data; in this case items with weights and values
item1 = {
    "weight": 7,
    "value": 5}

item2 = {
    "weight": 2,
    "value": 4}

item3 = {
    "weight": 1,
    "value": 7}

item4 = {
    "weight": 9,
    "value": 2}

box = [
    {"weight": 7, "value": 5},
    {"weight": 2, "value": 4},
    {"weight": 1, "value": 7},
    {"weight": 9, "value": 2}]

MAXWEIGHT = 15

population = []

# 2. Solutions; each element in the set (each item in the box)
#    randomly either selected or not.


def generateSolution(box):
    """For each item in the box, either select it or not.

    (Return a list of len(box) populated with either True or False (0 or 1).)
    """
    if type(box) != list:
        raise InvalidInputError(
            "generateSolution must be given a list of items")

    solution = [getrandbits(1) for dummy in range(len(box))]
    return solution

# 3. Score; add up the weights of each box selected (i.e. the ones where the
#    the solution has a 1) and if it's less than MAXWEIGHT, then add up the
#    values to get the score.


def getSolutionScore(box, solution):
    """Given the box, get the score for a solution."""

    if type(solution) != list:
        raise InvalidInputError("solution must be a binary list of items")

    for item in solution:
        if item not in [0, 1]:
            raise InvalidInputError("solution must be a binary list")

    if type(box) != list:
        raise InvalidInputError("box must be a list of items")

    for item in box:
        if type(item) != dict:
            raise InvalidInputError("Each item must be a dictionary")

    weightsum = score = 0
    for i in range(len(solution)):
        weightsum += solution[i] * box[i]["weight"]

    if weightsum <= MAXWEIGHT:
        for i in range(len(solution)):
            score += solution[i] * box[i]["value"]

    return score


def getsolutionscoredict(solution, score):
    """Create a dictionary with each solution and its corresponding score."""
    return {"solution": solution, "score": score}


def buildpopulation(population, solutionscoredict):
    """Build up the population with generated solutions and their scores."""
    population.append(solutionscoredict)
    return population


def selectsolutions(population):
    """Randomly select two solutions with scores from the population."""
    selectedsolutions = [choice(population), choice(population)]
    return selectedsolutions

# 4. Tournament selection - given two solutions, return the one that has
#    the higher score. (Randomly select the solutions.)


def tournament(solution1, solution2):
    """Tournament selection.

    The solution with the higher score wins.
    """
    if solution1["score"] > solution2["score"]:
        return solution1
    else:
        return solution2
    # There is almost certainly a better way to do this, but I think it works

# 5. The winners of the tournament are the parents for the next generation.


def collectparents(winningsolution):
    """After we've done two tournaments, we have parents for the next gen."""
    parents = []
    selectedsolutions = selectsolutions(population)
    parents.append(tournament(selectedsolutions[0],
                              selectedsolutions[1]))
    # Wondering if we actually need this...
    # It's not right as-is, anyway

# 6. The children are created by randomly choosing each element from either
#    one parent or the other. (There are other ways of creating the child.)


def crossover(parents):
    """Crossover as described in the video."""
    # Let's say (as a first approximation) that the child has a 50/50 chance
    # of inheriting a value from either parent.
    # (Later we could add a crossover rate...)
    child = []
    for i in range(len(parents[0]["solution"])):
        child.append(choice([parents[0]["solution"][i],
                             parents[1]["solution"][i]]))
    return child

# 7. For each element in the child solution, there's some chance that it could
#    be randomly changed.


def mutation(child):
    """Mutation as described in the video."""
    # For each element in the child, there's some probability that
    # the value could flip from a 0 to a 1 or vice versa.
    # Let's say (as a first approximation) that there's a 1/8 chance
    # of a mutation happening.
    for i in range(len(child)):
        if getrandbits(3) == 7:
            child[i] = int(not(child[i]))
    return child


def buildnextgeneration():
    """Build up the next generation of solutions."""
    pass


class InvalidInputError(TypeError):
    pass


if __name__ == "__main__":
    item1 = {
        "weight": 7,
        "value": 5}

    item2 = {
        "weight": 2,
        "value": 4}

    item3 = {
        "weight": 1,
        "value": 7}

    item4 = {
        "weight": 9,
        "value": 2}

    box = [
        {"weight": 7, "value": 5},
        {"weight": 2, "value": 4},
        {"weight": 1, "value": 7},
        {"weight": 9, "value": 2}]

    MAXWEIGHT = 15

    population = []

    parents = []

    nextgeneration = []

    while len(nextgeneration) < 8:
        for i in range(2):
            solution = generateSolution(box)
            score = getSolutionScore(box, solution)
            solutiondict = getsolutionscoredict(solution, score)
            population = buildpopulation(population, solutiondict)
            selectedsolutions = selectsolutions(population)
            winningsolution = tournament(selectedsolutions[0],
                                         selectedsolutions[1])
            parents.append(winningsolution)

        child = crossover(parents)
        child = mutation(child)
        # Wait: child still includes a score. But score could be different now.

        nextgeneration.append(child)
        # nextgeneration is now a new solution.
        # If we do this whole thing again, we have another new solution.
        # So then we should use the next generation as the new parents.
