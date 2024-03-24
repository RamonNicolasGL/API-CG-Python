from primitives.shapes.poligon import poligono
from primitives.shapes.insertPoint import insertPoint
import math

def circle(pixels, xc, yc, r, intensidade):
    c = []

    step_factor = 4 
    for ang in range(0, int(2*math.pi*step_factor), step_factor):
        insertPoint(c, math.floor(xc + r*math.cos(ang/step_factor)), math.floor(yc + r*math.sin(ang/step_factor)))
    poligono(pixels, c, intensidade)
