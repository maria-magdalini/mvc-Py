import tkinter as tk
from tkinter import ttk
from student import Student

class PageTwo(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        
        self.controller = controller

        self.student = self.controller.arr
        print(self.student, 'Student')
        
        label = tk.Label(self, text="2")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Επόμενη σελίδα",
                            command=lambda: controller.go_to_third_page()) #acts as a onClick event
        button.pack(pady=10, padx=10)

        

        # self.student_name = Student.name

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side='top',fill='both', expand=True)

        self.label_frame = tk.Frame(self.main_frame)
        self.label_frame.pack(padx=10, pady=10)

        self.name_label = tk.Label(self.label_frame)
        self.name_label.pack(padx=10, pady=10, side='left')