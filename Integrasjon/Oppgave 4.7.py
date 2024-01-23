def f(x):
    return 2 * x


a = 2
b = 8
n = 10000
delta_x = (b - a) / n

x = a
integral = 0

for i in range(n):
    rektangel = f(x) * delta_x
    integral += rektangel
    x += delta_x

print(f"En tilnærming av integralet er {integral:.2f}")
