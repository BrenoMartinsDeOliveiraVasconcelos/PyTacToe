import tkinter as tk
from lib import mechanics
import json

table = json.load(open("./table.json"))


def main():
    root = tk.Tk()
    root.title("PyTacToe")

    r, c = 0, -1
    foto = tk.PhotoImage(file="./assets/empty.png")

    for i in range(0, 9):
        overlabel = tk.PhotoImage()
        c += 1
        if c % 3 == 0:
            r += 1
            c = 0

        bt = tk.Button(image=foto,
                       command=lambda w=overlabel, x=i, y=c, z=r:
                       mechanics.imgbt(root, y, z, w))
        bt.grid(row=r, column=c, sticky="nsew")

    root.mainloop()


if __name__ == '__main__':
    main()
