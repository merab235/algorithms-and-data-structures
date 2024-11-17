def insertion_sort(arr):
    # Parcourir chaque élément à partir du deuxième
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Déplacer les éléments plus grands que key vers la droite
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insérer l'élément à la bonne position
        arr[j + 1] = key

    return arr


# Exemple de test
A = [31, 41, 59, 26, 41, 58]
print("Tableau avant tri :", A)
result = insertion_sort(A)
print("Tableau après tri :", result)
