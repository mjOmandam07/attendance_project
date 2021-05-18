import sqlite3
import secrets


class Database(object):
	def __init__(self, id_number=None, first_name=None, last_name=None, gender=None, username=None, password=None, current_id=None, unique_id=None):
		super(Database, self).__init__()
		
		self.unique_id = unique_id
		self.id_number = id_number
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.gender = gender
		self.current_id = current_id
		self.sec = secrets.Secreto()

	@classmethod
	def all(cls):
		conn = sqlite3.connect("attendance.db")
		cur = conn.cursor()
		cur.execute('SELECT * FROM student')
		data = cur.fetchall()
		cur.close()
		return data

	def createacc_student(self):
		conn = sqlit3.connect("attendance.db")
		cur = conn.cursor()
		cur.execute('INSERT INTO student(id_number, first_name, last_name, gender, username, password) VALUES(?, ?, ?, ?, ?, ?)', (self.id_number, self.first_name, self.last_name,self.gender, self.username, self.password))
		conn.commit()

	def login_student(self):
		username = self.username
		conn = sqlite3.connect("attendance.db")
		cur = conn.cursor()
		conn.row_factory = sqlite3.Row
		sql = ''' SELECT * FROM student WHERE username=?'''
		try:
			cur.execute(sql, (username,))
			data = cur.fetchone()
			if data:
				return data
			else:
				return False
		except Error as e:
			print(e)
