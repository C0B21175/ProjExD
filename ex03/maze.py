from calendar import c
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key =="Up":
        my -= 1
    if key =="Down":
        my += 1
    if key =="Left":
        mx -= 1
    if key =="Right":
        mx += 1
    cx, cy = mx*100+50 , my*100+50
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    
    cx, cy = 300,400
    mx , my = 1,1
    root.title("迷えるこうかとん")
    canv = tk.Canvas(width=1500,height=900,bg="black")
    canv.pack()
    mm.show_maze(canv,mm.make_maze(15,9))
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    canv.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()