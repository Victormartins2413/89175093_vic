import pygame
import sys
from moviepy.editor import VideoFileClip
import Jogando

# Inicialização do Pygame:
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (106, 159, 181)

# Definição da largura e altura da janela
WIDTH, HEIGHT = 900, 800

# Criar a janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Página do Jogo")

# Carregar a imagem
image = pygame.image.load("Imagens/Aurora-1.png")
scale_factor = 1.5
scaled_image = pygame.transform.scale(image, (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor)))

# Fonte
text_font = pygame.font.Font(None, 30)

# Função para desenhar a página do jogo
def draw_game_page():
    screen.fill(WHITE)
    screen.blit(scaled_image, ((WIDTH - scaled_image.get_width()) // 2, (HEIGHT - scaled_image.get_height()) // 2))

    # Desenhar o botão de entrar
    pygame.draw.rect(screen, BLUE, (WIDTH // 2 - 50, HEIGHT // 2 + 200, 100, 50))
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 50, HEIGHT // 2 + 200, 100, 50), 2)
    enter_text = text_font.render("Entrar", True, BLACK)
    enter_rect = enter_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 225))
    screen.blit(enter_text, enter_rect)

    pygame.display.flip()

# Função principal
def main():
    draw_game_page()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if WIDTH // 2 - 50 <= mouse_pos[0] <= WIDTH // 2 + 50 and HEIGHT // 2 + 200 <= mouse_pos[1] <= HEIGHT // 2 + 250:
                    print("Entrando!")
                    play_video("Imagens/Vídeo_de_entrada.mp4")
                    Jogando.main()  # Chama a função principal do jogo

def play_video(video_path):
    clip = VideoFileClip(video_path)
    clip_resized = clip.resize((WIDTH, HEIGHT))
    clip_resized.preview()

if __name__ == "__main__":
    main()
