# Name: Claudya Annisa
# NIM: 2611533024
# Question 3
# Soal A

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])
# Soal B

text = "Algoritma dan Pemograman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)

text = "Claudya Annisa"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)