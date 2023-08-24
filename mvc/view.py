import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.controller = controller
        

    def mainFrame(self):
        container=tk.Frame(self, bg='red')
        container.pack(side='top', fill="both", expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
       
       
        self.frames={}
        for F in (StartPage, PageOne, PageTwo):
       
            frame = F(container, self)
        
            self.frames[F]= frame
        
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
        tk.Tk.mainloop(self)

    def show_frame(self, cont):
        frame = self.frames[cont]  #select the given frame  
        
        frame.tkraise() #then raise it to the top of stack 

    
    def printit(self):
        self.val= 'hello'
        self.controller.print_val(self.val)



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        #passing the parent in the StartPage like this (tk.Frame(App))
        #its like: frame(App) -> the frame is hosted in the Parent witch is App
        tk.Frame.__init__(self,parent)
       
    
        label = tk.Label(self, text="Διαχειριστικό Σύστημα")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Epomenh",
                            command=lambda: controller.show_frame(PageOne) ) #acts as a onClick event
        button.pack(pady=10, padx=10)
        button2 = ttk.Button(self, text="Print",
                            command=lambda: controller.printit() ) #acts as a onClick event
        button2.pack(pady=10, padx=10)

class PageOne(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="1")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Epomenh selida",
                            command=lambda: controller.show_frame(PageTwo) ) #acts as a onClick event
        button.pack(pady=10, padx=10)

class PageTwo(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="2")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Διαχείριση Φοιτητών",
                            command=lambda: controller.show_frame(StartPage) ) #acts as a onClick event
        button.pack(pady=10, padx=10)

