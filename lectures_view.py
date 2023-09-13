import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame

class Add_Lectures(tk.Frame):
    def __init__(self, parent, contoller):
        tk.Frame.__init__(self, parent)

        self.controller = contoller
        self.deaprtments= [
            "Civil Engineering",
            "Architecture",
            "Planning and Regional Development",
            "Mechanical Engineering",
            "Electrical and Computer Engineering",
            "Economics",            
            "Business Administration"
        ]
        self.data = self.controller.model.fetch_lectures()
        # print(self.data)

        self.lecture_name = tk.StringVar()
        self.lecture_semetery = tk.IntVar()
        self.lecture_id = tk.IntVar()

        self.lectures_entry_frame= tk.Frame(self)
        self.lectures_entry_frame.pack(side='top', fill='both', expand=True)

        self.lectures_frame = tk.Frame(self)
        self.lectures_frame.pack(side='top', fill='both', expand=True)

        self.title = ttk.Label(self.lectures_frame, text='Add Lectures', font='Helvetica 16')
        self.title.pack(side='top', fill='both', expand=True)

        self.lectures_inside_frame = ttk.LabelFrame(self.lectures_frame, relief='solid')
        self.lectures_inside_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.make_lectures_entrys()
        self.make_buttons()

        self.lectures_tree_frame = ScrolledFrame(self.lectures_frame, autohide=True, height=400)
        self.lectures_tree_frame.pack(side='top', fill='both', expand=True)

        self.make_lectures_tree()


    def make_lectures_entrys(self):
        self.name_label = tk.Label(self.lectures_entry_frame, text="Τίτλος :")
        self.name_label.pack(pady=10, padx=10, side='left')

        self.name_entry = ttk.Entry(self.lectures_entry_frame, textvariable=self.lecture_name) 
        self.name_entry.pack(pady=10, padx=10, side='left')

        self.semetery_label = tk.Label(self.lectures_entry_frame, text="Εξάμηνο :")
        self.semetery_label.pack(pady=10, padx=10, side='left')

        self.semetery_entry = ttk.Entry(self.lectures_entry_frame, textvariable=self.lecture_semetery) 
        self.semetery_entry.pack(pady=10, padx=10, side='left')

        self.id_label = tk.Label(self.lectures_entry_frame, text="ID Μαθήματος :")
        self.id_label.pack(pady=10, padx=10, side='left')

        self.id_entry = ttk.Entry(self.lectures_entry_frame, textvariable=self.lecture_id) 
        self.id_entry.pack(pady=10, padx=10, side='left')

        self.uni_label = tk.Label(self.lectures_entry_frame, text="Σχολή :")
        self.uni_label.pack(pady=10, padx=10, side='left')

        self.uni_entry = ttk.Menubutton(self.lectures_entry_frame, text= "Επιλέξτε") 
        self.uni_entry.pack(pady=10, padx=10, side='left')

        self.uni_entry_menu= ttk.Menu(self.uni_entry)

        self.lecture_field= tk.StringVar()
        for department in self.deaprtments:
            self.uni_entry_menu.add_radiobutton(label=department, 
                                                variable=self.lecture_field, 
                                                command= lambda value=department : self.uni_entry.config(text=value) )
                                                 # with value = department we dont need to bind
                                       
        self.uni_entry['menu'] = self.uni_entry_menu
     
        

    def make_buttons(self):

        self.add_lecture_button = ttk.Button(self.lectures_inside_frame, text='Εισαγωγή Μαθήματος', 
                                             command= lambda: self.reload_lectures_tree() )
        
        self.add_lecture_button.pack(side='left', padx=10, pady=10)

        self.update_lecture_button = ttk.Button(self.lectures_inside_frame, text='Ενημέρωση Μαθήματος', 
                                                command= lambda: self.controller.model.update_lecture(self.lecture_id.get()))
        self.update_lecture_button.pack(side='left', padx=10, pady=10)

        self.delete_lecture_button = ttk.Button(self.lectures_inside_frame, text='Διαγραφή Μαθήματος',
                                                 command= lambda: self.controller.model.delete_lecture(self.lecture_id.get()), style='danger')
        self.delete_lecture_button.pack(side='left', padx=10, pady=10)

        self.main_page_button = ttk.Button(self.lectures_inside_frame, text='Πίσω στην Αρχική', command= lambda: self.controller.go_to_main_page())
        self.main_page_button.pack(side='left', padx=10, pady=10)

    
    def make_lectures_tree(self):
        def clicl(e):
            print(2)
            lecture.config(text='blue')
           
        x=0
        for i in self.data:

            lecture = tk.Label(self.lectures_tree_frame, text=f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} " )
            lecture.pack(padx=10, pady=10)
            arr = []
            arr.append(lecture)
            # arr[i].bind('<Button-1>', clicl)
            print(arr)
            x = x+1
        
    def reload_lectures_tree(self):
        self.controller.model.insert_lecture(self.lecture_name.get(), self.lecture_semetery.get(), self.lecture_id.get(), self.lecture_field.get())   
        self.data = self.controller.model.fetch_lectures()
        self.make_lectures_tree()