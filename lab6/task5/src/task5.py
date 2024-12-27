from lab6.utils_lab6 import write_data, read_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class ElectionsAdapter:
    def __init__(self):
        self.elect_dict = {}

    def add_num(self, name, cnt):
        self.elect_dict[name] = self.elect_dict.get(name, 0) + cnt

    def get_data(self):
        names_sorted = sorted(self.elect_dict.keys())
        return [f"{name} {self.elect_dict[name]}" for name in names_sorted]



def task5(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)


    elections_adapter = ElectionsAdapter()
    for line in read_data(PATH_INPUT):
        name, cnt = line.split()
        elections_adapter.add_num(name, int(cnt))

    arr_ans = elections_adapter.get_data()

    write_data(PATH_OUTPUT, *arr_ans)
    return arr_ans


if __name__ == '__main__':
    task5()