# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        
        self.alertButton = Button(self, text='Hello', command = self.hello)
        self.alertButton.pack()

        self.helloLabel = Label(self,text='Hello, world!')
        self.helloLabel.pack()
        
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Msg', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()