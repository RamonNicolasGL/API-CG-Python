from primitives.dda_aa import dda_aa

def poligono(pixels, pol, intensidade):
    if len(pol) < 2: 
        print ("menor que 2 lados")
        return
    
    
    for i in range(0, len(pol) - 1):
        dda_aa(pixels, pol[i][0], pol[i][1], pol[i + 1][0], pol[i + 1][1], intensidade)

    dda_aa(pixels, pol[-1][0], pol[-1][1], pol[0][0], pol[0][1], intensidade)