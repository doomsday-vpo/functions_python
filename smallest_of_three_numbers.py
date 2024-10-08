#Write a function that receives three integer numbers and returns the smallest. Print the result on the console. Use an appropriate name for the function.

def find_smallest_number(num1, num2, num3):
    return min(num1, num2, num3)

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(find_smallest_number(num1, num2, num3))