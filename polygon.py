
from vector import Vector
from point import Point
from line import Line

class Polygon(object):

    def __init__(self, puntos=list()):
        self._puntos = puntos

    def concavo(self):
        i = 0
        vec1 = Vector(self._puntos.get(i), self._puntos.get(i + 1))
        vec2 = Vector(self._puntos.get(i + 1), self._puntos.get(i + 2))
        prodVectorial = vec1.productoVectorial(vec2)
        positivo = prodVectorial >= 0
        i = 1
        for i in self._puntos:
            vec1 = Vector(self._puntos.get(i), self._puntos.get(i + 1))
            vec2 = Vector(self._puntos.get(i + 1), self._puntos.get(i + 2))
            prodVectorial = vec1.productoVectorial(vec2)
            if positivo != (prodVectorial >= 0):
                return True
        
        vec1 = Vector(self._puntos.get(i + 1), self._puntos.get(0))
        prodVectorial = vec2.productoVectorial(vec1)
        if positivo != (prodVectorial >= 0):
                return True
        
        return False

    def centroide(self):
        mod = self._puntos
        i = 0
        for i in self._puntos:
            A =+ self._puntos.get(i).getPosX() * self._puntos.get((i + 1)%mod).getPosY() - self._puntos((i + 1)%mod).getPosX()*self._puntos.get(i).getPosY()

        A = A/2

        for i in self._puntos:
            X =+ self._puntos.get(i).getPosX() + self._puntos.get((i + 1)%mod).getPosX() * self._puntos(i).getPosX() * self._puntos((i + 1)%mod).getPosY() - self._puntos((i + 1)%mod).getPosX() * self._puntos.get(i).getPosY()
        X = X/(6*A)

        for i in self._puntos:
            Y =+ self._puntos.get(i).getPosY() + self._puntos.get((i + 1)%mod).getPosY() * self._puntos(i).getPosX() * self._puntos((i + 1)%mod).getPosY() - self._puntos((i + 1)%mod).getPosX() * self._puntos.get(i).getPosY()
        Y = Y/(6*A)

        return Point(X, Y)

    def to_string(self):
        return str(self._puntos)