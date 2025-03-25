
import math
class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Galaxia(Estrella):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)   
        
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