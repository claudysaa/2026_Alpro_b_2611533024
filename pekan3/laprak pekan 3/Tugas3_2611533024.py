# INPUT
nama_3024 = input("Nama: ")
member_3024 = input("Member? (ya/tidak): ")
belanja_3024 = int(input("Total belanja: "))
barang_3024 = int(input("Jumlah barang: "))
promo_3024 = input("Kode promo: ")

# PERBANDINGAN
cek_belanja_3024 = belanja_3024 >= 200000
cek_barang_3024 = barang_3024 >= 3
cek_member_3024 = member_3024 == "ya"

# MEMBERSHIP
promo_list_3024 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
promo_ada_3024 = promo_3024 in promo_list_3024

# LOGIKA
diskon_3024 = cek_member_3024 and cek_belanja_3024
akses_3024 = cek_member_3024 or promo_ada_3024
bukan_member_3024 = not cek_member_3024

# ARITMATIKA
if diskon_3024:
    potongan_3024 = belanja_3024 * 10 / 100
else:
    potongan_3024 = 0

total_3024 = belanja_3024 - potongan_3024
rata_3024 = belanja_3024 / barang_3024
sisa_3024 = belanja_3024 % barang_3024

# ASSIGNMENT
poin_3024 = 0
poin_3024 += barang_3024

# IDENTITY
a_3024 = promo_list_3024
b_3024 = a_3024
print("Identity:", a_3024 is b_3024)
print("Identity:", a_3024 is not promo_list_3024.copy())

# BITWISE
akses_bit_3024 = 0
if cek_member_3024:
    akses_bit_3024 |= 1
if cek_belanja_3024:
    akses_bit_3024 |= 2
if cek_barang_3024:
    akses_bit_3024 |= 4
if promo_ada_3024:
    akses_bit_3024 |= 8

print("\n=== HASIL ===")
print("Nama:", nama_3024)
print("Diskon:", potongan_3024)
print("Total bayar:", total_3024)
print("Rata-rata:", rata_3024)
print("Sisa:", sisa_3024)
print("Poin:", poin_3024)
print("Belanja >= 200000:", cek_belanja_3024)
print("Barang >= 3:", cek_barang_3024)
print("Promo ada:", promo_ada_3024)
print("Akses bit:", format(akses_bit_3024, "04b"))
print("AND:", akses_bit_3024 & 1)
print("XOR:", akses_bit_3024 ^ 3)