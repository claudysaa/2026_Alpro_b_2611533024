n = int(input())

kas = {}
total_kas = 0

for i in range(n):
    data = input().split()

    nama = data[0]
    nominal = int(data[1])

    if nama in kas:
        kas[nama] += nominal
    else:
        kas[nama] = nominal

    total_kas += nominal

for nama, total in kas.items():
    print(nama + ":", total)

print("Total cash:", total_kas)

terbesar = -1
pemenang = ""

for nama, total in kas.items():
    if total > terbesar:
        terbesar = total
        pemenang = nama

print("Top contributor:", pemenang, "(" + str(terbesar) + ")")