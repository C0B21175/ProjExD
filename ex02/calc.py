import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn =event.widget
    num =btn["text"]
    #tkm.showinfo(f"{num}",f"{num}のボタンが押されました")
    entry.insert(tk.END, num)

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0,tk.END)
    entry.insert(tk.END,res)

def click_kai(event):
    kai = int(entry.get())
    ans = 1
    for i in range(kai,0,-1):
        ans *= i
    entry.delete(0,tk.END)
    entry.insert(tk.END,ans)

def click_AC(event):
    entry.delete(0,tk.END)

root = tk.Tk()
root.geometry("500x650")

entry= tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)



r,c = 1,0
numbers = list(range(9,-1,-1))


for i , num in enumerate(numbers,1):
    btn = tk.Button(root, text=f"{num}",font=("Times New Roman", 30),width=4,height=2)
    btn.bind("<1>",click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

c2=3
r2=0
operators = ["+","-","*","/",".","**2","**0.5","**"]
for j , op in enumerate(operators,1):
    btn = tk.Button(root, text=f"{op}",font=("Times New Roman", 30),width=4,height=2)
    btn.bind("<1>",click_number)
    btn.grid(row=r2, column=c2)
    r2 += 1
    if j%4 == 0:
        c2+=1
        r2=0

btn = tk.Button(root, text=f"=",font=("Times New Roman", 30),width=4,height=2)
btn.bind("<1>",click_equal)
btn.grid(row=r,column=2)

btn = tk.Button(root, text=f"AC",font=("Times New Roman", 30),width=4,height=2)
btn.bind("<1>",click_AC)
btn.grid(row=r,column=1)

btn = tk.Button(root, text=f"x!",font=("Times New Roman", 30),width=4,height=2)
btn.bind("<1>",click_kai)
btn.grid(row=r,column=3)

root.mainloop()