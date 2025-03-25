import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if self.x >= 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia 1"
        elif self.x < 0 and self.y >= 0 and self.z >= 0:
            return "Galaxia 2"
        elif self.x < 0 and self.y < 0 and self.z >= 0:
            return "Galaxia 3"
        elif self.x >= 0 and self.y < 0 and self.z >= 0:
            return "Galaxia 4"
        elif self.x >= 0 and self.y >= 0 and self.z < 0:
            return "Galaxia 5"
        elif self.x < 0 and self.y >= 0 and self.z < 0:
            return "Galaxia 6"
        elif self.x < 0 and self.y < 0 and self.z < 0:
            return "Galaxia 7"
        else:
            return "Galaxia 8"

    def distancia(self, otra_estrella):
        return math.sqrt((self.x - otra_estrella.x)**2 + (self.y - otra_estrella.y)**2 + (self.z - otra_estrella.z)**2)

# Creación de estrellas
estrella_A = Estrella(2, 3, 1)
estrella_B = Estrella(4, 4, 4)
estrella_C = Estrella(-3, -1, 0)

# Imprimir estrellas
print(f"Estrella A: {estrella_A}")
print(f"Estrella B: {estrella_B}")
print(f"Estrella C: {estrella_C}")

# Determinar galaxias
print(f"Galaxia de Estrella A: {estrella_A.galaxia()}")
print(f"Galaxia de Estrella B: {estrella_B.galaxia()}")
print(f"Galaxia de Estrella C: {estrella_C.galaxia()}")

# Calcular distancias
distancia_A_B = estrella_A.distancia(estrella_B)
distancia_B_C = estrella_B.distancia(estrella_C)
print(f"Distancia entre Estrella A y Estrella B: {distancia_A_B}")
print(f"Distancia entre Estrella B y Estrella C: {distancia_B_C}")

# (Opcional) Encontrar la estrella más lejos del origen
distancia_A_origen = estrella_A.distancia(Estrella())
distancia_B_origen = estrella_B.distancia(Estrella())
distancia_C_origen = estrella_C.distancia(Estrella())

if distancia_A_origen > distancia_B_origen and distancia_A_origen > distancia_C_origen:
    print("La estrella más lejos del origen es la Estrella A")
elif distancia_B_origen > distancia_A_origen and distancia_B_origen > distancia_C_origen:
    print("La estrella más lejos del origen es la Estrella B")
else:
    print("La estrella más lejos del origen es la Estrella C")