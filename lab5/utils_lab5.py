import time

import psutil


def func_mem_and_time(function):
    '''Декоратор измерения времени и памяти'''

    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print()
        print(f"Memory used: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")
        print('Elapsed time: %s sec' % round(time.perf_counter() - start_time, 5))
        return res
    return wrapped


def measure_mem_time(function, dataList):
    start_time = time.perf_counter()
    function(dataList)
    memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)
    time_work = round(time.perf_counter() - start_time, 5)
    return time_work, memory


def read_data(path, arr_num_type=int):
    f_in = open(path)
    input_arr = []
    for line in f_in:
        line = line.strip()
        if line.lstrip('-').isdigit():
            input_arr.append(int(line))
        else:
            try:
                input_arr.append([arr_num_type(i) for i in line.split()])
            except:
                input_arr.append(line)
    f_in.close()

    return input_arr

def write_data(path, *data):
    f_out = open(path, 'w')
    for item in data:
        if str(item).lstrip('-').replace('.','').isdigit():
            print(item, file=f_out)
        else:
            try:
                if item.isalpha():
                    print(item, file=f_out)
                else:
                    if isinstance(item, str):
                        print(item, file=f_out)

            except:
                print(*item, file=f_out)

    f_out.close()


def open_reading(path):
    global f_in
    f_in = open(path)

def close_reading(path):
    global f_in
    f_in.close()

def read_data_by_line(path, arr_num_type=int, read_as_arr=False):
    global f_in
    res = None
    line = f_in.readline().strip()
    if read_as_arr:
        try:
            res = [arr_num_type(i) for i in line.split()]
        except:
            res = line
    elif line.lstrip('-').isdigit():
        res = int(line)
    else:
        try:
            res = [arr_num_type(i) for i in line.split()]
        except:
            res = line

    return res