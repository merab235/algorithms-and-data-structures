import unittest

from lab6.task1.src.task1 import task1
from lab6.utils_lab6 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task1_1(self):
        #given
        data = [8, "A 2","A 5","A 3","? 2","? 4","A 2","D 2","? 2"]
        ans_to_check = ["Y","N","N"]

        #when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task1_2(self):
        # given
        data = [4, "A 1","? 1","D 1","? 1"]
        ans_to_check = ["Y","N"]

        # when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task1_3(self):
        # given
        data = [5, "A 1", "A 1", "A 1", "D 1","? 1"]
        ans_to_check = ["N"]

        # when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
  unittest.main()