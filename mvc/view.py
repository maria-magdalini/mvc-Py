import tkinter as tk
from tkinter import ttk
from pageOne import PageOne
from pageTwo import PageTwo
from thirdPage import PageThree
class View(tk.Tk):

    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.controller = controller
        print(self.controller.__class__)

    def mainFrame(self):
        container=tk.Frame(self, bg='red')
        container.pack(side='top')

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
       
        self.frames={}
        for F in (StartPage, PageOne, PageTwo, PageThree):
       
            frame = F(container, self.controller)
        
            self.frames[F]= frame
        
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
        tk.Tk.mainloop(self)

    def show_frame(self, cont):
        frame = self.frames[cont]  #select the given frame  
        
        frame.tkraise() #then raise it to the top of stack 

    
    def printit(self, frame):
        self.val= 'hello'
        self.controller.print_val(self.val)
        self.controller.change_frame(frame)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        #passing the parent in the StartPage like this (tk.Frame(App))
        #its like: frame(App) -> the frame is hosted in the Parent witch is App
        tk.Frame.__init__(self,parent)
       
    
        label = tk.Label(self, text="Διαχειριστικό Σύστημα")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Επόμενη σελίδα",
                            command=lambda: controller.go_to_first_page() ) #acts as a onClick event
        button.pack(pady=10, padx=10)
       




