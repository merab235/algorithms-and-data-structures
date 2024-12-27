from lab6.utils_lab6 import write_data, open_reading, read_data_by_line, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

class HashSet:
    def __init__(self, size=6*10**5):
        self.size = size
        self.hash_arr = [[] for i in range(size)]

    def add(self, key):
        ind = self.get_hash(key)
        if key not in self.hash_arr[ind]:
            self.hash_arr[ind].append(key)

    def pop(self, key):
        ind = self.get_hash(key)
        if key in self.hash_arr[ind]:
            self.hash_arr[ind].remove(key)

    def check(self, key):
        return key in self.hash_arr[self.get_hash(key)]

    def get_hash(self, key):
        return hash(key) % self.size


def task1(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT, int)
    mn = HashSet()
    ans_arr = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "A":
            mn.add(int(temp_list[1]))
        elif temp_list[0] == "D":
            mn.pop(int(temp_list[1]))
        else:
            if mn.check(int(temp_list[1])):
                ans_arr.append("Y")
            else:
                ans_arr.append("N")

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, ans_arr)
    return ans_arr


if __name__ == '__main__':
    task1()