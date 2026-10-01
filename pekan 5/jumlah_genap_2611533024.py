# Buat file dengan nama jumlah_fenap_2611533024.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3024
# Program ini menggunakan fungsi input()

ulang_3024 = int(input("Masukkan nilai batas: "))

jumlah = 0
for i_3024 in range(1, ulang_3024 +1):
    if i_3024 % 2 == 0:
        print(i_3024,end=" ")
        jumlah = jumlah + i_3024

        if i_3024 < ulang_3024:
            print("+", end=" ")
        else:
            print("=", jumlah, end="")
print()
print("Jumlah =:", jumlah)