class Veiculo:
    def __init__(self, marca, velocidade):
        self.marca = marca
        self.velocidade = velocidade
    
    def mover(self):
        return f"Veiculo {self.marca} se movendo"
    
class Carro(Veiculo):
    def __init__(self, marca, velocidade, ligar_motor):
        super().__init__(marca, velocidade)
        self.ligar_motor = ligar_motor

    def mover(self):
        return f"O Carro {self.marca} está {self.ligar_motor} a {self.velocidade} km/h"


class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade, pedalar):
        super().__init__(marca, velocidade)
        self.pedalar = pedalar
    
    def mover(self):
        return f"O Carro {self.marca} está {self.pedalar} a {self.velocidade} km/h"

veiculos = [
    Carro('Toyota', 120, "acelerando"),
    Bicicleta("Caloi", 25, "pedalando")
]

for v in veiculos:
    print(v.mover())