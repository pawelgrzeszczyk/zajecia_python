#Napisz prosty sekundnik odliczajcy czas do zadabnego momentu.
#Odliczanie rozpoczuna sie po wcisnieciu przycisku start. Kiedy czas sie skonczyl
#odlicznaie zatrzymuje sie a program wysywietla komunikat o zakonczeniu odliczania
from Tkinter import *

import time

def tim():
    print display.get()
    s = display.get()

    for x in range(int(s)):

        s = int(s) - 1
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