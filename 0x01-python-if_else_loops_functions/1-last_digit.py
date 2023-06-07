#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dgt = abs(number) % 10
if number < 0:
    lst_dgt = -lst_dgt
print("Last digit of {} is {} and is ".format(number, lst_dgt), end="")
if lst_dgt > 5:
    print("greater than 5")
elif lst_dgt == 0:
    print("0")
else:
    print("less than 6 and not 0")
