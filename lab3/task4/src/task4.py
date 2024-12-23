from lab3.utils_lab3 import write_data, read_data_by_line, open_reading, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def points_and_segments(segments, points):
    start_seg_dct = {}
    end_seg_dct = {}
    for a,b in segments:
        start_seg_dct[a] = start_seg_dct.get(a, 0) + 1
        end_seg_dct[b+1] = end_seg_dct.get(b+1, 0) + 1
    points_c = points.copy()
    points = sorted(set(points))
    start_seg_arr = sorted(start_seg_dct.keys())
    end_seg_arr = sorted(end_seg_dct.keys())

    i = j = 0
    cur_layers = 0
    ans_arr = {}
    for k in range(len(points)):
        if j >= len(end_seg_arr):
            ans_arr[points[k]] = cur_layers
        elif i < len(start_seg_arr) and j < len(end_seg_arr) and points[k] < start_seg_arr[i] and points[k] < end_seg_arr[j]:
            ans_arr[points[k]] = cur_layers
        else:
            while i < len(start_seg_arr) and points[k] >= start_seg_arr[i]:
                cur_layers += start_seg_dct[start_seg_arr[i]]
                i += 1

            while j < len(end_seg_arr) and points[k] >= end_seg_arr[j]:
                cur_layers -= end_seg_dct[end_seg_arr[j]]
                j += 1

            ans_arr[points[k]] = cur_layers

    return [ans_arr[i] for i in points_c]


def brute_force_sol(segments, points):
    ans_arr = []
    for pnt in points:
        cnt = 0
        for a,b in segments:
            if a <= pnt <= b:
                cnt += 1
        ans_arr.append(cnt)
    return ans_arr


def task4(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)
    s, p = read_data_by_line(PATH_INPUT)
    segments = []
    for _ in range(s):
        a, b = read_data_by_line(PATH_INPUT)
        segments.append((a,b))
    points = read_data_by_line(PATH_INPUT, int, True)
    close_reading(PATH_INPUT)

    ans_arr = points_and_segments(segments, points)
    ans_arr2 = brute_force_sol(segments, points)

    write_data(PATH_OUTPUT, (ans_arr==ans_arr2)+0)
    return (ans_arr==ans_arr2)+0


if __name__ == '__main__':
    task4()