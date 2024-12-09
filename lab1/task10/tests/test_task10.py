from lab1.task10.src.task10 import task10
from lab1.utils_lab1 import read_data,write_data,func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

@func_mem_and_time
def test_should_testing_task10():
    #given
    write_data(PATH_INPUT,
               6, 'QAZQAZ')

    #when
    string = task10()

    #then
    assert string == 'AQZZQA'

if __name__ == '__main__':
    test_should_testing_task10()