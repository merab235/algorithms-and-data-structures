from lab3.utils_lab3 import read_data, write_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def generate_worst_case(ln):
    arr = []
    for i in range(0, ln):
        arr += [i + 1]
        if i > 1:
            arr[-1], arr[i // 2] = arr[i // 2], arr[-1]
    return arr

def create_arr_for_test(n):
    if n==1:
        return [1]
    arr = [0] * n
    arr[0], arr[1] = 1, 2
    for i in range(2,n):
        arr[i] = i+1
        arr[i], arr[i//2] = arr[i//2], arr[i]
    return arr



def task2(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, data_to_write)

    n, = read_data(PATH_INPUT)
    arr = generate_worst_case(n)
    write_data(PATH_OUTPUT, arr)
    return arr


if __name__ == '__main__':
    task2()