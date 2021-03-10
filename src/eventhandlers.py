from tkinter import *
from tkinter import ttk
from tkinter import filedialog
def exitApp():
    "exits the application"
    print("Exiting...")
    exit()
def on_click_part():
    "activates when one of the part creation buttons is clicked"
    print("clicked part")
def on_del_tree(event=None, view = ttk.Treeview):
    #TODO this is utterly broken
    print("deleteed "+str(event.widget.focus())+" from treeview")
    view.delete(event.widget.focus())#remove item from treeview
def getFilename():
    "get the name of a file from the user"
    filedialog.askopenfilename()
def dialogSavePresetToDb():
    "Saves the current state of the conf dialog to the internal db"
def dialogExportPreset():
    "Exports the state of the conf dialog to external spec. file"