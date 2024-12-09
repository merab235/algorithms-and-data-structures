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
        if str(item).lstrip('-').isdigit():
            print(item, file=f_out)
        else:
            try:
                if item.isalpha():
                    print(item, file=f_out)
            except:
                print(*item, file=f_out)

    f_out.close()