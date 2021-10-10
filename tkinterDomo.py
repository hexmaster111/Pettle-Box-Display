import tkinter as tk

def rotate(angle=0):
    canvas.itemconfig(txt, angle=angle)
    canvas.after(100, rotate, angle+5)

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)

txt = canvas.create_text(250, 250, text="\n".join('around and around'))
rotate()
canvas.pack()
root.mainloop()