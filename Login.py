import pygame
import sys
import os
import sqlite3

import Jogo


# Inicialização do Pygame:
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (106, 159, 181)

# Definição da largura e altura da janela
WIDTH, HEIGHT = 900, 800

# Caminho completo para o arquivo do banco de dados
caminho_banco_de_dados = r'C:\Users\Victor\Music\Pasta_do_Tuguito\FIAP\Test-jogo\cadastro.db'

# Criar a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Login")

# Carregar a imagem
image = pygame.image.load("Imagens/Aurora-1.png")  # Substitua "Aurora-1.png" pelo caminho correto da sua imagem

# Definir o fator de escala da imagem
scale_factor = 1.5
scaled_image = pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor)))

# Fontes
title_font = pygame.font.Font(None, 48)
text_font = pygame.font.Font(None, 30)

# Função para desenhar a página de login
def draw_login_page(username, password, typing_username, typing_password, message=""):
    screen.fill(WHITE)

    # Desenhar a imagem
    screen.blit(scaled_image, ((WIDTH - scaled_image.get_width()) // 2, (HEIGHT - scaled_image.get_height()) // 2))

    # Desenhar o título
    title_text = title_font.render("Login", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)

    # Desenhar a entrada de texto para o nome de usuário
    pygame.draw.rect(screen, GRAY, (WIDTH // 4, HEIGHT // 2 - 50, WIDTH // 2, 40))
    pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 2 - 50, WIDTH // 2, 40), 2)
    username_label = text_font.render("Nome: ", True, BLACK)
    username_label_rect = username_label.get_rect(topleft=(WIDTH // 4 + 10, HEIGHT // 2 - 40))
    screen.blit(username_label, username_label_rect)
    if username:
        username_text = text_font.render(username, True, BLACK)
        username_rect = username_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
        screen.blit(username_text, username_rect)

    # Desenhar a entrada de texto para a senha
    pygame.draw.rect(screen, GRAY, (WIDTH // 4, HEIGHT // 2 + 10, WIDTH // 2, 40))
    pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 2 + 10, WIDTH // 2, 40), 2)
    password_label = text_font.render("Senha:", True, BLACK)
    password_label_rect = password_label.get_rect(topleft=(WIDTH // 4 + 10, HEIGHT // 2 + 20))
    screen.blit(password_label, password_label_rect)
    if password:
        password_text = text_font.render("*" * len(password), True, BLACK)
        password_rect = password_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
        screen.blit(password_text, password_rect)

    # Desenhar o botão de login
    pygame.draw.rect(screen, BLUE, (WIDTH // 4, HEIGHT // 2 + 90, WIDTH // 2, 50))
    pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 2 + 90, WIDTH // 2, 50), 2)
    login_text = text_font.render("Login", True, BLACK)
    login_rect = login_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 115))
    screen.blit(login_text, login_rect)

    # Desenhar o botão de voltar
    pygame.draw.rect(screen, GRAY, (WIDTH // 4, HEIGHT // 2 + 160, WIDTH // 2, 50))
    pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 2 + 160, WIDTH // 2, 50), 2)
    back_text = text_font.render("Voltar", True, BLACK)
    back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 185))
    screen.blit(back_text, back_rect)

    # Desenhar a mensagem de erro
    if message:
        error_text = text_font.render(message, True, BLACK)
        error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 250))
        screen.blit(error_text, error_rect)

    pygame.display.flip()

# Função para desenhar a página de configuração do jogo
def draw_game_configuration_page():
    screen.fill(WHITE)
    # Aqui você pode desenhar os elementos da página de configuração do jogo, como botões para escolher a dificuldade, configurações de áudio, etc.
    pygame.display.flip()

# Função para processar o login
def login(username, password):
    conn = sqlite3.connect(caminho_banco_de_dados)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cadastro WHERE nome=? AND senha=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login bem-sucedido!")
        Jogo.main()  # Chama a função main() do módulo Jogo.py para mostrar a página do jogo
    else:
        draw_login_page("", "", False, False, "Dados inválidos.")

# Função principal
def main():
    draw_login_page("", "", False, False)
    username = ""
    password = ""
    typing_username = False
    typing_password = False
    back_button_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 160, WIDTH // 2, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button_rect.collidepoint(mouse_pos):
                    os.system("python main.py")
                    pygame.quit()
                    sys.exit()
                elif WIDTH // 4 <= mouse_pos[0] <= 3 * WIDTH // 4 and HEIGHT // 2 - 50 <= mouse_pos[1] <= HEIGHT // 2 - 10:
                    typing_username = True
                    typing_password = False
                elif WIDTH // 4 <= mouse_pos[0] <= 3 * WIDTH // 4 and HEIGHT // 2 + 10 <= mouse_pos[1] <= HEIGHT // 2 + 50:
                    typing_username = False
                    typing_password = True
                elif WIDTH // 4 <= mouse_pos[0] <= 3 * WIDTH // 4 and HEIGHT // 2 + 90 <= mouse_pos[1] <= HEIGHT // 2 + 140:
                    login(username, password)
            elif event.type == pygame.KEYDOWN:
                if typing_username:
                    if event.key == pygame.K_RETURN:
                        typing_username = False
                        typing_password = True
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif typing_password:
                    if event.key == pygame.K_RETURN:
                        typing_password = False
                        login(username, password)
                    elif event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
        draw_login_page(username, password, typing_username, typing_password)
        if typing_username:
            pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 2 - 50, WIDTH // 2, 40), 2)
        elif typing_password:
            pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 2 + 10, WIDTH // 2, 40), 2)
        pygame.display.flip()

# Chamar a função principal
if __name__ == "__main__":
    main()
