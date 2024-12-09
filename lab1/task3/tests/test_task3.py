from lab1.task3.src.task3 import task3
from lab1.utils_lab1 import read_data,write_data,func_mem_and_time
import random

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task3():
    #given
    n = 10
    write_data(PATH_INPUT, n, [random.randint(1, 10 ** 3) for _ in range(n)])

    #when
    ans_arr = task3()
    n, arr = read_data(PATH_INPUT)

    #then
    assert sorted(arr, reverse=True) == ans_arr

if __name__ == '__main__':
    test_should_testing_task3()