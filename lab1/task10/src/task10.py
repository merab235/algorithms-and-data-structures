from lab1.utils_lab1 import read_data, write_data
PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"

def palindrom(n,s):

    cnt_let = [0] * 26
    offset = 65
    for i in s:
        cnt_let[ord(i) - offset] += 1

    mn_i = -1
    for i in range(len(cnt_let)):
        if cnt_let[i] % 2 == 1:
            mn_i = i
            break

    new_s = ''

    for i in range(len(cnt_let)):
        if cnt_let[i] != 0:
            new_s += chr(i + offset) * (cnt_let[i] // 2)

    if mn_i != -1:
        new_s = new_s + chr(mn_i + offset) + new_s[::-1]
    else:
        new_s += new_s[::-1]

    return new_s

def task10():
    n, s = read_data(PATH_INPUT)
    new_s = palindrom(n,s)
    write_data(PATH_OUTPUT, new_s)
    return new_s

if __name__ == '__main__':
    task10()