from lab2.task5.src.task5 import task5
from lab2.utils_lab2 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task5_1():
    #given
    n = 5
    arr = [2,3,9,2,2]
    write_data(PATH_INPUT, n, arr)

    #when
    is_majority = task5()

    #then
    assert is_majority == 1


@func_mem_and_time
def test_should_testing_task5_2():
    #given
    n = 4
    arr = [1,2,3,4]
    write_data(PATH_INPUT, n, arr)

    #when
    is_majority = task5()

    #then
    assert is_majority == 0


if __name__ == '__main__':
  test_should_testing_task5_1()
  test_should_testing_task5_2()