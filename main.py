import tkinter as tk
from lib import lib
import json

table = json.load(open("./table.json"))


def main():
    root = tk.Tk()
    root.title("PyTacToe")

    r, c = 0, -1
    foto = tk.PhotoImage(file="./assets/empty.png")

    overlabel = tk.PhotoImage(file=f"./assets/{table['next']}.png")

    for i in range(0, 9):
        c += 1
        if c % 3 == 0:
            r += 1
            c = 0

        bt = tk.Button(image=foto,
                       command=lambda x=i, y=c, z=r: lib.imgbt(root, y, z, overlabel),
                       width=100, height=100)
        bt.grid(row=r, column=c)

    root.mainloop()


if __name__ == '__main__':
    main()
