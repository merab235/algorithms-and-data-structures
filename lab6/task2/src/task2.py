from lab6.utils_lab6 import write_data, open_reading, read_data_by_line, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class PhoneAdapter:
    def __init__(self):
        self.numb_dict = {}

    def add_num(self, number, name):
        self.numb_dict[number] = name

    def pop_num(self, number):
        if number in self.numb_dict:
            del self.numb_dict[number]

    def find_num(self, number):
        return self.numb_dict.get(number, "not found")


def task2(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT, int)
    phone_adapter = PhoneAdapter()
    arr_ans = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "add":
            phone_adapter.add_num(int(temp_list[1]), temp_list[2])
        elif temp_list[0] == "del":
            phone_adapter.pop_num(int(temp_list[1]))
        else:
            arr_ans.append(phone_adapter.find_num(int(temp_list[1])))


    close_reading(PATH_INPUT)

    write_data(PATH_OUTPUT, arr_ans)
    return arr_ans


if __name__ == '__main__':
    task2()