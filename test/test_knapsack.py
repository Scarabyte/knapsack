# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:16:37 2020

@author: scara
"""
# Test the knapsack functions
import unittest
import src.knapsack as knapsack

item1 = {"weight": 7, "value": 5}
item2 = {"weight": 2, "value": 4}
item3 = {"weight": 1, "value": 7}
item4 = {"weight": 9, "value": 2}

box = [item1, item2, item3, item4]


class TestGenerateSolution(unittest.TestCase):
    """Test the generateSolution function"""

    # Notes: I want to supply a box with a certain number of items in it,
    # and I want the function to either select that item or not.

    def setUp(self):
        pass

    # To start with, the length of the solution should be the same as the
    # number of items in the box, i.e. if I supply a box with 4 items in it,
    # the function should return a list with 4 elements in it to indicate
    # whether each item was selected or not.
    def test_solution_length(self):
        solution = knapsack.generateSolution(box)
        self.assertEqual(len(box), len(solution))


if __name__ == "__main__":
    pass
