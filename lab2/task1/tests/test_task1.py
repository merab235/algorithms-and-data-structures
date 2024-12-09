from lab2.task1.src.task1 import task1
from lab2.utils_lab2 import read_data,write_data,func_mem_and_time
import random

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task1():
    #given
    n = 10 ** 5
    arr = [random.randint(1, 10 ** 9) for _ in range(n)]
    arr_c = arr.copy()
    write_data(PATH_INPUT, n, arr)

    #when
    ans_arr = task1()

    #then
    assert ans_arr == sorted(arr_c)

if __name__ == '__main__':
  test_should_testing_task1()