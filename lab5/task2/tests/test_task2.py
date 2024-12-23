import unittest

from lab5.task2.src.task2 import task2
from lab5.utils_lab5 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task2_1(self):
        #given
        data = [5, (4, -1, 4, 1, 1)]
        ans_to_check = 3

        #when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task2_2(self):
        # given
        data = [5, (-1, 0, 4, 0, 3)]
        ans_to_check = 4

        # when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task2_3(self):
        # given
        data = [7, [-1, 0, 0, 1, 1, 2, 2]]
        ans_to_check = 3

        # when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()