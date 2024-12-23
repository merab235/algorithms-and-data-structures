from collections import deque

from lab5.utils_lab5 import write_data, read_data

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)



def recursive_find_height(node):
    if not node.children:
        return 1

    heights = [recursive_find_height(child) for child in node.children]
    return max(heights) + 1


def get_tree_height(arr):
    nodes_arr = [TreeNode(i) for i in range(len(arr))]
    root_id = -1
    tree_dict = {i:[] for i in range(len(arr))}
    for i in range(len(arr)):
        if arr[i] != -1:
            tree_dict[arr[i]].append(i)
        else:
            root_id = i

    queue = deque(zip(tree_dict[root_id],[root_id]*len(tree_dict[root_id])))
    checked = [0] * len(arr)

    while queue:
        node, node_root = queue.popleft()
        if checked[node] == 0:
            nodes_arr[node_root].add_child(nodes_arr[node])
            checked[node] = 1
            for item in tree_dict[node]:
                if not checked[item]:
                    queue.append((item, node))

    return recursive_find_height(nodes_arr[root_id])


def task2(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    n, arr = read_data(PATH_INPUT)
    arr_ans = get_tree_height(arr)

    write_data(PATH_OUTPUT, arr_ans)
    return arr_ans


if __name__ == '__main__':
    task2()