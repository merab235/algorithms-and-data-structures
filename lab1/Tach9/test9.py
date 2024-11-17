def binary_addition(A, B):
    n = len(A)
    C = [0] * (n + 1)  # Le résultat aura n+1 bits

    carry = 0  # Variable pour le transport
    for i in range(n - 1, -1, -1):
        # Additionner les bits correspondants et le transport
        sum_bits = A[i] + B[i] + carry
        C[i + 1] = sum_bits % 2  # Stocker le bit de résultat
        carry = sum_bits // 2  # Calculer le transport

    # Si un transport reste, il est stocké dans le premier bit
    C[0] = carry

    return C

# Exemple de test
A = [1, 0, 1, 1]  # Représente le nombre binaire 1011 (11 en décimal)
B = [1, 1, 0, 1]  # Représente le nombre binaire 1101 (13 en décimal)
result = binary_addition(A, B)
print("Résultat de l'addition binaire :", result)
