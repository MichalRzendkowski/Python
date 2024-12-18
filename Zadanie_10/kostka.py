import tkinter as tk
from PIL import Image, ImageTk
import random

images = [Image.open(f"grafika/kostka_{i}.png").resize((270, 270)) for i in range(7)]

root = tk.Tk()
root.title("Kostka")
root.geometry("300x500")
root.eval('tk::PlaceWindow . center')
root.resizable(width=False, height=False)

image = ImageTk.PhotoImage(images[0])
label = tk.Label(root, image=image)
label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def throw():
    image = ImageTk.PhotoImage(images[random.randint(1, 6)])
    label.image = image
    label.configure(image=image)

button = tk.Button(root, text="RZUĆ", command=throw)
button.configure(width=7, height=3, font=("Ubuntu Medium", 50, "bold"))
button.place(relx=0.5, rely=0.22, anchor=tk.CENTER)
root.mainloop()
