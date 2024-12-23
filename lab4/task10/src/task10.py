from collections import deque

from lab4.utils_lab4 import write_data, open_reading, close_reading, read_data_by_line

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def bakery_queue(n,arr_data):
    deq = deque()

    arr_ans = [""]*n
    ind_now = 0
    time_end = arr_data[0][0]+10
    deq.append(arr_data[0])
    smth_add = True
    ind_now += 1
    while ind_now < n:
        if arr_data[ind_now][0] > time_end and not deq:
            deq.append(arr_data[ind_now])
            time_end = arr_data[ind_now][0]
            smth_add = True

        if not smth_add:
            while deq and arr_data[ind_now][0] < time_end:
                temp_arr = deq.popleft()
                arr_ans[temp_arr[2]] = convert_to_hours_min(time_end)
                time_end += 10
            if ind_now < n and deq and deq[-1] != arr_data[ind_now]:
                deq.append(arr_data[ind_now])
        smth_add = False
        while ind_now < n and arr_data[ind_now][0] < time_end:
            if arr_data[ind_now][1] >= len(deq):
                deq.append(arr_data[ind_now])
                smth_add = True
            else:
                arr_ans[arr_data[ind_now][2]] = convert_to_hours_min(arr_data[ind_now][0])
            ind_now += 1

        temp_arr = deq.popleft()

        arr_ans[temp_arr[2]] = convert_to_hours_min(time_end)
        time_end += 10

    while deq:
        temp_arr = deq.popleft()
        arr_ans[temp_arr[2]] = convert_to_hours_min(time_end)
        time_end += 10

    return arr_ans


def convert_to_hours_min(num):
    return f"{num//60} {num%60}"



def task10(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT)
    arr_data = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, int, True)
        arr_data.append((temp_list[0]*60+temp_list[1],temp_list[2],i))

    close_reading(PATH_INPUT)


    ans = bakery_queue(n,arr_data)

    write_data(PATH_OUTPUT, *ans)
    return ans

if __name__ == '__main__':
    task10()