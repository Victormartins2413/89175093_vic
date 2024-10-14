import pygame
import sys
import os
import sqlite3

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
pygame.display.set_caption("Cadastro")

# Carregar a imagem
image = pygame.image.load("Imagens/Aurora-1.png")  # Substitua "Aurora-1.png" pelo caminho correto da sua imagem

# Definir o fator de escala da imagem
scale_factor = 1.5
scaled_image = pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor)))

# Fontes
title_font = pygame.font.Font(None, 40)
text_font = pygame.font.Font(None, 30)

# Função para inserir os dados no banco de dados
def inserir_dados(nome, idade, altura, peso, senha, email):
    conn = sqlite3.connect(caminho_banco_de_dados)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO cadastro (nome, idade, altura, peso, senha, email) VALUES (?, ?, ?, ?, ?, ?)''',
                   (nome, idade, altura, peso, senha, email))
    conn.commit()
    conn.close()

# Função principal
def main():
    fields = {
        "Nome:": "",
        "Idade:": "",
        "Altura (cm):": "",
        "Peso (kg):": "",
        "Senha:": "",
        "Gmail ou E-mail:": ""
    }
    active_field = None
    draw_register_page(fields, active_field)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar se o mouse foi clicado em um campo de entrada
                mouse_x, mouse_y = event.pos
                top_offset = HEIGHT // 4
                for label, _ in fields.items():
                    field_rect = pygame.Rect(WIDTH // 4, top_offset, WIDTH // 2, 40)
                    if field_rect.collidepoint(mouse_x, mouse_y):
                        active_field = label
                    top_offset += 60
                # Verificar se o mouse foi clicado nos botões
                top_offset = HEIGHT - 140
                button_rect = pygame.Rect(WIDTH // 4 - 25, top_offset, WIDTH // 2, 50)
                if button_rect.collidepoint(mouse_x, mouse_y) and all(fields.values()):
                    # Extrair os valores dos campos
                    nome = fields["Nome:"]
                    idade = int(fields["Idade:"])
                    altura = float(fields["Altura (cm):"])
                    peso = float(fields["Peso (kg):"])
                    senha = fields["Senha:"]
                    email = fields["Gmail ou E-mail:"]
                    # Inserir os dados no banco de dados
                    inserir_dados(nome, idade, altura, peso, senha, email)
                    print("Cadastrado!")
                top_offset += 70
                button_rect = pygame.Rect(WIDTH // 4 - 25, top_offset, WIDTH // 2, 50)
                if button_rect.collidepoint(mouse_x, mouse_y):
                    os.system("python main.py")
                    pygame.quit()
                    sys.exit()
                draw_register_page(fields, active_field)
            elif event.type == pygame.KEYDOWN:
                if active_field is not None:
                    if event.key == pygame.K_RETURN:
                        active_field = None
                    elif event.key == pygame.K_BACKSPACE:
                        fields[active_field] = fields[active_field][:-1]
                    else:
                        fields[active_field] += event.unicode
                    draw_register_page(fields, active_field)

# Função para desenhar a página de cadastro
def draw_register_page(fields, active_field):
    screen.fill(WHITE)
    
    # Desenhar a imagem redimensionada centralizada na tela
    screen.blit(scaled_image, ((WIDTH - scaled_image.get_width()) // 2, (HEIGHT - scaled_image.get_height()) // 20))

    # Desenhar o título
    draw_text("Cadastro", title_font, BLACK, (WIDTH // 2, HEIGHT // 8), center=True)

    # Desenhar os campos de entrada
    top_offset = HEIGHT // 4
    for label, value in fields.items():
        # Desenhar o nome do campo fora da caixa
        draw_text(label, text_font, BLACK, (WIDTH // 4 - 200, top_offset + 5))
        # Desenhar a caixa de entrada
        draw_rect(WIDTH // 3 - 100, top_offset, WIDTH // 2, 40, GRAY, BLACK)
        if active_field == label:
            draw_rect(WIDTH // 3 - 98, top_offset + 2, WIDTH // 2 - 4, 36, BLUE, BLACK, 2)
        # Desenhar o valor dentro da caixa
        masked_value = "*" * len(value) if label == "Senha:" else value
        draw_text(masked_value, text_font, BLACK, (WIDTH // 2, top_offset + 20), center=True)
        top_offset += 60
    
    # Desenhar os botões
    draw_button("Cadastrar", (WIDTH // 4 - 25, HEIGHT - 140, WIDTH // 2, 50))
    draw_button("Voltar!", (WIDTH // 4 - 25, HEIGHT - 70, WIDTH // 2, 50))
    
    pygame.display.flip()

# Função para desenhar texto
def draw_text(text, font, color, pos, center=False):
    rendered_text = font.render(text, True, color)
    rect = rendered_text.get_rect()
    if center:
        rect.center = pos
    else:
        rect.topleft = pos
    screen.blit(rendered_text, rect)

# Função para desenhar retângulos
def draw_rect(x, y, width, height, fill_color, border_color, border_width=1):
    pygame.draw.rect(screen, fill_color, (x, y, width, height))
    pygame.draw.rect(screen, border_color, (x, y, width, height), border_width)

# Função para desenhar botões
def draw_button(text, rect):
    draw_rect(*rect, GRAY, BLACK)
    draw_text(text, text_font, BLACK, (rect[0] + rect[2] // 2, rect[1] + rect[3] // 2), center=True)

# Chamar a função principal
if __name__ == "__main__":
    main()
