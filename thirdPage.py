
import tkinter as tk
from tkinter import ttk




class View_Grades(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="3")
        label.pack(pady=10, padx=10)

        self.controller = controller
        self.student = self.controller.label

        button = ttk.Button(self, text="Επιστρωφή στην Αρχή",
                            command=lambda: controller.go_to_main_page() ) #acts as a onClick event
        button.pack(pady=10, padx=10)

        self.main_frame = tk.LabelFrame(self, text=f"Καρτέλα Βαθμών : {self.student[0]} {self.student[1]} {self.student[2]}", font='Helvetica 13 bold')
        self.main_frame.pack(side='top',fill='both', expand=True, padx=10, pady=10)

        self.buttons_frame = tk.LabelFrame(self.main_frame)
        self.buttons_frame.pack(fill='x', expand=True, padx=10, pady=10, anchor='n')

        self.make_buttons()

    def make_buttons(self):
        self.update_button = ttk.Button(self.buttons_frame, text= "Update", style='success')
        self.update_button.pack(side='left', padx=10, pady=10)

        self.delete_button = ttk.Button(self.buttons_frame, text= "Delete", style='danger')
        self.delete_button.pack(side='left', padx=10, pady=10)

        self.insert_button = ttk.Button(self.buttons_frame, text= "Insert", command=lambda: self.controller.go_to_second_page())
        self.insert_button.pack(side='left', padx=10, pady=10)