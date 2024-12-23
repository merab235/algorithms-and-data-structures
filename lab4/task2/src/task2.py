from lab4.utils_lab4 import write_data, read_data_by_line, open_reading, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Queue:
    def __init__(self, n: int):
        self.queue = [None] * n
        self.head = 0
        self.tail = 0
        self.count_el = 0
        self.n = n

    def append(self, item):
        if self.count_el < self.n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.n
            self.count_el += 1
        else:
            raise IndexError("Queue overflow")

    def pop(self):
        if self.count_el > 0:
            temp_per = self.queue[self.head]
            self.head = (self.head + 1) % self.n
            self.count_el -= 1
            return temp_per
        else:
            raise IndexError("Queue empty")


    def print(self):
        if self.head > self.tail:
            print(self.queue[self.head:] + self.queue[:self.tail])
        else:
            print(self.queue[self.head:self.tail])




def task2(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)


    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT, int)
    q = Queue(n)
    arr = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "+":
            q.append(int(temp_list[1]))
        else:
            arr.append(q.pop())

    close_reading(PATH_INPUT)

    st = "\n".join(map(str, arr))

    write_data(PATH_OUTPUT, *arr)
    return st


if __name__ == '__main__':
    task2()