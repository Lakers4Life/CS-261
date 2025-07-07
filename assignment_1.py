#Name: Ranson Touch
#OSU Email: touchr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1 - Python Fundamentals
# Due Date: 6/8/2025
# Description: 10 separate problems must be solved in Python in order to ensure that Python fundamentals are learned.

import random
from static_array import *

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
def min_max(arr: StaticArray) -> tuple[int, int]:
    """A function that receives a one-dimensional array and returns a Python Tuple with 2 values - the min and max values"""
    min_value = arr.get(0)
    max_value = arr.get(0)

    for i in range(1, length(arr)):
        value = arr.get(i)
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    return (min_value, max_value)




