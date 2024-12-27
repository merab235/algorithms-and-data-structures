from lab7.utils_lab7 import write_data, open_reading, read_data_by_line, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def lev_dist(st1, st2):

    now_row = [i for i in range(len(st1) + 1)]
    for i in range(1, len(st2) + 1):
        prev_row, now_row = now_row, [i] + [0] * len(st1)
        for j in range(1, len(st1) + 1):
            now_row[j] = min(prev_row[j] + 1, now_row[j - 1] + 1, prev_row[j - 1] + (st1[j - 1] != st2[i - 1]))

    return now_row[-1]




def task3(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    st1 = read_data_by_line(PATH_INPUT)
    st2 = read_data_by_line(PATH_INPUT)
    ans = lev_dist(st1,st2)

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, ans)
    return ans


if __name__ == '__main__':
    task3()