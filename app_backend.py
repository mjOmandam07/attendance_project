import sqlite3
import secrets

conn = sqlite3.connect('attendance.db')


class db(object):
	def __init__(self, id_number=None, first_name=None, last_name=None,
						gender=None, username=None, password=None,
						current_id=None, unique_id=None,
						course_name=None, course_code=None, created_on=None,
						expire_date=None, is_active=None, lecturer=None, current_datetime = None,
						has_pass=None, section=None, class_filter=None):

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

		self.class_filter = class_filter


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

		sql = ''' SELECT s.id, s.id_number, s.first_name, s.last_name,
					s.gender, s.username, s.password, s.section, sec.name  FROM (student as s LEFT JOIN sections as sec)
						 WHERE username=? and s.section=sec.id '''
		cur = conn.cursor()
		try:
			cur.execute(sql, (username,))
			data = cur.fetchone()
			if data:
				return data
			else:
				return False
		except Exception as e:
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

	def student_classes(self):
		cursor = conn.cursor()
		if self.class_filter == 'active':
			sql = """ SELECT c.id, c.course_name, c.course_code, date(c.created_on),
					 time(c.created_on), date(c.expire_date), time(c.expire_date), c.is_active, l.first_name, l.last_name
					 	FROM (course as c LEFT JOIN lecturer as l) 
					 		WHERE  c.section = '{}' AND c.is_active = 1 AND c.lecturer = l.id_number ORDER BY c.id DESC""".format(self.section)
		else:
			sql = """ SELECT c.id, c.course_name, c.course_code, date(c.created_on),
					 time(c.created_on), date(c.expire_date), time(c.expire_date), c.is_active, l.first_name, l.last_name
					 	FROM (course as c LEFT JOIN lecturer as l) 
					 		WHERE  c.section = '{}' AND c.is_active = 0 AND
					 			date(c.expire_date) = '{}' AND c.lecturer = l.id_number ORDER BY c.id DESC""".format(self.section, self.current_datetime)

		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return display
		else:
			return False

	def add_attendance(self):
		cursor = conn.cursor()
		info = (self.id_number, self.current_id, self.section, self.lecturer, self.course_name, self.course_code)
		sql = """
				INSERT INTO attendance (course_id, student_id, is_present, section, lecturer_id, time_joined, subject_name, subject_code)
				VALUES(?,?,True,?,?,julianday('now', 'localtime'),?,?)  
			""" 

		try:
			cursor.execute(sql, info)
			conn.commit()
		except Exception as e:
			print(e)

	def check_if_present(self):
		cursor = conn.cursor()
		sql = """SELECT is_present FROM attendance 
					WHERE student_id = '{}' AND section = '{}'
					 AND course_id = '{}' AND lecturer_id = '{}'""".format(self.current_id, self.section, self.id_number, self.lecturer)

		cursor.execute(sql)
		display = cursor.fetchone()

		if display:
			return display
		else:
			False

	def view_student_attendance(self):
		cursor = conn.cursor()
		sql = """
				SELECT c.course_name, c.course_code, l.first_name, l.last_name, a.student_id, datetime(a.time_joined), a.is_present
	 					FROM (((attendance as a JOIN course as c ON a.course_id = c.id)
	 							JOIN student as s ON s.id_number = a.student_id) JOIN lecturer as l ON a.lecturer_id = l.id_number)
	 							WHERE s.id_number = '{}' and is_present = True """.format(self.current_id)

		try:
			cursor.execute(sql)
			display = cursor.fetchall()
			return display
		except Exception as e:
			print(e)


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
		sql = """ SELECT id_number, last_name, first_name, gender FROM student WHERE section = '{}'""".format(self.section)

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

	def attendance_view_all_class(self):
		cursor = conn.cursor()
		sql = """ SELECT c.id, c.course_name, c.course_code
				 	FROM (course as c LEFT JOIN lecturer as l) 
				 		WHERE c.lecturer = '{}' AND c.is_active = 1 AND l.id_number = c.lecturer""".format(self.id_number)

		cursor.execute(sql)
		display = cursor.fetchall()

		if display:
			return display
		else:
			return False

	def attendance_view_all_expired_class(self):
		cursor = conn.cursor()
		sql = """ SELECT c.id, c.course_name, c.course_code
				 	FROM (course as c LEFT JOIN lecturer as l) 
				 		WHERE c.lecturer = '{}' AND c.is_active = 0 AND l.id_number = c.lecturer""".format(self.id_number)

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
				 time(c.updated_on), c.password, c.section, l.first_name, l.last_name, l.id_number
				 	FROM (course as c LEFT JOIN lecturer as l) 
				 		WHERE c.id = '{}' AND l.id_number = c.lecturer""".format(self.id_number)

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

	def view_teacher_attendance(self):
		cursor = conn.cursor()
		sql = """
				SELECT s.id_number, s.first_name, s.last_name,  datetime(a.time_joined), a.is_present
	 					FROM (((attendance as a LEFT JOIN student as s ON s.id_number = a.student_id)
	 						 LEFT JOIN lecturer as l ON l.id_number = a.lecturer_id)
	 						 	LEFT JOIN course as c ON c.id = a.course_id)
	 							WHERE a.lecturer_id = '{}' AND c.id = '{}' AND is_present = True """.format(self.current_id, self.id_number)

		try:
			cursor.execute(sql)
			display = cursor.fetchall()
			return display
		except Exception as e:
			print(e)

	def view_all_attendance(self):
		cursor = conn.cursor()
		sql = """
				SELECT s.id_number, s.first_name, s.last_name, a.subject_name, a.subject_code, c.is_active,  datetime(a.time_joined), a.is_present
	 					FROM (((attendance as a LEFT JOIN student as s ON s.id_number = a.student_id)
	 						 LEFT JOIN lecturer as l ON l.id_number = a.lecturer_id)
	 						 	LEFT JOIN course as c ON c.id = a.course_id)
	 							WHERE a.lecturer_id = '{}' """.format(self.current_id)

		try:
			cursor.execute(sql)
			display = cursor.fetchall()
			return display
		except Exception as e:
			print(e)