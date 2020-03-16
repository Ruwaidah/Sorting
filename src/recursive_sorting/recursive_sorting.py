# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print([0]*2)
    print(arrA, arrB)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    mid = len(arr) // 2
    print(merge([a for a in arr[:mid]], [b for b in arr[mid:]]))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


print(merge_sort([8, 2, 5, 4, 1, 3, 0]))
