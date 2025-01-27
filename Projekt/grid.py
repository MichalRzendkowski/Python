import tkinter as tk
from tkmacosx import Button
from game import GameOfLife
from time import time
import random

MARGIN = 20

class Grid(tk.Frame):

    def __init__(self, root, m, n, size, stopEvent):
        self.m = m
        self.n = n
        self.root = root
        self.stopEvent = stopEvent
        self.game = GameOfLife(m+MARGIN, n+MARGIN)
        self.game_speed = 2
        self.size = size
        super().__init__(root)
        
        height = size//max(self.m, self.n)
        width = size//max(self.m, self.n)
        self.buttons = [[Button(self, height=height, width=width, bg="white")\
                         for i in range(m)] for j in range(n)]
        
        for i in range(m):  
            for j in range(n):
                self.buttons[i][j].grid(row=i, column=j, padx=2, pady=2)
                cmd = lambda i=i, j=j : self.changeButton(i, j)
                self.buttons[i][j].config(command=cmd)


    def changeButton(self, x, y):
        if self.buttons[x][y]['bg'] == 'black':
            self.setButtonColor(x, y, False)
            self.setButtonValue(x, y, False)
        else:
            self.setButtonColor(x, y, True)
            self.setButtonValue(x, y, True)

    def setButtonColor(self, x, y, value):
        if value:
            self.buttons[x][y].config(bg='black')
        else:
            self.buttons[x][y].config(bg='white')

    def setButtonValue(self, x, y, value):
            self.game.setCell(x+MARGIN//2, y+MARGIN//2, value)

    def nextState(self):
        self.game.nextState()
        matrix = self.game.getMatrix()

        for i in range(self.m):
            for j in range(self.n):
                self.setButtonColor(i, j, matrix[i+MARGIN//2][j+MARGIN//2])

    def clear(self):
        self.game = GameOfLife(self.m+MARGIN, self.n+MARGIN)
        for i in range(self.m):
            for j in range(self.n):
                self.setButtonColor(i, j, False)

    def speedUp(self):
        self.game_speed += 0.5

    def slowDown(self):
        if self.game_speed > 0.5:
            self.game_speed -= 0.5

    def loop(self):
        start = time()
        while not self.stopEvent.is_set():
            t = time()
            if t - start > 1/self.game_speed:
                self.nextState()
                start = t
            self.root.update()
        self.stopEvent.clear()

    def setRandom(self):
        self.clear()
        for i in range(self.m):
            for j in range(self.n):
                if bool(random.getrandbits(1)):
                    self.changeButton(i, j)
