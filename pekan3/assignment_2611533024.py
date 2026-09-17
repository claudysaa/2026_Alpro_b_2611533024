# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 variabel nim terakhir contoh: angka1_3024
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Phyton

angka1_3024 = int(input("Input angka-1: "))
angka2_3024 = int(input("Input angka-2: "))

print("\nNilai awal angka1_3024 =",angka1_3024)
print("\nNilai awal angka2_3024 =", angka2_3024)

# Assignment biasa
hasil = angka1_3024 
print("\nAssigment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_3024
hasil += angka2_3024
print("\nAssigment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_3024
hasil -= angka2_3024
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_3024
hasil *= angka2_3024
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3024 !=0:
    hasil = angka1_3024
    hasil /= angka2_3024
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_3024
    hasil //= angka2_3024
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_3024
    hasil %= angka2_3024
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan,")
    print("Angka kedua tidak boleh bernilai 0.")

    # Operator tambahan: assignment perpangkatan
    hasil = angka1_3024
    hasil **= angka2_3024
    print("\nAssignment perpangkatan (**=)")
    print("Hasil =", hasil)