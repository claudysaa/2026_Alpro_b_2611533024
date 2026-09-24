# Buat file dengan nama multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_3024
# Program ini menggunakan fungsi input()

umur_3024 = int(input("Input umur anda: "))
sim_3024 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_3024 >= 17 and sim_3024 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_3024 >= 17 and sim_3024 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3024 < 17 and sim_3024 == 'y':
    print("Anda belum cukup umur punya SIM ")

if umur_3024 < 17 and sim_3024 != 'y':
    print("Anda Belum Cukup umur bawa motor")