# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 9/26/2026
# Purpose: generates a sequence of 20 random values between 0 and 99, stores them in a list, prints the sequence, sorts it,
# and prints the sorted sequence. 
# Usage: ./lab3a.py
import random

seq = []
for x in range(20):
    seq.append(random.randint(0, 99))

print(seq)