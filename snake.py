import math
import tkinter as tk
from tkinter import messagebox
import random
import pygame

class cube(object):
    rows = 0
    width = 0
    def __init__(self,start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass
    
    def reset(self, pos):
        pass

    def addCube(self):
        pass
    
    def draw(self, surface):
        pass

def drawGrid(width, rows, surface):
    sizeBtwn = width // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
    
        pygame.draw.line(surface, (255,255,255), (x, 0), (x,width))
        pygame.draw.line(surface, (255,255,255), (0, y), (width,y))
        

def redrawWindow(surface, rows, width):
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    pass

def messagebox(subject, content):
    pass

def main():
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(30)
        clock.tick(10)
        redrawWindow(win, rows, width)
    pass

main()
