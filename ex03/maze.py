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
    global cx, cy 
    if key =="Up":
        cy += 20
    if key =="Down":
        cy -= 20
    if key =="Left":
        cx -= 20
    if key =="Right":
        cx += 20
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    cx, cy = 300,400
    root.title("迷えるこうかとん")
    canv = tk.Canvas(width=1500,height=900,bg="black")
    canv.pack()
    tori = tk.PhotoImage(file="ex03/fig/5.png")
    canv.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    mm.show_maze(canv,mm.make_maze(15,9))
    main_proc()
    root.mainloop()