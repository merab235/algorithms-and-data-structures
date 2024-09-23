
def calc_fib_last_digit(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10 
    return b

with open('input.txt', 'r') as infile:
    n = int(infile.readline().strip()) 

result = calc_fib_last_digit(n)


with open('output.txt', 'w') as outfile:
    outfile.write(f'{result}\n') 

