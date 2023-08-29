import tkinter as tk
# from tkinter import ttk 
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview


class PageOne(tk.Frame):
    def __init__(self,parent, controller):
        self.deaprtments= [
            "Civil Engineering",
            "Architecture",
            "Planning and Regional Development",
            "Mechanical Engineering",
            "Electrical and Computer Engineering",
            "Economics",            
            "Business Administration"
        ]
        tk.Frame.__init__(self,parent)
        
        self.entrys_holder = tk.Frame(self)
        self.entrys_holder.pack(side='top',fill='both', expand=True, pady=30)

        self.controller= controller
        label = tk.Label(self.entrys_holder, text="Διαχείρηση Φοιτητών", font='Helvetica 16 bold')
        label.pack(pady=10, padx=10)

        button = ttk.Button(self.entrys_holder, text="Εισαγωγή Βαθμών",
                            command=lambda: self.switch_frame() ) #acts as a onClick event
        button.pack(pady=10, padx=10)
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.serial_tag = tk.IntVar()
        self.university = tk.StringVar()
        
        self.students = self.controller.students
        self._make_all_entrys()
        
        self.selection = self.get_selection
    def get_selection(self):
        self.controller.get_entrys(self.name.get(), self.last_name.get(), self.serial_tag.get(), self.uni_value.get())
        # print (selection)
        # return selection
    
    def switch_frame(self):
        # self.values = self.name.get(), self.last_name.get(), self.serial_tag.get(), self.uni_value.get()
        # self.controller.arr = self.values
        self.controller.get_entrys(self.name.get(), self.last_name.get(), self.serial_tag.get(), self.uni_value.get())
        # self.controller.go_to_second_page(self.values)

    def _make_all_entrys(self):
        self._make_name_entrys()
        self._make_lastname_entrys()
        self._make_serial_tag_entry()
        self._make_university_entrys()
        self._makes_students_list(self.students)

    def _make_name_entrys(self):
        self.name_label = tk.Label(self.entrys_holder, text="Όνομα :")
        self.name_label.pack(pady=10, padx=10, side='left')

        self.name_entry = ttk.Entry(self.entrys_holder, textvariable=self.name) 
        self.name_entry.pack(pady=10, padx=10, side='left')

        self.name_button = ttk.Button(self.entrys_holder, text='print', command=lambda: self.get_selection())
        self.name_button.pack(pady=10, padx=10, side='left')

    def _make_lastname_entrys(self):
        self.last_name_label = tk.Label(self.entrys_holder, text="Επώνυμο :")
        self.last_name_label.pack(pady=10, padx=10, side='left')

        self.last_name_entry = ttk.Entry(self.entrys_holder, textvariable=self.last_name) 
        self.last_name_entry.pack(pady=10, padx=10, side='left')
    
    def _make_serial_tag_entry(self):
        self.serial_tag_label = tk.Label(self.entrys_holder, text= "Αριθμός Μητρώου :")
        self.serial_tag_label.pack(pady=10, padx=10, side='left')

        self.serial_tag_entry = ttk.Entry(self.entrys_holder, textvariable=self.serial_tag)
        self.serial_tag_entry.pack(pady=10, padx=10, side='left')
    
    def get_university(self,value):
        self.uni_entry.config(text=value)

        print(value)
    def _make_university_entrys(self):
        self.uni_label = tk.Label(self.entrys_holder, text="Σχολή :")
        self.uni_label.pack(pady=10, padx=10, side='left')

        self.uni_entry = ttk.Menubutton(self.entrys_holder, text= "Επιλέξτε") 
        self.uni_entry.pack(pady=10, padx=10, side='left')

        self.uni_entry_menu= ttk.Menu(self.uni_entry)

        self.uni_value= tk.StringVar()
        for department in self.deaprtments:
            self.uni_entry_menu.add_radiobutton(label=department, 
                                                variable=self.uni_value, 
                                                command= lambda value=department : self.get_university(value))
                                                 # with value = department we dont need to bind
       
        self.uni_entry['menu'] = self.uni_entry_menu

    def _get_student_(self,e):
            iid= self.students_list.view.selection()
            value = self.students_list.view.item(iid,'values')
           

    def _makes_students_list(self,students):
        

        self.list_frame = tk.Frame(self)
        self.list_frame.pack(padx=10,pady=10,side='bottom')
        self.columns=['Name', 'Last Name', 'AM', 'Department']
        self.students_list = Tableview(self.list_frame, coldata=self.columns, rowdata = students, searchable=True, paginated=True)
        self.students_list.pack()
       
            
        def _get_student_(e):
            iid= self.students_list.view.selection()
            selction = self.students_list.view.item(iid,'values') # values from the selected student in the list
            self.clear_entrys(selction)
        
        self.students_list.view.bind('<<TreeviewSelect>>',  _get_student_)

    def clear_entrys(self, selection):
        self.name_entry.delete(0,tk.END)
        self.last_name_entry.delete(0,tk.END)
        self.serial_tag_entry.delete(0,tk.END)
        
        """
        to check the university based on the selected item in the list 
        we need to set the variable  to the university value of the selected item
        """
        self.uni_entry.config(text=selection[3])
        self.uni_value.set(selection[3])
        self.name_entry.insert(0, selection[0])
        self.last_name_entry.insert(0, selection[1])
        self.serial_tag_entry.insert(0, selection[2])
        # self.get_selection(selection)


