from view import View, StartPage,PageOne,PageTwo,PageThree
from model import Model
from student import Student
class Controller():
    def __init__(self):
        self.view = View(self) # pass the Controller and its methods to the View Class
        
        self.label = 3
        self.model= Model()
        self.arr= []
        
        
        self.students= self.model.studets
        
    def print_val(self,val):
        print(val)

    def change_frame(self, frame):
        self.view.show_frame(frame)

    def go_to_first_page(self):
        self.view.show_frame(PageOne)

    def go_to_second_page(self,student_values):
        self.student_class = Student(student_values)
        
        self.view.show_frame(PageTwo)
        
         
    def go_to_third_page(self):
        self.view.show_frame(PageThree)


    def go_to_main_page(self):
        self.view.show_frame(StartPage)

    def print_value(self, *value):
        return value[0]
        print (value[0])


    def get_entrys(self,*args):
        value= args
        self.view.test()
        # name= value[0]
        # lastname= value
        self.arr = value
        self.label= self.print_value(value)
        self.view.show_frame(PageTwo)
        print(value, " sent to controller")
    
if __name__== "__main__":
    root =  Controller()
    
    root.view.mainFrame()  