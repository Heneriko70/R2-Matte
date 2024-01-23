def f(x):
    return x**2 + 1  # Definerer funksjonen vi skal integrere


a = 0  # Setter startverdien til 0
b = 2  # Setter sluttverdien til 2
n = 1000  # Setter antall rektangler til 1000

delta_x = (b - a) / n  # Regner ut delta_x
x = a  # Setter x til å være lik startverdien
areal = 0  # Setter arealet til 0

for i in range(n):  # Kjører løkken n ganger
    trapes = (f(x) + f(x + delta_x)) * delta_x / 2  # Regner ut arealet av trapeset
    areal += trapes  # Legger til arealet av trapeset til arealet
    x += delta_x  # Øker x med delta_x

print(f"Arealet er {areal:.2f}")  # Printer ut arealet med 2 desimaler
