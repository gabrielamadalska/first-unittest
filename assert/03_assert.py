width = int(input("Enter the width of the rectangle: "))
assert width > 0, "Width must be positive number"
height = int(input("Enter the height of the rectangle: "))
assert height > 0, "Height must be positive number"

area = width * height
print(f'Area: {area}')
