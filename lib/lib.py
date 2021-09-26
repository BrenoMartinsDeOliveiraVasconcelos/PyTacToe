import tkinter as tk
import json


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

    open("./table.json", "w").write(json.dumps(table))

    img.grid(row=r, column=c, sticky="nsew")
