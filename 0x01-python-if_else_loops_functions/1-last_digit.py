#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10
if last > 5:
    stat = "and is greater than 5"
elif last == 0:
    stat = "and is 0"
else:
    stat = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {stat}")
