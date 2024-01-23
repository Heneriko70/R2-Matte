import math


def f(x):
    return math.log(x)


a = 1
b = 5
n = 10000
delta_x = (b - a) / n

x = a
integral = 0

for i in range(n):
    rektangel = f(x) * delta_x
    integral += rektangel
    x += delta_x

print(f"En tilnærming av integralet er {integral:.2f}")
