<<<<<<< HEAD
MAX_ATTEMPTS = 3  
correct_pin = "1234"  
attempt = 1  

pin = input("Enter PIN: ")  
while pin != correct_pin and attempt < MAX_ATTEMPTS:  
    print("Incorrect PIN.")  
    attempt += 1  
pin = input("Enter PIN: ")  
if pin == correct_pin:  
    print("Access granted")  
else:  
=======
MAX_ATTEMPTS = 3  
correct_pin = "1234"  
attempt = 1  

pin = input("Enter PIN: ")  
while pin != correct_pin and attempt < MAX_ATTEMPTS:  
    print("Incorrect PIN.")  
    attempt += 1  
pin = input("Enter PIN: ")  
if pin == correct_pin:  
    print("Access granted")  
else:  
>>>>>>> 227d915a98d41ebf5340ba90bc4bd924ca1b6155
    print("Account locked")