import sqlite3
import secrets
import datetime
import random

conn = sqlite3.connect('attendance.db')


class db(object):
	def __init__(self, id_number=None, first_name=None, last_name=None,
						gender=None, username=None, password=None,
						current_id=None, unique_id=None, sessions_id=None):

		self.unique_id = unique_id
		self.id_number = id_number
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.gender = gender
		self.current_id = current_id
		self.sessions_id = sessions_id
		self.sec = secrets.Secreto()




	def add_student(self):
		cursor = conn.cursor()

		hashed_pass = self.sec.to_hash(self.password)
		student = (self.id_number, self.first_name, self.last_name, self.gender, self.username, hashed_pass,)
		sql = """
				INSERT INTO student (id_number, first_name, last_name, gender, username, password)
				VALUES(?,?,?,?,?,?)  
			""" 

		try:
			cursor.execute(sql, student)
			conn.commit()

		except Exception as e:
			print(e)
		

	def update_student(self):
		cursor = conn.cursor()
		hashed_pass = self.sec.to_hash(self.password)
		student = (self.id_number, self.first_name, 
                								self.last_name, 
                								self.gender, 
                								self.username, 
                								hashed_pass,
                								self.current_id,)
		sql = """UPDATE student SET id_number= ?, first_name = ?,
		 					last_name = ?, gender = ?, username = ?, password = ?
                WHERE id_number = ?""" 

		try:
			cursor.execute(sql, student)
			conn.commit()
		except Exception as e:
			print(e)

	def update_student_password(self):
		cursor = conn.cursor()
		hashed_pass = self.sec.to_hash(self.password)
		teacher = (hashed_pass, self.current_id)

		sql = """UPDATE student SET password = ? WHERE id_number = ?"""

		try:
			cursor.execute(sql, teacher)
			conn.commit()
		except Exception as e:
			print(e)

	def check_student_username(self):
		cursor = conn.cursor()
		sql = """
				SELECT username FROM student WHERE username = '{}'""".format(self.username)
		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return True
		else:
			return False

	def check_student_id(self):
		cursor = conn.cursor()
		sql = """
				SELECT id_number FROM student WHERE id_number = '{}'""".format(self.id_number)
		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return True
		else:
			return False

	def login_student(self):
		username = self.username
		cursor = conn.cursor()
		conn.row_factory = sqlite3.Row
		sql = ''' SELECT * FROM student WHERE username=? '''
		cur = conn.cursor()
		try:
			cur.execute(sql, (username,))
			data = cur.fetchone()
			if data:
				return data
			else:
				return False
		except Error as e:
			print(e)
		

	def login_student_back(self):
		cursor = conn.cursor()
		sql = """SELECT * FROM student WHERE id = '{}'""".format(self.unique_id)
		cursor.execute(sql)
		display = cursor.fetchone()

		if display:
			return display
		else:
			return False

########################################### TEACHER PART #######################################33
	def add_teacher(self):
		cursor = conn.cursor()

		hashed_pass = self.sec.to_hash(self.password)
		teacher = (self.id_number, self.first_name, self.last_name, self.gender, self.username, hashed_pass)

		sql = """
				INSERT INTO lecturer (id_number, first_name, last_name, gender, username, password)
				VALUES(?,?,?,?,?,?)  
			"""

		
		try:
			cursor.execute(sql, teacher)
			conn.commit()
			
		except Exception as e:
			print(e)


	def update_teacher(self):
		cursor = conn.cursor()
		teacher = (self.id_number, self.first_name, 
                								self.last_name, 
                								self.gender, 
                								self.username, 
                								self.current_id,)
		
		sql = """UPDATE lecturer SET id_number= ?, first_name = ?,
		 					last_name = ?, gender = ?, username = ?
                WHERE id_number = ?"""

		try:
			cursor.execute(sql, teacher)
			conn.commit()
		except Exception as e:
			print(e)

	def update_teacher_password(self):
		cursor = conn.cursor()
		hashed_pass = self.sec.to_hash(self.password)
		teacher = (hashed_pass, self.current_id)

		sql = """UPDATE lecturer SET password = ? WHERE id_number = ?"""

		try:
			cursor.execute(sql, teacher)
			conn.commit()
		except Exception as e:
			print(e)


	def check_teacher_username(self):
		cursor = conn.cursor()
		sql = """
				SELECT username FROM lecturer WHERE username = '{}'""".format(self.username)
		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return True
		else:
			return False

	def check_teacher_id(self):
		cursor = conn.cursor()
		sql = """
				SELECT id_number FROM lecturer WHERE id_number = '{}'""".format(self.id_number)
		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return True
		else:
			return False

	def view_all_students(self):
		cursor = conn.cursor()
		sql = """ SELECT id_number, last_name, first_name, gender FROM student"""

		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return display
		else:
			pass


	def login_teacher(self):
		username = self.username
		cursor = conn.cursor()
		conn.row_factory = sqlite3.Row
		sql = ''' SELECT * FROM lecturer WHERE username=? '''
		cur = conn.cursor()
		try:
			cur.execute(sql, (username,))
			data = cur.fetchone()
			if data:
				return data
			else:
				return False
		except Error as e:
			print(e)
		
	def login_teacher_back(self):
		cursor = conn.cursor()
		sql = """SELECT * FROM lecturer WHERE id = '{}'""".format(self.unique_id)
		cursor.execute(sql)
		display = cursor.fetchone()

		if display:
			return display
		else:
			return False

	def student_attended_classes(self):
		#date,subject,section,course,start_time,end_time,status in order
		sql = """ SELECT  """
		cur = conn.cursor()
		cur.execute(sql)
		data = cur.fetchall()

		return data

