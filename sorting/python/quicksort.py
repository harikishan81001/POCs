""""
1 - If the list is empty, return the list and terminate. (base case)
2 - Choose a pivot element in the list.
3 - Take all of the elements that are less than or equal to the pivot
    and use quicksort on them.
4 - Take all of the elements that are greater than the pivot and use
    quicksort on them.
5 - Return the concatenation of the quicksorted list of elements that are less
    than or equal to the pivot, the pivot, and the quicksorted list of elements
    that are greater than the pivot.

Note:
    Selecting the leftmost element as the pivot
"""


def quicksort(array):
    lessThenPivot = []
    greaterThenPivot = []
    pivotList = []

    if len(array) <= 0:
        return array

    pivot = array[0]
    for elm in array:
        if elm < pivot:
            lessThenPivot.append(elm)
        elif elm > pivot:
            greaterThenPivot.append(elm)
        else:
            pivotList.append(elm)
    lessThenPivot = quicksort(lessThenPivot)
    greaterThenPivot = quicksort(greaterThenPivot)
    return lessThenPivot + pivotList + greaterThenPivot


if __name__ == "__main__":
    print("Please input array list")
    arrayList = []
    while True:
        number = raw_input("Number/N (for termination)")
        if number == "N" or number == "":
            break
        arrayList.append(int(number))
    print quicksort(arrayList)
