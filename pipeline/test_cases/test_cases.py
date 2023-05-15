"""
Test Cases module.
"""

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from function.basic_ops import sum_of_two_numbers

def test_sum_function_01():
    """
    Test Case 01
    """
    assert sum_of_two_numbers(15, 2) == 17

def test_sum_function_02():
    """
    Test Case 02
    """
    assert sum_of_two_numbers(0, 1) == 1

def test_sum_function_03():
    """
    Test Case 03
    """
    assert sum_of_two_numbers(4, 4) == 8
