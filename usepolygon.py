
from polygon import Polygon
from vector import Vector
from point import Point
from line import Line

class UsePolygon:
    def __init__(self):
        puntoA = Point(2, 10) 
        puntoB = Point(0, 5)
        puntoC = Point(2, 0)
        puntoD = Point(8, 0)
        puntoE = Point(10, 5)
        puntoF = Point(8, 10)
        puntoP = Point(5, 5)

        vector1 = Vector(puntoA, puntoB)
        vector2 = Vector(puntoB, puntoC)
        listapuntos = list()
        listapuntos.append(puntoA)
        listapuntos.append(puntoB)
        listapuntos.append(puntoC)
        listapuntos.append(puntoD)
        listapuntos.append(puntoE)
        listapuntos.append(puntoF)
        listapuntos.append(puntoP)
        poligono = Polygon(listapuntos)

        listapuntos = list()
        listapuntos.append(puntoA)
        listapuntos.append(puntoC)
        listapuntos.append(puntoD)
        listapuntos.append(puntoF)
        poligono2 = Polygon(listapuntos)

        ln =  Line(1, Point(1, 1))
        ln2 =  Line(2, Point(0, 0))
        print(puntoA.toString()) 
        print(puntoB.toString())
        print(puntoC.toString())
        print(vector1.to_string())
        print(vector2.to_string())
        print(poligono.concavo())
        print(poligono2.concavo())
        print(poligono.centroide())
        print(poligono.concavo())    
        print(ln.to_string())  
        print(ln2.to_string())  
        print(ln.punto_corte(ln2))  



use = UsePolygon()
use.__init__()
"""
print(use.puntoA.toString()) 
print(use.puntoB.toString())
print(use.puntoC.toString())
print(use.vector1.to_string())
print(use.vector2.to_string())
print(use.poligono.concavo())
print(use.poligono2.concavo())
print(use.poligono.centroide())
print(use.poligono.concavo())    
print(use.ln.to_string())  
print(use.ln2.to_string())  
print(use.ln.punto_corte(use.ln2))  
"""
