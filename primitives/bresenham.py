from primitives.setPixel import set_pixel
import math

def bresenham(screen, xi, yi, xf, yf, intensidade):
    dx = xf - xi    
    dy = yf - yi

    y = yi
    p = dx - 2*dy
    
    for x in range (xi, xf):
        if p < 0:
            p = p - 2*dy + 2*dx
            y = y + 1
        else:
            p = p - 2*dy
        
        set_pixel(screen, x, y, intensidade);