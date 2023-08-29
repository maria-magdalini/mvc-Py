from view import View, StartPage,PageOne,PageTwo,View_Grades
from model import Model
from student import Student
from lectures_view import Add_Lectures
model= Model()
class Controller():
    
    def __init__(self):
        self.view = View(self) # pass the Controller and its methods to the View Class
        
        self.model = Model()
        self.label = 3
        
        

        
        self.students= self.model.studets
        
        self.lectures = self.model.lectures
        # var = self.model.insert_student()
        
    
    def print_val(self,val):
        print(val)

    def change_frame(self, frame):
        self.view.show_frame(frame)

    def go_to_first_page(self):
        self.view.show_frame(PageOne)


        self.view.show_frame(PageTwo)    
         
    def go_to_third_page(self):
        self.view.show_frame(View_Grades)


    def go_to_main_page(self):
        self.view.show_frame(StartPage)

    def go_to_view_students_grade(self):
        self.view.show_frame(View_Grades)

    def go_to_add_lectures(self):
        self.view.show_frame(Add_Lectures)

    def _get_selected_student(self, *value):
        return value[0]

    def insert_std(self):
        # self.model.insert_student(args)
        # print(args)
         self.var = self.model.insert_student()
    


    def get_entrys(self,*args):
        value= args
        self.view.test()
        self.label= self._get_selected_student(value)
        self.view.show_frame(PageTwo)
        print(value, " sent to controller")

    def grade_student_lecture(self, grade):
        self.model.insert_student()
    
   
if __name__== "__main__":
    root =  Controller()
    
    root.view.mainFrame()  