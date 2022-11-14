"""
Find Low/High Index of a Key in a Sorted Array

We’re given a sorted array of integers, nums, and an integer value, target. Return the low and high index
of the given target element. If the indexes are not found, return -1.

Example:
    array = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
    For target= 5: low = 2 and high = 9
"""

array = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]  # For target= 5: low = 2 and high = 9
array = [9, 6, 6, 6, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1,
         1]  # For target= 2: low = 17 and high = 21
array = [[1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6,
          9]]  # For target= 8: low = -2 and high = -2


def find_low_index(nums, target):
    _index = 0
    for index, n in enumerate(nums):
        if n == target:
            _index = index
            break
    if _index:
        return _index
    return -2


def find_high_index(nums, target):
    _index = 0
    _total_indices = len(nums) - 1
    nums.reverse()
    for index, n in enumerate(nums):
        if n == target:
            _index = index
            break
    if _index:
        return _total_indices - _index
    return -2


low_index, high_index = find_low_index(array, 8), find_high_index(array, 8)

print("low_index: ", low_index)
print("high_index: ", high_index)
