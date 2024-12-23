import unittest

from lab4.task13_1.src.task13_1 import task13_1
from lab4.utils_lab4 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task13_1_1(self):
        #given
        test_arr = ["8","+ 1","?","+ 10","?","+ 12","?","-","?"]
        ans_to_check = ["1", "1 10", "1 10 12", "1 10"]

        #when
        ans = task13_1(test_arr)
        time, memory = measure_mem_time(task13_1, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task13_1_2(self):
        #given
        test_arr = ["4","+ 1","-","+ 2","?"]
        ans_to_check = ["2"]

        #when
        ans = task13_1(test_arr)
        time, memory = measure_mem_time(task13_1, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task13_1_3(self):
        #given
        test_arr = ["7","+ 1","+ 2","+ 3","+ 4","+ 5","-","?"]
        ans_to_check = ["1 2 3 4"]

        #when
        ans = task13_1(test_arr)
        time, memory = measure_mem_time(task13_1, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()