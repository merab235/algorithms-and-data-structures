import random
import unittest

from lab3.task4.src.task4 import task4
from lab3.utils_lab3 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64

    def test_should_testing_task4(self):
        #given
        s = random.randint(1, 5000)
        p = random.randint(1, 5000)
        arr_seg = []
        for i in range(s):
            st_n = random.randint(-10**8,10**8)
            end_n = st_n + random.randint(0,10**8)
            arr_seg.append((st_n, end_n))
        arr_points = []
        for i in range(p):
            n = random.randint(-25,25)
            arr_points.append(n)
        data = ((s,p), *arr_seg, arr_points)

        #when
        ans = task4(data)
        time, memory = measure_mem_time(task4, data)

        #then
        self.assertTrue(ans)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


if __name__ == '__main__':
    unittest.main()