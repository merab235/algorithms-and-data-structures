import unittest

from lab7.task5.src.task5 import task5
from lab7.utils_lab7 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task5_1(self):
        #given
        data = [3, "1 2 3", 3, "2 1 3", 3, "1 3 5"]
        ans_to_check = 2

        #when
        ans_get = task5(data)
        time, memory = measure_mem_time(task5, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task5_2(self):
        # given
        data = [5, "8 3 2 1 7", 7, "8 2 1 3 8 10 7", 6, "6 8 3 1 4 7"]
        ans_to_check = 3

        # when
        ans_get = task5(data)
        time, memory = measure_mem_time(task5, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task5_3(self):
        # given
        data = [3, "1 2 3", 3, "4 5 6", 3, "7 8 9"]
        ans_to_check = 0

        # when
        ans_get = task5(data)
        time, memory = measure_mem_time(task5, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()