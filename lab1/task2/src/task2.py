from lab1.utils_lab1 import read_data,write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def ins_sort_2(arr):
    ind_arr = [-1] * len(arr)
    ind_arr[0] = 1
    for j in range(1, len(arr)):
        i = j - 1
        k = arr[j]
        while arr[i] > k and i >= 0:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = k
        ind_arr[j] = i + 2
    return ind_arr, arr

def task2():
    n, arr = read_data(PATH_INPUT)
    ans_arr = ins_sort_2(arr)
    write_data(PATH_OUTPUT, *ans_arr)
    return ans_arr

if __name__ == '__main__':
    task2()