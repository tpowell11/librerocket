# import tkinter module 
from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk

# creating main tkinter window/toplevel 
root = Tk() 

# this will create a label widget 
l1 = Label(root, text = "Height") 
l2 = Label(root, text = "Width") 
label_frame = LabelFrame(root, text = 'Parts')
label_frame.grid(row = 0, column = 1)
parts = ["1","2","3","4"]
for part in parts:
    button = Button(label_frame, text = part)
    button.pack()
# checkbutton widget 
c1 = Checkbutton(root, text = "Preserve") 
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2) 

# adding image (remember image should be PNG and not JPG) 
#img = PhotoImage(file = r"../img/wierstrass.png") 
#img1 = img.subsample(4, 4) 

# Creating treeview window
treeview = ttk.Treeview(root)  
 
treeview.grid(row = 0, column = 0) #grid the view to root
 
# Inserting items to the treeview 
# Inserting parent
treeview.insert('', '0', 'item1', 
                text ='GeeksforGeeks') 
 
# Inserting child
treeview.insert('', '1', 'item2', 
                text ='Computer Science')
treeview.insert('', '2', 'item3', 
                text ='GATE papers')
treeview.insert('', 'end', 'item4',
                text ='Programming Languages')
 
# Inserting more than one attribute of an item
treeview.insert('item2', 'end', 'Algorithm', 
                text ='Algorithm')  
treeview.insert('item2', 'end', 'Data structure', 
                text ='Data structure') 
treeview.insert('item3', 'end', '2018 paper', 
                text ='2018 paper')  
treeview.insert('item3', 'end', '2019 paper', 
                text ='2019 paper')
treeview.insert('item4', 'end', 'Python', 
                text ='Python')
treeview.insert('item4', 'end', 'Java', 
                text ='Java')
 
# Placing each child items in parent widget
treeview.move('item2', 'item1', 'end')  
treeview.move('item3', 'item1', 'end')
treeview.move('item4', 'item1', 'end')



# setting image with the help of label 
# Label(root, image = img1).grid(row = 0, column = 2, 
# 	columnspan = 2, rowspan = 2, padx = 5, pady = 5) 

# button widget 
b1 = Button(root, text = "Zoom in") 
b2 = Button(root, text = "Zoom out") 
# arranging button widgets 
b1.grid(row = 2, column = 2, sticky = E) 
b2.grid(row = 2, column = 3, sticky = E) 
canv = Canvas(root,bd=4)
canv.grid(row = 4)
mainloop() 
