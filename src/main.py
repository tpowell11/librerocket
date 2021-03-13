# import tkinter module  
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
import diagramparts #functions to draw parts to the canvas
import rocket
import eventhandlers as eh #all gui event functions
import partdialogs
import json #for reading the GUI config json
with open("../cfg/theme.json") as f: #themeing file for the gui
    cfg = json.load(f)

rock = rocket.Rocket('test/test.json',
                     [
                        rocket.fileParent('Rocket'),
                        rocket.tube('alex',24.3,62.3,57.3,0.2),
                        rocket.tube('jon',32,56,89,0.2),
                        [rocket.tube('a',43,56,9,0.2),
                            rocket.tube('b',34,25,8.,0.2),
                            rocket.tube('c',23,10,7,0.2)], #the part in {} is a set, the rest is tuple
                        rocket.motor('m',40,24,56,40,{})
                     ]
                     )
rock.SaveJson('test.json')

# creating main tkinter window/toplevel 
root = Tk() #main window root
root.title('LibreRocket V0')
#root.iconbitmap('../img/icon.ico') #TODO make icon
partdialogs.initdialogs(root)

partdialogs.inittree(rock.parts)
root.configure(bg=cfg['backgroundColor']) #loads color options from cfg json
menubar = Menu(root) #top-of-window menubar
file = Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open",command=eh.getFilename)  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close",command=eh.exitApp)
menubar.add_cascade(label='File',menu=file) 
root.config(menu=menubar) 
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
outlineframe = ttk.LabelFrame(designTab,text = 'Outline')
outlineframe.grid(row=1,column=0)
partsframe = ttk.LabelFrame(designTab, text = 'Parts')
partsframe.grid(row = 1, column = 1)
diagramframe = ttk.LabelFrame(designTab,text = 'Diagram')
diagramframe.grid(row=4)

# Handlers for UI events on Design tab

# 
parts = ["1","2","3","4","|","5","6","7","8","|","9","10","11","12","|","13"]
#the following converts a list into an array of buttons based on the placement of | chars
row,col = 0,0
for part in parts:
    if part == "|":
        col +=1
        row = -1
    if part != "|":
        button = Button(partsframe, text = part, command=eh.on_click_part)
        button.grid(row = row, column = col)
    row += 1

def on_double_click(event):
    sel = event.widget.focus()
    print("selected "+str(sel)+" from treeview")
    if sel == 'b':
        messagebox.showinfo("information",partsframe)  

# Creating treeview window
treeview = ttk.Treeview(outlineframe)
treeviewcontrols = Frame(outlineframe)
treeviewcontrols.grid(row=0,column=1)
moveupbutton = ttk.Button(treeviewcontrols, text = "Move up") 
moveupbutton.grid(row=0)
movedownbutton = ttk.Button(treeviewcontrols,text = "Move down")
movedownbutton.grid(row=1)
deletebutton = ttk.Button(treeviewcontrols, text="Delete") #TODO make this button remove items from the view
deletebutton.grid(row=2)

treeview.bind("<Double-Button-1>", partdialogs.tubedialog)
treeview.bind("d",eh.on_del_tree)
treeview.grid(row = 0, column = 0) #grid the view to root
# Inserting items to the treeview 
# Inserting parent
def maketreeviewTEMP():
    
    for item in rock.parts:
        if type(item) == rocket.fileParent:
            treeview.insert('','end',item,text= item.name) #makes the root element of the rocket
        elif type(item) != list and type(item) != rocket.fileParent:
            #print(item)
            treeview.insert(rock.parts[0],'end',item,text = item.name)
        elif type(item) == list:
            par = item[0]
            treeview.insert('','end',par,text = par.name)
            del item[0]
            for si in item:
                #print(si)
                treeview.insert(par,'end',si,text = si.name)
            treeview.move(par,rock.parts[0],'end')
maketreeviewTEMP()

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
