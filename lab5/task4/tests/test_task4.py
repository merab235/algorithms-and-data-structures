import unittest

from lab5.task4.src.task4 import task4
from lab5.utils_lab5 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task6_1(self):
        #given
        data = (5, [5, 4, 3, 2, 1])
        ans_to_check = (3, (1, 4), (0,1), (1,3))

        #when
        ans_get = task4(data)
        time, memory = measure_mem_time(task4, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task6_2(self):
        # given
        data = (5, [1, 2, 3, 4, 5])
        ans_to_check = (0,)

        # when
        ans_get = task4(data)
        time, memory = measure_mem_time(task4, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task6_3(self):
        # given
        data = (10**5, [1]*10**5)
        ans_to_check = (0,)

        # when
        ans_get = task4(data)
        time, memory = measure_mem_time(task4, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()