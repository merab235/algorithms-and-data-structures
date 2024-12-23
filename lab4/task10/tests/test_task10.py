import unittest

from lab4.task10.src.task10 import task10
from lab4.utils_lab4 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task8_1(self):
        #given
        test_arr = ["5","13 0 100", "14 0 0 ", "14 1 0", "14 2 3", "14 3 0"]
        ans_to_check = ["13 10", "14 10", "14 1", "14 20", "14 3"]

        #when
        ans = task10(test_arr)
        time, memory = measure_mem_time(task10, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task8_2(self):
        #given
        test_arr = ["8","10 0 0","11 0 0","11 1 1","12 2 0","12 3 3","13 4 3","13 5 6","13 24 0"]
        ans_to_check = ['10 10', '11 10', '11 20', '12 12', '12 22', '13 14', '13 24', '13 34']

        #when
        ans = task10(test_arr)
        time, memory = measure_mem_time(task10, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task8_3(self):
        #given
        test_arr = ["3","10 0 0","10 1 1","10 2 1"]
        ans_to_check = ["10 10","10 20","10 2"]

        #when
        ans = task10(test_arr)
        time, memory = measure_mem_time(task10, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
    unittest.main()