
import sqlite3

class Model:
    def __init__(self, controller):
        self.controller= controller
        self.studets = [
            ('Nikos', 'Louzis', 4465 , 'Architecture'),
            ('Giannis', 'Keramas', 4534, 'Economics')
        ]

        self.lectures = [
            ('C #', 2, 3423 , 'Architecture'),
            ('Java', 3, 1134, 'Economics')
        ]

        self.conn = sqlite3.connect("Students.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY , name TEXT, lastname TEXT, serial INTEGER, university TEXT)")
        self.conn.commit()
        
        self.answer = self.insert_student()
    def insert_student(self):
        # self.cur.execute("INSERT INTO students VALUES(NULL,?,?,?,?)", (args[0], args[1],args[2], args[3]))
        # self.conn.commit()
        print(self.model.insert_student())
        return ('hello')

    def update_student(self,*args):
        pass

    def delete_student(self,*args):
        pass
    
    def insert_student(self,*args):
        pass
