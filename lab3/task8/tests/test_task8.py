import unittest

from lab3.task8.src.task8 import task8
from lab3.utils_lab3 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task8(self):
        #given
        data = [(3, 2), (3, 3), (5, -1), (-2, 4)]
        ans_to_check = '[3,3],[-2,4]'

        #when
        ans = task8(data)
        time, memory = measure_mem_time(task8, data)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()