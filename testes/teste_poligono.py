from primitives.shapes.poligon import poligono
from primitives.shapes.insertPoint import insertPoint


def runPoligonTest(pixels):
    pol = []
    insertPoint(pol, 400, 500)
    insertPoint(pol, 500, 300)
    insertPoint(pol, 300, 300)
    poligono(pixels, pol, (255,255,255))
