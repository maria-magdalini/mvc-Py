import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame

class Add_Lectures(tk.Frame):
    def __init__(self, parent, contoller):
        tk.Frame.__init__(self, parent)

        self.controller = contoller
        
        self.lectures_frame = tk.Frame(self)
        self.lectures_frame.pack(side='top', fill='both', expand=True)

        self.title = ttk.Label(self.lectures_frame, text='Add Lectures', font='Helvetica 16')
        self.title.pack(side='top', fill='both', expand=True)

        self.lectures_inside_frame = ttk.LabelFrame(self.lectures_frame, relief='solid')
        self.lectures_inside_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.make_buttons()

        self.lectures_tree_frame = ScrolledFrame(self.lectures_frame, autohide=True, height=400)
        self.lectures_tree_frame.pack(side='top', fill='both', expand=True)

        self.make_lectures_tree()



    def make_buttons(self):

        self.add_lecture_button = ttk.Button(self.lectures_inside_frame, text='Εισαγωγή Μαθήματος', command= lambda: None)
        self.add_lecture_button.pack(side='left', padx=10, pady=10)

        self.update_lecture_button = ttk.Button(self.lectures_inside_frame, text='Ενημέρωση Μαθήματος', command= lambda: None)
        self.update_lecture_button.pack(side='left', padx=10, pady=10)

        self.delete_lecture_button = ttk.Button(self.lectures_inside_frame, text='Διαγραφή Μαθήματος', command= lambda: None, style='danger')
        self.delete_lecture_button.pack(side='left', padx=10, pady=10)

        self.main_page_button = ttk.Button(self.lectures_inside_frame, text='Πίσω στην Αρχική', command= lambda: self.controller.go_to_main_page())
        self.main_page_button.pack(side='left', padx=10, pady=10)

    def make_lectures_tree(self):
        for i in range(20):
            button = ttk.Button(self.lectures_tree_frame, text=i)
            button.pack(padx=10, pady=10)
