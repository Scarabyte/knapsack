# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:52:21 2020

@author: scara
"""
from random import getrandbits, choice
# The Knapsack Problem as described in https://youtu.be/MacVqujSXWE
#
# Steps:
# 1. Data; in this case boxes with weights and values
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

boxes = [
    {"weight": 7, "value": 5},
    {"weight": 2, "value": 4},
    {"weight": 1, "value": 7},
    {"weight": 9, "value": 2}]

MAXWEIGHT = 15

population = []

# 2. Solutions; each element in the set (each box in the set of boxes)
#    randomly either selected or not.


def generateSolution(boxes):
    """For each element in the boxes, either select it or not.

    (Return a list of len(boxes) populated with either True or False)
    """
    solution = []
    [solution.append(getrandbits(1)) for x in range(len(boxes))]
    return solution

# 3. Score; add up the weights of each box selected (i.e. the ones where the
#    the solution has a 1) and if it's less than MAXWEIGHT, then add up the
#    values to get the score.


def getscore(boxes, solution):
    """Get the score for each solution."""
    weightsum = score = 0
    for i in range(len(solution)):
        weightsum += solution[i] * boxes[i]["weight"]

    if weightsum <= MAXWEIGHT:
        for i in range(len(solution)):
            score += solution[i] * boxes[i]["value"]

    return score

# 4. Tournament selection - given two solutions, return the one that has
#    the higher score. (Randomly select the solutions.)


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


def tournament(solution1, solution2):
    """Tournament selection.

    The solution with the higher score wins.
    """
    if solution1["score"] > solution2["score"]:
        return solution1
    else:
        return solution2
    # There is almost certainly a better way to do this, but I think it works


def collectparents(winningsolution):
    """After we've done two tournaments, we have parents for the next gen."""
    parents = []
    selectedsolutions = selectsolutions(population)
    parents.append(tournament(selectedsolutions[0],
                              selectedsolutions[1]))
    # Wondering if we actually need this...
    # It's not right as-is, anyway


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

    boxes = [
        {"weight": 7, "value": 5},
        {"weight": 2, "value": 4},
        {"weight": 1, "value": 7},
        {"weight": 9, "value": 2}]

    MAXWEIGHT = 15

    population = []

    parents = []

    for i in range(2):
        solution = generateSolution(boxes)
        score = getscore(boxes, solution)
        solutiondict = getsolutionscoredict(solution, score)
        population = buildpopulation(population, solutiondict)
        selectedsolutions = selectsolutions(population)
        winningsolution = tournament(selectedsolutions[0],
                                     selectedsolutions[1])
        parents.append(winningsolution)

    child = crossover(parents)
    child = mutation(child)
    # Wait: child still includes a score. But score could be different now.

    nextgeneration = []
    nextgeneration.append(child)
    # nextgeneration is now a new solution.
    # So if we repeat this whole thing again, we have two new...
    # (This implementation is not quite what was described in the video...)
