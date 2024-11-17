def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Trouver le plus petit élément dans la partie non triée
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Échange

def main():
    try:
        with open('input.txt', 'r') as f:
            n = int(f.readline().strip())
            arr = list(map(int, f.readline().strip().split()))

        selection_sort(arr)

        with open('output.txt', 'w') as f:
            f.write(" ".join(map(str, arr)) + "\n")

    except FileNotFoundError:
        print("Erreur : Le fichier 'input.txt' est introuvable.")
    except ValueError:
        print("Erreur : Problème de format de données dans 'input.txt'.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()
