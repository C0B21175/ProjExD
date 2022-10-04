import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):
    btn =event.widget
    num =int(btn["text"])
    #tkm.showinfo(f"{num}",f"{num}のボタンが押されました")
    entry.insert(tk.END, num)


root = tk.Tk()
root.geometry("300x500")

entry= tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)



r=1
c=0
for i , num in enumerate(range(9,-1,-1),1):
    btn = tk.Button(root, text=f"{num}",font=("Times New Roman", 30),width=4,height=2)
    btn.bind("<1>",click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0






root.mainloop()