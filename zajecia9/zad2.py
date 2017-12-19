#przeprowadz debugowanie dowolnego programu wykonywanego na poprzednich zajeciach

from Tkinter import *
import time
import pdb

def tim():
    print display.get()
    s = display.get()
    pdb.set_trace()

    for x in range(int(s)):

        s = int(s) - 1
        pdb.set_trace()
        print s
        time.sleep(1)

    display.insert(0, "KONIEC")
    print "KONIEC"

master = Tk()
display = Entry(master)
display.pack()

button = Button(master, text="START",command=tim)
button.pack()

master.title("Odliczanie")
master.mainloop()