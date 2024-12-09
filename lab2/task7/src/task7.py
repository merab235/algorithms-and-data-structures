from lab2.utils_lab2 import read_data,write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def max_subarray_linear(arr):
    min_pref = min(arr[0], 0)
    max_sum = arr[0]
    cur_sum = arr[0]
    for i in range(1,len(arr)):
        cur_sum += arr[i]
        max_sum = max(max_sum, cur_sum - min_pref)
        min_pref = min(cur_sum, min_pref)
    return max_sum


def max_subarray_linear_for_comparing(nums):
    max_sum = nums[0]
    cur_sum = 0

    for i in nums:
        if cur_sum < 0:
            cur_sum = 0

        cur_sum += i
        max_sum = max(max_sum, cur_sum)

    return max_sum



def task7():
    n, arr = read_data(PATH_INPUT)
    arr_ans1 = max_subarray_linear_for_comparing(arr)
    arr_ans2 = max_subarray_linear(arr)
    write_data(PATH_OUTPUT, arr_ans1, arr_ans2)
    return arr_ans1, arr_ans2

if __name__ == '__main__':
    task7()