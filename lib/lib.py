import tkinter as tk


def imgbt(root: tk.Tk, c: int, r: int, limg: tk.PhotoImage):
    print("Clic")
    limg = tk.Label(root, image=limg, width=100, height=100)
    limg.grid(row=r, column=c, sticky="nsew")
