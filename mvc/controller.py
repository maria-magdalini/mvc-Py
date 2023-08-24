from view import View
class Controller():
    def __init__(self):
        self.view = View(self) # pass the Controller and its methods to the View Class
        self.view.mainFrame()
        
    def print_val(self,val):
        print(val)


if __name__== "__main__":
    root =  Controller()
       