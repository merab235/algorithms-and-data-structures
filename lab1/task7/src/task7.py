from lab1.utils_lab1 import read_data,write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def ins_sort_plus(n,arr):
    arr = [(item, ind + 1) for ind, item in enumerate(arr)]
    for j in range(1, len(arr)):
        i = j-1
        k = arr[j]
        while arr[i][0] > k[0] and i >= 0:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = k

    return arr[0][1], arr[n//2][1], arr[-1][1]

def task7():
    n, arr = read_data(PATH_INPUT, arr_num_type=float)
    ans = ins_sort_plus(n,arr)
    write_data(PATH_OUTPUT, ans)
    return ans

if __name__ == '__main__':
    task7()