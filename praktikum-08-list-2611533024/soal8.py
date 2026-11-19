number_of_rows = 4
seats_per_row = 5

# Membuat denah kursi
seats = []

for i in range(number_of_rows):
    seats.append(["."] * seats_per_row)

count = 0

while True:
    # Menampilkan denah
    for i in range(number_of_rows):
        print("Row", i + 1, ":", *seats[i])

    row = int(input("Row (0 to stop): "))

    if row == 0:
        break

    seat = int(input("Seat: "))

    # Memeriksa nomor kursi
    if row < 1 or row > 4 or seat < 1 or seat > 5:
        print("Invalid seat.")

    elif seats[row - 1][seat - 1] == "X":
        print("Seat already taken.")

    else:
        seats[row - 1][seat - 1] = "X"
        count += 1
        print("Seat booked.")

print("Seats taken:", count)