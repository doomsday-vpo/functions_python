def is_even(number):
    return number % 2 == 0

numbers = input().split()
even_numbers = list(filter(lambda x: is_even(int(x)), map(int, numbers)))
result = ' '.join(map(str, even_numbers))

print('[' + ', '.join(map(str, even_numbers)) + ']')

