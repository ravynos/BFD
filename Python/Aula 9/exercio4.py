from calculos_funcoes import media_numeros

def calcular_situacao(nome, n1, n2, n3):
    lista = [n1, n2, n3]
    return media_numeros(lista)
    
n = "Thiago"
m = calcular_situacao(n, 5, 8, 3)

print(f'A media de {n}, é {m:.2f}')