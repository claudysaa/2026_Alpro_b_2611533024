# Buat nama dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_3024
# Program ini menggunakan fungsi input()

umur_3024 = int(input("Input umur anda: "))
sim_3024 = input("Apakah Anda Sudah Punya Sim C ")[0]

if umur_3024 >= 17 and sim_3024 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_3024 >= 17 and sim_3024 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3024 < 17 and sim_3024 == 'y':
    print("Anda belum cukup umur punya sim")
else:
    print("Anda belum  cukup umur dan tidak boleh bawa motor")
print("Program Selesai")