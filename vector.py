from point import Point
import math

class VectorClass(object):
    def __init__(self, point1 = Point, point2 = Point ):
        self._punto1 = point1
        self._punto2 = point2

    def coordenada_x(self):
        return self._punto2._x - self._punto1._x

    def coordenada_y(self):
        return self._punto2._y - self._punto1._y

    def modulo(self):
        return math.sqrt(math.pow(self.coordenada_x(), 2) + math.pow(self.coordenada_y(), 2))

    def producto_vectorial(self, vector):
        return self.coordenada_x()*vector.coordenada_y() - self.coordenada_y() * vector.coordenada_x()

    def to_string(self):
        return "y="+ str(self._punto2._x - self._punto1._x) + "x+" + str( self._punto2._y - self._punto1._y )


    