import random
import os

chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
         "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
         "a","b","c","d","e","f","g","h","i","j","k","l","m",
         "n","o","p","q","r","s","t","u","v","w","x","y","z",
         "1","2","3","4","5","6","7","8","9","0","!","*","#","$",]

number = input("Number of passwords: ")
number = int(number)
label = raw_input("What is the password for? ")
username = raw_input("Username: ")
length = input("Password length: ")
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)

print(password)

def open_file():
    file_to_open = os.path.expanduser('/Users/jamesrodgers/Documents/Projects/passgen/passwords.txt')
    f = open(file_to_open,"a")
    f.write(label)
    f.write(":")
    f.write(username)
    f.write(":")
    f.write(password)


open_file()
print("Program complete!")
