import tkinter as tk
from tkinter import messagebox
import sqlite3

class Model:
    def __init__(self,controller):
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
        self.cur.execute("CREATE TABLE IF NOT EXISTS lectures (id INTEGER PRIMARY KEY , lecture_ame TEXT, semester INTEGER, lecture_id INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS grades (id INTEGER PRIMARY KEY , lecture_id TEXT, student_id, grade INTEGER )")
        
    def count(self,serial):
        self.cur.execute("SELECT COUNT(*) FROM students WHERE serial=?",(int(serial),))
        
        row = self.conn.commit()
        print(row)

    def insert_student(self, *students_data):
        self.cur.execute("SELECT COUNT(*) FROM students WHERE serial=?",(students_data[2],))
        res =  self.cur.fetchall()             
        

        if res[0][0] >= 1 :
            return messagebox.showerror('Error' , 'Ο Βαθμός του μαθήματος πρένει να είναι απο 0 έως 10.')
        else:
            pass
            self.cur.execute("INSERT INTO students VALUES(NULL,?,?,?,?)", (students_data[0], students_data[1], students_data[2],students_data[3]))
            self.conn.commit()
            self.reload_table_data(students_data[4])

        print(res[0][0])
        
    def reload_table_data(self,treeview):
        self.cur.execute("SELECT name,lastname,serial,university FROM students")
        res = self.cur.fetchall()
        print(res)
        treeview.delete_rows()
        for entry in res:
            treeview.insert_row(tk.END, entry) #insert the data 
        treeview.load_table_data()# display the data
        return

       
        
    def show_all_students(self):
        self.cur.execute("SELECT name,lastname,serial,university FROM students")
        res = self.cur.fetchall()
        return res
        
    def show_all_lectures(self):
        self.cur.execute("SELECT * FROM lectures")
        res = self.cur.fetchall()
        return res
    
    def show_all_grades(self):
        self.cur.execute("SELECT * FROM grades")
        res = self.cur.fetchall() 
        return res

    def update_student(self,*students_data):
        # self.cur.execute("UPDATE students SET VALUES(NULL,?,?,?,?)",(students_data[0], students_data[1], students_data[2],students_data[3]))
        # self.conn.commit()
        student_rows =  self.cur.execute("SELECT * FROM students WHERE serial=?",(students_data[4],))
        self.conn.commit()
        print(student_rows)

        print(students_data)

    def delete_student(self,*students_data):
        self.conn.execute("DELETE * FROM students WHERE serrial=?",(students_data[2],))
        self.conn.commit()
        pass
    
    # def insert_student(self):
    #     print('Inserting student')

# Model().cur.execute("INSERT INTO students VALUES(NULL,?,?,?,?)", ('Nikos', 'Louzis', 4465 , 'Architecture') )
