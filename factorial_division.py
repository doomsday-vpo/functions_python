# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


a = int(input())
b = int(input())
result = factorial(a) / factorial(b)
print(f"{result:.2f}")
