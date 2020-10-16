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


class Test_generateSolution(unittest.TestCase):
    """Test the generateSolution function"""

    # Notes: I want to supply a box with a certain number of items in it,
    # and I want the function to either select that item or not.
    # Since each element in the box is either selected or not randomly,
    # I don't know what the solution will actually look like; it will change
    # every time. However, I know the form the solution should take.
    # The solution should have the same number of elements as the box,
    # and all of its elements should be either 0 or 1 to indicate whether
    # an element was selected.

    # Let's start by generating a solution to use for this set of tests.
    solution = knapsack.generateSolution(box)
    print("solution = ", solution)

    def setUp(self):
        pass

    # To start with, the length of the solution should be the same as the
    # number of items in the box, i.e. if I supply a box with 4 items in it,
    # the function should return a list with 4 elements in it to indicate
    # whether each item was selected or not.
    def test_solution_type(self):
        """The solution should be a list of elements."""
        self.assertIsInstance(self.solution, list)

    def test_solution_length(self):
        """The solution should have the same number of elements as the box."""
        self.assertEqual(len(box), len(self.solution))

    # Now, the solution should be a list of len(box) boolean values (0 or 1)
    # to indicate whether or not each item in the box was selected.
    def test_solution_values(self):
        """The solution values should be either 0 or 1."""
        allowedValues = [0, 1]
        [self.assertTrue(item in allowedValues) for item in self.solution]

    # I assume that the input to generateSolution is a list of items.
    # But what if the input isn't a list?
    # Some object types have a len() property, others don't.
    def test_incorrect_input_type(self):
        """generateSolution should return a meaningful error with bad input."""
        self.assertRaises(knapsack.InvalidInputError,
                          knapsack.generateSolution, 3)


class Test_getSolutionScore(unittest.TestCase):
    """Given the box of all items and a solution, calculate the score."""
    # The items should have properties including weight and score.
    # The box contains all items.
    # The solution is a binary list that indicates if an item was selected.
    # For all selected items, add up the total score.

    # Let's start by giving it a known example, and seeing if it calculates
    # the correct score.
    # For solution = [1, 0, 0, 1] -> score = 0 because it's over the MAXWEIGHT
    def test_known_example(self):
        """Verify that the right score is returned for known solutions."""
        self.assertEqual(knapsack.getSolutionScore(box, [1, 0, 0, 1]), 0)
        self.assertEqual(knapsack.getSolutionScore(box, [1, 0, 1, 0]), 12)
        self.assertEqual(knapsack.getSolutionScore(box, [0, 1, 1, 1]), 13)
        self.assertEqual(knapsack.getSolutionScore(box, [0, 1, 0, 0]), 4)

    # Now, what if the input is not correct - solution is not a list?
    def test_solution_not_a_list(self):
        """If the supplied solution is not a list, raise InvalidInputError"""
        self.assertRaises(knapsack.InvalidInputError,
                          knapsack.getSolutionScore, box, 2)

    # What if solution IS a list, but not binary?
    def test_solution_list_is_not_binary(self):
        """If the solution is not a binary list, raise InvalidInputError"""
        self.assertRaises(knapsack.InvalidInputError,
                          knapsack.getSolutionScore, box, [0, 1, 2, 1])

    # What format do I expect the box to have?
    # 1. List of items
    # 2. Each item is a dictionary including a weight and score
    # (Note: Maybe we'll change this later, but for now that's what we have.)
    def test_box_is_not_a_list(self):
        """If the box is not a list of items, raise InvalidInputError"""
        self.assertRaises(knapsack.InvalidInputError,
                          knapsack.getSolutionScore, "box", [1, 1, 1, 0])

    def test_items_are_not_dictionaries(self):
        """Each item in the box should be a dictionary"""
        badbox = [item1, item2, "Not a dictionary", item4]
        self.assertRaises(knapsack.InvalidInputError,
                          knapsack.getSolutionScore, badbox, [1, 1, 0, 1])

    def test_item_dictionary_contents(self):
        """The item's dictionary should include a weight and a value"""
        baditem = {"weight": 3, "somekey": 6}
        badbox = [item1, baditem, item3, item4]
        self.assertRaises(knapsack.InvalidInputError,
                          knapsack.getSolutionScore, badbox, [0, 1, 0, 1])

    def test_item_dictionary_values(self):
        """The value of each key in the item dictionary should be an int"""
        baditemvalue = {"weight": "notint", "somekey": 6}
        badbox = [item1, item2, baditemvalue, item4]
        self.assertRaises(knapsack.InvalidInputError,
                          knapsack.getSolutionScore, badbox, [1, 1, 0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
