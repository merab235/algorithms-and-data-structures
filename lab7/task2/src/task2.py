from lab7.utils_lab7 import write_data, open_reading, read_data_by_line, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def prim_calc(n):
    order_ans = [[] for i in range(n + 1)]
    order_ans[1] = [1]
    cnt_oper_arr = [0] * (n + 1)

    for i in range(2, n + 1):
        min_cnt = float('inf')
        ind_min_cnt = -1

        if (i % 3 == 0) and cnt_oper_arr[i // 3] + 1 < min_cnt:
            min_cnt, ind_min_cnt = cnt_oper_arr[i // 3] + 1, i //3

        if (i % 2 == 0) and cnt_oper_arr[i // 2] + 1 < min_cnt:
            min_cnt, ind_min_cnt = cnt_oper_arr[i // 2] + 1, i // 2

        if cnt_oper_arr[i - 1] + 1 < min_cnt:
            min_cnt, ind_min_cnt = cnt_oper_arr[i - 1] + 1, i - 1

        cnt_oper_arr[i] = min_cnt
        order_ans[i] = order_ans[ind_min_cnt] + [i]

    return cnt_oper_arr[-1], order_ans[-1]



def task2(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, data_to_write)

    open_reading(PATH_INPUT)

    n = int(read_data_by_line(PATH_INPUT))
    ans_cnt, ans_seq = prim_calc(n)

    close_reading(PATH_INPUT)

    write_data(PATH_OUTPUT, ans_cnt, ans_seq)
    return ans_cnt, ans_seq


if __name__ == '__main__':
    task2()