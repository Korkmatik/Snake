import pygame
import random

class Food:

    def __init__(self, x_pos, y_pos, food_size, screen_size):
        self.__pos = [x_pos, y_pos]
        self.__size = food_size
        self.__color = (165, 42, 42)

    def get_position(self):
        return self.__pos

    def is_colliding(self, pos):
        if self.__pos[0] == pos[0] and self.__pos[1] == pos[1]:
            return True
        else
            return False

    def spawn(self):
        self.__pos[0] = random.randint(0, screen_size)
        self.__pos[1] = random.randint(0, screen_size)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.__color, (self.__pos[0], self.__pos[1], self.__size, self.__size))
