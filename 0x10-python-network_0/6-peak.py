#!/usr/bin/python3
"""
find the peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """ find peak element"""
    if list_of_integers == []:
        return None

    def recursive(list_of_integers, left=0, right=len(list_of_integers) - 1):
        """ helper recursive function """
        mid = (left + right) // 2

        # check if the mid elem > its neighbors
        if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid])):
            return list_of_integers[mid]

        # if left of mid > its neigbor
        # find peak recursively in the left sublist
        if mid - 1 >= 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return recursive(list_of_integers, left, mid - 1)

        # if right neighbor of mid > mid elem
        # find the peak recursively in the right sublist
        reeturn recursive(list_of_integers, mid + 1, right)

    return recursive(list_of_integers)
