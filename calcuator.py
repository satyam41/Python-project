from tkinter import *

def click(event):
    global scValue
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            value = eval(scValue.get())
        
        scValue.set(value)
        screen.update()

    elif text == "C":
        scValue.set('')
        screen.update()
    else:
        scValue.set(scValue.get() + text)
        screen.update()


root = Tk()
root.geometry("600x850")
root.title("Calculator")

scValue = StringVar()
scValue.set("")
screen = Entry(root, textvar=scValue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="white")
b = Button(f,text="7", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="8", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="9", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="white")
b = Button(f,text="4", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="5", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="6", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="white")
b = Button(f,text="1", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="2", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="3", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="white")
b = Button(f,text="+", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="0", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="-", padx=28, pady=22, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="white")
b = Button(f,text="*", padx=12, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="/", padx=12, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="=", padx=12, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="C", padx=12, pady=8, font="lucida 35 bold")
b.pack(side=LEFT, padx=10, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()