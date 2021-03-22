
from vector import VectorClass
from point import Point
from line import Line

class Polygon(object):

    def __init__(self, puntos):
        self._puntos = puntos

    def concavo(self):
        i = 0
        vec1 = VectorClass(self._puntos[i], self._puntos[i + 1])
        vec2 = VectorClass(self._puntos[i + 1], self._puntos[i + 2])
        prodVectorial = vec1.productoVectorial(vec2)
        positivo = prodVectorial >= 0
        i = 1
        j = 1
        for i in self._puntos:

            vec1 = VectorClass( self._puntos[j], self._puntos[j + 1])
            vec2 = VectorClass( self._puntos[j + 1], self._puntos[j + 2])
            prodVectorial = vec1.productoVectorial(vec2)
            if positivo != (prodVectorial >= 0):
                return True
        
        vec1 = VectorClass(self._puntos[j + 1], self._puntos[0])
        prodVectorial = vec2.productoVectorial(vec1)
        if positivo != (prodVectorial >= 0):
                return True
        j + 1
        return False

    def to_string(self):
        return str(self._puntos)


    def centroide(self):
        mod = len(self._puntos)
        j = 0
        i = 0
        for i in self._puntos:
            A =+ self._puntos[j].getPosX() * self._puntos[(j + 1)%mod].getPosY() - self._puntos[(j + 1)%mod].getPosX()*self._puntos[j].getPosY()
            j + 1
        A = A/2

        j = 0
        i = 0
        for i in self._puntos:
            X =+ self._puntos[j].getPosX() + self._puntos[(j + 1)%mod].getPosX() * self._puntos[j].getPosX() * self._puntos[(j + 1)%mod].getPosY() - self._puntos[(j + 1)%mod].getPosX() * self._puntos[j].getPosY()
            j + 1
        X = X/(6*A)

        j = 0
        i = 0
        for i in self._puntos:
            Y =+ self._puntos[j].getPosY() + self._puntos[(j + 1)%mod].getPosY() * self._puntos[j].getPosX() * self._puntos[(j + 1)%mod].getPosY() - self._puntos[(j + 1)%mod].getPosX() * self._puntos[j].getPosY()
            j + 1
        Y = Y/(6*A)
      
        return Point(int(X), int(Y))
  