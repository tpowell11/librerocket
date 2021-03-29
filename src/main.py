# import tkinter module  

from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
import tkinter as tk
import diagramparts #functions to draw parts to the canvas
import rocket
import eventhandlers as eh #all gui event functions
import partdialogs
import json #for reading the GUI config json
import new
class app(tk.Tk):
    "main class"
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        #rest of gui code below
        ttk.Label(parent,text='test').pack()
        
        
class labelledEntry(tk.Tk):
    def __init__(self,root,label:str):
        self.container = ttk.Frame(root)
        self.label = ttk.Label(self.container,text=label)
        self.entry = ttk.Entry(self.container)
        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
with open("../cfg/theme.json") as f: #themeing file for the gui
    cfg = json.load(f)
rock = rocket.Rocket('test/test.json',
                     [
                        rocket.fileParent('Rocket'),
                        rocket.tube('alex',24.3,62.3,57.3,0.2),
                        rocket.tube('jon',32,56,89,0.2),
                        rocket.tube('a',43,56,9,0.2),
                            rocket.tube('b',34,25,8.,0.2,'a'),
                            rocket.tube('c',23,10,7,0.2,'a'), #the part in {} is a set, the rest is tuple
                        rocket.motor('m',40,24,56,40,{}),
                        rocket.nosecone('nose',0,24,16,True,10)
                     ]
                     )
rock.SaveJson('test.json')
#rock = rocket.loadJsontoObject('test.json')
#print(rock.parts)
# creating main tkinter window/toplevel 
root = tk.Tk() #main window root
root.title('LibreRocket V0')
#root.iconbitmap('../img/icon.ico') #TODO make icon
eh.initsavefile(rock)
partdialogs.initdialogs(root)
partdialogs.inittree(rock.parts)
root.configure(bg=cfg['backgroundColor']) #loads color options from cfg json
menubar = tk.Menu(root) #top-of-window menubar
file = tk.Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open",command=eh.getFilename)  
file.add_command(label="Save")  
#file.add_command(label="Save as...",command=lambda rocket: eh.saveAs(rocket))
#file.add_command(label="Save as...",command=eh.saveAs(rock))  
file.add_command(label="Save as...")
file.add_command(label="Close",command=eh.exitApp)
menubar.add_cascade(label='File',menu=file) 
tools = tk.Menu(menubar,tearoff=0)
tools.add_command(label='Settings') #launch settings dialog
tools.add_command(label='User Presets') #launch user presets management dialog
menubar.add_cascade(label='Tools',menu=tools)
root.config(menu=menubar) 
tabControl = ttk.Notebook(root) #tabbed layout for multiple tasks
#pushing tabs to container
tabControl.add(new.DesignTab(tabControl), text = "Design")
tabControl.add(new.MotorTab(tabControl), text = "Motor Configuration")
tabControl.add(new.CalcTab(tabControl), text = "Calculations")
tabControl.grid(row=0)

#
# Design Tab
#

# Frame definitions for designTab
# outlineframe = ttk.LabelFrame(designTab,text = 'Outline')
# outlineframe.grid(row=1,column=0)
# partsframe = ttk.LabelFrame(designTab, text = 'Parts')
# partsframe.grid(row = 1, column = 1)
# diagramframe = ttk.LabelFrame(designTab,text = 'Diagram')
# diagramframe.grid(row=4)

# Handlers for UI events on Design tab

# # 
# parts = ["1","2","3","4","|","5","6","7","8","|","9","10","11","12","|","13"]
# #the following converts a list into an array of buttons based on the placement of | chars
# row,col = 0,0
# for part in parts:
#     if part == "|":
#         col +=1
#         row = -1
#     if part != "|":
#         button = Button(partsframe, text = part, command=eh.on_click_part)
#         button.grid(row = row, column = col)
#     row += 1

# def on_double_click(event):
#     sel = event.widget.focus()
#     print("selected "+str(sel)+" from treeview")
#     if sel == 'b':
#         messagebox.showinfo("information",partsframe)  

# # Creating treeview window
# treeview = ttk.Treeview(outlineframe)
# treeviewcontrols = Frame(outlineframe)
# treeviewcontrols.grid(row=0,column=1)
# moveupbutton = ttk.Button(treeviewcontrols, text = "Move up") 
# moveupbutton.grid(row=0)
# movedownbutton = ttk.Button(treeviewcontrols,text = "Move down")
# movedownbutton.grid(row=1)
# deletebutton = ttk.Button(treeviewcontrols, text="Delete") #TODO make this button remove items from the view
# deletebutton.grid(row=2)

# treeview.bind("<Double-Button-1>", partdialogs.tubedialog)
# treeview.bind("d",eh.on_del_tree)
# treeview.grid(row = 0, column = 0) #grid the view to root
# # Inserting items to the treeview 
# # Inserting parent
# def maketreeviewTEMP():
#     for item in rock.parts:
#         if type(item) == rocket.fileParent:
#             print('found main')
#             treeview.insert('','end',item.name,text = item.name)
#         elif item.parent != '':
#             print('found unparented object')
#             treeview.insert(item.parent,'end',item.name,text = item.name)
#         else:
#             print('found parented object')
#             treeview.insert(rock.parts[0].name,'end',item.name,text = item.name)
# maketreeviewTEMP()

# canv = tk.Canvas(diagramframe,bd=4)
# canv.grid(row=4,columnspan=3)
# coord = 10, 50, 240, 210
# #arc = canv.create_arc(coord, start=0, extent=150, fill="red")
# tube = diagramparts.drawTube(canv,100,100)

# #
# # Motor Tab
# #
# # Frame definitions for motorTab
# mountsList = LabelFrame(motorTab, text = 'Motor Mounts')
# mountsList.grid(row=0,column=0)
# motorsList = LabelFrame(motorTab, text = "Motor Configurations")
# # Elements for motortab
# mntlist = ttk.Treeview(mountsList)
# mntlist.grid(row=0,column=0)


tk.mainloop() 
