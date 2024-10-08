# Write a function that receives two characters and returns a single string with all the characters in between them (according to the ASCII code),
# separated by a single space. Print the result on the console

def chars_in_range(char1, char2):
    result = []
    for char in range(ord(char1) + 1, ord(char2)):
        result.append(chr(char))
    return " ".join(result)


char1 = input()
char2 = input()
print(chars_in_range(char1, char2))