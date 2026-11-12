# Name: Claudya Annisa
# NIM: 2611533024
# Question 7

name = "claudya annisa"
nim = "2611533024"

space = name.find(" ")
first_name = name if space == -1 else name[:space]
username = first_name + nim[-3:]
intake = "20" + nim[:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)