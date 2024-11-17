def sortland_meeting(n, wealth):
    # Créer une liste de tuples (richesse, index)
    indexed_wealth = [(wealth[i], i + 1) for i in range(n)]

    # Trier par richesse
    indexed_wealth.sort()

    # Identifier le plus pauvre, le médian et le plus riche
    poorest = indexed_wealth[0][1]
    richest = indexed_wealth[-1][1]
    median = indexed_wealth[n // 2][1]

    return poorest, median, richest


# Exemple de test
n = 5
wealth = [10.00, 8.70, 0.01, 5.00, 3.00]
result = sortland_meeting(n, wealth)
print("Indices du plus pauvre, du médian et du plus riche :", result)
