#!/usr/bin/env python3

from snake import Snake
from food import Food

class Game:

    def __init__(self, board_size):
        self.__board_size = board_size
        self.__snake = Snake([board_size//2, board_size//2])
          self.__food = Food(5, 5, 50, board_size)

        self.__init_game()

    def start(self, FPS):
        clock = pygame.time.Clock()

        self.__init()

        while not game_over:
           self.__logic()
           self.__render()

           clock.tick(FPS)

    def __init_game(self):
        pygame.init()

        self.__screen = pygame.display.set_mode((self.board_size+150, self.board_size+100))
        self.__game_over = False

    def __render(self):
        self.__food.draw(screen)
        self._snake.draw(screen)

        pygame.display.update()

if __name__ == '__main__':
    pass
