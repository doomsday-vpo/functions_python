#Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a sorted list of numbers in ascending order. Use sorted().

numbers = input()

# Convert the input string into a list of integers
numbers_list = list(map(int, numbers.split()))

# Sort the list using sorted()
sorted_list = sorted(numbers_list)

# Print the sorted list
print(sorted_list)
