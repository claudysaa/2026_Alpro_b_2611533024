schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"]
}

# 6A
terbanyak = 0
hari_terpadat = ""

for hari, matkul in schedule.items():
    if len(matkul) > terbanyak:
        terbanyak = len(matkul)
        hari_terpadat = hari

print("Busiest day:", hari_terpadat,
      "(" + str(terbanyak) + " courses)")

# 6B
course = input()

jumlah = 0

for hari, matkul in schedule.items():
    if course in matkul:
        jumlah += 1

print(course + ":", jumlah, "days")