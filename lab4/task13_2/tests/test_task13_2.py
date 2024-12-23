import unittest

from lab4.task13_2.src.task13_2 import task13_2
from lab4.utils_lab4 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task13_2_1(self):
        #given
        test_arr = ["9","+ 1","?","+ 10","?","+ 12","?","-","-","?"]
        ans_to_check = ["1", "1 10", "1 10 12", "12"]

        #when
        ans = task13_2(test_arr)
        time, memory = measure_mem_time(task13_2, test_arr)


        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task13_2_2(self):
        #given
        test_arr = ["9","+ 1","+ 3","-","?","+ 12","?","+ 13","-","?"]
        ans_to_check = ["3", "3 12", "12 13"]

        #when
        ans = task13_2(test_arr)
        time, memory = measure_mem_time(task13_2, test_arr)


        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task13_2_3(self):
        #given
        test_arr = ["8","+ 1","+ 2","+ 3","-","-","-","+ 555","?"]
        ans_to_check = ["555"]

        #when
        ans = task13_2(test_arr)
        time, memory = measure_mem_time(task13_2, test_arr)


        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()