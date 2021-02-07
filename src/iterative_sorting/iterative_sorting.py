# TO-DO: Complete the selection_sort() function below
import random


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for index in range(cur_index+1, len(arr)):
            if arr[index] < arr[smallest_index]:
                smallest_index = index
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(0, len(arr)-1):
            print(i, change)
            if arr[i] > arr[i+1]:
                change = True
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


arr4 = random.sample(range(200), 50)
print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
print(bubble_sort(arr4))
