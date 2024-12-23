import unittest

from lab4.task2.src.task2 import task2
from lab4.utils_lab4 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task2_1(self):
        #given
        data = ["4","+ 1", "+ 10", "-", "-"]
        ans_to_check = "1\n10"

        #when
        st = task2(data)
        time, memory = measure_mem_time(task2, data)

        #then
        self.assertEqual(st,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task2_2(self):
        #given
        data = ["5","+ 7","-", "+ 7", "+ 4", "-"]
        ans_to_check = "7\n7"

        #when
        st = task2(data)
        time, memory = measure_mem_time(task2, data)

        #then
        self.assertEqual(st,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task2_3(self):
        #given
        n = 100000
        data = [n] + ["+ 1","-"] * (n//2)
        ans_to_check = ("1\n" * (n//2)).rstrip()

        #when
        st = task2(data)
        time, memory = measure_mem_time(task2, data)

        #then
        self.assertEqual(st,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
  unittest.main()