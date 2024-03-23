import pygame
import numpy as np
from createImage import createImage
from imageShow import imageShow
from primitives.setPixel import set_pixel
from primitives.testes.teste_dda import runTesteDDA
from primitives.testes.teste_setPixel import runTestSetPixel


# Inicialize o Pygame
pygame.init()

#Cria janela com altura e largura especificadas
pixels = createImage(500,500)

runTestSetPixel (pixels)
runTesteDDA(pixels)

#Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    #Atualiza o display
    imageShow()

# Encerre o Pygame
pygame.quit()