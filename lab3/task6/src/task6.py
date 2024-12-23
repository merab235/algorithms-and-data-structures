from lab3.utils_lab3 import read_data, write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def sort_integer_nums(arr_a, arr_b):
    arr = [i*j for i in arr_a for j in arr_b]
    cnt_s_a = [0]*40001

    for i in arr:
        cnt_s_a[i] += 1
    sorted_arr = []
    for i in range(len(cnt_s_a)):
        if cnt_s_a[i] != 0:
            sorted_arr.extend([i]*cnt_s_a[i])
    sm = sum(sorted_arr[i] for i in range(0, len(sorted_arr), 10))
    return sm



def task6(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    n_m, arr_a, arr_b = read_data(PATH_INPUT)

    ans = sort_integer_nums(arr_a, arr_b)
    write_data(PATH_OUTPUT, ans)
    return ans


if __name__ == '__main__':
    task6()