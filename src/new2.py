import tkinter.ttk as ttk
import tkinter as tk
class test():
    def __init__(self, root) -> None:
        self.frame = ttk.Frame(root).grid(row=0,column=0)
        self.text = ttk.Label(self.frame)
class main():
    def __init__(self,parent):
        self.parent = parent
        tabbed = ttk.Notebook(self.parent)
        tabbed.add(test(tabbed).text,text='test')
if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()