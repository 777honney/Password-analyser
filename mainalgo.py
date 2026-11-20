#Password analyser algorithm
import string

number="0123456789"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"

password = input("Enter a password: ")

#Weak Password Conditions 

if len(password) < 8 :
    print("It is less than 8 characters long.")
else:
    print("Password length is sufficient.")

if not any(char in number for char in password):
    print("It does not contain any numbers.")
else:
    print("Password contains at least one number.")

if not any(char in uppercase for char in password):
    print("It does not contain any uppercase letters.")      
else:
    print("Password contains at least one uppercase letter.")

if not any(char in lowercase for char in password):
    print("It does not contain any lowercase letters.")
else:
    print("Password contains at least one lowercas letter.")

if len(password) >= 8 and any(char in number for char in password) and any(char in uppercase for char in password) and any(char in lowercase for char in password):
    print("STRONG PASSWORD: It meets all the criteria for a strong password.")
else:
    print()

if len(password) < 8 or not any(char in number for char in password) or not any(char in uppercase for char in password) or not any(char in lowercase for char in password):
    print("WEAK PASSWORD: It does not meet all the criteria for a strong password.")
else:
    print()