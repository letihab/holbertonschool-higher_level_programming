#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # Obtient la valeur absolue du nombre et calcule le dernier chiffre.
is_negative = number < 0  # Vérifie si le nombre est négatif.

if is_negative:
    last_digit = -last_digit  # Change le signe du dernier chiffre si le nombre est négatif.

print("Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
