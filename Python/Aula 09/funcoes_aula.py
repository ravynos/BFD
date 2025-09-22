def div(i,j):
    if j == 0:
        print("O valor do j nunca pode ser 0.")
    else:
        return i / j

if __name__ == '__main__':
    
    i = float(input('Digite o primeiro numero: '))
    j = float(input('Digite o segundo numero: '))

    r = div(i,j)
    print(f'A divisão de {i} por {j} é {r:.2f}')