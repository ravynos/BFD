def media_numeros(numeros):
    if len(numeros)==0:
        return 0
    return sum(numeros) / len(numeros)

#lista = [5,5,5,5]
#media = media_numeros(lista)
#print(f'A media do aluno é {media}')