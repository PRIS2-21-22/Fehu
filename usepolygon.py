from polygon import Polygon
from vector import VectorClass
from point import Point
from line import Line

class UsePolygon:
    def __init__(self):
        punto_a = Point(2, 10) 
        punto_b = Point(0, 5)
        punto_c = Point(2, 0)
        punto_d = Point(8, 0)
        punto_e = Point(10, 5)
        punto_f = Point(8, 10)
        punto_p = Point(5, 5)

        vector1 = VectorClass(punto_a, punto_b)
        vector2 = VectorClass(punto_b, punto_c)
        listapuntos = []
        listapuntos.append(punto_a)
        listapuntos.append(punto_b)
        listapuntos.append(punto_c)
        listapuntos.append(punto_d)
        listapuntos.append(punto_e)
        listapuntos.append(punto_f)
        listapuntos.append(punto_p)
        poligono = Polygon(listapuntos)

        listapuntos = []
        listapuntos.append(punto_a)
        listapuntos.append(punto_c)
        listapuntos.append(punto_d)
        listapuntos.append(punto_f)
        poligono2 = Polygon(listapuntos)

        ln =  Line(1, Point(1, 1))
        ln2 =  Line(2, Point(0, 0))
        print(punto_a.to_string()) 
        print(punto_b.to_string())
        print(punto_c.to_string())
        print(vector1.to_string())
        print(vector2.to_string())
        print(poligono.concavo())
        print(poligono2.concavo())
        print(poligono.centroide().to_string())
        print(poligono.concavo())    
        print(ln.to_string())  
        print(ln2.to_string())  
        print(ln.punto_corte(ln2))  



use = UsePolygon()
use.__init__()
