menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
sales = []

# Input penjualan
for i in range(3):
    daily = []
    for menu in menus:
        angka = int(input(f"Day {i+1}, {menu}: "))
        daily.append(angka)
    sales.append(daily)

# Total per hari
print("Total per day:")
for i in range(3):
    total = 0
    for j in range(3):
        total += sales[i][j]
    print(f"Day {i+1}: {total}")

# Total per menu
menu_totals = []

for j in range(3):
    total = 0
    for i in range(3):
        total += sales[i][j]
    menu_totals.append((menus[j], total))

print("Total per menu:", menu_totals)

# Menu terlaris
best_name, best_total = menu_totals[0]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")