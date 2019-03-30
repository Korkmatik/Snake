#!/usr/bin/env python3

import pygame

class Snake:
    
    def __init__(self, symbol, start_pos):
        self.__score = 0
        self.__snake = []
        self.__snake.append(start_pos)
        self.__symbol = symbol
        self.__rect_size = 10
        self.__color = (0, 255, 0)

    def move(self, amount):
        # getting position of the head
        x_pos_prev = self.__snake[0][0]
        y_pos_prev = self.__snake[0][1]

        x_pos_cur = 0
        y_pos_cur = 0

        # moving the head
        self.__snake[0][0] += amount[0]
        self.__snake[0][1] += amount[1]
        
        # moving the tail
        for i in range(1, len(self.__snake)):
            x_pos_cur = self.__snake[i][0]
            y_pos_cur = self.__snake[i][1]

            # setting the current tail to the position of the tail which is ahead of them
            self.__snake[i][0] = x_pos_prev
            self.__snake[i][1] = x_pos_prev
            
            x_pos_prev, y_pos_prev = x_pos_cur, y_pos_cur

    def draw(self, screen):
        for i in range(len(self.__snake)):
            pygame.draw.rect(screen, self.__color, (self.__snake[i][0], self.__snake[i][1], self.__rect_size, self.__rect_size))

    def get_postion(self):
        return self.__snake[0]

    def get_score(self):
        return self.__score

    def get_length(self):
        return len(self.__snake)

    def add_point(self):
        back_tail = self.__snake[self.__score]
        x_pos = back_tail[0]+1
        y_pos = back_tail[1]

        self.__score += 1

        # add a new tail
        self.__snake.append([x_pos, y_pos])

    def get_rect_size(self):
        return self.__rect_size

    def get_color(self):
        return self.__color
               
if __name__ == '__main__':
    pygame.init()   
    s = Snake('O', [5, 5])
    
    screen = pygame.display.set_mode((800, 400))

    while True:
        s.draw(screen)

        pygame.display.update()
