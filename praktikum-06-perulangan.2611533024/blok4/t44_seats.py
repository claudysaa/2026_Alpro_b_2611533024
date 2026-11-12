<<<<<<< HEAD
blocked_seat = int(input("Enter blocked seat: "))

for row in range(1, 4):
    print("Row", row, end=": ")

    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")

=======
blocked_seat = int(input("Enter blocked seat: "))

for row in range(1, 4):
    print("Row", row, end=": ")

    for seat in range(1, 6):
        if seat == blocked_seat:
            break
        print(seat, end=" ")

>>>>>>> 227d915a98d41ebf5340ba90bc4bd924ca1b6155
    print()