import pygame
import sys
import numpy as np
import copy
from environment import *
from ai import *
from pygame.locals import *



class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode([1200, 806])
        pygame.display.set_caption("Gobang")
        self.initialize()

    def initialize(self):
        self.map = np.zeros((15, 15))
        self.player_color = 1
        self.ai_color = 3 - self.player_color
        self.running = True
        self.turn = 1
        drawboard(self.screen)
        pygame.display.flip()

    def play(self):
        while True:
            self.initialize()
            self.mainloop()

    def replay(self):
        self.initialize()

    def mainloop(self):
        while True:
            pygame.display.flip()

            if self.turn == self.ai_color and self.running:

                ai = AI(self.map,self.ai_color)
                i, j = ai.ai_move()
                print("AI", i, j)

                self.map[i][j] = self.ai_color
                drawchess(i, j, self.screen, self.ai_color)

                result = self.checkwin(i, j, self.ai_color)
                if result != 0:
                    self.running = False

                self.turn = 3 - self.turn
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos[0], event.pos[1]
                        i = (x - 83) // 40
                        j = (y - 83) // 40
                        if 0 <= i < 15 and 0 <= j < 15 and self.running and self.turn == self.player_color:

                            print("Human", i, j)
                            drawchess(i, j, self.screen, self.player_color)
                            self.map[i][j] = self.player_color

                            result = self.checkwin(i,j,self.player_color)
                            if result != 0:
                                self.running = False
                            self.turn = 3 - self.turn
                            pygame.display.flip()

                        if 900 < x < 1100 and 500 < y < 600:
                            return

                        if 900 < x < 1100 and 650 < y < 750:
                            pygame.quit()
                            sys.exit()

    def checkwin(self,i,j,turn):
        if win1(i, j, self.map):
            if turn == 1:
                print("Black win")
                displaytext('Black wins', self.screen, 30)
                return 1
            elif turn == 2:
                print("White win")
                displaytext('White wins', self.screen, 30)
                return 2
        return 0


def printmap(map):
    for i in range(15):
        string = ""
        for j in range(15):
            string = string + str(map[j][i])
        print(string)


if __name__ == "__main__":
    game = Game()
    game.play()
