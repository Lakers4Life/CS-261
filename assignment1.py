#Name: Ranson Touch
#OSU Email: touchr@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment 1 - Python Fundamentals
# Due Date: 6/8/2025
# Description: 10 separate problems must be solved in Python in order to ensure that Python fundamentals are learned.

import random

from static_array import StaticArray

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
def min_max(arr: StaticArray) -> tuple[int, int]:
    """A function that receives a one-dimensional array and returns a Python Tuple with 2 values - the min and max values"""
    min_value = arr.get(0)
    max_value = arr.get(0)

    for i in range(1, arr.length()):
        value = arr.get(i)
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    return min_value, max_value

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
def fizz_buzz(arr: StaticArray) -> StaticArray:
    """A function that receives a StaticArray of integers and returns a new StaticArray object with the content of the original array """

    result = StaticArray(arr.length())

    for i in range(0, arr.length()):
        value = arr.get(i)

        if value % 3 ==0 and value % 5 == 0:
            value = "fizzbuzz"
        elif value % 5 == 0:
            value = "buzz"
        elif value % 3 == 0:
            value = "fizz"

        result.set(i, value)        # Continues the Loop

    return result

# ------------------- PROBLEM 3 - REVERSE -----------------------------------
def reverse(arr: StaticArray) -> None:
    """A function that receives a StaticArray and reverses the order of the elements in the array."""

    left = 0
    right = arr.length() - 1

    while left < right:
        left_value = arr.get(left)
        right_value = arr.get(right)

        arr.set(left, right_value)
        arr.set(right, left_value)

        left += 1
        right -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------
def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """A function that receives a StaticArray and an integer value called steps, and creates and returns a new StaticArray object with their position shifted right or left steps number of times"""
    N = arr.length()

    k = steps % N
    if k < 0:
        k += N

    result = StaticArray(N)

    for i in range(N):
        value = arr.get(i)
        new_index = (i +k) % N
        result.set(new_index, value)

    return result

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
def sa_range(start: int, end: int) -> StaticArray:
    """A function that receives 2 integers start and end, and returns a StaticArray that contains all the integers between start and end(inclusive) """
    length = abs(end - start) + 1

    result = StaticArray(length)

    step = 1 if end >= start else -1

    current = start
    for i in range(length):
        result.set(i, current)
        current += step

    return result
# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
def is_sorted(arr: StaticArray) -> int:
    """A function that receives a StaticArray and returns an integer that describes whether the array is sorted. IIt returns 1 if the array is sorted in ascending order, -1 if the list is in descending order, or 0 if otherwise"""
    n = arr.length()
    if n <= 1:
        return 1

    ascending = True    # Assuming both are true until either or is proven wrong
    descending = True

    previous = arr.get(0)
    for i in range(1, n):
        value = arr.get(i)

        if not (value > previous):
            ascending = False

        if not (value < previous):
            descending = False

        if not ascending and not descending:
            return 0

        previous = value

    if ascending:
        return 1
    if descending:
        return -1
    return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------
def find_mode(arr: StaticArray) -> tuple[object, int]:
    """A function that receives a StaticArray and returns the mode of the element (the most-occurring element in the array and its frequency (how many times it appears). If there is more than one element that has the highest frequency, the one that occurs first in the array is selected."""

    n = arr.length()
    mode = arr.get(0)
    mode_counter = 1

    current = mode
    current_count = 1

    for i in range(1, n):
        value = arr.get(i)
        if value == current:
            current_count += 1
        else:
            if current_count > mode_counter:
                mode = current
                mode_counter = current_count
            current = value
            current_count = 1

    if current_count > mode_counter:
        mode = current
        mode_counter = current_count

    return (mode, mode_counter)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------
def remove_duplicates(arr: StaticArray) -> StaticArray:
    """A function that receives a StaticArray that is already in sorted order, and return a new StaticArray with all duplicate values removed"""
    n = arr.length()
    unique_count = 1
    for i in range(1, n):
        if arr.get(i) != arr.get(i-1):
            unique_count+=1

    result = StaticArray(unique_count)

    write_pointer = 0
    result.set(write_pointer, arr.get(0))
    for i in range(1, n):
        current = arr.get(i)
        previous = arr.get(i-1)
        if current != previous:
            write_pointer += 1
            result.set(write_pointer, current)

    return result
# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
def count_sort(arr: StaticArray) -> StaticArray:
    """"""
pass
# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------
def sorted_squares(arr: StaticArray) -> StaticArray:
    """"""
pass