#imports library in
import re
filename = input("Enter file name: ")
file = open(filename)
sum = 0
for line in file:
    numbers = re.findall('[0-9]+',line)
    if len(numbers) < 1: continue
    for number in numbers:
        number = int(number)
        sum = sum + number
print(sum)
