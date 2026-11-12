# Name: Claudya Annisa
# NIM: 2611533024
# Question 

sentence = input("Masukkan kalimat: ")
clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")