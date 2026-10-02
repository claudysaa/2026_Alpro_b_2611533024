print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_3024 = int(input("Masukkan ukuran skala jam pasir (N): "))

lebar_3024 = 4 * n_3024 + 5

# Bingkai atas
print("#", end="")
for i_3024 in range(lebar_3024):
    print("=", end="")
print("#")

# Fase atas
for baris_3024 in range(n_3024, 0, -1):
    print("| ", end="")

    # Spasi kiri
    for spasi_3024 in range(2 * (n_3024 - baris_3024)):
        print(" ", end="")

    # Angka turun
    for angka_3024 in range(baris_3024, 0, -1):
        print(angka_3024, end=" ")

    print("<*>", end=" ")

    # Angka naik
    for angka_3024 in range(1, baris_3024 + 1):
        print(angka_3024, end=" ")

    # Spasi kanan
    for spasi_3024 in range(2 * (n_3024 - baris_3024)):
        print(" ", end="")

    print(" |")

# Titik tengah
print("| ", end="")

for spasi_3024 in range(2 * n_3024):
    print(" ", end="")

print("<*>", end="")

for spasi_3024 in range(2 * n_3024 + 1):
    print(" ", end="")

print(" |")

# Fase bawah
for baris_3024 in range(1, n_3024 + 1):
    print("| ", end="")

    # Spasi kiri
    for spasi_3024 in range(2 * (n_3024 - baris_3024)):
        print(" ", end="")

    # Angka turun
    for angka_3024 in range(baris_3024, 0, -1):
        print(angka_3024, end=" ")

    print("<*>", end=" ")

    # Angka naik
    for angka_3024 in range(1, baris_3024 + 1):
        print(angka_3024, end=" ")

    # Spasi kanan
    for spasi_3024 in range(2 * (n_3024 - baris_3024)):
        print(" ", end="")

    print(" |")

# Bingkai bawah
print("#", end="")
for i_3024 in range(lebar_3024):
    print("=", end="")
print("#")