import os
import doctest
import unittest

print('Current working directory:', os.getcwd())  # function in os are platform independent
os.system('dir')  # dir is executed in shell, so this is not platform independent


def average(values):
    """
    Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.01

    """
    return sum(values) / len(values)


doctest.testmod()  # performs tests embedded in docstring - wrong response is placed intentionally in docstring example


class MyFunctionalityTest(unittest.TestCase):
    
    def testAverage(self):
        self.assertEqual(average([20, 30, 70]), 40.0)


unittest.main()  # performs tests derived from unittest.TestCase
