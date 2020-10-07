from ArraySort import arraySort

class main():

    list1 = [2,3,1,3,2,4,6,7,9,2,19]
    list2 = [2,1,4,3,9,6]
    new_arraySort = arraySort(list1, list2)
    length = len(list2)
    new_arraySort.handleArray1(length)