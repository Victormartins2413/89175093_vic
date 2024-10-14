import pygame
import sys


# Ligação dos outros arquivos:

from Login import main as login_main
from Cadastro import main as register_main






# Inicialização do Pygame:
pygame.init()




# Definição das cores
WHITE = (255, 255, 255)




# Definição da largura e altura da janela
WIDTH, HEIGHT = 900, 800




# Criar a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aurora's Realm: The Enchanted Adventure")




# Fonte
font = pygame.font.Font(None, 35)




# Função principal
def main():




    # Carregar a imagem da tela de entrada:
    original_image = pygame.image.load("Imagens/Cidade_de_Aurora.png").convert_alpha()




    # Definir o fator de escala
    scale_factor = 1.5




    # Redimensionar a imagem
    scaled_image = pygame.transform.scale(original_image, (original_image.get_width() * scale_factor, original_image.get_height() * scale_factor))




    # Desenhar a imagem redimensionada centralizada na tela
    screen.blit(scaled_image, ((WIDTH - scaled_image.get_width()) // 2, (HEIGHT - scaled_image.get_height()) // 2))




    # Definir as dimensões e a posição do botão "Start"
    button_width = 200
    button_height = 40
    button_x = (WIDTH - button_width) // 2
    button_y = HEIGHT - 200  




    # Desenhar o botão "Start"
    pygame.draw.rect(screen, WHITE, (button_x, button_y, button_width, button_height))
    text = font.render("Start", True, (0, 0, 0))
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)




    # Atualizar a tela
    pygame.display.flip()




    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:



                # Verificar se o botão "Start" foi clicado
                if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:



                    # Após clicar em "Start", oferecer opções para login ou cadastro
                    offer_options()

def offer_options():



    # Definir as dimensões e a posição dos botões de opção
    button_width = 200
    button_height = 40
    button_x = (WIDTH - button_width) // 2
    login_button_y = HEIGHT // 2 - 50
    register_button_y = HEIGHT // 2 + 20




    # Desenhar botões de opção para login e cadastro
    pygame.draw.rect(screen, WHITE, (button_x, login_button_y, button_width, button_height))
    login_text = font.render("Login", True, (0, 0, 0))
    login_text_rect = login_text.get_rect(center=(button_x + button_width // 2, login_button_y + button_height // 2))
    screen.blit(login_text, login_text_rect)

    pygame.draw.rect(screen, WHITE, (button_x, register_button_y, button_width, button_height))
    register_text = font.render("Cadastro", True, (0, 0, 0))
    register_text_rect = register_text.get_rect(center=(button_x + button_width // 2, register_button_y + button_height // 2))
    screen.blit(register_text, register_text_rect)




    # Atualizar a tela
    pygame.display.flip()




    # Loop para verificar qual botão foi clicado
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:



                # Verificar se o botão de login foi clicado
                if button_x <= event.pos[0] <= button_x + button_width and login_button_y <= event.pos[1] <= login_button_y + button_height:
                    login_main()  # Chamar a função principal do login




                # Verificar se o botão de cadastro foi clicado
                elif button_x <= event.pos[0] <= button_x + button_width and register_button_y <= event.pos[1] <= register_button_y + button_height:
                    register_main()  # Chamar a função principal do cadastro




# Chamar a função principal
if __name__ == "__main__":
    main()
