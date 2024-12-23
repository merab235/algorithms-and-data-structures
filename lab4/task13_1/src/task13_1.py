from lab4.utils_lab4 import write_data, open_reading, close_reading, read_data_by_line

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"



class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.last = None

    def is_empty(self):
        return self.last is None

    def pop(self):
        if not self.is_empty():
            temp_data = self.last.data
            self.last = self.last.next
            return temp_data
        else:
            raise IndexError("Stack is empty")

    def push(self, data):
        temp_node = Node(data)
        temp_node.next = self.last
        self.last = temp_node

    def print(self):
        if not self.is_empty():
            last = self.last
            temp_arr = []
            while last:
                temp_arr.append(str(last.data))
                last = last.next
            return " ".join(reversed(temp_arr))


def task13_1(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT)
    stack = Stack()
    ans_arr = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "+":
            stack.push(int(temp_list[1]))
        elif temp_list[0] == "-":
            stack.pop()
        elif temp_list[0] == "?":
            ans_arr.append(stack.print())

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, *ans_arr)
    return ans_arr

if __name__ == '__main__':
    task13_1()