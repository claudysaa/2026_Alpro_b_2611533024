# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_3024
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program ini menggunakan operator perbandingan dalam Phyton

angka1_3024 = int(input("input angka-1:"))
angka2_3024 = int(input("input angka-2:"))

# Lebih besar dari
hasil = angka1_3024 > angka2_3024
print("\nOperator Lebih Besar Dari")
print("angka1_3024 > angka2_3024 =", hasil)

# Lebih kecil dari
hasil = angka1_3024 < angka2_3024
print("\nOperator Lebih Kecil Dari")
print("angka1_3024 < angka2_3024 =", hasil)

# Lebih besar dari sama dengan
hasil = angka1_3024 >= angka2_3024
print("\nOperator lebih besar dari sama dengan")
print("angka1_3024 >= angka2_3024 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_3024 <= angka2_3024
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_3024 <= angka2_3024 =", hasil)

# Sama dengan
hasil = angka1_3024 == angka2_3024
print("\nOperator sama dengan")
print("angka1_3024 == angka2_3024 =", hasil)

# Tidak sama dengan
hasil = angka1_3024 != angka2_3024
print("\nOperator tidak sama dengan")
print("angka1_3024 != angka2_3024 =", hasil)

# Tambahan: perbandingan berantai dalam Python
hasil = 0 < angka1_3024 < 100
print("\nPerbandingan berantai")
print("0 < angka1_3024 < 100 =", hasil)

hasil = 0 < angka2_3024 < 100
print("0 < angka2_3024 < 100 =", hasil)