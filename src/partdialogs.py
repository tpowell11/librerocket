from os import name
from tkinter import *
from tkinter import ttk
import rocket
import eventhandlers
givenroot = None #stores the value for root gotten by the init()
rockettree = None 
def initdialogs(root):
    "initialzes a variable to point to the main window root for use in popups"
    givenroot = root #assign the passed root value to a global for later use
def inittree(tree):
    rockettree = tree
def tubedialog(event):
    "the dialog diplayed when a bodytube element is double clicked in tree or in diagram"
    dialog = Toplevel(givenroot)#make the dialog root
    menubar = Menu(dialog)
    file = Menu(menubar,tearoff=0)
    file.add_command(label='Save Preset')
    file.add_command(label='Export Preset')
    menubar.add_cascade(label='File',menu=file)
    dialog.config(menu=menubar)
    #component name entry
    nameLabel = ttk.Label(dialog, text='Part Name')
    nameEntry = ttk.Entry(dialog, bd=5)
    nameEntry.grid(row=0,column=1)
    nameLabel.grid(row=0,column=0)
    #parameter entry notebook
    paramTabs = ttk.Notebook(dialog)
    generalTab = ttk.Frame(paramTabs)
    overrideTab = ttk.Frame(paramTabs)
    commentTab = ttk.Frame(paramTabs)
    paramTabs.add(generalTab, text= "General")
    paramTabs.add(overrideTab, text= "Overrides")
    paramTabs.add(commentTab, text= "Comments")
    paramTabs.grid(row=1)
    print('called tube configuration dialog')
    sel = event.widget.focus()
    print("selected "+str(sel)+" from treeview")
def dialogselector(event):
    "selects which dialog template is appropriate for a given part type"
    #NOTE Cannot be fully implemented until rocket.py classes are finished
    sel = event.widget.focus()
    if sel.name == rocket.tube:
        print('selected tube')