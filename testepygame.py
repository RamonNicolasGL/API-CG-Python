import pygame
import numpy as np
from createImage import createImage
from imageShow import imageShow
from primitives.setPixel import set_pixel
from primitives.testes.teste_dda import runTesteDDA


# Inicialize o Pygame
pygame.init()

#Cria janela com altura e largura especificadas
pixels = createImage(500,500)

#RGB(255,255,255)
set_pixel(pixels, 50, 50, (255, 255, 255))
set_pixel(pixels, 150, 50, (255, 255, 255))
set_pixel(pixels, 300, 50, (255, 255, 255))
set_pixel(pixels, 50, 400, (255, 255, 255))
set_pixel(pixels, 70, 350, (255, 255, 255))

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