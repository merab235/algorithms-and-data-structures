from lab2.utils_lab2 import read_data, write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    arr1 = arr[p:q + 1]
    arr2 = arr[q + 1:r + 1]

    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[p + i + j] = arr1[i]
            i += 1
        else:
            arr[p + i + j] = arr2[j]
            j += 1

    while i < len(arr1):
        arr[p + i + j] = arr1[i]
        i += 1

    while j < len(arr2):
        arr[p + i + j] = arr2[j]
        j += 1


def task1():
    n, arr = read_data(PATH_INPUT)
    merge_sort(arr, 0, len(arr) - 1)
    write_data(PATH_OUTPUT, arr)
    return arr


if __name__ == '__main__':
    task1()