def sortland_habitants(input_file, output_file):
    # Lecture des données depuis input.txt
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())  # Nombre d'habitants
        wealth = list(map(float, f.readline().strip().split()))  # Richesse des habitants

    # Créer une liste de tuples (richesse, index)
    indexed_wealth = [(wealth[i], i + 1) for i in range(n)]  # L'index commence à 1
    # Trier par richesse
    indexed_wealth.sort()

    # Identifier le plus pauvre, le médian et le plus riche
    poorest = indexed_wealth[0][1]  # Identifiant du plus pauvre
    richest = indexed_wealth[-1][1]  # Identifiant du plus riche
    median = indexed_wealth[n // 2][1]  # Identifiant du médian

    # Écrire les résultats dans output.txt
    with open(output_file, 'w') as f:
        f.write(f"{poorest} {median} {richest}\n")

# Exemple d'utilisation
sortland_habitants('input.txt', 'output.txt')
