from lab7.utils_lab7 import write_data, open_reading, read_data_by_line, close_reading, func_mem_and_time

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def get_longest_sub(arr1, arr2, arr3):

    dp = [[[0] * (len(arr3) + 1) for i in range(len(arr2) + 1)] for j in range(len(arr1) + 1)]

    for i in range(1, len(arr1) + 1):
        for j in range(1, len(arr2) + 1):
            for k in range(1, len(arr3) + 1):
                if arr1[i - 1] == arr2[j - 1] == arr3[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[-1][-1][-1]

@func_mem_and_time
def task5(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    n1 = read_data_by_line(PATH_INPUT)
    arr1 = read_data_by_line(PATH_INPUT, int, True)
    n2 = read_data_by_line(PATH_INPUT)
    arr2 = read_data_by_line(PATH_INPUT, int, True)
    n3 = read_data_by_line(PATH_INPUT)
    arr3 = read_data_by_line(PATH_INPUT, int, True)
    ans = get_longest_sub(arr1,arr2,arr3)

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, ans)
    return ans


if __name__ == '__main__':
    task5()