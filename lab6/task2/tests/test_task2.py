import unittest

from lab6.task2.src.task2 import task2
from lab6.utils_lab6 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task2_1(self):
        #given
        data = [8, "find 3839442", "add 123456 me","add 0 granny",
                "find 0","find 123456","del 0","del 0","find 0"]
        ans_to_check = ["not found","granny","me","not found"]

        #when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task2_2(self):
        # given
        data = [12, "add 911 police", "add 76213 Mom", "add 17239 Bob", "find 76213",
                "find 910","find 911","del 910","del 911","find 911","find 76213",
                "add 76213 daddy","find 76213"]

        ans_to_check = ["Mom","not found","police","not found","Mom","daddy"]


        # when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task2_3(self):
        # given
        data = [6, "add 123 pavel", "find 123", "del 123", "find 123",  "add 123 tima", "find 123"]
        ans_to_check = ["pavel","not found","tima"]

        # when
        ans_get = task2(data)
        time, memory = measure_mem_time(task2, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()