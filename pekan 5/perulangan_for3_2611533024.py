<<<<<<< HEAD
# Buat file dengan nama perulangan_for3_2611533024.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3024
# Program ini menggunakan fungsi input()

ulang_3024 = int(input("Masukkan jumlah perulangan: "))

jumlah = 0
for i in range(1, ulang_3024 + 1):
    print(i,end=" ")
    jumlah = jumlah + i

    if i < ulang_3024:
        print(" + ", end="")
    else:
        print(" = ", jumlah,end="")
print()
=======
# Buat file dengan nama perulangan_for3_2611533024.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3024
# Program ini menggunakan fungsi input()

ulang_3024 = int(input("Masukkan jumlah perulangan: "))

jumlah = 0
for i in range(1, ulang_3024 + 1):
    print(i,end=" ")
    jumlah = jumlah + i

    if i < ulang_3024:
        print(" + ", end="")
    else:
        print(" = ", jumlah,end="")
print()
>>>>>>> 227d915a98d41ebf5340ba90bc4bd924ca1b6155
print("Jumlah =", jumlah)