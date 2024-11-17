def secretary_sort(arr):
    swaps = []
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append(f"Swap elements at indices {i + 1} and {min_index + 1}")

    swaps.append("No more swaps needed.")
    return swaps

def main():
    try:
        with open('input.txt', 'r') as f:
            n = int(f.readline().strip())
            arr = list(map(int, f.readline().strip().split()))

        swaps = secretary_sort(arr)

        with open('output.txt', 'w') as f:
            for swap in swaps:
                f.write(swap + "\n")
            f.write("Sorted array: " + " ".join(map(str, arr)) + "\n")

    except FileNotFoundError:
        print("Erreur : Le fichier 'input.txt' est introuvable.")
    except ValueError:
        print("Erreur : Problème de format de données dans 'input.txt'.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()
