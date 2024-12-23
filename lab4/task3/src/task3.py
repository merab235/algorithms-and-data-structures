from lab4.utils_lab4 import read_data, write_data
PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def valid_brackets(s):
    stack = []

    for ch in s:
        if ch in "([":
            stack.append(ch)
        elif ch in ")]":
            if len(stack) == 0 or ("(" != stack[-1] if ch == ")" else "[" != stack[-1]):
                return False
            else:
                stack.pop()

    return len(stack) == 0

def task3(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)


    n, *strings = read_data(PATH_INPUT)
    arr_ans = []
    for i in strings:
        if valid_brackets(i):
            arr_ans.append("YES")
        else:
            arr_ans.append("NO")

    write_data(PATH_OUTPUT, *arr_ans)
    return arr_ans


if __name__ == '__main__':
    task3()