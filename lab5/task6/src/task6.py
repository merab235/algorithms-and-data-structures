import heapq

from lab5.utils_lab5 import write_data, read_data_by_line, open_reading, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.position = {}
        self.index = 0
        self.ans_arr = []

    def add_element(self, item):
        heapq.heappush(self.heap, (item, self.index))
        self.position[self.index] = item
        self.index += 1

    def pop_minimum(self):
        while self.heap and (self.heap[0][1] not in self.position or self.position[self.heap[0][1]] != self.heap[0][0]):
            heapq.heappop(self.heap)
        if self.heap:
            value, index = heapq.heappop(self.heap)
            self.ans_arr.append(str(value))
            del self.position[index]
        else:
            self.ans_arr.append('*')
        self.index += 1

    def replace_item_with_index(self, index, item):
        index -= 1
        if index in self.position:
            self.position[index] = item
            heapq.heappush(self.heap, (item, index))
        self.index += 1

    def get_ans(self):
        return self.ans_arr



def task6(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT)
    pr_queue = PriorityQueue()
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "A":
            pr_queue.add_element(int(temp_list[1]))
        elif temp_list[0] == "X":
            pr_queue.pop_minimum()
        elif temp_list[0] == "D":
            pr_queue.replace_item_with_index(int(temp_list[1]), int(temp_list[2]))

    close_reading(PATH_INPUT)

    arr_ans = pr_queue.get_ans()

    write_data(PATH_OUTPUT, *arr_ans)
    return arr_ans


if __name__ == '__main__':
    task6()