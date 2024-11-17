def selection_sort(arr):
    # Parcourir chaque élément
    for i in range(len(arr)):
        # Trouver le plus petit élément dans la partie non triée
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Échanger l'élément trouvé avec le premier élément non trié
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Exemple de test
A = [64, 25, 12, 22, 11]
print("Tableau avant tri :", A)
result = selection_sort(A)
print("Tableau après tri par sélection :", result)
