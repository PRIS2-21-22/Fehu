from point import Point

class Line(object):
    def __init__(self, pendiente, point = Point):
        self._x = pendiente
        self._n = -pendiente*point.getPosX() + point.getPosY()

    def to_string(self):
        return "y = "  + self._x + "x + ("  + self._n + ")"

    def implicita(self):
        return self._x + "x - y (" + self._n + ") = 0" 

    def punto_corte(self, otra):
            if (self._x == otra._x):
                return "paralelas o coincidentes"
            coordenadaX = (self._n-otra._n)/(self._x-otra._x)*(-1)
            coordenadaY = self._x*coordenadaX + self._n
            return "(" + coordenadaX + ", " + coordenadaY + ")"
