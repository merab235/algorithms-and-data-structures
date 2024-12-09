from lab2.task7.src.task7 import task7
from lab2.utils_lab2 import read_data,write_data,func_mem_and_time
import random

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task7():
    #given
    n = 10**5
    arr = [random.randint(-10**2, 10 ** 2) for _ in range(n)]
    write_data(PATH_INPUT, n, arr)

    #when
    ans1, ans2 = task7()

    #then
    assert ans1 == ans2


if __name__ == '__main__':
    test_should_testing_task7()