import unittest

from lab5.task1.src.task1 import task1
from lab5.utils_lab5 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task1_1(self):
        #given
        data = [5, (1,0,1,2,0)]
        ans_to_check ="NO"

        #when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task1_2(self):
        # given
        data = [5, (1,3,2,5,4)]
        ans_to_check = "YES"

        # when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task1_3(self):
        # given
        data = [100000, list(range(1, 100001))]
        ans_to_check = "YES"

        # when
        ans_get = task1(data)
        time, memory = measure_mem_time(task1, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
  unittest.main()