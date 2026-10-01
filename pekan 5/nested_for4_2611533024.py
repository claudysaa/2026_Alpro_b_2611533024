# Buat file dengan nama nested_for4_2611533024.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_3024
# Program ini menggunakan fungsi input()

tinggi_3024 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3024 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3024 = tinggi_3024
    c_3024 = a_3024
    lebar_3024= (2 * tinggi_3024) -2

    for i_3024 in range(1, tinggi_3024 + 1):
        b_3024 = c_3024 + 1

        for j_3024 in range(1, lebar_3024 +1):

            # Baris atas dan bawah
            if i_3024 == 1 or i_3024 == tinggi_3024:
                if j_3024 == 1 or j_3024 == lebar_3024:
                    print("*", end=" ")
                else:
                    print(" ", end="") 

            # Baris isi
            else:
                if j_3024 == 1 or j_3024 == lebar_3024:
                    print("!", end=" ")
                else:
                    if j_3024 == c_3024:
                         print("<", end="")
                    elif j_3024 == b_3024:
                         print(">", end="")
                    elif j_3024 == (lebar_3024 - c_3024):
                         print("<", end="")
                    elif j_3024 == (lebar_3024 - c_3024 + 1):
                         print(">", end="")
                    elif j_3024 > b_3024 and j_3024 < (lebar_3024 -c_3024):
                         print("=", end="")
                    else:
                         print(" ",end="")

        print()

        # Logika asli Java
        a_3024 -= 2 
    
        if a_3024 <= 0:
            c_3024= (-a_3024) + 2
        else:
            c_3024 = a_3024