import unittest

from lab5.task6.src.task6 import task6
from lab5.utils_lab5 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task6_1(self):
        #given
        data = ["8","A 3","A 4","A 2","X","D 2 1","X","X","X"]
        ans_to_check = ["2","1","3","*"]

        #when
        ans_get = task6(data)
        time, memory = measure_mem_time(task6, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task6_2(self):
        # given
        data = ["8", "A 3", "A 2", "A 1", "X", "D 2 1", "X", "D 1 1", "X"]
        ans_to_check = ["1", "1", "1"]

        # when
        ans_get = task6(data)
        time, memory = measure_mem_time(task6, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task6_3(self):
        # given
        data = ["6", "X", "A 1", "X", "A 2", "D 4 8", "X"]
        ans_to_check = ["*", "1", "8"]

        # when
        ans_get = task6(data)
        time, memory = measure_mem_time(task6, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()