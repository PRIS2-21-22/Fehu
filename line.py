from point import Point

class Line(object):
    def __init__(self, pendiente, point = Point):
        self._x = pendiente
        self._n = -pendiente + point._x + point._y

    def to_string(self):
        return "y = "  + str(self._x) + "x + ("  + str(self._n) + ")"

    def implicita(self):
        return self._x + "x - y (" + self._n + ") = 0" 

    def punto_corte(self, otra):
            if (self._x == otra._x):
                return "paralelas o coincidentes"
            coordenada_x = (self._n-otra._n)/(self._x-otra._x)*(-1)
            coordenada_y = self._x*coordenada_x + self._n
            return "(" + str(coordenada_x) + ", " + str(coordenada_y) + ")"
