from tkinter import *
givenroot: None #stores the value for root gotten by the init()
def initdialogs(root):
    "initialzes a variable to point to the main window root for use in popups"
    givenroot = root
def tubedialog(root):
    "the dialog diplayed when a bodytube element is double clicked in tree or in diagram"
    dialog = Toplevel(root)#make the dialog root
    button = Button(dialog,text='test')
    button.pack()
    print('test')

