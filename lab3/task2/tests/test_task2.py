import unittest

from lab3.task2.src.task2 import task2, create_arr_for_test
from lab3.utils_lab3 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task2(self):
        #given
        n = 10**3
        data = n
        ans_to_check = create_arr_for_test(n)

        #when
        arr = task2(data)
        time, memory = measure_mem_time(task2, data)


        #then
        self.assertEqual(arr, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
  unittest.main()