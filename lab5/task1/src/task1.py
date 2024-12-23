from lab5.utils_lab5 import write_data, read_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def is_heap(arr):
    for i in range(len(arr)//2):
        rt = 2 * i + 2
        lt = 2 * i + 1

        if (rt < len(arr) and arr[i] > arr[rt]) or (lt < len(arr) and arr[i] > arr[lt]):
            return "NO"

    return "YES"


def task1(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    n, arr = read_data(PATH_INPUT)
    arr_ans = is_heap(arr)

    write_data(PATH_OUTPUT, arr_ans)
    return arr_ans


if __name__ == '__main__':
    task1()