from Tkinter import Button
import tkMessageBox

def ButtonCreator(Container,Text,Command,Number):
     for i in range (0, Number):
         Button(Container, text = Text[i], height = 1,
                   width=20, command = Command[i]).pack()
     return
	
def LabelCreator(Container,Text,Number):
    for i in range (0, Number) :
	      Label(Container, text = menuone_button1_title).grid(row=4,
                                                         sticky=W)
