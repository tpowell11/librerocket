from tkinter import *
import rocket
givenroot = None #stores the value for root gotten by the init()
def initdialogs(root):
    "initialzes a variable to point to the main window root for use in popups"
    givenroot = root #assign the passed root value to a global for later use
def tubedialog(event):
    "the dialog diplayed when a bodytube element is double clicked in tree or in diagram"
    dialog = Toplevel(givenroot)#make the dialog root
    button = Button(dialog,text='test')
    button.pack()
    print('called tube configuration dialog')
    sel = event.widget.focus()
    print("selected "+str(sel)+" from treeview")
def dialogselector(event):
    "selects which dialog template is appropriate for a given part type"
    #NOTE Cannot be fully implemented until rocket.py classes are finished
    sel = event.widget.focus()
    if sel.name == rocket.tube:
        print('selected tube')