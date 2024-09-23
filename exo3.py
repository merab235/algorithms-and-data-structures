# ouvrons le fichier pour lire
with open('input.txt', 'r') as infile:
    # lisons la ligne
    lines = infile.readlines()

# ouvrons le fichier pour ecrire
with open('output.txt', 'w') as outfile:
    # traitons chaque ligne
    for line in lines:
        a, b = map(int, line.split())
        # ecrivons le resultat de la somme dans le fichier
        outfile.write(f'{a + b}\n')