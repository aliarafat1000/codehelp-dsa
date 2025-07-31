import numpy as np

# str = input()
# print(str)

a = input("Put a sentence: ")
print(a)

import getpass

password = getpass.getpass("Enter password: ")

import sys

line = sys.stdin.readline()
print("You typed:", line.strip())

a, b = input("Enter two numbers: ").split()
