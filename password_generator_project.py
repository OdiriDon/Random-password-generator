# Generating a random password

import random


characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_-"
while 1:
    password_len = int(input("What length would you like your password to be: "))
    password_count = int(input("How many passwords would you like: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_character = random.choice(characters)
            password += password_character
            print("Here is your random password : ", password)
            
import random 
characters = "abcdefghijklmnopqrstuvwxyz1234567890"
while 1:
    pass_len = int(input("How long do you want your password: "))
    pass_count = int(input("How many times do you want your random password? : "))
    for x in range(0, pass_count):
        password = ""
        for x in range(0, pass_len):
            pass_char = random.choice(characters)
            passowrd += pass_char
            print("This is your random password ", password )