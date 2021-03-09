import tkinter as tk
givenroot: None #stores the value for root gotten by the init()
def initdialogs(root):
    "initialzes a variable to point to the main window root for use in popups"
    givenroot = root
def tubedialog():
    "the dialog diplayed when a bodytube element is double clicked in tree or in diagram"
    dialog = tk.Toplevel(givenroot)#make the dialog root
    button = tk.Button(dialog,text='test')
    button.pack()
    print('test')

