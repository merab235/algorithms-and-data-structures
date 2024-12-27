import unittest

from lab7.task1.src.task1 import task1
from lab7.utils_lab7 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task1_1(self):
        #given
        data = ["2 3","1 3 4"]
        ans_to_check = 2

        #when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task1_2(self):
        # given
        data = ["34 3", "1 3 4"]
        ans_to_check = 9

        # when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task1_3(self):
        # given
        data = ["18 3", "1 2 5"]
        ans_to_check = 5

        # when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
  unittest.main()