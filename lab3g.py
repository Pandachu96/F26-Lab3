# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 9/30/2026
# Purpose: A program that reads values from standard input from user(using input function), 
# stores the inputted values in a list, multiplies each element by 10, and prints the result in reverse order.
# Usage: ./lab3g.py

# Follow the specific instructions given in the README.md file
nums = []

while len(nums) != 6:
    nums.append(10 * int(input('Enter number: ')))

nums.sort(reverse=True)
print(nums)