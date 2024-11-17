def binary_addition(A, B):
    n = len(A)
    C = [0] * (n + 1)  # Résultat de taille n+1
    carry = 0  # Variable de retenue

    for i in range(n - 1, -1, -1):  # Parcours de droite à gauche
        total = A[i] + B[i] + carry
        C[i + 1] = total % 2  # Le bit de résultat
        carry = total // 2  # La retenue

    C[0] = carry  # Dernière retenue
    return C

def main():
    try:
        with open('input.txt', 'r') as f:
            A = list(map(int, f.readline().strip().split()))
            B = list(map(int, f.readline().strip().split()))

        if len(A) != len(B):
            raise ValueError("Les deux nombres binaires doivent avoir la même longueur.")

        result = binary_addition(A, B)

        with open('output.txt', 'w') as f:
            f.write(" ".join(map(str, result)) + "\n")

    except FileNotFoundError:
        print("Erreur : Le fichier 'input.txt' est introuvable.")
    except ValueError as ve:
        print(f"Erreur : {ve}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()
