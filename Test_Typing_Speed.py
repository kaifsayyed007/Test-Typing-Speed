import tkinter as tk
import random,time

with open("sentence.txt") as f:
    lines=f.read().splitlines()

s=""
start=0
run=False

def new():
    global s,run
    run=False
    s=random.choice(lines)
    sen.config(text=s)
    box.delete("1.0",tk.END)
    res.config(text="")
    t.config(text="Time: 0")
    w.config(text="WPM: 0")
    a.config(text="Accuracy: 0%")

def timer():
    if run:
        t.config(text=f"Time: {time.time()-start:.1f}s")
        root.after(100,timer)

def typing(e):
    global start,run
    if not run:
        run=True
        start=time.time()
        timer()

def submit(e=None):
    global run
    if not run:return "break"
    run=False

    typed=box.get("1.0",tk.END).strip()
    tt=time.time()-start
    wpm=(len(s.split())/tt)*60

    c=0
    for i in range(min(len(s),len(typed))):
        if s[i]==typed[i]:
            c+=1

    acc=c/len(s)*100

    t.config(text=f"Time: {tt:.2f}s")
    w.config(text=f"WPM: {int(wpm)}")
    a.config(text=f"Accuracy: {acc:.1f}%")

    if typed==s:
        res.config(text="Perfect! 🎉",fg="green")
    else:
        res.config(text="Mistakes Found!",fg="red")
    return "break"

root=tk.Tk()
root.title("Typing Speed Test")
root.geometry("700x430")
root.config(bg="#222831")

tk.Label(root,text="Typing Speed Test",
font=("Arial",18,"bold"),
bg="#222831",fg="cyan").pack(pady=10)

sen=tk.Label(root,bg="#393E46",fg="white",
font=("Arial",11),wraplength=620,padx=10,pady=10)
sen.pack(pady=10)

box=tk.Text(root,height=5,width=70,font=("Arial",11))
box.pack()
box.bind("<Key>",typing)
box.bind("<Return>",submit)

tk.Label(root,text="Press ENTER to Submit",
bg="#222831",fg="yellow").pack()

f=tk.Frame(root,bg="#222831")
f.pack(pady=8)

tk.Button(f,text="Submit",bg="dodgerblue",fg="white",
command=submit,width=10).grid(row=0,column=0,padx=10)

tk.Button(f,text="Restart",bg="orange",fg="white",
command=new,width=10).grid(row=0,column=1,padx=10)

t=tk.Label(root,text="Time: 0",bg="#222831",fg="white")
t.pack()

w=tk.Label(root,text="WPM: 0",bg="#222831",fg="white")
w.pack()

a=tk.Label(root,text="Accuracy: 0%",bg="#222831",fg="white")
a.pack()

res=tk.Label(root,text="",bg="#222831",
font=("Arial",13,"bold"))
res.pack(pady=10)

new()
root.mainloop()