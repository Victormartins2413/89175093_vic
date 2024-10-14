import pygame
import sys
import os
import time

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 1100
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tela de Configuração")

# Carregar a imagem de fundo
background_image = pygame.image.load('Imagens/Cidade_de_Aurora.png')

# Definir o fator de escala
fator_escala = 2
bg_width = int(background_image.get_width() * fator_escala)
bg_height = int(background_image.get_height() * fator_escala)
background_image = pygame.transform.scale(background_image, (bg_width, bg_height))

# Calcular posição centralizada da imagem de fundo
bg_x = (screen_width - bg_width) // 2
bg_y = (screen_height - bg_height) // 2

# Definir cores
white = (255, 255, 255)
black = (0, 0, 0)
back_button_color = (200, 0, 0)  # Cor diferente para o botão "Voltar"

# Variável para armazenar a mensagem e o tempo de exibição
message = ""
message_start_time = 0
message_duration = 2  # duração da mensagem em segundos

# Função para desenhar botões
def draw_button(screen, color, x, y, width, height, text, font_size=24):
    pygame.draw.rect(screen, color, [x, y, width, height])
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

# Função para desenhar mensagem
def draw_message(screen, message):
    font = pygame.font.Font(None, 48)
    text_surface = font.render(message, True, black)
    text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height - 50))
    screen.blit(text_surface, text_rect)

# Posições dos botões
button_positions = [
    (100, 100, "Movimento do personagem."),
    (100, 200, "Velocidade do personagem."),
    (100, 300, "Som dos passos dos jogadores."),
    (100, 400, "Som de ataques dos inimigos."),
    (100, 500, "Configuração da tela."),
    (600, 100, "Configuração do gráfico."),
    (600, 200, "Regulagem do brilho."),
    (600, 300, "Zoom da tela."),
    (600, 400, "Editar os personagens."),
    (600, 500, "Criar seu próprio personagem."),
]

# Adicionar posição do botão "Voltar" no canto esquerdo
back_button_position = (10, 10, "Voltar")  # Posição no canto superior esquerdo

# Loop principal do jogo
running = True
while running:
    current_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, (x, y, text) in enumerate(button_positions):
                if x <= mouse_x <= x + 300 and y <= mouse_y <= y + 50:  # Tamanho dos botões
                    message = f"{text} ativada"
                    message_start_time = current_time
            # Verificar clique no botão "Voltar"
            x, y, text = back_button_position
            if x <= mouse_x <= x + 100 and y <= mouse_y <= y + 30:  # Tamanho do botão "Voltar"
                os.execv(sys.executable, ['python', 'Jogando.py'])  # Executa jogando.py e fecha a tela atual

    # Desenhar o fundo
    screen.blit(background_image, (bg_x, bg_y))

    # Desenhar os botões
    for x, y, text in button_positions:
        draw_button(screen, white, x, y, 300, 50, text)  # Tamanho dos botões

    # Desenhar o botão "Voltar"
    x, y, text = back_button_position
    draw_button(screen, back_button_color, x, y, 100, 30, text, font_size=20)  # Botão "Voltar" pequeno

    # Desenhar a mensagem se estiver dentro do tempo de exibição
    if current_time - message_start_time < message_duration:
        draw_message(screen, message)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
