def f(x):
    return 3 * x**2


a = -1
b = 2
n = 1000
delta_x = (b - a) / n

x = a
integral = 0

for i in range(n):
    trapes = (f(x) + f(x + delta_x)) * delta_x / 2
    integral += trapes
    x += delta_x

print(f"En tilnærming av integralet er {integral:.2f}")
