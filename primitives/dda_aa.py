from primitives import setPixel
import math

#problema 1 = a intensidade está como tupla, ai o dda nao vai funcionar corretamente


def sign(numero):
    if numero <0:
        return -1
    elif (numero == 0):
        return 0
    else:
        return 1
    

def dda_aa(screen, xi, yi, xf, yf, intensidade):
    dx = xf-xi
    dy = yf-yi
    if (abs(dx) > abs(dy)):
        passos = abs(dx)
    else:
        passos = abs(dy)

    passo_x = dx/passos
    passo_y = dy/passos

    x = xi
    y = yi

    intensity = tuple(intensidade)
    setPixel.set_pixel(screen, x, y, intensity)
    for p in range (0, passos):
        x = x + passo_x
        y = y + passo_y
        if passo_x == 1:
            proporcao = abs(y - math.floor(y))
            color = [round((1-proporcao)*intensidade[0]), round((1-proporcao)*intensidade[1]), round((1-proporcao)*intensidade[2])]
            color_tuple = tuple(color)
            setPixel.set_pixel(screen, math.floor(x), math.floor(y), color_tuple)
            color2 = [round((proporcao)*intensidade[0]), round((proporcao)*intensidade[1]), round((proporcao)*intensidade[2])]
            color_tuple2 = tuple(color2)

            setPixel.set_pixel(screen, math.floor(x), math.floor(y + sign(passo_y)), color_tuple2)
        else:
            proporcao = abs(x - math.floor(x))
            color = [round((1-proporcao)*intensidade[0]), round((1-proporcao)*intensidade[1]), round((1-proporcao)*intensidade[2])]
            color_tuple = tuple(color)
            setPixel.set_pixel(screen, math.floor(x), math.floor(y), color_tuple)
            color2 = [round((proporcao)*intensidade[0]), round((proporcao)*intensidade[1]), round((proporcao)*intensidade[2])]
            color_tuple2 = tuple(color2)

            setPixel.set_pixel(screen, math.floor(x + sign(passo_x)), math.floor(y), color_tuple2)
