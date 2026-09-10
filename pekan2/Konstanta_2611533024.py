# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234
from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3024 = float(input('Masukkan niali jari-jari: '))
luas_3024 = PI * jari_3024 * jari_3024
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f") % (jari_3024, luas_3024)