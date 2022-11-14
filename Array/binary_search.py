"""
Implement Binary Search on a Sorted Array

We are given an array of integers, nums, sorted in ascending order, and an integer value, target.
If the target exists in the array, return its index. If the target does not exist, then return -1.

"""

asc_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# asc_array = [1, 2, ]
asc_array = []

asc_array = []#, [0,1], [1,2,3], [-1,0,3,5,9,12], [-1,0,3,5,9,12]


def binary_search(array: list, searched_num: int):
    _len_array = len(array)
    if _len_array == 0:
        return -1

    if _len_array == 1:
        if array[0] == searched_num:
            return 0
        else:
            return -1
    _start_pointer, _end_pointer = 0, _len_array - 1
    while _start_pointer <= _end_pointer:
        _mid_index = int(abs(_start_pointer + _end_pointer)/2)
        if array[_mid_index] > searched_num:
            _end_pointer = _mid_index - 1
        elif array[_mid_index] < searched_num:
            _start_pointer = _mid_index + 1
        elif array[_mid_index] == searched_num:
            return _mid_index
    return -1

find_number = 3
num_index = binary_search(asc_array, find_number)
print(num_index)
if asc_array and asc_array[num_index] == find_number:
    print("Index found")
else:
    print("Index not found")
