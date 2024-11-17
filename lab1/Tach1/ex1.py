def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    try:
        with open('input.txt', 'r') as f:
            n = int(f.readline().strip())
            arr = list(map(int, f.readline().strip().split()))

        insertion_sort(arr)

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
