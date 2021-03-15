from os import name
from tkinter import *
from tkinter import ttk
import tkinter
import rocket
import eventhandlers
givenroot = None #stores the value for root gotten by the init()
rockettree = None 
class labelledEntry(object):
    "quick way to make a labelled entry container, access frame with"
    def __init__(self, label:str, root):
        self.frame = ttk.Frame(root)
        self.label = ttk.Label(self.frame, text=label)
        self.entry = ttk.Entry(self.frame)
        self.label.grid(column=0,row=0,sticky='W')
        self.entry.grid(column=1,row=0,sticky='E')
class labelledUnitEntry(labelledEntry):
    "same as labelledEntry, but with a unit after the entry box"
    def __init__(self, label:str, root, unit:str):
        self.frame = ttk.Frame(root)
        self.label = ttk.Label(self.frame, text=label)
        self.ulabel = ttk.Label(self.frame, text=unit)
        self.entry = ttk.Entry(self.frame)
        self.label.grid(column=0,row=0,sticky='W')
        self.ulabel.grid(column=2,row=0,sticky='W')
        self.entry.grid(column=1,row=0,sticky='E')
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
    topEntryFrame = ttk.Frame(dialog)
    nameLabel = ttk.Label(topEntryFrame, text='Part Name')
    nameEntry = ttk.Entry(topEntryFrame)
    nameEntry.grid(row=0,column=1)
    nameLabel.grid(row=0,column=0)
    topEntryFrame.grid(column=0,row=0)
    #parameter entry notebook
    paramTabs = ttk.Notebook(dialog)

    # general data entry tab
    generalTab = ttk.Frame(paramTabs)
    entryFrame = ttk.Labelframe(generalTab,text="Parameters")
    leng_entry = labelledUnitEntry('Length',entryFrame,"m")
    leng_entry.frame.grid(column=0,row=0,pady=(0,10),sticky='W')
    diam_entry = labelledEntry('Diameter',entryFrame)
    diam_entry.frame.grid(column=0,row=1,pady=(0,10),sticky='W')
    wall_entry = labelledEntry('Wall Thickness', entryFrame)
    wall_entry.frame.grid(column=0,row=2,pady=(0,10),sticky='W')
    entryFrame.grid(row=0,column=0)
    
    #override tab layout
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