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
    global cx, cy, mx, my,hp
    hp = 10
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
            hp -= 1
            my += 1
            
        if key =="Down":
            hp -= 1
            my -= 1
        if key =="Left":
            hp -= 1
            mx += 1
        if key =="Right":
            hp -= 1
            mx -= 1
    canv.coords("tori",cx,cy)
    if cx == 1350 and cy == 750:
        tkm.showinfo("GREAT","goalに着きました")
        canv.create_image(cx,cy,image=tori1,tag="tori1")
    elif hp == 0:
        tkm.showinfo("BAD!!","hpが0になりました")
    else:
        root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canv = tk.Canvas(width=1500,height=900,bg="black")
    canv.pack()
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv,maze_lst)
    canv.create_rectangle(200,200,100,100,fill="blue")
    canv.create_rectangle(1300,700,1400,800,fill="red")
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    tori1= tk.PhotoImage(file="ex03/fig/9.png")
    mx,my = 1,1
    cx, cy = mx*100+50,my*100+50
    canv.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()