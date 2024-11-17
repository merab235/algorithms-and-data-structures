def secretary_sort(arr):
    swaps = []
    n = len(arr)

    for i in range(n):
        # Trouver l'élément minimum dans la partie non triée
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Échanger les éléments
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append(f"Swap elements at indices {i + 1} and {min_index + 1}")

    swaps.append("No more swaps needed.")
    return swaps


# Exemple de test
A = [3, 1, 4, 2]
swaps = secretary_sort(A)
for swap in swaps:
    print(swap)
