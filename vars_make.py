"""
author: Viktoriia Hromiak
date: 2026/ 02 /12
0.4 - Variables (Make)

"""
import math
# Input
c_radius = int(input("Please enter the radius of the circle: "))
rectangle_l = int(input("Please enter the length of the rectangle: "))
rectangle_w =int(input("Please enter the width of the rectangle: "))
octagon = int(input("Please enter a side length of the octagon: "))

# Processing

circle_a = math.pi * {c_radius} ** 2
circle_p = 2 * math.pi * {c_radius}

rectangle_a = rectangle_l * rectangle_w
rectangle_p = 2 * (rectangle_l + rectangle_w)

octagon_a = 2 * (1 + math.sqrt(2)) * octagon ** 2
octagon_p = 8 * octagon

# Output

print(f"The circle has an area of {circle_a} and a perimeter of {circle_p}")
print(f"The rectangle has an area of {rectangle_a} and a perimeter of {rectangle_p}")
print(f"The octagon has an area of {octagon_a} and a perimeter of {octagon_p}")