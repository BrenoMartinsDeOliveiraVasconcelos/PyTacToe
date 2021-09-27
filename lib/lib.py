import tkinter as tk
import json
from tkinter import messagebox


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

    for k, v in keypositions.items():
        if k != "line":
            print(f"KEY: {k}")
            index = 0
            i = ""
            for i in v:
                if index < len(v) - 1:
                    if i == v[index+1]:
                        equality = True
                    else:
                        equality = False
                    print(equality)
            if equality:
                messagebox.showinfo("ok", i)

    open("./table.json", "w").write(json.dumps(table, indent=2))

    img.grid(row=r, column=c, sticky="nsew")
