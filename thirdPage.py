
import tkinter as tk
from tkinter import ttk




class PageThree(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="3")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Επιστρωφή στην Αρχή",
                            command=lambda: controller.go_to_main_page() ) #acts as a onClick event
        button.pack(pady=10, padx=10)
