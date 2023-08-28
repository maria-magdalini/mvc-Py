import tkinter as tk
from tkinter import ttk
from student import Student
from ttkbootstrap.tableview import Tableview

class PageTwo(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        
        self.controller = controller

        self.student  = self.controller.get_entrys
        self.lectuers = self.controller.lectures
        
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

        self.grade_value = tk.DoubleVar()

        

        # self.name_label = tk.Label(self.label_frame , text=self.controller.label[0])
        # self.name_label.pack(padx=10, pady=10, side='left')
        self._make_all_entrys()

    def _make_all_entrys(self):
        self._make_name_entrys()
        self._make_lastname_entrys()
        self._make_serial_tag_entry()
        self.grades_frame = tk.Frame(self.main_frame)
        self.grades_frame.pack(padx=10, pady=10)
        self._make_grages_label_and_entrys()
        self._makes_grades_list(self.lectuers)
        
    def void(self):
        pass
    def _make_name_entrys(self):
        self.name_label = tk.Label(self.label_frame, text="Όνομα :")
        self.name_label.pack(pady=10, padx=10, side='left')

        self.name_entry = ttk.Entry(self.label_frame, textvariable=None) 
        self.name_entry.pack(pady=10, padx=10, side='left')
        self.name_entry.insert(0, self.controller.label[0])
        self.name_entry.config(state='read')
    

       

    def _make_lastname_entrys(self):
        self.last_name_label = tk.Label(self.label_frame, text="Επώνυμο :")
        self.last_name_label.pack(pady=10, padx=10, side='left')

        self.last_name_entry = ttk.Entry(self.label_frame) 
        self.last_name_entry.pack(pady=10, padx=10, side='left')
        self.last_name_entry.insert(0, self.controller.label[1])
        self.last_name_entry.config(state='read')
    
    def _make_serial_tag_entry(self):
        self.serial_tag_label = tk.Label(self.label_frame, text= "Αριθμός Μητρώου :")
        self.serial_tag_label.pack(pady=10, padx=10, side='left')

        self.serial_tag_entry = ttk.Entry(self.label_frame, textvariable=None)
        self.serial_tag_entry.pack(pady=10, padx=10, side='left')
        self.serial_tag_entry.insert(0, self.controller.label[2])
        self.serial_tag_entry.config(state='read')


    def _make_grages_label_and_entrys(self):
        self.lecture_label = ttk.Label(self.grades_frame, text="Μάθημα : ")
        self.lecture_label.pack(pady=10, padx=10, side='left')

        self.lecture_entry = ttk.Label(self.grades_frame)
        self.lecture_entry.pack(pady=10, side='left')

        self.grade_label = ttk.Label(self.grades_frame, text="  Βαθμός : ")
        self.grade_label.pack(pady=10, padx=10, side='left')

        self.grade_entry = ttk.Entry(self.grades_frame , textvariable=self.grade_value )
        self.grade_entry.pack(pady=10, padx=10, side='left')

        self.grade_button = ttk.Button(self.grades_frame, text="Βαθμολόγηση", style="success", command= lambda : self.controller.grade_student_lecture(self.grade_value))
        self.grade_button.pack(pady=10, padx=10, side='left')
        
        self.view_grades = ttk.Button(self.grades_frame, text="Προβολή Βαθμών", style="success", command= lambda : self.controller.grade_student_lecture(self.grade_value))
        self.view_grades.pack(pady=10, padx=10, side='left')
        

    def _makes_grades_list(self,lectures):
        

        self.list_frame = tk.Frame(self)
        self.list_frame.pack(padx=10,pady=10,side='bottom')
        self.columns=['Name', 'Semetery', 'Serial No.', 'Department']
        self.grades_list = Tableview(self.list_frame, coldata=self.columns, rowdata = lectures, searchable=True, paginated=True)
        self.grades_list.pack()
       
            
        def _get_lecture(e):
            iid= self.grades_list.view.selection()
            selection = self.grades_list.view.item(iid,'values') # values from the selected student in the list
            self.clear_entrys(selection)
        
        self.grades_list.view.bind('<<TreeviewSelect>>',  _get_lecture)

    def clear_entrys(self, selection):
        self.lecture_entry.config(text=selection[0])
