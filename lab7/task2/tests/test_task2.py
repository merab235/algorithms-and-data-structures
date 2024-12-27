import unittest

from lab7.task2.src.task2 import task2
from lab7.utils_lab7 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task2_1(self):
        #given
        data = 1
        ans_to_check = (0, [1])

        #when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task2_2(self):
        # given
        data = 5
        ans_to_check = (3, [1, 2, 4, 5])


        # when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task2_3(self):
        # given
        data = 10**3
        ans_to_check = (9, [1, 2, 4, 12, 36, 37, 111, 333, 999, 1000])

        # when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()