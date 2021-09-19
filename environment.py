import numpy as np
import pygame

background=(201,202,187)
checkerboard=(80,80,80)
button=(52,53,44)

def drawboard(screen):

    screen.fill(background)

    for i in range(14):
        pygame.draw.line(screen, checkerboard, (40 * i + 103, 103), (40 * i + 103, 663))
        pygame.draw.line(screen, checkerboard, (103, 40 * i + 103), (663, 40 * i + 103))

    pygame.draw.line(screen, checkerboard, (103, 103), (663, 103), 5)
    pygame.draw.line(screen, checkerboard, (103, 103), (103, 663), 5)
    pygame.draw.line(screen, checkerboard, (663, 103), (663, 663), 5)
    pygame.draw.line(screen, checkerboard, (103, 663), (663, 663), 5)

    pygame.draw.circle(screen, checkerboard, (223, 223), 6)
    pygame.draw.circle(screen, checkerboard, (223, 543), 6)
    pygame.draw.circle(screen, checkerboard, (543, 223), 6)
    pygame.draw.circle(screen, checkerboard, (543, 543), 6)
    pygame.draw.circle(screen, checkerboard, (383, 383), 6)

    pygame.draw.rect(screen, button, [900, 500, 200, 100], 5)
    pygame.draw.rect(screen, button, [900, 650, 200, 100], 5)
    s_font = pygame.font.Font('arial.ttf', 40)
    text2 = s_font.render("Restart", True, button)
    text3 = s_font.render("Exit", True, button)
    screen.blit(text2, (920, 520))
    screen.blit(text3, (920, 670))


def drawchess(x,y,screen,color):
    if color == 1:
        chess = pygame.image.load("Black_chess.png").convert_alpha()
        screen.blit(chess,(40*x+88,40*y+88))
    if color == 2:
        chess = pygame.image.load("White_chess.png").convert_alpha()
        screen.blit(chess,(40*x+88,40*y+88))


def displaytext(s,screen,size):
    pygame.draw.rect(screen,background,[850,100,1200,100])
    s_font=pygame.font.Font('arial.ttf',size)
    s_text=s_font.render(s,True,button)
    screen.blit(s_text,(880,100))
    pygame.display.flip()

