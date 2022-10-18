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
    if maze_lst[my][mx] == 0:
        cx, cy = mx*100+50 , my*100+50
    else:
        if key =="Up":
            my += 1
        if key =="Down":
            my -= 1
        if key =="Left":
            mx += 1
        if key =="Right":
            mx -= 1 
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(width=1500,height=900,bg="black")
    canv.pack()
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv,maze_lst)
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    mx,my = 1,1
    cx, cy = mx*100+50,my*100+50
    canv.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()