import tkinter as tk
import json
from tkinter import messagebox
from lib import utils


def imgbt(root: tk.Tk, c: int, r: int, limg: tk.PhotoImage):
    print("Clic")

    table = json.load(open("./table.json"))

    img = tk.Label(root, image=limg, width=100, height=100)

    if table["next"] == "circle":
        limg.config(file=f"./assets/x.png")
        table["next"] = "x"
    elif table["next"] == "x":
        limg.config(file=f"./assets/circle.png")
        table["next"] = "circle"

    table["positions"][r - 1][c] = table["next"]

    keypositions = {
        "diagonal1": [table["positions"][0][0], table["positions"][1][1],
                      table["positions"][2][2]],
        "diagonal2": [table["positions"][0][2], table["positions"][1][1],
                      table["positions"][2][0]],
        "line": [table["positions"][0][:], table["positions"][1][:],
                 table["positions"][2][:]]
    }

    equality = False
    win = ""
    for k, v in keypositions.items():
        print(f"KEY: {k}")
        if k != "line":
            equality = utils.compare(v)
        else:
            for i in v:
                equality = utils.compare(i)
                if equality:
                    break
        if equality:
            win = table["next"]
            break

    if equality:
        numb = -1
        for row in table["positions"]:
            for column in range(len(row)):
                numb += 1
                row[column] = f"{numb}"
        messagebox.showinfo("Há um ganhador!", f"{win} ganhou!")

    open("./table.json", "w").write(json.dumps(table, indent=2))

    img.grid(row=r, column=c)