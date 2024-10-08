# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"


numbers = input().split()
numbers = list(map(int, numbers))

print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum number is: {sum(numbers)}")