import tkinter as tk
from tkinter import ttk
from pageOne import PageOne
from pageTwo import PageTwo
from thirdPage import View_Grades
class View(tk.Tk):

    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.controller = controller
        self.val = None
        print(self.val)
        
    def mainFrame(self):
        self.container=tk.Frame(self, bg='red')
        self.container.pack(side='top')

        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)
       
        self.frames={}
        # for F in (StartPage, PageOne, PageTwo, View_Grades):
       
        #     frame = F(container, self.controller)
        
        #     self.frames[F]= frame
        
        #     frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)
        
        tk.Tk.mainloop(self)

    def show_frame(self, page):
        frame = page(self.container, self.controller)

        frame.grid(row=0, column=0, sticky="nsew") # make page expand and visible
  
        frame.tkraise() #then raise it to the top of stack 

    
    def printit(self, frame):
        self.val= 'hello'
        self.controller.print_val(self.val)
        self.controller.change_frame(frame)
    def test(self):
        self.val = 2
        
        return self.val

class StartPage(tk.Frame):
    def __init__(self, parent, controller, *args):
        #passing the parent in the StartPage like this (tk.Frame(App))
        #its like: frame(App) -> the frame is hosted in the Parent witch is App
        tk.Frame.__init__(self,parent)
       
    
        label = tk.Label(self, text="Διαχειριστικό Σύστημα")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Επόμενη σελίδα",
                            command=lambda: controller.go_to_first_page() ) #acts as a onClick event
        button.pack(pady=10, padx=10)

        add_lectures_button = ttk.Button(self, text="Εισαγωγή Μαθημάτων", command= lambda : controller.go_to_add_lectures())
        add_lectures_button.pack(pady=10, padx=10)
       

    


