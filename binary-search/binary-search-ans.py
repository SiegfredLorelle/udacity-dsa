"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    array = input_array
    while True:
        # If index error is raised then the value is not in the list
        try:
            # Index of the middle element (if 2 middle elements then this is the lowerbound)
            middle_index = len(array) // 2
            # If value is the center element, then return its index
            if value == array[middle_index]:
                return input_array.index(value)
            # If value is less than the center element then change the array's element to only consists values below the center element
            elif value < array[middle_index]:
                array = array[:middle_index]
            # If value is more than the center element then change the array's element to only consists values above the center element
            else:
                array = array[middle_index + 1:]
        except IndexError:
            return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)