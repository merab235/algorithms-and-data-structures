from collections import deque

from lab4.utils_lab4 import write_data, open_reading, close_reading, read_data_by_line

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def max_slide_window(arr, w_len):

    ans_arr = []
    deq = deque()

    for ind, item in enumerate(arr):
        while deq and arr[deq[-1]] <= item:
            deq.pop()

        deq.append(ind)

        if deq[0] == ind - w_len:
            deq.popleft()

        if ind + 1 >= w_len:
            ans_arr.append(arr[deq[0]])

    return ans_arr


def task7(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)
    n = read_data_by_line(PATH_INPUT)
    arr_data = read_data_by_line(PATH_INPUT, int, True)
    w_len = read_data_by_line(PATH_INPUT)
    ans = max_slide_window(arr_data, w_len)

    close_reading(PATH_INPUT)

    write_data(PATH_OUTPUT, ans)
    return ans

if __name__ == '__main__':
    task7()