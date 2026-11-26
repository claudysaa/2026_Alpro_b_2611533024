kelas = input().split()
pengumpul = input().split()

kelas_set = set(kelas)
pengumpul_set = set(pengumpul)

belum = kelas_set - pengumpul_set

print("Submitted:", len(kelas_set) - len(belum), "students")
print("Not submitted:", len(belum), "students")

for nomor in kelas:
    if nomor not in pengumpul_set:
        print(nomor)