
import sys
from sqlite3 import Error
import sqlite3
import os
import secrets


class Student():
    def __init__(self):
        self.DATABASE = r"/attendance.db"
        self.basedir = os.path.abspath(os.path.dirname(__file__))

    def select_student(self, username):
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        conn.row_factory = sqlite3.Row
        sql = ''' SELECT * FROM student WHERE username=? '''
        cur = conn.cursor()

        try:
            cur.execute(sql, (username,))
            data = cur.fetchone()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()

    def create_student(self, student_id, student_first_name, student_last_name, student_gender, student_username, student_password):
        sec = secrets.Secreto()
        self.student_id = student_id
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
        self.student_gender = student_gender
        self.student_username = student_username
        self.student_password = sec.to_hash(student_password)

        student = (self.student_id, self.student_first_name,
                   self.student_last_name, self.student_gender, self.student_username, self.student_password,)
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        sql = ''' INSERT INTO student(id_number, first_name, last_name, gender, username, password)
                VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()

        try:
            cur.execute(sql, student)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def delete_student(self, id):
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        sql = ''' DELETE FROM student WHERE id_number=? '''
        cur = conn.cursor()

        try:
            cur.execute(sql, id)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

class Lecturer:
    def __init__(self):
        self.DATABASE = r"/attendance.db"
        self.basedir = os.path.abspath(os.path.dirname(__file__))

    def select_lecturer(self, username):
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        conn.row_factory = sqlite3.Row
        sql = ''' SELECT * FROM lecturer WHERE username=? '''
        cur = conn.cursor()

        try:
            cur.execute(sql, (username,))
            data = cur.fetchone()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()

    def create_lecturer(self, lecturer_id, lecturer_first_name, lecturer_last_name, lecturer_gender, lecturer_username, lecturer_password):
        sec = secrets.Secreto()
        self.lecturer_id = lecturer_id
        self.lecturer_first_name = lecturer_first_name
        self.lecturer_last_name = lecturer_last_name
        self.lecturer_gender = lecturer_gender
        self.lecturer_username = lecturer_username
        self.lecturer_password = sec.to_hash(lecturer_password)

        lecturer = (self.lecturer_id, self.lecturer_first_name,
                   self.lecturer_last_name, self.lecturer_gender, self.lecturer_username, self.lecturer_password,)
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        sql = ''' INSERT INTO lecturer(id_number, first_name, last_name, gender, username, password)
                VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()

        try:
            cur.execute(sql, lecturer)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def delete_student(self, id):
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        sql = ''' DELETE FROM lecturer WHERE id_number=? '''
        cur = conn.cursor()

        try:
            cur.execute(sql, id)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

if __name__ == '__main__':
    Student()
    Lecturer()