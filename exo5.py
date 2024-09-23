def calc_fib(n):
    if n <= 1:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)

# ouvrons le fichier input.txt pour lire
with open('input.txt', 'r') as infile:
    n = int(infile.readline())

# calculons le nombre de Fibonacci
result = calc_fib(n)

# ouvrons le fichier output.txt pour ecrire
with open('output.txt', 'w') as outfile:
    outfile.write(f'{result}\n')
