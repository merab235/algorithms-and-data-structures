import unittest

from lab7.task3.src.task3 import task3
from lab7.utils_lab7 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task3_1(self):
        #given
        data = ["ab","ab"]
        ans_to_check = 0

        #when
        ans_get = task3(data)
        time, memory = measure_mem_time(task3, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task3_2(self):
        # given
        data = ["short", "ports"]
        ans_to_check = 3

        # when
        ans_get = task3(data)
        time, memory = measure_mem_time(task3, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task3_3(self):
        # given
        data = ["editing", "distance"]
        ans_to_check = 5

        # when
        ans_get = task3(data)
        time, memory = measure_mem_time(task3, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()