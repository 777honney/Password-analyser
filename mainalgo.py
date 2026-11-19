#Password dico

import re 
import string

number="0123456789"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"

password = input("Enter a password: ")

print ("The password is: " + password + " is")

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

if len(password) >= 8 :
    print("Correct Password: It is at least 8 characters long.")

if any(char in number for char in password):
    print("Correct Password: It contains at least one number.")

if any(char in uppercase for char in password):
    print("Correct Password: It contains at least one uppercase letter.")

if any(char in lowercase for char in password):
    print("Correct Password: It contains at least one lowercase letter.")       

#Robust Password Conditions

if len(password) >= 8 and any(char in number for char in password) and any(char in uppercase for char in password) and any(char in lowercase for char in password):
    print("Robust Password: It meets all the criteria for a strong password.")