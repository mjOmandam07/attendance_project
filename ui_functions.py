import re
from app_main import *
from app_backend import *
from more_itertools import unique_everseen

class signUp_ui_functions(signUp_window):
	def buttons(self):
		self.ui.im_a_student.clicked.connect(self.signUp_buttons)
		self.ui.im_a_teacher.clicked.connect(self.signUp_buttons)
		self.ui.student_signUp.clicked.connect(self.signUp_buttons)
		self.ui.teacher_signUp.clicked.connect(self.signUp_buttons)

	def popups(self, category):
		msg = QMessageBox()
		
		if category == 'id_valid':
			msg.setWindowTitle("ERROR!")
			msg.setText("Please Enter a valid I.D Number")
			msg.setIcon(QMessageBox.Critical)

		elif category == 'id':
			msg.setWindowTitle("ERROR!")
			msg.setText("I.D Number already exist")
			msg.setIcon(QMessageBox.Critical)

		elif category == 'username':
			msg.setWindowTitle("ERROR!")
			msg.setText("Username already in use, please try another")
			msg.setIcon(QMessageBox.Critical)

		elif category == 'student_success':
			msg.setWindowTitle("Success!")
			msg.setText("Student Sign Up Complete!")
			msg.setIcon(QMessageBox.Information)

		elif category == 'teacher_success':
			msg.setWindowTitle("Success!")
			msg.setText("Teacher Sign Up Complete!")
			msg.setIcon(QMessageBox.Information)

		elif category == 'update_success':
			msg.setWindowTitle("Success!")
			msg.setText("Account Updated!")
			msg.setIcon(QMessageBox.Information)

		x = msg.exec_()



	def student_signup_validations(self):
		
		id_num = self.ui.student_id.text()
		username = self.ui.student_username.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_student_id():
			signUp_ui_functions.popups(self, "id")

		elif check_username.check_student_username():
			signUp_ui_functions.popups(self, "username")

		else:
			signUp_ui_functions.addStudent(self)



	def addStudent(self):
		fname = self.ui.student_fname.text().upper()
		lname = self.ui.student_lname.text().upper()
		id_num = self.ui.student_id.text()
		gender = self.ui.student_gender.currentText().upper()
		username = self.ui.student_username.text()
		password = self.ui.student_password.text()

		database = db(id_number = id_num, first_name = fname, last_name = lname, gender = gender,
					 username = username, password=password)

		database.add_student()

		signUp_ui_functions.popups(self, "student_success")


	def teacher_signup_validations(self):
		
		id_num = self.ui.teacher_id.text()
		username = self.ui.teacher_username.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_teacher_id():
			signUp_ui_functions.popups(self, "id")

		elif check_username.check_teacher_username():
			signUp_ui_functions.popups(self, "username")

		else:
			signUp_ui_functions.addTeacher(self)
			

	def addTeacher(self):
		fname = self.ui.teacher_fname.text().upper()
		lname = self.ui.teacher_lname.text().upper()
		id_num = self.ui.teacher_id.text()
		gender = self.ui.teacher_gender.currentText().upper()
		username = self.ui.teacher_username.text()
		password = self.ui.teacher_password.text()

		database = db(id_number = id_num, first_name = fname, last_name = lname,gender = gender,
					 username = username, password=password)

		database.add_teacher()

		signUp_ui_functions.popups(self, "teacher_success")
		

###########################     STUDENT DASHBOARD      ############################################
class student_dash_ui_functs(student_dashboard):
	def buttons(self):
		self.ui.student_home.clicked.connect(self.student_dash_buttons)
		self.ui.student_view_account.clicked.connect(self.student_dash_buttons)
		self.ui.student_edit.clicked.connect(self.student_dash_buttons)


	def view_student_account(self):
		fname = self.ui.student_fname_edit.setText(current_user[1])
		lname = self.ui.student_lname_edit.setText(current_user[2])
		id_num = self.ui.student_id_edit.setText(current_user[0])

		if current_user[3] == 'MALE':
			index = 1
		elif current_user[3] == 'FEMALE':
			index = 2

		gender = self.ui.student_gender_edit.setCurrentIndex(index)
		username = self.ui.student_username_edit.setText(current_user[4])
		password = self.ui.student_password_edit.setText(current_user[5])



	def student_edit_validations(self):
		
		id_num = self.ui.student_id_edit.text()
		username = self.ui.student_username_edit.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_student_id() and id_num != current_user[0]:
			signUp_ui_functions.popups(self, "id")

		elif check_username.check_student_username() and username != current_user[4]:
			signUp_ui_functions.popups(self, "username")

		else:
			student_dash_ui_functs.update_student(self)


	def update_student(self):
		fname = self.ui.student_fname_edit.text().upper()
		lname = self.ui.student_lname_edit.text().upper()
		id_num = self.ui.student_id_edit.text()
		gender = self.ui.student_gender_edit.currentText().upper()
		username = self.ui.student_username_edit.text()
		password = self.ui.student_password_edit.text()

		details = id_num, fname, lname, gender, username, password

		database = db(id_number = id_num, first_name = fname, last_name = lname, gender = gender, username = username, 
					password = password, current_id = current_user[0])


		database.update_student()

		current_user.clear()
		for item in details:
			current_user.append(item)

		signUp_ui_functions.popups(self, "update_success")

		self.disable_student_edit()

		


###########################     TEACHER DASHBOARD      ############################################
class teacher_dash_ui_functs(teacher_dashboard):
	def buttons(self):
		self.ui.teacher_home.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_view_account.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_view_students.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_edit.clicked.connect(self.teacher_dash_buttons)


	def view_teacher_account(self):
		fname = self.ui.teacher_fname_edit.setText(current_user[1])
		lname = self.ui.teacher_lname_edit.setText(current_user[2])
		id_num = self.ui.teacher_id_edit.setText(current_user[0])

		if current_user[3] == 'MALE':
			index = 1
		elif current_user[3] == 'FEMALE':
			index = 2

		gender = self.ui.teacher_gender_edit.setCurrentIndex(index)
		username = self.ui.teacher_username_edit.setText(current_user[4])
		password = self.ui.teacher_password_edit.setText(current_user[5])




	def teacher_edit_validations(self):
		
		id_num = self.ui.teacher_id_edit.text()
		username = self.ui.teacher_username_edit.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_teacher_id() and id_num != current_user[0]:
			signUp_ui_functions.popups(self, "id")

		elif check_username.check_teacher_username() and username != current_user[4]:
			signUp_ui_functions.popups(self, "username")

		else:
			teacher_dash_ui_functs.update_teacher(self)



	def update_teacher(self):
		fname = self.ui.teacher_fname_edit.text().upper()
		lname = self.ui.teacher_lname_edit.text().upper()
		id_num = self.ui.teacher_id_edit.text()
		gender = self.ui.teacher_gender_edit.currentText().upper()
		username = self.ui.teacher_username_edit.text()
		password = self.ui.teacher_password_edit.text()

		details = id_num, fname, lname, gender, username, password

		database = db(id_number = id_num, first_name = fname, last_name = lname, gender = gender, username = username, 
					password = password, current_id = current_user[0])


		database.update_teacher()

		current_user.clear()
		for item in details:
			current_user.append(item)

		signUp_ui_functions.popups(self, "update_success")

		self.disable_teacher_edit()


	def view_student_list(self):
		entry = self.ui.search_student_lineEdit.text()
		database = db()
		display = database.view_all_students()
		self.ui.student_count.setText(str(len(display)))
		data = []
		searched = []
		for row in display:
			n = (str(row[0]), row[1], row[2])
			data.append(list(n))

		self.ui.treeWidget.clear()
		for row in data:
			for field in row:
				if entry.lower() in field.lower():
					searched.append(row)
		n = list(unique_everseen(searched))

		for i in n:
			self.ui.treeWidgetItem(self.ui.treeWidget, [i[0], i[1], i[2]])