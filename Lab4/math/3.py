import math

def area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

num_sides = 4
side_length = 25
area = area(num_sides, side_length)
print(f"Number of sides: {num_sides}")
print(f"Length of a side: {side_length}")
print(f"The area: {area:.1f}")