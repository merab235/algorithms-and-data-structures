from lab2.task6.src.task6 import task6
from lab2.utils_lab2 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task6():
    #given
    arr = [100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]
    n = len(arr)
    write_data(PATH_INPUT, n, arr)

    #when
    arr_ans = list(task6())

    #then
    assert arr_ans == [7, 10, 43]


if __name__ == '__main__':
  test_should_testing_task6()