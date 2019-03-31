#!/usr/bin/env python3

import pygame

class Snake:
    
    def __init__(self, start_pos, board_dim):
        self.__score = 0
        self.__snake = []
        self.__snake.append(start_pos)
        self.__rect_size = 50
        self.__color = (0, 255, 0)
        self.__SPEED = 10
        self.__board_dim = board_dim
        self.__changed = False

    def move(self, amount):
        # getting position of the head
        x_pos_prev = self.__snake[0][0]
        y_pos_prev = self.__snake[0][1]
        
        # making it harder
        if self.__score != 0 and not self.__changed and self.__score % 5 == 0:
            self.__SPEED += 3 
            self.__changed = True
        elif self.__score % 5 != 0:
            self.__changed = False

        x_pos_cur = 0
        y_pos_cur = 0

        # moving the head
        self.__snake[0][0] += amount[0] * self.__SPEED
        self.__snake[0][1] += amount[1] * self.__SPEED
        
        if self.__is_colliding(x_pos_cur, y_pos_cur):
            return True

        # moving the tail
        for i in range(1, len(self.__snake)):
            x_pos_cur = self.__snake[i][0]
            y_pos_cur = self.__snake[i][1]
            

            # setting the current tail to the position of the tail which is ahead of them
            self.__snake[i][0] = x_pos_prev
            self.__snake[i][1] = y_pos_prev
            
            x_pos_prev, y_pos_prev = x_pos_cur, y_pos_cur

        return False

    def __is_colliding(self, x_pos, y_pos):
        if (x_pos <= self.__snake[0][0] and x_pos >= self.__snake[0][0]+self.__rect_size) or (self.__snake[0][0] <= x_pos and self.__snake[0][0] >= x_pos+self.__rect_size):
            if (y_pos <= self.__snake[0][1] and y_pos >= self.__snake[0][1]+self.__rect_size) or (self.__snake[0][1] <= y_pos and self.__snake[0][1] >= y_pos+self.__rect_size):
                print("is colliding")
                return True

        pos = self.get_position()
        
        if pos[0] < 0 or pos[0] > self.__board_dim[0] or pos[1] < 0 or pos[1] > self.__board_dim[1]:
            return True

        return False

    def draw(self, screen):
        for i in range(len(self.__snake)):
            pygame.draw.rect(screen, self.__color, (self.__snake[i][0], self.__snake[i][1], self.__rect_size, self.__rect_size))

    def get_position(self):
        return self.__snake[0]

    def get_score(self):
        return self.__score

    def get_length(self):
        return len(self.__snake)

    def add_point(self):
        back_tail = self.__snake[self.__score]
        x_pos = back_tail[0]
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
    s = Snake([5, 5])
    
    screen = pygame.display.set_mode((800, 400))

    while True:
        s.draw(screen)

        pygame.display.update()
