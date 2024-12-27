import unittest

from lab6.task5.src.task5 import task5
from lab6.utils_lab6 import measure_mem_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class Test(unittest.TestCase):
    expected_time = 1
    expected_memory = 64


    def test_should_testing_task5_1(self):
        #given
        data = [("McCain","10"),("McCain","5"),
                ("Obama","9"),("Obama","8"),("McCain","1")]
        ans_to_check = ["McCain 16","Obama 17"]

        #when
        ans_get = task5(data)
        time, memory = measure_mem_time(task5, data)

        #then
        self.assertEqual(ans_get,ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task5_2(self):
        # given
        data = [("ivanov", "100"), ("ivanov", "500"),("ivanov", "300"),
                ("petr", "70"), ("tourist", "1"), ("tourist", "2")]
        ans_to_check = ["ivanov 900", "petr 70", "tourist 3"]

        # when
        ans_get = task5(data)
        time, memory = measure_mem_time(task5, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)


    def test_should_testing_task5_3(self):
        # given
        data = [("ivan", "1"), ("petya", "2"), ("lol", "3"),
                ("tim", "4"), ("fedora", "5"), ("trump", "999")]
        ans_to_check = ['fedora 5', 'ivan 1', 'lol 3', 'petya 2', 'tim 4', 'trump 999']

        # when
        ans_get = task5(data)
        time, memory = measure_mem_time(task5, data)

        # then
        self.assertEqual(ans_get, ans_to_check)
        self.assertLessEqual(time, self.expected_time)
        self.assertLessEqual(memory, self.expected_memory)

if __name__ == '__main__':
  unittest.main()