import unittest

from lab3.task9.src.task9 import task9
from lab3.utils_lab3 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task9(self):
        #given
        data = [11, (4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1), (-1, -1), (3, -1), (-4, 2), (-2, 4)]
        ans_to_check = '1.414213'

        #when
        ans = task9(data)
        time, memory = measure_mem_time(task9, data)


        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()