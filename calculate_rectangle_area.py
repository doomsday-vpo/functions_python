# Create a function that calculates and returns the area of a rectangle by a given width and height. Print the result on the console.

def calculate_rectangle_area(width, height):
    return width * height


width = int(input())
height = int(input())
area = calculate_rectangle_area(width, height)

print(area)
