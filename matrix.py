def diagonal_difference(matrix):
    n = len(matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += matrix[i][i]  # Diagonal utama
        secondary_diagonal_sum += matrix[i][n - 1 - i]  # Diagonal kedua

    # Hitung selisihnya
    difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    return difference

# Meminta input dari pengguna
n = int(input("Masukkan ukuran matriks (N x N): "))
matrix = []

print("Masukkan elemen matriks:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = diagonal_difference(matrix)
print("Hasil selisih diagonal:", result)
