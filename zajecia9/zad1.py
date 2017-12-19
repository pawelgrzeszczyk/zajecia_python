#dodaj logowanie do pliku do kalkulatora wykonanego na poprzednich zajeciach.
#wykorzystaj rozne poziomy logowania

# -*-coding: utf-8-*-
from Tkinter import *
import logging


logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.info("start")


class calc:
    def getandreplace(self):
        self.expression = self.e.get()
        self.newtext = self.expression.replace(self.newdiv, '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):
        self.getandreplace()
        logging.info('=')
        try:
            self.value = eval(self.newtext)
        except SyntaxError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
            logging.warning("invalid input")
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def clearall(self):
        self.e.delete(0, END)
        logging.debug("clear")

    def action(self, argi):
        self.e.insert(END, argi)
        logging.info(argi)

    def __init__(self, master):
        master.title('Calulator')
        master.geometry()
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()

        self.div = 'x'
        self.newdiv = self.div.decode('utf-8')

        Button(master, text="=", width=3, command=lambda: self.equals()).grid(row=4, column=2,)
        Button(master, text='AC', width=3, command=lambda: self.clearall()).grid(row=4, column=0)
        Button(master, text="+", width=3, command=lambda: self.action('+')).grid(row=4, column=3)
        Button(master, text="x", width=3, command=lambda: self.action('x')).grid(row=2, column=3)
        Button(master, text="-", width=3, command=lambda: self.action('-')).grid(row=3, column=3)
        Button(master, text="/", width=3, command=lambda: self.action('/')).grid(row=1, column=3)
        Button(master, text="7", width=3, command=lambda: self.action(7)).grid(row=1, column=0)
        Button(master, text="8", width=3, command=lambda: self.action(8)).grid(row=1, column=1)
        Button(master, text="9", width=3, command=lambda: self.action(9)).grid(row=1, column=2)
        Button(master, text="4", width=3, command=lambda: self.action(4)).grid(row=2, column=0)
        Button(master, text="5", width=3, command=lambda: self.action(5)).grid(row=2, column=1)
        Button(master, text="6", width=3, command=lambda: self.action(6)).grid(row=2, column=2)
        Button(master, text="1", width=3, command=lambda: self.action(1)).grid(row=3, column=0)
        Button(master, text="2", width=3, command=lambda: self.action(2)).grid(row=3, column=1)
        Button(master, text="3", width=3, command=lambda: self.action(3)).grid(row=3, column=2)
        Button(master, text="0", width=3, command=lambda: self.action(0)).grid(row=4, column=1)




root = Tk()
obj = calc(root)
root.mainloop()
logging.info("koniec")