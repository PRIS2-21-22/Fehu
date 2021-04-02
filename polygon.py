from vector import VectorClass
from point import Point

class Polygon(object):

    def __init__(self, puntos):
        self._puntos = puntos

    def concavo(self):
        i = 0
        vec1 = VectorClass(self._puntos[i], self._puntos[i + 1])
        vec2 = VectorClass(self._puntos[i + 1], self._puntos[i + 2])
        prod_vectorial = vec1.producto_vectorial(vec2)
        positivo = prod_vectorial >= 0

        mod = len(self._puntos)
        i = 1
        for i in range(mod - 2):

            vec1 = VectorClass( self._puntos[i], self._puntos[i + 1])
            vec2 = VectorClass( self._puntos[i + 1], self._puntos[i + 2])
            prodVectorial = vec1.producto_vectorial(vec2)
            if positivo != (prodVectorial >= 0):
                return True
        
        vec1 = VectorClass(self._puntos[i + 1], self._puntos[0])
        prod_vectorial = vec2.producto_vectorial(vec1)
        if positivo != (prod_vectorial >= 0):
                return True
        return False

    def to_string(self):
        return str(self._puntos)


    def centroide(self):
        mod = len(self._puntos)
        
        for i in range(mod):
            A =+ self._puntos[i]._x * self._puntos[(i + 1)%mod]._y - self._puntos[(i + 1)%mod]._x*self._puntos[i]._y
        A = A/2

    
        for i in range(mod):
            X =+ self._puntos[i]._x + self._puntos[(i + 1)%mod]._x * self._puntos[i]._x * self._puntos[(i + 1)%mod]._y - self._puntos[(i + 1)%mod]._x * self._puntos[i]._y
        X = X/(6*A)

      
        for i in range(mod):
            Y =+ self._puntos[i]._y + self._puntos[(i + 1)%mod]._y * self._puntos[i]._x * self._puntos[(i + 1)%mod]._y - self._puntos[(i + 1)%mod]._x * self._puntos[i]._y
        Y = Y/(6*A)
      
        return Point(int(X), int(Y))
  