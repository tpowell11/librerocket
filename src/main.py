# import tkinter module 
from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
import diagramparts #functions to draw parts to the canvas
import rocket
import json #for reading the GUI config json
with open("../cfg/theme.json") as f: #themeing file for the gui
    cfg = json.load(f)
# creating main tkinter window/toplevel 
root = Tk() 
root.configure(bg=cfg['backgroundColor'])
#ttk.Style().configure("TButton", padding=6, relief="flat",bg=cfg["partbuttonColor"])
# this will create a label widget 
outlineframe = LabelFrame(root,text = 'Outline')
outlineframe.grid(row=0,column=0)
partsframe = LabelFrame(root, text = 'Parts')
partsframe.grid(row = 0, column = 1)
diagramframe = LabelFrame(root,text = 'Diagram')
diagramframe.grid(row=4)

def on_click_part():
    print("clicked part")

parts = ["1","2","3","4","|","5","6","7","8","|","9","10","11","12"]
#parts = ["1","2","3","4","|","5","6","7","8"]
row = 0
col=0
for part in parts:
    if part == "|":
        col +=1
        row = -1
    if part != "|":
        button = Button(partsframe, text = part, command=on_click_part)
        button.grid(row = row, column = col)
    #row += 1 if col ==0 else -1
    #row += 1 if col == 0 else 1
    # if col != 0:
    #     row =0
    row += 1
# checkbutton widget 
c1 = Checkbutton(root, text = "Preserve") 
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2) 

# adding image (remember image should be PNG and not JPG) 
#img = PhotoImage(file = r"../img/wierstrass.png") 
#img1 = img.subsample(4, 4) 

def on_double_click(event):
    print("selected "+str(event.widget.focus())+" from treeview")
# Creating treeview window

treeview = ttk.Treeview(outlineframe)  
#treeview.bind("<<TreeviewSelect>>", root.on_tree_select)
treeview.bind("<Double-Button-1>", on_double_click)  
treeview.grid(row = 0, column = 0) #grid the view to root
# Inserting items to the treeview 
# Inserting parent

tree=["Rocket","b","c",["d","dd","ddd"],"e"]
for item in tree: #this only supports level 1 nesting
    if type(item) == list:
        treeview.insert('','end',str(item[0]),text = str(item[0]))
        parent = item[0]
        del item[0]
        for subitem in item:
            treeview.insert(str(parent),'end',str(subitem),text=str(subitem))
    else:
        treeview.insert('','end',str(item),text = str(item))
# # Placing each child items in parent widget
treeview.move('b', 'Rocket', 'end')  
treeview.move('c', 'Rocket', 'end')
treeview.move('d', 'Rocket', 'end')
# def on_tree_select(event):
#         print("selected items:")
#         for item in treeview.selection():
#             item_text = treeview.item(item,"text")
#             print(item_text)



canv = Canvas(diagramframe,bd=4)
canv.grid(row=4,columnspan=3)
coord = 10, 50, 240, 210
#arc = canv.create_arc(coord, start=0, extent=150, fill="red")
tube = diagramparts.drawTube(canv,100,100)
mainloop() 
