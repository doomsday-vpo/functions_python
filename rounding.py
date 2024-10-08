# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().

numbers = input().split()
rounded_numbers = []

for num in numbers:
    rounded_numbers.append(round(float(num)))

print(rounded_numbers)
