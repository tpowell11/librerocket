import tkinter.ttk as ttk
import tkinter as tk
class test(ttk.Frame):
    def __init__(self, m, *args, **kwargs) -> None:
        self.f = ttk.Frame.__init__(m,*args,**kwargs)
        self.l = ttk.Label(self.f, text='test')
        self.l.grid(row=0,column=0)
class main():
    def __init__(self,parent):
        self.l = ttk.Label(parent,text='main')
        self.l.grid(row=0,column=0)
        self.nb = ttk.Notebook(parent)
        inc = test(parent)
        self.nb.add(inc.f)
        self.nb.grid(row=1,column=0)
    
if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()