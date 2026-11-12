# Name: Claudya Annisa
# NIM: 2611533024
# Question 4

phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)

phone = "08123456789"
jumlah_bintang = len(phone) - 7
masked = phone[:4] + "*" * jumlah_bintang + phone[-3:]
print(masked)

phone = "082611533024"
jumlah_bintang = len(phone) - 7
masked = phone[:4] + "*" * jumlah_bintang + phone[-3:]
print(masked)