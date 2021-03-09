# import tkinter module 
from os import truncate
from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
import diagramparts #functions to draw parts to the canvas
import rocket

#from partdialogs import tubedialog
import partdialogs
import json #for reading the GUI config json
with open("../cfg/theme.json") as f: #themeing file for the gui
    cfg = json.load(f)
# creating main tkinter window/toplevel 
root = Tk() #main window root
root.resizable(False,False)
root.title('LibreRocket V0')
#root.iconbitmap('../img/icon.ico') #TODO make icon
partdialogs.initdialogs(root)
root.configure(bg=cfg['backgroundColor']) #loads color options from cfg json
menu = Menu(root) #top-of-window menu
tabControl = ttk.Notebook(root) #tabbed layout for multiple tasks
designTab = ttk.Frame(tabControl) #the rocket design tab
motorTab = ttk.Frame(tabControl) #the motor selection and data entry tab
calcTab = ttk.Frame(tabControl) #simulation / calculation tab
#pushing tabs to container
tabControl.add(designTab, text = "Design")
tabControl.add(motorTab, text = "Motor Configuration")
tabControl.add(calcTab, text = "Calculations")
tabControl.grid(row=0)

#
# Design Tab
#

# Frame definitions for designTab
outlineframe = LabelFrame(designTab,text = 'Outline')
outlineframe.grid(row=1,column=0)
partsframe = LabelFrame(designTab, text = 'Parts')
partsframe.grid(row = 1, column = 1)
diagramframe = LabelFrame(designTab,text = 'Diagram')
diagramframe.grid(row=4)

# Handlers for UI events on Design tab
def on_click_part():
    "activates when one of the part creation buttons is clicked"
    print("clicked part")
# 
parts = ["1","2","3","4","|","5","6","7","8","|","9","10","11","12","|","13"]
#the following converts a list into an array of buttons based on the placement of | chars
row,col = 0,0
for part in parts:
    if part == "|":
        col +=1
        row = -1
    if part != "|":
        button = Button(partsframe, text = part, command=on_click_part)
        button.grid(row = row, column = col)
    row += 1

def on_double_click(event):
    sel = event.widget.focus()
    print("selected "+str(sel)+" from treeview")
    if sel == 'b':
        messagebox.showinfo("information",partsframe)  
def on_del_tree(event):
    print("deleteed "+str(event.widget.focus())+" from treeview")
    treeview.delete(event.widget.focus())#remove item from treeview
# Creating treeview window
treeview = ttk.Treeview(outlineframe)
treeviewcontrols = Frame(outlineframe)
treeviewcontrols.grid(row=0,column=1)
moveupbutton = Button(treeviewcontrols, text = "Move up") 
moveupbutton.grid(row=0)
movedownbutton = Button(treeviewcontrols,text = "Move down")
movedownbutton.grid(row=1)
deletebutton = Button(treeviewcontrols, text="Delete")
deletebutton.grid(row=2)
#treeview.bind("<<TreeviewSelect>>", root.on_tree_select)
treeview.bind("<Double-Button-1>", lambda x :partdialogs.tubedialog())
treeview.bind("d",on_del_tree)
treeview.grid(row = 0, column = 0) #grid the view to root
# Inserting items to the treeview 
# Inserting parent
def maketreeviewTEMP():
    tree=["Rocket",
        rocket.tube('alex',24.3,62.3,57.3,0.2),
        rocket.tube('jon',32,56,89,0.2),
        [rocket.tube('a',43,56,9,0.2),rocket.tube('b',34,25,8.,0.2),rocket.tube('c',23,10,7,0.2)],
        rocket.motor('m',40,24,56,40,{})]
    for item in tree: #this only supports level 1 nesting
        print(item)
        print(type(item))
        if type(item) == list:
            treeview.insert('','end',str(item[0]),text = str(item[0]))
            parent = item[0]
            del item[0]
            for subitem in item:
                treeview.insert(str(parent),'end',str(subitem),text=str(subitem))
        elif type(item) == str:
            treeview.insert('','end',item,text = item)
        elif type(item) != str:
            treeview.insert('','end',str(item.name),text=str(item.name))
        if type(item) == str and type(item) != list and item != "Rocket":
            treeview.move(item, "Rocket", 'end')
        elif item == "Rocket":
            pass
        else:
            treeview.move(item.name,"Rocket",'end')

canv = Canvas(diagramframe,bd=4)
canv.grid(row=4,columnspan=3)
coord = 10, 50, 240, 210
#arc = canv.create_arc(coord, start=0, extent=150, fill="red")
tube = diagramparts.drawTube(canv,100,100)

#
# Motor Tab
#
# Frame definitions for motorTab
mountsList = LabelFrame(motorTab, text = 'Motor Mounts')
mountsList.grid(row=0,column=0)
motorsList = LabelFrame(motorTab, text = "Motor Configurations")
# Elements for motortab
mntlist = ttk.Treeview(mountsList)
mntlist.grid(row=0,column=0)


mainloop() 
