#!/usr/bin/env python3

from snake import Snake
from food import Food
import sys
import pygame
import random

class Game:

    def __init__(self, board_size):
        self.__board_size = board_size
        self.__food = Food(random.randint(0, board_size//4), random.randint(0, board_size//6), 50, board_size)
        self.__snake_vel = [0, 0]

        self.__init_game()

    def start(self, FPS):
        clock = pygame.time.Clock()

        while not self.__game_over:
           self.__logic()
           self.__input()
           self.__render()

           clock.tick(FPS)

    def __init_game(self):
        pygame.init()

        self.__BACKGROUND_COLOR = (0, 0, 0)
        self.__score_font = pygame.font.SysFont("monospace", 35)
        
        self.__WIDTH = self.__board_size+150
        self.__HEIGHT = self.__board_size+100
 
        self.__snake = Snake([self.__board_size//2, self.__board_size//2], (self.__WIDTH, self.__HEIGHT))

        self.__screen = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.__game_over = False

    def __logic(self):
        if self.__food.is_colliding(self.__snake.get_position(), self.__snake.get_rect_size()):
            self.__snake.add_point()
            self.__food.spawn()

    def __input(self):
        for event in pygame.event.get():
            # the X button is pressed
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.__snake_vel = [-1, 0]
                elif event.key == pygame.K_RIGHT:
                    self.__snake_vel = [1, 0]
                elif event.key == pygame.K_UP:
                    self.__snake_vel = [0, -1]
                elif event.key == pygame.K_DOWN:
                    self.__snake_vel = [0, 1]

        self.__game_over = self.__snake.move(self.__snake_vel)

    def __render(self):
        self.__screen.fill(self.__BACKGROUND_COLOR)

        self.__food.draw(self.__screen)
        self.__snake.draw(self.__screen)

        self.__print_score()

        pygame.display.update()

    def __print_score(self):
        text = "Score: " + str(self.__snake.get_score())
        COLOR = (255, 255, 0) # yellow

        label = self.__score_font.render(text, 1, COLOR)
        self.__screen.blit(label, (5, self.__HEIGHT-40))

if __name__ == '__main__':
    g = Game(800)

    g.start(30)
