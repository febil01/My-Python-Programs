import tkinter
from tkinter import END

def add_to_cart():
    if str(items.get()) == "":
        return
    listbox.insert(END,items.get())
    items.delete(0,END)

def remove_from_cart():
    listbox.delete(listbox.curselection())

tk=tkinter.Tk()
tk.minsize(210,260)
tk.maxsize(210,260)
tk.title("My Cart")
tk.config(bg="#a6addb")

listbox=tkinter.Listbox(tk,bg="#d3d3d3",fg="black")
listbox.pack()

items=tkinter.Entry(tk,bg="#d3d3d3",fg="black")
items.pack()

add_cart=tkinter.Button(tk,text="ADD TO CART",bg="#383c49",fg="white",command=add_to_cart)
add_cart.pack()

remove_cart=tkinter.Button(tk,text="REMOVE SELECTION FROM CART",bg="#383c49",fg="white",command=remove_from_cart)
remove_cart.pack()

tk.mainloop()