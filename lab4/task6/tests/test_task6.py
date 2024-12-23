import unittest

from lab4.task6.src.task6 import task6
from lab4.utils_lab4 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task6_1(self):
        #given
        test_arr = ["7", "+ 1", "?", "+ 10", "?", "-", "?", "-"]
        ans_to_check = [1, 1, 10]

        #when
        ans = task6(test_arr)
        time, memory = measure_mem_time(task6, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task6_2(self):
        #given
        test_arr = [8, "+ 3", "-", "+ 4", "?", "+ 1", "?", "+ 2", "?"]
        ans_to_check = [4, 1, 1]

        #when
        ans = task6(test_arr)
        time, memory = measure_mem_time(task6, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task6_3(self):
        #given
        test_arr = [8, "+ 3", "+ 3", "+ 3", "+ 3", "+ 3", "?", "-", "?"]
        ans_to_check = [3, 3]

        #when
        ans = task6(test_arr)
        time, memory = measure_mem_time(task6, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()