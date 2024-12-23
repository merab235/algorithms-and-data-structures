from lab3.utils_lab3 import write_data, open_reading, close_reading, read_data_by_line

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def recursion_pair_closest(arr_s_x, arr_s_y):
    if len(arr_s_x) <= 3:
        min_dist = 10**18
        best_pair = ()
        for i in range(len(arr_s_x)):
            for j in range(i + 1, len(arr_s_x)):
                min_d = find_dist(arr_s_x[i], arr_s_x[j])
                if min_d < min_dist:
                    min_dist = min_d
                    best_pair = (arr_s_x[i], arr_s_x[j])

        return min_dist, best_pair

    mid = len(arr_s_x) // 2
    mid_sep = arr_s_x[mid][0]

    left_arr_x, right_arr_x = arr_s_x[:mid], arr_s_x[mid:]
    left_arr_y = [d for d in arr_s_y if d[0] < mid_sep]
    right_arr_y = [d for d in arr_s_y if d[0] > mid_sep]

    dist_l, pair_l = recursion_pair_closest(left_arr_x, left_arr_y)
    dist_r, pair_r = recursion_pair_closest(right_arr_x, right_arr_y)

    min_d = min(dist_l, dist_r)
    if dist_l < dist_r:
        best_pair = pair_l
    else:
        best_pair = pair_r

    strip_line_arr = []
    for dot in arr_s_y:
        if abs(dot[0] - mid_sep) < min_d:
            strip_line_arr.append(dot)

    for i in range(len(strip_line_arr)):
        for j in range(i + 1, min(i + 7, len(strip_line_arr))):
            ds = find_dist(strip_line_arr[i], strip_line_arr[j])
            if ds < min_d:
                min_d = ds
                best_pair = (strip_line_arr[i], strip_line_arr[j])

    return min_d, best_pair

def find_dist(dot1, dot2):
    return ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) ** 0.5



def task9(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)
    n = read_data_by_line(PATH_INPUT)
    arr_dots = []
    for _ in range(n):
        a, b = read_data_by_line(PATH_INPUT)
        arr_dots.append((a, b))
    close_reading(PATH_INPUT)

    arr_sorted_by_x = sorted(arr_dots, key=lambda x: x[0])
    arr_sorted_by_y = sorted(arr_dots, key=lambda x: x[1])
    dist, pair = recursion_pair_closest(arr_sorted_by_x, arr_sorted_by_y)
    dist = f'{dist:.7f}'[:-1]
    write_data(PATH_OUTPUT, dist)
    return dist

if __name__ == '__main__':
    task9()