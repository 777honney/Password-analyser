#Password dico
number="0123456789"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"

password = input("Enter a password: ")

print ("The password is: ", password)

#Weak Password Conditions 

if len(password) < 8:
    print("Weak Password: It must be at least 8 characters long.")

if not any(char in number for char in password):
    print("Weak Password: It must contain at least one number.")

if not any(char in uppercase for char in password):
    print("Weak Password: It must contain at least one uppercase letter.")

if not any(char in lowercase for char in password):
    print("Weak Password: It must contain at least one lowercase letter.")

#Correct Password Conditions

