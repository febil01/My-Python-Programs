#The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. (Note: Tk itself is not part of Python; it is maintained at ActiveState)

import tkinter
from tkinter import messagebox
from tkinter import END
from tkinter import INSERT
from tkinter import END

def button_click(text):
    tkinter.messagebox.showinfo("You clicked the button",f"you typed \"{text}\"")

tk=tkinter.Tk()

#LABEL
label=tkinter.Label(tk,text="Type Something here....")
label.pack()

tk.title("Basic window") #SETS THE TITLE OF THE WINDOW
tk.minsize(200,200) #SETS THE MINIMUM WINDOW SIZE BY SPECIFYING THE WIDTH AND HEIGHT
tk.maxsize(1200,700) #MAXIMUM WINDOWS SIZE

#ENTRY BOX
entry=tkinter.Entry(tk) #Creates an entry box
entry.insert(END,"type something here...")
entry.pack() #Adds it in the window and aligns it in the center

#BUTTON
button=tkinter.Button(tk,text="Click here", command=lambda: button_click(str(entry.get()))) #Creates a button and button_click method gets invoked when button is clicked
button.pack()


#TEXTBOX
text=tkinter.Text(tk)
text.insert(INSERT,"You can type stuff here. ")
text.insert(END,"Have fun")
text.pack()

#LISTBOX
listbox=tkinter.Listbox(tk)
listbox.insert(0,"This is a listbox","You can enter a lot of stuff in the list box")
listbox.insert(2,"hope you enjoy using listbox")
listbox.delete(1)
listbox.insert(END,'hello')
listbox.insert(END,'bye')

listbox.pack()

tk.mainloop() #RUNS OR OPENS THE WINDOW

