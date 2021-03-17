from point import Point
import math 
class Vector(object):
    def __init__(self, point1, point2):
        self._punto1 = point1
        self._punto2 = point2

    def coordenadaX(self):
        return self._punto2.getPosX - self._punto1.getPosX

    def coordenadaY(self):
        return self._punto2.getPosY - self._punto1.getPosY

    def modulo(self):
        return math.sqrt(math.pow(self.coordenadaX(), 2) + math.pow(self.coordenadaY(), 2))

    def productoVectorial(self, vector):
        return self.coordenadaX()*vector.coordenadaY() - self.coordenadaY() * vector.coordenadaX

    def to_string(self):
        return "y="+( str(self._punto2.getPosX()) - str(self._punto1.getPosX()) )+"x+"+( str(self._punto2.getPosY()) - str(self._punto1.getPosY()) )


    