import math
import os
import random
import re
import sys

def solve(s):
    parts = s.split()  # Split the input string by spaces
    result = []  # List to store the final result
    
    for part in parts:
        if part.isdigit():  # Check if the part is a number
            result.append(int(part))  # Append the number as an integer
        else:
            result.append(part.capitalize())  # title the non-number part first letter in Upper case 
    return ' '.join(map(str, result))

s = input()
print(solve(s))
