from lab2.utils_lab2 import read_data, write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def max_subarray(arr, low, high):
    if low == high:
        return (low, high, arr[low])
    else:
        m = (low + high) // 2
        lt_low, lt_high, lt_sum = max_subarray(arr, low, m)
        rt_low, rt_high, rt_sum = max_subarray(arr, m + 1, high)
        crs_low, crs_high, crs_sum = max_cross_subarray(arr, low, m, high)
        if lt_sum >= rt_sum and lt_sum >= crs_sum:
            return (lt_low, lt_high, lt_sum)
        elif rt_sum >= lt_sum and rt_sum >= crs_sum:
            return (rt_low, rt_high, rt_sum)
        else:
            return (crs_low, crs_high, crs_sum)


def max_cross_subarray(arr, low, m, high):
    lt_sum = rt_sum = float('-inf')
    temp_sum = 0
    for i in range(m, low - 1, -1):
        temp_sum += arr[i]
        if temp_sum > lt_sum:
            lt_sum = temp_sum
            mx_lt = i

    temp_sum = 0
    for i in range(m + 1, high + 1):
        temp_sum += arr[i]
        if temp_sum > rt_sum:
            rt_sum = temp_sum
            mx_rt = i
    return (mx_lt, mx_rt, lt_sum + rt_sum)


def task6():
    n, arr = read_data(PATH_INPUT)
    razn_arr = [j - i for i, j in zip(arr, arr[1:])]
    arr_ans = max_subarray(razn_arr, 0, len(razn_arr) - 1)
    write_data(PATH_OUTPUT, arr_ans)
    return arr_ans


if __name__ == '__main__':
    task6()