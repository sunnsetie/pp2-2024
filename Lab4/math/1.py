import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = 15
radian = degree_to_radian(degree)
print(f"{degree}")
print(f"{radian:.6f}")