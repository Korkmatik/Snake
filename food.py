import pygame
import random

class Food:

    def __init__(self, x_pos, y_pos, food_size, screen_size):
        self.__pos = [x_pos, y_pos]
        self.__size = food_size
        self.__color = (165, 42, 42)
        self.__screen_size = screen_size

    def get_position(self):
        return self.__pos

    def is_colliding(self, pos, size):
        f_x = self.__pos[0]
        f_y = self.__pos[1]

        o_x = pos[0]
        o_y = pos[1]

        if (f_x >= o_x and f_x < (o_x + size)) or (o_x >= f_x and o_x <= (f_x + self.__size)):
            if (f_y >= o_y and f_y < (o_y + size)) or (o_y >= f_y and o_y < (f_y + self.__size)):
                return True
        
        return False

    def spawn(self):
        self.__pos[0] = random.randint(0, self.__screen_size)
        self.__pos[1] = random.randint(0, self.__screen_size)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.__color, (self.__pos[0], self.__pos[1], self.__size, self.__size))
