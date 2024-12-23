import unittest

from lab4.task7.src.task7 import task7
from lab4.utils_lab4 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task9_1(self):
        #given
        test_arr = [8,(2,7,3,1,5,2,6,2),4]
        ans_to_check = [7, 7, 5, 6, 6]

        #when
        ans = task7(test_arr)
        time, memory = measure_mem_time(task7, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task9_2(self):
        #given
        test_arr = [5,(2,7,3,1,5),5]
        ans_to_check = [7]

        #when
        ans = task7(test_arr)
        time, memory = measure_mem_time(task7, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

    def test_should_testing_task9_3(self):
        #given
        test_arr = [5,(2,7,3,1,5,10),2]
        ans_to_check = [7,7,3,5,10]

        #when
        ans = task7(test_arr)
        time, memory = measure_mem_time(task7, test_arr)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()