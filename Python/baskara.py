print("Calculando baskara!!!")

a = float(input("Qual o valor de a? "))
b = float(input("Qual valor de b? "))
c = float(input("Qual valor de c? "))
delta = (b ** b) - (4 * a * c)

if delta < 0:
    print(f"O delta é {delta:.2f}. Não há raiz real")
elif delta == 0:
    print(f"O delta é {delta:.2f}. A equação possui 1 raiz real.")
    raiz1 = -b / (2 * a)
    print(f"A raiz da equação de segundo grau é {raiz1} ")
else:
    print(f" O delta é {delta:.2f}. A equação possui 2 raizes reais.")
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    print(f"As raizes da equação de segundo grau são {raiz1:.2f} e {raiz2:.2f}")
