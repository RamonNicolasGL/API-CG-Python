from primitives.setPixel import set_pixel

def runTestSetPixel (pixels): 
    #RGB(255,255,255)
    set_pixel(pixels, 50, 50, (255, 255, 255))
    set_pixel(pixels, 150, 50, (255, 255, 255))
    set_pixel(pixels, 300, 50, (255, 255, 255))
    set_pixel(pixels, 50, 400, (255, 255, 255))
    set_pixel(pixels, 70, 350, (255, 255, 255))