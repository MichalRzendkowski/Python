from grid import Grid
import tkinter as tk
from tkmacosx import Button
from threading import *
from PIL import Image, ImageTk

SIZE = 20

if __name__ == '__main__':

    images = [Image.open(f"images/btn_{i}.png").resize((30, 30)) for i in range(1, 7)]
    play_event = Event()

    root = tk.Tk()
    root.title("Game of Life")
    root.geometry("600x680")

    g = Grid(root, SIZE, SIZE, 500, play_event)
    g.grid(row=2, column=1, sticky="nsew")

    top = tk.Frame(root)
    top.grid(row=0, column=1, pady=10, sticky="nsew")

    def buttonPlay():
        btnPlay.configure(command=buttonStop)
        image = ImageTk.PhotoImage(images[1])
        btnPlay.image = image
        btnPlay.configure(image=image)
        g.loop()

    def buttonStop():
        play_event.set()
        btnPlay.configure(command=buttonStop)
        image = ImageTk.PhotoImage(images[2])
        btnPlay.image = image
        btnPlay.configure(image=image)
        btnPlay.configure(command=buttonPlay)

    btnPlay = Button(top, height=50, width=50, command=buttonPlay)
    btnPlay.grid(row=1, column=1, sticky="e")
    image = ImageTk.PhotoImage(images[2])
    btnPlay.image = image
    btnPlay.configure(image=image)

    btnNext = Button(top, height=50, width=50, command=g.nextState)
    btnNext.grid(row=1, column=0, sticky="e")
    image = ImageTk.PhotoImage(images[0])
    btnNext.image = image
    btnNext.configure(image=image)

    btnPlus = Button(top, height=50, width=50, command=g.speedUp)
    btnPlus.grid(row=1, column=2, sticky="e")
    image = ImageTk.PhotoImage(images[4])
    btnPlus.image = image
    btnPlus.configure(image=image)

    btnMinus = Button(top, height=50, width=50, command=g.slowDown)
    btnMinus.grid(row=1, column=3, sticky="e")
    image = ImageTk.PhotoImage(images[3])
    btnMinus.image = image
    btnMinus.configure(image=image)

    btnClear = Button(top, height=50, width=50, command=g.clear)
    btnClear.grid(row=1, column=4, sticky="e")
    image = ImageTk.PhotoImage(images[5])
    btnClear.image = image
    btnClear.configure(image=image)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(3, weight=1)

    root.mainloop()