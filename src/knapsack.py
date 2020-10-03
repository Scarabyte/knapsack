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
box1 = {
        "weight": 7,
        "value": 5}

box2 = {
        "weight": 2,
        "value": 4}

box3 = {
        "weight": 1,
        "value": 7}

box4 = {
        "weight": 9,
        "value": 2}

boxes = [
        {"weight": 7, "value": 5},
        {"weight": 2, "value": 4},
        {"weight": 1, "value": 7},
        {"weight": 9, "value": 2}]

MAXWEIGHT = 15

# 2. Solutions; each element in the set (each box in the set of boxes)
#    randomly either selected or not.


def generatesolutions(boxes):
    """For each element in the boxes, either select it or not.

    (Return a list of len(boxes) populated with either True or False)
    """
    solution = []
    [solution.append(getrandbits(1)) for x in len(boxes)]
    return solution

# 3. Score; add up the weights of each box selected (i.e. the ones where the
#    the solution has a 1) and if it's less than MAXWEIGHT, then add up the
#    values to get the score.


def getscore(boxes, solution):
    """Get the score for each solution."""
    weightsum = score = 0
    for i in range(len(solution)):
        weightsum += solution[i]*boxes[i]["weight"]

    if weightsum <= MAXWEIGHT:
        for i in range(len(solution)):
            score += solution[i]*boxes[i]["value"]

    return score

# 4. Tournament selection - given two solutions, return the one that has
#    the higher score. (Randomly select the solutions.)


def getsolutionscoredict(solution, score):
    """Create a dictionary with each solution and its corresponding score."""
    return {"solution": solution, "score": score}


def selectsolutions(solutionspace):
    """Randomly select two solutions with scores."""
    return [choice(solutionspace), choice(solutionspace)]


def tournament():
    """Tournament selection.

    The solution with the higher score wins.
    """
    pass


if __name__ == "__main__":
    solutionspace = []  # Perhaps not a good variable name but whatever.
    pass
