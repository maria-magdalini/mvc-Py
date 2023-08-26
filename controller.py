from view import View, StartPage,PageOne,PageTwo,PageThree
from model import Model
from student import Student
class Controller():
    def __init__(self):
        self.view = View(self) # pass the Controller and its methods to the View Class
        self.page_one = PageOne
        self.page_two = PageTwo
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
        PageTwo.student = self.student_class
        self.view.show_frame(PageTwo)
        
        
    def go_to_third_page(self):
        self.view.show_frame(PageThree)


    def go_to_main_page(self):
        self.view.show_frame(StartPage)

    def print_value(self, value):
        print(value)


    def get_entrys(self,*args):
        value= args
        # name= value[0]
        # lastname= value
        print(value)
if __name__== "__main__":
    root =  Controller()
    
    root.view.mainFrame()  