import tkinter as tk
import tkinter.ttk as ttk
import eventhandlers as eh
import rocket
tl = [
        ['Nosecone','../img/wierstrass.png'],
        ['Bodytube','../img/wierstrass.png'],
        ['Elliptical Finset','../img/wierstrass.png'],
        ['Trapesoidal Finset','../img/wierstrass.png'],
        ['Freeform Finset','../img/wierstrass.png'],
        ['Tube Coupler','../img/wierstrass.png']
    ]
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
class labelledEntry(tk.Tk):
    def __init__(self,main,label:str):
        self.container = ttk.Frame(main)
        self.label = ttk.Label(self.container,text=label)
        self.entry = ttk.Entry(self.container)
        self.label.grid(row=1, column=0)
        self.entry.grid(row=1, column=1)
        
        
class buttonGrid(ttk.Frame):
    """
    Takes a list of:\n
    [
        ['item','path/to/image']
    ]\n
    and returns grid of tkinter buttons
    """
    def __init__(self, main,rows:int,parts:'list[list[str]]', *args, **kwargs):
        ttk.Frame.__init__(self,*args,**kwargs)
        row,col = 0,0
        for pair in parts:
            img = tk.PhotoImage(file=pair[1])
            ttk.Button(self,text=pair[0],image=img,compound=tk.LEFT,command=eh.on_click_part).grid(row=row,column=col)
            row+=1
            if row == rows:
                row=0
                col+=1
        
        
class DesignTab(ttk.Frame):
    "class for the main / design area of the application"
    def __init__(self, main, *args, **kwargs):
        ttk.Frame.__init__(self,*args,**kwargs)
        self.testlabel=ttk.Label(self,text='test').grid(row=0,column=0)
        t=ttk.LabelFrame(self,text='test').grid(row=0,column=0)
        # self.outlineframe = ttk.LabelFrame(self,text = 'Outline').grid(row=1,column=0)
        # self.partsframe = ttk.LabelFrame(self, text = 'Parts').grid(row = 0, column = 1)
        # self.diagramframe = ttk.LabelFrame(self,text = 'Diagram').grid(row=4,columnspan=2,sticky='nsew')
        self.bg = buttonGrid(self, 4,tl).grid(row=1, column=1)
        self.treeview = ttk.Treeview(self).grid(row=1,column=0)
        
        self.canvas = tk.Canvas(self).grid(row=4)
        self.grid(row=0,column=0)
        

class MotorTab(ttk.Frame):
    def __init__(self,main,*args,**kwargs):
        ttk.Frame.__init__(self,*args,**kwargs)
        # self.mountsList = ttk.LabelFrame(self, text = 'Motor Mounts').grid(row=1,column=0)
        # self.motorsConf = ttk.LabelFrame(self, text = "Motor Configurations").grid(row=1,column=1)
        # # Elements for motortab
        # self.mntlist = ttk.Treeview(self.mountsList).grid(row=1,column=0)
        # self.cnflist = ttk.Treeview(self.motorsConf).grid(row=1,column=1)
        # self.grid(row=0,column=0)

class CalcTab(ttk.Frame):
    def __init__(self,main,*args,**kwargs):
        ttk.Frame.__init__(self,*args,**kwargs)
        self.tl=ttk.Label(self,text='calc').grid(row=0,column=0)
        
        

    