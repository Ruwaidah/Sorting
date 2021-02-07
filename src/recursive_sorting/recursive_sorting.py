# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print(arrA, arrB)
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1

        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1

        elif arrA[a] > arrB[b]:
            merged_arr[i] = arrB[b]
            b += 1

        else:
            merged_arr[i] = arrA[a]
            a += 1
    print("mergged_array", merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print(arr)
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_side = merge_sort(arr[: mid])
    right_side = merge_sort(arr[mid:])
    return merge(left_side, right_side)
    # return arr


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


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
