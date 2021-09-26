import tkinter as tk

imagem = tk.PhotoImage(file="./assets/circle.png")


def imgbt(root: tk.Tk, c: int, r: int):
    print("Clic")
    limg = tk.Label(root, image=imagem, width=100, height=100)
    limg.grid(row=r, column=c, sticky="nsew")
