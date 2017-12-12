#Przygotuj okno skladajace sie z jednego buttonu i trzech radioButtonow okreslajacych podstawowe kolory.
#Zmiana zaznaczenia radio zmienia kolor tekstu na przycisku. Wcisniecie przycisku powoduje
#wyswietlenie dowolnego komunikat


from Tkinter import *


def bg():
    if(v.get() == 1):
        button.config(fg="red")
    elif(v.get() == 2):
        button.config(fg="blue")
    else:
        button.config(fg="green")
def text():
    print "ok"

master = Tk()
button = Button(master, text="TEKST", command=text)
button.pack()
v = IntVar()
b1=Radiobutton(master, text="RED",variable=v, value=1, command=bg)
b1.pack(anchor=W)
b2=Radiobutton(master, text="BLUE",variable=v, value=2, command=bg)
b2.pack(anchor=W)
b3=Radiobutton(master, text="GREEN",variable=v, value=3, command=bg)
b3.pack(anchor=W)

master.mainloop()