# Formula de baskara

# ax2+bx+x = 0
# a = ? b = ? c = ?

# delta = b2-4ac

# delta < 0 = raiz invalida
# delta = 0 = 1 raiz
# delta > 0 = 2 raizes

# raiz 1 = -b + (delta) quadrado / 2 a

# raiz 2 = -b - (delta)2

# msg = As raizes da equação ax2+bx+c=0 são. 

print("Calculando baskara!!!")

a = int(input("Qual o valor de a? "))
b = int(input("Qual valor de b? "))
c = int(input("Qual valor de c? "))
delta = b * b - 4 * a * c

if delta < 0:
    print("Não a raiz real!")
elif delta == 0:
    print("Delta possui 1 raiz.")
    raiz1 = -b + delta ** 0.5 / 2 * a
    print(f"A raiz da equação de segundo grau é {raiz1} ")
else:
    print("Delta possui 2 raizes.")
    raiz1 = (-b + delta ** 0.5) / 2 * a
    raiz2 = (-b - delta ** 0.5) / 2 * a
    print("As raizes da equação de segundo grau são {raiz1} e {raiz2}")
