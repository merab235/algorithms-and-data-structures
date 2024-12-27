from lab6.utils_lab6 import write_data, open_reading, read_data_by_line, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class StitchedHashMap:
    def __init__(self):
        self.prev_dep = {}
        self.next_dep = {}
        self.data = {}
        self.values_queue = []


    def get(self, item):
        return self.data.get(item, "<none>")

    def prev(self, val):
        if val in self.prev_dep and self.prev_dep[val] in self.data:
            return self.data[self.prev_dep[val]]
        else: return "<none>"

    def next(self, item):
        if item in self.next_dep and self.next_dep[item] in self.data:
            return self.data[self.next_dep[item]]
        else: return "<none>"


    def put(self, key, val):
        if key not in self.data:
            if self.values_queue:
                last_key = self.values_queue[-1]
                self.next_dep[last_key] = key
                self.prev_dep[key] = last_key
            self.values_queue.append(key)
        self.data[key] = val


    def delete(self, val):
        if val in self.data:
            ind = self.values_queue.index(val)
            if ind > 0:
                self.next_dep[self.values_queue[ind - 1]] = self.next_dep[val]
            if ind < len(self.values_queue) - 1:
                self.prev_dep[self.values_queue[ind + 1]] = self.prev_dep[val]
            self.values_queue.pop(ind)
            self.prev_dep.pop(val, "")
            self.next_dep.pop(val, "")
            del self.data[val]





def task4(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n = read_data_by_line(PATH_INPUT, int)
    hs_map = StitchedHashMap()
    arr_ans = []
    for i in range(n):
        temp_list = read_data_by_line(PATH_INPUT, str, True)
        if temp_list[0] == "put":
            hs_map.put(temp_list[1],temp_list[2])
        elif temp_list[0] == "get":
            arr_ans.append(hs_map.get(temp_list[1]))
        elif temp_list[0] == "prev":
            arr_ans.append(hs_map.prev(temp_list[1]))
        elif temp_list[0] == "next":
            arr_ans.append(hs_map.next(temp_list[1]))
        else:
            hs_map.delete(temp_list[1])

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, *arr_ans)
    return arr_ans


if __name__ == '__main__':
    task4()