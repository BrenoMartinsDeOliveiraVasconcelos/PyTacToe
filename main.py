import tkinter as tk
from lib import lib


def main():
    root = tk.Tk()
    root.title("PyTacToe")

    r, c = 0, -1
    foto = tk.PhotoImage(file="./assets/empty.png")

    for i in range(0, 9):
        c += 1
        if c % 3 == 0:
            r += 1
            c = 0

        bt = tk.Button(image=foto,
                       command=lambda x=i: lib.imgbt(root, c, r),
                       width=100, height=100)
        bt.grid(row=r, column=c)

    root.mainloop()


if __name__ == '__main__':
    main()
