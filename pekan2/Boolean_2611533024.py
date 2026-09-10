# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_3024 = True
is_cumlaude_3024 = True

# Menggunakan Boolean
nilai_3024 = 75
batas_lulus_3024 =75

# Menentukan nilai Boolean da ri kondisi
status_kelulusan = nilai_3024 >= batas_lulus_3024  # Hasilnya akan True

print("=== Check kelulusan ===")
print("Nilai:", nilai_3024)
print("Apakah lulus?:", status_kelulusan)
if is_lulus_3024 and is_cumlaude_3024:
        print("Selamat, Anda lulus dengan predikat Cum Laude!")