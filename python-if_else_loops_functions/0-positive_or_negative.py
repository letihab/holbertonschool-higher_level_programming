#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f" the number {number} is positive")
elif number == 0:
    print(f"the number {number} is zero")
else:
    print(f"the number {number} is negative")
