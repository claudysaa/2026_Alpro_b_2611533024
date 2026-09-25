# Program Sistem Loket Alpro Adventure Park
# NIM: 2611533024

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung
nama_pengunjung_3024 = input("Masukkan Nama Pengunjung: ")
umur_3024 = int(input("Input umur anda: "))
sim_3024 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()
jumlah_tiket_3024 = int(input("Masukkan jumlah tiket        : "))

# Validasi jumlah tiket dengan IF tunggal
if jumlah_tiket_3024 <= 0:
    print("Peringatan: Jumlah tiket tidak valid.")

# 2. Pilihan Paket Wahana
print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba       (Rp 50.000)")
print("2. Arung Jeram        (Rp 75.000)")
print("3. Motor ATV Ekstrim  (Rp 120.000)")
print("4. Roller Coaster Kilat (Rp 100.000)")
print("5. All-Access VIP     (Rp 220.000)")

paket_3024 = int(input("Masukkan nomor paket (1-5): "))

harga_satuan_3024 = 0
nama_paket_3024 = ""
paket_valid_3024 = True

# Match-case
match paket_3024:
    case 1:
        nama_paket_3024 = "Safari Rimba"
        harga_satuan_3024 = 50000
    case 2:
        nama_paket_3024 = "Arung Jeram"
        harga_satuan_3024 = 75000
    case 3:
        nama_paket_3024 = "Motor ATV Ekstrim"
        harga_satuan_3024 = 120000
    case 4:
        nama_paket_3024 = "Roller Coaster Kilat"
        harga_satuan_3024 = 100000
    case 5:
        nama_paket_3024 = "All-Access VIP"
        harga_satuan_3024 = 220000
    case _:
        print("Paket wahana tidak valid!")
        paket_valid_3024 = False

if not paket_valid_3024:
    raise SystemExit

# Input member dan promo
is_member_3024 = input("Apakah Anda member? (y/t): ").strip().lower()
kode_promo_valid_3024 = input("Apakah kode promo valid? (y/t): ").strip().lower()

# 3. Validasi izin berkendara
print("\n--- Validasi Izin Wahana ---")

if paket_3024 == 3 and umur_3024 >= 17 and sim_3024 == 'y':
    print("Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_3024 == 3 and umur_3024 >= 17 and sim_3024 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_3024 == 3 and umur_3024 < 17 and sim_3024 == 'y':
    print("Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_3024 == 3 and umur_3024 < 17:
    print("Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif paket_3024 != 3 and umur_3024 >= 10:
    print("Anda memenuhi batas umur untuk wahana.")
else:
    print("Anda belum cukup umur untuk wahana ini.")

# 4. Menghitung subtotal
subtotal_3024 = harga_satuan_3024 * jumlah_tiket_3024
total_diskon_persen_3024 = 0

# Multi-if untuk akumulasi diskon
if subtotal_3024 >= 200000:
    total_diskon_persen_3024 += 10

if is_member_3024 in ['y', 'ya']:
    total_diskon_persen_3024 += 5

if kode_promo_valid_3024 in ['y', 'ya']:
    total_diskon_persen_3024 += 15

if jumlah_tiket_3024 >= 5:
    total_diskon_persen_3024 += 5

# 5. Menghitung pembayaran
nominal_diskon_3024 = subtotal_3024 * (total_diskon_persen_3024 / 100)
total_bayar_3024 = subtotal_3024 - nominal_diskon_3024

# Evaluasi bonus dengan IF-ELSE
if total_bayar_3024 > 300000:
    bonus_3024 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    bonus_3024 = "Terima kasih telah berkunjung."

# 6. Rincian pembayaran
print("\n=== RINCIAN PEMBAYARAN ===")
print(f"Nama Pengunjung     : {nama_pengunjung_3024}")
print(f"Paket Wahana        : {nama_paket_3024}")
print(f"Harga Satuan        : Rp {harga_satuan_3024:,.0f}")
print(f"Jumlah Tiket        : {jumlah_tiket_3024}")
print(f"Subtotal            : Rp {subtotal_3024:,.0f}")
print(f"Total Diskon        : {total_diskon_persen_3024}%")
print(f"Nominal Diskon      : Rp {nominal_diskon_3024:,.0f}")
print(f"Total Bayar         : Rp {total_bayar_3024:,.0f}")
print(f"Bonus               : {bonus_3024}")
print("=== TRANSAKSI SELESAI ===")