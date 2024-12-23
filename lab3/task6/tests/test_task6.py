import unittest

from lab3.task6.src.task6 import task6
from lab3.utils_lab3 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task6(self):
        #given
        data = [(4,4), (7,1,4,9), (2,7,8,11)]
        ans_to_check = 51

        #when
        ans = task6(data)
        time, memory = measure_mem_time(task6, data)

        #then
        self.assertEqual(ans, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()