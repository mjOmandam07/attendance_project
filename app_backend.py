import sqlite3
import secrets

conn = sqlite3.connect('attendance.db')


class db(object):
	def __init__(self, id_number=None, first_name=None, last_name=None,
						gender=None, username=None, password=None,
						current_id=None, unique_id=None,
						course_name=None, course_code=None, created_on=None,
						expire_date=None, is_active=None, lecturer=None, current_datetime = None,
						has_pass=None, section=None):

		self.unique_id = unique_id
		self.id_number = id_number
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.gender = gender
		self.section = section
		self.current_id = current_id
		self.sec = secrets.Secreto()

		self.course_name = course_name
		self.course_code = course_code
		self.created_on = created_on
		self.expire_date = expire_date
		self.current_datetime = current_datetime
		self.is_active = is_active
		self.lecturer = lecturer
		self.has_pass = has_pass


########################################### GENERAL ITEMS FOR UI ##########################################################
	def get_sections(self):
		cursor = conn.cursor()
		section = list()
		sql = """ SELECT name FROM sections """ 

		try:
			cursor.execute(sql)
			display = cursor.fetchall()
			for item in display:
				section.append(item[0])
			return section
		except Exception as e:
			print(e)


########################################### STUDENTS PART #################################################################
	def add_student(self):
		cursor = conn.cursor()
		hashed_pass = self.sec.to_hash(self.password)
		student = (self.id_number, self.first_name, self.last_name, self.gender, self.username, hashed_pass, self.section)
		sql = """
				INSERT INTO student (id_number, first_name, last_name, gender, username, password,section)
				VALUES(?,?,?,?,?,?,?)  
			""" 

		try:
			cursor.execute(sql, student)
			conn.commit()

		except Exception as e:
			print(e)
		
	def update_student(self):
		cursor = conn.cursor()
		student = (self.id_number, self.first_name, 
                								self.last_name, 
                								self.gender, 
                								self.username,
                								self.section, 
                								self.current_id)
		sql = """UPDATE student SET id_number= ?, first_name = ?,
		 					last_name = ?, gender = ?, username = ?, section = ?
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

########################################### TEACHER PART ##################################################################
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

###########################################  TEACHER CLASS  PART ##########################################################

	def add_class(self):
		cursor = conn.cursor()

		if not self.has_pass:
			new_class = (self.course_name, self.course_code, self.expire_date, self.is_active, self.lecturer, self.section)
			sql = """
				INSERT INTO course (course_name, course_code, created_on, expire_date, is_active, lecturer, section)
				VALUES(?,?,julianday('now', 'localtime') ,julianday(?),?,?,?)  
			"""
		else:
			hashed_pass = self.sec.to_hash(self.password)
			new_class = (self.course_name, self.course_code, self.expire_date, self.is_active, self.lecturer, hashed_pass, self.section)
			sql = """
				INSERT INTO course (course_name, course_code, created_on, expire_date, is_active, lecturer, password, section)
				VALUES(?,?,julianday('now', 'localtime'),julianday(?),?,?,?,?)  
			"""
		try:
			cursor.execute(sql, new_class)
			conn.commit()
			
		except Exception as e:
			print(e)

	def view_all_class(self):
		cursor = conn.cursor()
		sql = """ SELECT c.id, c.course_name, c.course_code, date(c.created_on),
				 time(c.created_on), date(c.expire_date), time(c.expire_date), c.is_active, l.first_name, l.last_name
				 	FROM (course as c LEFT JOIN lecturer as l) 
				 		WHERE c.lecturer = '{}' AND l.id_number = c.lecturer ORDER BY c.id DESC""".format(self.id_number)

		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return display
		else:
			return False

	def view_select_class(self):
		cursor = conn.cursor()
		sql = """ SELECT c.id, c.course_name, c.course_code, date(c.expire_date),
				 time(c.expire_date), c.is_active,  date(c.created_on),
				 time(c.created_on),  date(c.updated_on),
				 time(c.updated_on), c.password, c.section
				 	FROM (course as c LEFT JOIN lecturer as l) 
				 		WHERE c.id = '{}'""".format(self.id_number)

		cursor.execute(sql)
		display = cursor.fetchone()

		if display:
			return display
		else:
			return False

	def delete_class(self):
		cursor = conn.cursor()
		sql = """DELETE FROM course WHERE id = '{}' AND lecturer = '{}'""".format(self.id_number, self.current_id)

		try:
			cursor.execute(sql)
			conn.commit()
			
		except Exception as e:
			print(e)

	def update_class(self):
		cursor = conn.cursor()
		if not self.has_pass:
			update_class = (self.course_name, self.course_code, self.expire_date, self.section, self.id_number)
			if self.is_active == False:
				sql = """UPDATE course SET course_name= ?, course_code = ?, expire_date = julianday(?),
					updated_on = julianday('now','localtime'), is_active = True, section = ?
	                WHERE id = ?"""
			else:
				sql = """UPDATE course SET course_name= ?, course_code = ?, expire_date = julianday(?),
				 updated_on = julianday('now','localtime'), section = ? WHERE id = ?"""
		
		else:
			hashed_pass = self.sec.to_hash(self.password)
			update_class = (self.course_name, self.course_code, self.expire_date, hashed_pass, self.section, self.id_number)
			if self.is_active == False:
				sql = """UPDATE course SET course_name= ?, course_code = ?, expire_date = julianday(?),
					updated_on = julianday('now','localtime'), is_active = True, password= ?, section = ?
	                WHERE id = ?"""
			else:
				sql = """UPDATE course SET course_name= ?, course_code = ?, expire_date = julianday(?), updated_on = julianday('now','localtime'),
						password = ?, section = ?
	                WHERE id = ?"""
			pass

		try:
			cursor.execute(sql, update_class)
			conn.commit()
		except Exception as e:
			print(e)

	def remove_class_password(self):
		cursor = conn.cursor()
		class_field = (self.id_number, self.current_id)

		sql = """UPDATE course SET password = Null WHERE id = ? AND lecturer = ?"""

		try:
			cursor.execute(sql, class_field)
			conn.commit()
		except Exception as e:
			print(e)

	def view_expired_classes(self):
		cursor = conn.cursor()
		sql = """ SELECT id FROM course WHERE is_active = False AND lecturer = '{}' """.format(self.id_number)

		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			for item in display:
				return item
		else:
			return False


'''class_name = 'Sample Course'
class_code = 'CSC123'
class_expire_datetime = '2021-06-06 13:06'
lecturer = '2018-0001'
section = 1

database = db(course_name=class_name, course_code=class_code, expire_date=class_expire_datetime, is_active=True,
								 lecturer=lecturer, has_pass=False, section=section)

database2 = db(id_number=8)
print(database2.view_select_class())


#database.add_class()
#Sample Course CSC123 2021-06-06 13:06 True 2018-0001 1'''