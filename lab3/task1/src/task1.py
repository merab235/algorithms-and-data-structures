import random

from lab3.utils_lab3 import read_data, write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def quick_sort_p2(arr,l,r):
    if l < r:
        m = partition2(arr, l,r)
        quick_sort_p2(arr, l, m - 1)
        quick_sort_p2(arr, m + 1, r)

def partition2(arr, l, r):
    x_ind = random.randint(l,r)
    arr[l], arr[x_ind] = arr[x_ind], arr[l]
    x = arr[l]
    j = l
    for i in range(l+1, r+1):
        if arr[i] <= x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort_p3(arr,l,r):
    if l < r:
        lt, gt = partition3(arr, l, r)
        quick_sort_p3(arr, l, lt - 1)
        quick_sort_p3(arr, gt + 1,r)


def partition3(arr, l, r):
    x_ind = random.randint(l, r)
    arr[l], arr[x_ind] = arr[x_ind], arr[l]
    x = arr[l]
    lt = l
    eq = l
    gt = r
    while eq <= gt:
        if arr[eq] < x:
            arr[lt], arr[eq] = arr[eq], arr[lt]
            lt += 1
            eq += 1
        elif arr[eq] > x:
            arr[gt], arr[eq] = arr[eq], arr[gt]
            gt -= 1
        else:
            eq += 1

    return lt, gt


def task1(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    n, arr = read_data(PATH_INPUT)
    quick_sort_p3(arr, 0, n - 1)
    write_data(PATH_OUTPUT, arr)
    return arr


if __name__ == '__main__':
    task1()