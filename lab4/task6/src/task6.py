from collections import deque

from lab4.utils_lab4 import write_data, read_data_by_line, open_reading, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class QueueMin:
    def __init__(self, n: int):
        self.queue = [None] * n
        self.min_deque = deque(maxlen=n)
        self.head = 0
        self.tail = 0
        self.count_el = 0
        self.n = n

    def append(self, item):
        if self.count_el < self.n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.n
            self.count_el += 1

            while self.min_deque and self.min_deque[-1] > item:
                self.min_deque.pop()
            self.min_deque.append(item)

        else:
            raise IndexError("Queue overflow")

    def pop(self):
        if self.count_el > 0:
            temp_per = self.queue[self.head]
            self.head = (self.head + 1) % self.n
            self.count_el -= 1

            if self.min_deque and temp_per == self.min_deque[0]:
                self.min_deque.popleft()

            return temp_per
        else:
            raise IndexError("Queue empty")

    def min(self):
        if self.min_deque:
            return self.min_deque[0]
        raise IndexError("Queue empty")


    def print(self):
        if self.head > self.tail:
            print(self.queue[self.head:] + self.queue[:self.tail])
        else:
            print(self.queue[self.head:self.tail])



def task6(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT, int)
    q = QueueMin(n)
    arr = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "+":
            q.append(int(temp_list[1]))
        elif temp_list[0] == "-":
            q.pop()
        elif temp_list[0] == "?":
            arr.append(q.min())


    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, *arr)
    return arr


if __name__ == '__main__':
    task6()