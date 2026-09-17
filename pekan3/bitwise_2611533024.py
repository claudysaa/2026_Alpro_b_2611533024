# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_3024
# Program ini menggunakan fungsi input()

print("\n===================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_3024 = int(input("Masukkan angka bitwise-1: "))
angka2_3024 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner:")
print("angka1_3024 =", angka1_3024, "| biner =", bin(angka1_3024))
print("angka2_3024 =", angka2_3024, "| biner =", bin(angka2_3024))

# Bitwise AND
hasil = angka1_3024 & angka2_3024
print("\nBitwise AND (&)")
print(angka1_3024, "&", angka2_3024, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_3024 | angka2_3024
print("\nBitwise OR (|)")
print(angka1_3024, "|", angka2_3024, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1_3024 ^ angka2_3024
print("\nBitwise XOR (^)")
print(angka1_3024, "^", angka2_3024, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1_3024
print("\nBitwise NOT (~)")
print("~", angka1_3024, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_3024 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_3024, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_3024 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_3024, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))