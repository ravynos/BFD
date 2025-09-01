def calculo_area(base, altura):
    return base * altura

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def saudacao_horario(nome, hora):
    if 5 <= hora < 12:
        return f"Bom dia, {nome}!"
    elif 12 <= hora < 18:
        return f"Boa tarde, {nome}!"
    else:
        return f'Boa noite, {nome}'
    

area =  calculo_area(5,3)
print(f'A area é {area}')

temp_f = celsius_para_fahrenheit(25)
print(f'25 C = {temp_f}F')

msg = saudacao_horario('Thiago', 15)
print(msg)