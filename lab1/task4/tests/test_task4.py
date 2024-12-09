from lab1.task4.src.task4 import task4
from lab1.utils_lab1 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task4():
    #given
    write_data(PATH_INPUT,
               [1,3,4,5,6,4,8,3],4)
    #when
    cnt, arr = task4()

    #then
    assert cnt == 2 and arr == [2,5]

if __name__ == '__main__':
    test_should_testing_task4()