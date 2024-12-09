from lab2.utils_lab2 import read_data,write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def bin_search(arr, key):
    lt = -1
    rt = len(arr)
    while rt - lt > 1:
        m = (rt+lt) // 2
        if key > arr[m]:
            lt = m
        else:
            rt = m

    if rt < len(arr) and arr[rt] == key:
        return rt
    else:
        return -1



def task4():
    n, arr_n, k, arr_k = read_data(PATH_INPUT)
    ans_arr = [bin_search(arr_n, el) for el in arr_k]
    write_data(PATH_OUTPUT, ans_arr)
    return ans_arr

if __name__ == '__main__':
    task4()