from lab4.utils_lab4 import write_data, open_reading, close_reading, read_data_by_line

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class Queue:
    def __init__(self, max_length=10**3):
        self.head = None
        self.tail = None
        self.max_length = max_length
        self.length = 0


    def enqueue(self, data):
        if self.length == self.max_length:
            raise OverflowError("Queue is overflow")

        temp_node = Node(data)
        if self.head is None:
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next = temp_node
            self.tail = temp_node

        self.length += 1


    def dequeue(self):
        if self.length == 0:
            raise IndexError("Queue is empty")

        temp_data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return temp_data


    def is_full(self):
        return self.length == self.max_length


    def is_empty(self):
        return self.length == 0


    def print(self):
        if not self.is_empty():
            now_node = self.head
            temp_arr = []
            while now_node:
                temp_arr.append(str(now_node.data))
                now_node = now_node.next
            return " ".join(temp_arr)




def task13_2(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT)
    queue = Queue()
    ans_arr = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "+":
            queue.enqueue(int(temp_list[1]))
        elif temp_list[0] == "-":
            queue.dequeue()
        elif temp_list[0] == "?":
            ans_arr.append(queue.print())

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, *ans_arr)
    return ans_arr

if __name__ == '__main__':
    task13_2()