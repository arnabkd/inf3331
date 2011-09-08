import random
import sys

n = input ("Enter n :")
sum = 0;

for x in range (n):
    sum += random.uniform(-1 , 1)

print sum/n
