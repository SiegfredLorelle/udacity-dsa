"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    # Base Case: Stop this function wen two elements left in array
    if len(array) > 2:
        
        # Decide pivot and starting index
        pivot_index = len(array) - 1
        current_index = 0

        # Loop until all elements lower than pivot is on its left, and all elements higher than pivot is on its right
        while True:
            # Stop loop when elements are sorted with respect to pivot
            if current_index == pivot_index:
                break
            # If current value is greater than pivot then switch elements so that current is on the right of pivot
            if array[current_index] > array[pivot_index]:
                # Save the current value (to be placed on the right of pivot)
                tmp = array[current_index]
                # Place the element on the closest left of pivot to the current position
                array[current_index] = array[pivot_index - 1]
                # Move pivot to the left by 1 
                array[pivot_index - 1] = array[pivot_index]
                # Place the current value to the previous position of pivot (now current is on the right of pivot)
                array[pivot_index] = tmp
                # Adjust pivot index since the value was moved
                pivot_index -= 1
            # If current value is less than pivot, then check the next value
            else:
                current_index += 1

        # After sorting elements by with respect to pivot, sort the left and right side of pivot by using the same function
        left = quicksort(array[:pivot_index])
        right = quicksort(array[pivot_index:])
        # Return the full array by combining the sorted left and right
        return left + right

    # Two elements left in array, this function is finished
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))