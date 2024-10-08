repeat_string = lambda string, n: string * n

input_string = input()
count = int(input())
result = repeat_string(input_string, count)

print(result)
