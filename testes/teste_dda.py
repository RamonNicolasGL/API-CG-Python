from primitives.dda_aa import dda_aa


def runTesteDDA (pixels):
    ## Teste DDA
    dda_aa(pixels, 20, 20, 50, 50, (255, 255, 255)) #45 graus
    dda_aa (pixels, 80, 80, 30, 30, (255, 255, 255)) #45 graus ao contrario

    dda_aa (pixels, 40, 40, 150, 390, (255, 255, 255))
    dda_aa (pixels, 20, 400, 120, 10, (255, 255, 255))

    dda_aa (pixels, 30, 30, 450, 30, (255, 255, 255)) #reta no y 30
    dda_aa (pixels, 450, 450, 40, 450, (255, 255, 255)) #reta voltando no 450

    dda_aa (pixels, 160, 40, 160, 400, (255, 255, 255)) #reta vertical x= 160
    dda_aa (pixels, 20, 20, 50, 50, (255, 255, 255))

    ## unico dda com aa, passando lista como parametro
    dda_aa (pixels, 590, 400, 590, 50, [255, 255, 255]) #reta vertical voltando x = 590

    dda_aa (pixels, 500, 40, 200, 310, (255, 255, 255))
    dda_aa (pixels, 450, 450, 200, 200, (255,255,255))