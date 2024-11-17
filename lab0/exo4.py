# ouvros le fichier input.txt pour lire
with open('input.txt', 'r') as infile:
    # lisons la ligne et la convertir en deux nombres
    a, b = map(int, infile.readline().split())

# ouvrons le fichier output.txt pour ecrire
with open('output.txt', 'w') as outfile:
    # ecrivons le resultat a + b^2 dans le fichier
    outfile.write(f'{a + b ** 2}\n')
