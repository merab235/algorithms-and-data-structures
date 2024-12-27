import unittest

from lab6.task4.src.task4 import task4
from lab6.utils_lab6 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task4_1(self):
        #given
        data = ["14","put zero a","put one b","put two c","put three d",
                "put four e", "get two", "prev two", "next two", "delete one",
                "delete three", "get two", "prev two", "next two"," next four"]
        ans_to_check = ["c","b","d","c","a","e","<none>"]

        #when
        ans_get = task4(data)
        time, memory = measure_mem_time(task4, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task4_2(self):
        # given
        data = ["8", "put zero 0", "put one 1", "put two 2", "delete one",
                "prev zero", "next zero", "prev two", "next two"]
        ans_to_check = ["<none>","2","0","<none>"]

        # when
        ans_get = task4(data)
        time, memory = measure_mem_time(task4, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task4_3(self):
        # given
        data = ["7", "put abakar g", "delete abakar", "put abakar g", "put abakar g",
                "next abakar", "put tima s", "next abakar"]
        ans_to_check = ["<none>", "s"]

        # when
        ans_get = task4(data)
        time, memory = measure_mem_time(task4, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()