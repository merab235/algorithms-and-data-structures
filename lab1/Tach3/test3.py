def insertion_sort_descending(arr):
    # Parcourir chaque élément à partir du deuxième
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Déplacer les éléments plus petits que key vers la droite
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insérer l'élément à la bonne position
        arr[j + 1] = key

    return arr


# Exemple de test
A = [31, 41, 59, 26, 41, 58]
print("Tableau avant tri :", A)
result = insertion_sort_descending(A)
print("Tableau après tri en ordre décroissant :", result)
