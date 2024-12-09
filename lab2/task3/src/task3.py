from lab2.utils_lab2 import read_data, write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def merge_sort_2(arr, p, r):
    k = 0
    if p < r:
        q = (p + r) // 2
        k = merge_sort_2(arr, p, q) + merge_sort_2(arr, q + 1, r) + merge_2(arr, p, q, r)
    return k


def merge_2(arr, p, q, r):
    # global k
    k = 0
    arr1 = arr[p:q + 1]
    arr2 = arr[q + 1:r + 1]

    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[p + i + j] = arr1[i]
            i += 1

        else:
            arr[p + i + j] = arr2[j]
            j += 1
            k += len(arr1) - i

    while i < len(arr1):
        arr[p + i + j] = arr1[i]
        i += 1
        k += len(arr2) - j

    while j < len(arr2):
        arr[p + i + j] = arr2[j]
        j += 1

    return k


def task3():
    n, arr = read_data(PATH_INPUT)
    k = merge_sort_2(arr, 0, len(arr) - 1)
    write_data(PATH_OUTPUT, k)
    return k


if __name__ == '__main__':
    task3()