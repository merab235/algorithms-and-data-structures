from lab2.task4.src.task4 import task4
from lab2.utils_lab2 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task4():
    #given
    n = 5
    arr_n = [1,5,8,12,13]
    k = 5
    arr_k = [8,1,23,1,11]
    write_data(PATH_INPUT, n, arr_n, k, arr_k)

    #when
    arr_bs = task4()

    #then
    assert arr_bs == [2,0,-1,0,-1]

if __name__ == '__main__':
  test_should_testing_task4()