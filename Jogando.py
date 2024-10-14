import pygame
import sys
import os

# Inicializar o Pygame
pygame.init()

# Definir cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurar a tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo 2D - Controlando o Liam")

# Definir o fator de escala
fator_escala = 0.9

try:
    # Carregar a imagem de fundo
    imagem_fundo = pygame.image.load('Imagens/Cidade_de_Aurora_test.png')
    print("Imagem de fundo carregada com sucesso.")
except pygame.error as e:
    print(f"Erro ao carregar a imagem de fundo: {e}")
    sys.exit()

# Obter o tamanho original da imagem de fundo
largura_fundo, altura_fundo = imagem_fundo.get_size()

# Calcular o novo tamanho com base no fator de escala
nova_largura_fundo = int(largura_fundo * fator_escala)
nova_altura_fundo = int(altura_fundo * fator_escala)

# Redimensionar a imagem de fundo
imagem_fundo = pygame.transform.scale(imagem_fundo, (nova_largura_fundo, nova_altura_fundo))
retangulo_fundo = imagem_fundo.get_rect()

try:
    # Carregar as imagens do personagem
    imagem_liam = pygame.image.load('Imagens/Liam.png')
    imagem_liam = pygame.transform.scale(imagem_liam, (30, 30))  # Redimensionar a imagem
    imagem_ataque_liam = pygame.image.load('Imagens/Liam1.png')
    imagem_ataque_liam = pygame.transform.scale(imagem_ataque_liam, (30, 30))  # Redimensionar a imagem de ataque
    print("Imagens do personagem carregadas com sucesso.")
except pygame.error as e:
    print(f"Erro ao carregar as imagens do personagem: {e}")
    sys.exit()

# Definir a imagem inicial do personagem
imagem_atual = imagem_liam
retangulo_liam = imagem_atual.get_rect()
# Definir a posição inicial do personagem na rua
retangulo_liam.topleft = (375, 500)  # Coordenadas iniciais (ajuste conforme necessário)

# Definir a velocidade de movimento do personagem
velocidade = 2

# Função para verificar se o personagem está nas ruas
def esta_na_rua(x, y):
    return 0 <= x <= largura_tela - retangulo_liam.width and 0 <= y <= altura_tela - retangulo_liam.height

# Função para desenhar um botão
def desenhar_botao(texto, cor, posicao):
    fonte = pygame.font.Font(None, 36)
    texto_renderizado = fonte.render(texto, True, cor)
    retangulo_botao = texto_renderizado.get_rect()
    retangulo_botao.topleft = posicao
    tela.blit(texto_renderizado, retangulo_botao)
    return retangulo_botao

def main():
    # Loop principal do jogo
    executando = True
    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verificar se o botão Sair foi clicado
                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()
                # Verificar se o botão Configuração foi clicado (ainda não implementado)
                if botao_configuracao.collidepoint(evento.pos):
                    os.execv(sys.executable, ['python', 'Configuração.py'])

        # Obter todas as teclas pressionadas
        teclas = pygame.key.get_pressed()

        # Armazenar a posição atual
        posicao_original = retangulo_liam.topleft

        # Mudar a imagem do personagem para a de ataque se a tecla T estiver pressionada
        if teclas[pygame.K_t]:
            imagem_atual = imagem_ataque_liam
        else:
            imagem_atual = imagem_liam

        # Mover o personagem
        if teclas[pygame.K_LEFT]:
            retangulo_liam.x -= velocidade
        if teclas[pygame.K_RIGHT]:
            retangulo_liam.x += velocidade
        if teclas[pygame.K_UP]:
            retangulo_liam.y -= velocidade
        if teclas[pygame.K_DOWN]:
            retangulo_liam.y += velocidade

        # Verificar se a nova posição é válida
        if not esta_na_rua(retangulo_liam.x, retangulo_liam.y):
            retangulo_liam.topleft = posicao_original  # Reverter para a posição original

        # Preencher a tela com branco
        tela.fill(BRANCO)

        # Desenhar o fundo
        tela.blit(imagem_fundo, retangulo_fundo)

        # Desenhar o personagem na tela
        tela.blit(imagem_atual, retangulo_liam)

        # Desenhar os botões
        botao_sair = desenhar_botao("Sair", VERMELHO, (10, 10))
        botao_configuracao = desenhar_botao("Configuração", AZUL, (largura_tela - 200, 10))

        # Atualizar a tela
        pygame.display.flip()

        # Definir a taxa de frames por segundo (FPS)
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()
