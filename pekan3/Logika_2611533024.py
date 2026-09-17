# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_3024
# Program ini menggunakan fungsi input()
# Program operator logika dalam Phyton

# Memasukkan nilai boolean 
# input tidak pekka terhadap huruf besar dan kecil
a1_3024 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3024 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3024)
print("A2 =", a2_3024)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_3024 and a2_3024
print("\nKonjungsi (AND)")
print("A1_3024 and A2_3024 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1_3024 or a2_3024
print("\nDisjungsi (OR)")
print("A1_3024 or A2_3024 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_3024
print("\nNegasi A1 (NOT)")
print("not A1_3024 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_3024
print("\nNegasi A2 (NOT)")
print("not A2_3024 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1_3024 != a2_3024
print("\nDisjungsi Eksklusif (XOR)")
print("A1_3024 XOR A2_3024 =", hasil)