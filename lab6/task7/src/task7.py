from string import ascii_lowercase as alph_lc

from lab6.utils_lab6 import write_data, read_data_by_line, open_reading, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def get_b_pairs(st_rocks, arr_pairs):
    ans = 0
    index_dict = {i:[] for i in alph_lc}

    for i in range(len(st_rocks)):
        index_dict[st_rocks[i]].append(i)

    for x, y in arr_pairs:
        arr1, arr2 = index_dict[x], index_dict[y]

        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr2[j] > arr1[i]:
                ans += (len(arr2) - j)
                i += 1
            else:
                j += 1

    return ans


def task7(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n, k = read_data_by_line(PATH_INPUT)
    st_rocks = read_data_by_line(PATH_INPUT)
    arr_pairs = []
    for i in range(k):
        arr_pairs.append(read_data_by_line(PATH_INPUT))

    close_reading(PATH_INPUT)
    arr_ans = get_b_pairs(st_rocks, arr_pairs)

    write_data(PATH_OUTPUT, arr_ans)
    return arr_ans


if __name__ == '__main__':
    task7()