import pygame
import random

# Inicializa o pygame
pygame.init()

# Tamanho da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🏀 Bola Maluca!")

# Cores
BRANCO = (255, 255, 255)
AZUL = (30, 144, 255)

# Propriedades da bola
raio = 30
x = random.randint(raio, largura - raio)
y = random.randint(raio, altura - raio)
vel_x = random.choice([-4, 4])
vel_y = random.choice([-4, 4])

# Loop do jogo
relogio = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualiza a posição da bola
    x += vel_x
    y += vel_y

    # Rebater nas bordas
    if x - raio <= 0 or x + raio >= largura:
        vel_x *= -1
    if y - raio <= 0 or y + raio >= altura:
        vel_y *= -1

    # Preenche o fundo
    tela.fill(BRANCO)

    # Desenha a bola
    pygame.draw.circle(tela, AZUL, (x, y), raio)

    # Atualiza a tela
    pygame.display.flip()

    # Controla os FPS
    relogio.tick(60)

pygame.quit()