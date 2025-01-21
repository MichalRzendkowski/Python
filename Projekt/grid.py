import tkinter as tk
from tkmacosx import Button
from game import GameOfLife
import time

PAD = 10

class Grid(tk.Label):

    def __init__(self, root, m, n, size, stopEvent):
        self.m = m
        self.n = n
        self.root = root
        self.stopEvent = stopEvent
        self.game = GameOfLife(m+PAD, n+PAD)
        self.game_speed = 2
        self.size = size
        super().__init__(root)
        self.buttons = [[Button(self, height=size//max(self.m, self.n), width=size//max(self.m, self.n), bg="white") for i in range(m)] for j in range(n)]
        for i in range(m):  
            for j in range(n):
                self.buttons[i][j].grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j].config(command=lambda i=i, j=j : self.changeButton(i, j))


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
            self.game.setCell(x+PAD//2, y+PAD//2, value)

    def nextState(self):
        self.game.nextState()
        matrix = self.game.getMatrix()

        for i in range(self.m):
            for j in range(self.n):
                self.setButtonColor(i, j, matrix[i+PAD//2][j+PAD//2])

    def clear(self):
        self.game = GameOfLife(self.m+PAD, self.n+PAD)
        for i in range(self.m):
            for j in range(self.n):
                self.setButtonColor(i, j, False)

    def speedUp(self):
        self.game_speed += 0.5

    def slowDown(self):
        if self.game_speed > 0.5:
            self.game_speed -= 0.5

    def loop(self):
        start = time.time()
        while not self.stopEvent.is_set():
            t = time.time()
            if t - start > 1/self.game_speed:
                self.nextState()
                start = t
            self.root.update()
        self.stopEvent.clear()