# This code if for hard password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
put_letters = int(input("How many letters would you like in your password?\n"))
put_symbols = int(input(f"How many symbols would you like?\n"))
put_numbers = int(input(f"How many numbers would you like?\n"))


password = []
output = ""
for letter in range(0, put_letters):
    password.append(random.choice(letters))
for symbol in range(0, put_symbols):
    password.append(random.choice(symbols))
for number in range(0, put_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
your_password = ""

for total in password:
    your_password += total
print(f"Your password is: {your_password}")