import pygame


# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura = 800
altura = 600
tamanho_janela = (largura, altura)

# Cria a janela
janela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Janela do Pygame")

# Loop principal
while True:
    # Verifica se o usuário clicou no botão fechar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a janela
    pygame.display.update()