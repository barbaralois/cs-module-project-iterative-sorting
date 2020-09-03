def linear_search(arr, target):
    # progress through the array item by item
    for i in range(len(arr)):
        # check if that item is the target
        if arr[i] == target:
            # if it is, return i. Otherwise it keeps going through the loop
            return i

    return -1   # if you get to the end and it isn't there: not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set variables for the smallest and largest unchecked values
    min = 0
    max = len(arr)-1

    while min <= max:
        # find the difference of the min and max positions
        mid = (min + max) // 2
        # guess the item right in the middle
        guess = arr[mid]
        if guess == target:
            # if that's the target, return it
            return mid
        elif target > guess:
            # if that's smaller than the target, set the min to one higher than the checked num
            min = mid + 1
        else:
            # if that's larger than the target, set the max to one lower than the checked num
            max = mid - 1

    return -1  # if you get to the end and it isn't there: not found
