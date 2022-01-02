import pygame
import constantes
from random import randint


class Game_Snake:
    def __init__(self):
        # Criando janela
        pygame.init()
        self.windows = pygame.display.set_mode(
            (constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.NOME_GAME)
        self.font = pygame.font.match_font('arial')
        self.frames = pygame.time.Clock()
        self.playing = True

    def snake_draw(self, x, y, maca_x, maca_y):
        # Desenhando objetos na tela(snake)
        self.snake = pygame.draw.rect(self.windows, constantes.COR_GREEN,
                                      (x, y, 30, constantes.SIZE_Y_SNAKE))
        # Desenhando Maça
        self.maca = pygame.draw.circle(self.windows, constantes.COR_RED,
                                       (maca_x, maca_y), constantes.APPLE_SIZE)

    def snake_enyme(self, masterx=-40, mastery=-40, masterx2=-40, mastery2=-40):
        # Obstaculos
        self.obstaculo1 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (430, 100, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo2 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (430, 300, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo3 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (350, 500, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo4 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (150, 300, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo5 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (180, 200, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo6 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (280, 120, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo7 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (35, 430, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo8 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (10, 238, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo9 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (118, 20, constantes.SIZE_W, constantes.SIZE_H))
        self.obstaculo10 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (20, 118, constantes.SIZE_W, constantes.SIZE_H))
        self.master = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (masterx, mastery, 40, 40))
        self.master2 = pygame.draw.rect(
            self.windows, constantes.COR_WHITE, (masterx2, mastery2, 40, 40))

    def count_point(self, ponto):
        # mostrar pontuação
        fonte = pygame.font.Font(self.font, 15)
        text = fonte.render(f'Pontuação: {ponto}', True, (255, 255, 255))
        self.windows.blit(text, constantes.LOCAL_PLACAR)


snake = Game_Snake()

# movimentação inicial da snake
move_x = move_y = 0

# movimentação aleatoria dos Master
master_x = randint(40, 440)
master_y = randint(40, 560)
master_x2 = randint(40, 440)
master_y2 = randint(40, 560)

# movimentação da maça
maca_x = randint(10, 450)
maca_y = randint(10, 575)

# Placar do jogo
ponto = 0

while snake.playing:
    snake.frames.tick(60)
    snake.windows.fill((0, 0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    # Movimenta o personagem
    if pygame.key.get_pressed()[pygame.K_a]:
        if move_x >= 10:  # nao deixa o persongem sair da tela
            move_x -= 4
    if pygame.key.get_pressed()[pygame.K_d]:
        if move_x <= constantes.LARGURA - 40:  # nao deixa persongem sair tela
            move_x += 4
    if pygame.key.get_pressed()[pygame.K_w]:
        if move_y >= 10:  # nao deixa o persongem sair da tela
            move_y -= 4
    if pygame.key.get_pressed()[pygame.K_s]:
        if move_y <= constantes.ALTURA - 35:  # nao deixa o persongem sair tela
            move_y += 4

    snake.snake_draw(move_x, move_y, maca_x, maca_y)

    # movimenta a maça toda vez que ela for pega
    if snake.snake.colliderect(snake.maca):
        maca_x = randint(10, 450)
        maca_y = randint(10, 575)
        ponto += 1

    if ponto >= 5:  # ativa os inimigos
        snake.snake_enyme()

        if snake.snake.colliderect(snake.obstaculo1) or snake.snake.colliderect(snake.obstaculo2) or snake.snake.colliderect(snake.obstaculo3):
            move_x = move_y = 0
            ponto -= 1
        elif snake.snake.colliderect(snake.obstaculo4) or snake.snake.colliderect(snake.obstaculo5) or snake.snake.colliderect(snake.obstaculo6):
            move_y = move_x = 0
            ponto -= 1
        elif snake.snake.colliderect(snake.obstaculo7) or snake.snake.colliderect(snake.obstaculo8) or snake.snake.colliderect(snake.obstaculo9):
            move_y = move_x = 0
            ponto -= 1
        elif snake.snake.colliderect(snake.obstaculo10):
            move_y = move_x = 0
            ponto -= 1

    if ponto >= 15:  # ativa os Master

        snake.snake_enyme(master_x, master_y, master_x2, master_y2)
        if snake.snake.colliderect(snake.master):
            move_y = move_x = 0
            ponto -= ponto
        elif snake.snake.colliderect(snake.maca):
            master_x = randint(40, 440)
            master_y = randint(40, 560)

        if ponto >= 25:
            if snake.snake.colliderect(snake.master):
                move_y = move_x = 0
                ponto -= ponto
            elif snake.snake.colliderect(snake.maca):
                master_x2 = randint(40, 440)
                master_y2 = randint(40, 560)

    # Conta o Placar do jogo
    snake.count_point(ponto)
    pygame.display.update()
