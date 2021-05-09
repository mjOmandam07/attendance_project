import sqlite3

conn = sqlite3.connect('attendance.db')


class db(object):
	def __init__(self, id_number=None, first_name=None, last_name=None,
						gender=None, username=None, password=None,
						current_id=None):

		self.id_number = id_number
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.gender = gender
		self.current_id = current_id




	def add_student(self):
		cursor = conn.cursor()
		sql = """
				INSERT INTO student (id_number, first_name, last_name, gender, username, password)
				VALUES('%s', '%s', '%s', '%s', '%s', '%s')  
			""" % (self.id_number, self.first_name, self.last_name, self.gender, self.username, self.password)

		cursor.execute(sql)
		conn.commit()


	def update_student(self):
		cursor = conn.cursor()
		sql = """UPDATE student SET id_number= '%s', first_name = '%s',
		 					last_name = '%s', gender = '%s', username = '%s', password = '%s'
                WHERE id_number = '%s'"""  % (self.id_number, self.first_name, 
                								self.last_name, 
                								self.gender, 
                								self.username, 
                								self.password,
                								self.current_id)

		cursor.execute(sql)
		conn.commit()

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


############################################ TEACHER PART #######################################33
	def add_teacher(self):
		cursor = conn.cursor()
		sql = """
				INSERT INTO lecturer (id_number, first_name, last_name, gender, username, password)
				VALUES('%s', '%s', '%s', '%s', '%s', '%s')  
			""" % (self.id_number, self.first_name, self.last_name, self.gender, self.username, self.password)

		cursor.execute(sql)
		conn.commit()


	def update_teacher(self):
		cursor = conn.cursor()
		sql = """UPDATE lecturer SET id_number= '%s', first_name = '%s',
		 					last_name = '%s', gender = '%s', username = '%s', password = '%s'
                WHERE id_number = '%s'"""  % (self.id_number, self.first_name, 
                								self.last_name, 
                								self.gender, 
                								self.username, 
                								self.password,
                								self.current_id)

		cursor.execute(sql)
		conn.commit()

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
		sql = """ SELECT id_number, last_name, first_name FROM student"""

		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return display
		else:
			pass






