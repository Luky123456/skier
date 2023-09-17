import tkinter as tk

win = tk.Tk()

w = 1000
h = 1000

canvas = tk.Canvas(width = w,height = h, bg = "black")
canvas.pack()


def skier(x,y,d,depth):
    if depth > 0:
        depth -= 1
        canvas.create_rectangle(x, y, x+d, y+d, fill="white")
        skier(x, y, d // 3, depth)
        skier(x + d // 3, y, d // 3, depth)
        skier(x + 2 * (d // 3), y, d // 3, depth)
        skier(x, y + d // 3, d // 3, depth)
        skier(x + 2 * (d // 3), y + d // 3, d // 3, depth)
        skier(x, y + 2 * (d // 3), d // 3, depth)
        skier(x + d // 3, y + 2 * (d // 3), d // 3, depth)
        skier(x + 2 * (d // 3), y + 2 * (d // 3), d // 3, depth)
       

skier(50, 50, 800, 6)

win.mainloop()
