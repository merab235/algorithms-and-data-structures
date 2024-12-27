import unittest

from lab6.task7.src.task7 import task7
from lab6.utils_lab6 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task7_1(self):
        #given
        data = ["7 1","abacaba","aa"]
        ans_to_check = 6

        #when
        ans_get = task7(data)
        time, memory = measure_mem_time(task7, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task7_2(self):
        # given
        data = ["7 3","abacaba","ab","ac","bb"]
        ans_to_check = 7

        # when
        ans_get = task7(data)
        time, memory = measure_mem_time(task7, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task7_3(self):
        # given
        data = [f"{10**5} 1", "a"*10**5, "aa"]
        ans_to_check = 4999950000

        # when
        ans_get = task7(data)
        time, memory = measure_mem_time(task7, data)
        print(ans_get)
        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()