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
        self.outlineframe = ttk.LabelFrame(self,text = 'Outline').grid(row=1,column=0)
        self.partsframe = ttk.LabelFrame(self, text = 'Parts').grid(row = 1, column = 1)
        self.diagramframe = ttk.LabelFrame(self,text = 'Diagram').grid(row=4,columnspan=2,sticky='nsew')
        buttonGrid(self.partsframe, 4,tl).grid()
        self.treeview = ttk.Treeview(self.outlineframe).grid(row=1,column=0)
        
        self.canvas = tk.Canvas(self.diagramframe).grid(row=4)
        

class MotorTab(ttk.Frame):
    def __init__(self,main,*args,**kwargs):
        ttk.Frame.__init__(self,*args,**kwargs)
        self.mountsList = ttk.LabelFrame(self, text = 'Motor Mounts').grid(row=1,column=0)
        self.motorsConf = ttk.LabelFrame(self, text = "Motor Configurations").grid(row=1,column=1)
        # Elements for motortab
        self.mntlist = ttk.Treeview(self.mountsList).grid(row=1,column=0)
        self.cnflist = ttk.Treeview(self.motorsConf).grid(row=1,column=1)
        

class CalcTab(ttk.Frame):
    def __init__(self,main,*args,**kwargs):
        ttk.Frame.__init__(self,*args,**kwargs)
        self.tl=ttk.Label(self,text='calc').grid(row=0,column=0)
        
        
class app(ttk.Frame):
    def __init__(self, main, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
        #rest of gui code below
        #ttk.Label(root,text='test').pack()
        #
        # Top menu
        #
        self.menubar = tk.Menu(main) #top-of-window menubar
        self.file = tk.Menu(self.menubar,tearoff=0)
        self.file.add_command(label="New")
        self.file.add_command(label="Open",command=eh.getFilename)  
        self.file.add_command(label="Save")  
        #file.add_command(label="Save as...",command=lambda rocket: eh.saveAs(rocket))
        #file.add_command(label="Save as...",command=eh.saveAs(rock))  
        self.file.add_command(label="Save as...")
        self.file.add_command(label="Close",command=eh.exitApp)
        self.menubar.add_cascade(label='File',menu=self.file) 
        tools = tk.Menu(self.menubar,tearoff=0)
        tools.add_command(label='Settings') #launch settings dialog
        tools.add_command(label='User Presets') #launch user presets management dialog
        self.menubar.add_cascade(label='Tools',menu=tools)
        root.config(menu=self.menubar) 
        #
        #Tabbed layout configuration
        
        self.tabControl = ttk.Notebook(self) #tabbed layout for multiple tasks
        self.designTab = DesignTab(self.tabControl)
        self.motorTab = MotorTab(self.tabControl) #the motor selection and data entry tab
        self.calcTab = CalcTab(self.tabControl) #simulation / calculation tab
        #pushing tabs to container
        self.tabControl.add(self.designTab, text = "Design")
        self.tabControl.add(self.motorTab, text = "Motor Configuration")
        self.tabControl.add(self.calcTab, text = "Calculations")
        self.tabControl.grid(row=0)

if __name__ == '__main__':
    root = tk.Tk()
    #app(root).pack(side='top',fill='both',expand=True)
    app(root).grid()
    root.mainloop()
    