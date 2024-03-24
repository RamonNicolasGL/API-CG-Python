from primitives.shapes.poligon import poligono
from primitives.shapes.insertPoint import insertPoint
import math

def frange (start, stop=None, step=None):
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    count = 0
    while True:
        temp = float (start + count * step)
        if step > 0 and temp >=stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count +=1




def circle(pixels, xc, yc, r, intensidade):
    c = []

    for ang in frange(0, 2*math.pi, 0.25):
        insertPoint(c, math.floor(xc + r*math.cos(ang)), math.floor(yc + r*math.sin(ang)))
    poligono(pixels, c, intensidade)
