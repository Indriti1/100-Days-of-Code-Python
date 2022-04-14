# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for letter in range(1, nr_letters + 1):
    random_letter_index = random.randint(0, len(letters) - 1)
    password += letters[random_letter_index]

for symbol in range(1, nr_symbols + 1):
    random_symbol_index = random.randint(0, len(symbols) - 1)
    password += symbols[random_symbol_index]

for number in range(1, nr_numbers + 1):
    random_number_index = random.randint(0, len(numbers) - 1)
    password += numbers[random_number_index]

print(f"Easy level password (Order not randomized): {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password2 = ""
list_of_elements = []
total_elements = nr_letters + nr_numbers + nr_symbols

for letter in range(1, nr_letters + 1):
    random_letter_index = random.randint(0, len(letters) - 1)
    list_of_elements.append(letters[random_letter_index])

for symbol in range(1, nr_symbols + 1):
    random_symbol_index = random.randint(0, len(symbols) - 1)
    list_of_elements.append(symbols[random_symbol_index])

for number in range(1, nr_numbers + 1):
    random_number_index = random.randint(0, len(numbers) - 1)
    list_of_elements.append(numbers[random_number_index])

for element in range(1, len(list_of_elements) + 1):
    random_element_index = random.randint(0, len(list_of_elements) - 1)
    password2 += list_of_elements.pop(random_element_index)

print(f"Hard level password (Order randomized): {password2}")