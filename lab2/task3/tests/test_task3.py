from lab2.task3.src.task3 import task3
from lab2.utils_lab2 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task3():
    #given
    n = 10
    arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
    write_data(PATH_INPUT, n, arr)

    #when
    num = task3()

    #then
    assert num == 17


if __name__ == '__main__':
  test_should_testing_task3()