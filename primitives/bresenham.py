from primitives.setPixel import set_pixel
from primitives.dda_aa import sign

def bresenham(pixels, xi, yi, xf, yf, intensidade):
    
    if xf < xi:
        aux = xf
        xf = xi
        xi = aux

        aux = yf
        yf = yi
        yi = aux

    dx = abs(xf - xi)
    dy = abs(yf - yi)

    aux = 0 
    if dy>dx:
        aux = dx
        dx = dy
        dy = aux
        aux = 1

    y = 0
    dy2 = 2*dy
    dy2dx2 = dy2 - 2*dx
    s = sign(yf-yi)

    p = dx -dy2

    for x in range(0, dx):
        if p < 0:
            p = p - dy2dx2
            y = y + 1
        else:
            p = p - dy2

        if aux == 0:
            set_pixel(pixels, xi +x, yi + s*y, intensidade)
        else:
            set_pixel(pixels, xi +y, yi + s*x, intensidade)

