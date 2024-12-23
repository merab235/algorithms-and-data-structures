import unittest

from lab4.task3.src.task3 import task3
from lab4.utils_lab4 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task3_1(self):
        #given
        arr_data = ["5","()()","([])","([)]","((]]",")("]
        arr_to_check = ["YES", "YES", "NO", "NO", "NO"]

        #when
        ans = task3(arr_data)
        time, memory = measure_mem_time(task3, arr_data)

        #then
        self.assertEqual(ans, arr_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task3_2(self):
        #given
        arr_data = ["3","))","([([])])","[[))"]
        arr_to_check = ["NO", "YES", "NO"]

        #when
        ans = task3(arr_data)
        time, memory = measure_mem_time(task3, arr_data)

        #then
        self.assertEqual(ans, arr_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task3_3(self):
        #given
        arr_data = ["3",")","(","[[[[(([()]))]]]]"]
        arr_to_check = ["NO", "NO", "YES"]

        #when
        ans = task3(arr_data)
        time, memory = measure_mem_time(task3, arr_data)

        #then
        self.assertEqual(ans, arr_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()