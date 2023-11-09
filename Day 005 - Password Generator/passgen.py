import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_choice = int(input("How many letters would you like in your password?\n"))
symbol_choice = int(input("How many symbols?\n"))
number_chocie = int(input("How many numbers?\n"))

password = []

for char in range(1, letters_choice + 1):
    password.append(random.choice(letters))


for char in range(1, symbol_choice + 1):
    password.append(random.choice(symbols))

for char in range(1, number_chocie + 1):
    password.append(random.choice(numbers))

random.shuffle(password)

print(f"Your password is {''.join(password)}")