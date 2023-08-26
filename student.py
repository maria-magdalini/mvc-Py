class Student():
    def __init__(self, *args):
        
        self.name = args[0][0]
        self.last_name = args[0][1]
        self.university = args[0][2]
        self.serial_Tag = args[0][3]
        print(args, "args")