import Tkinter as tk
import tkFont

def labelConfig (label, txt):
    label.config(text = txt, fg= "light green", bg = "dark green")


root  = tk.Tk()
w = tk.Label (root, text= 'Hello')
labelConfig(w, "123")
w.pack()






root = tk.Tk()
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=40)
root.option_add("*Font", default_font)
L1 = tk.Label(root, text="L1", bg="green")
L1.grid(row= 2, column=1, columnspan=1)
L2 = tk.Label(root, text="L2", bg="red")
L2.grid(row= 3, column=1)




from Tkinter import *
import tkMessageBox

def show_entry_fields():
    tkMessageBox.showinfo("Message ",e1.get())

master = Tk()
Label(master, text="write").grid(row=0)
e1 = Entry(master)
Button(master, text="quit",command = master.quit()).grid(row=4, column=0, pady=4)
Button(master, text="show",command =master.attributes()).grid(row=5, column=0)

master.mainloop()