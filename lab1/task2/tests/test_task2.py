from lab1.task2.src.task2 import task2
from lab1.utils_lab1 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task2():
    #given
    n = 10
    arr = [1,8,4,2,3,7,5,6,9,0]
    write_data(PATH_INPUT, n, arr)

    #when
    ans_arr = task2()
    n, arr = read_data(PATH_INPUT)
    arr1, arr2 = ans_arr

    #then
    assert arr1 == [1,2,2,2,3,5,5,6,9,1] and arr2 == [0,1,2,3,4,5,6,7,8,9]

if __name__ == '__main__':
    test_should_testing_task2()