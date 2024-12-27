from lab7.utils_lab7 import write_data, open_reading, read_data_by_line, close_reading

PATH_INPUT = "../txtf/input.txt"
PATH_OUTPUT = "../txtf/output.txt"


def get_min_cnt(amount, coin_arr):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for item in coin_arr:
        for i in range(item, amount + 1):
            dp[i] = min(dp[i - item] + 1, dp[i])

    return dp[amount]


def task1(data_to_write=None):
    if not data_to_write is None:
        write_data(PATH_INPUT, *data_to_write)

    open_reading(PATH_INPUT)

    amount, coin_cnt = read_data_by_line(PATH_INPUT, int)
    coin_arr = read_data_by_line(PATH_INPUT, int)
    ans = get_min_cnt(amount, coin_arr)

    close_reading(PATH_INPUT)


    write_data(PATH_OUTPUT, ans)
    return ans


if __name__ == '__main__':
    task1()