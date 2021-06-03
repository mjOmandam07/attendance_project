import re
import secrets
from datetime import datetime, date, timedelta
from app_main import *
from app_backend import *
from more_itertools import unique_everseen



class login_signUp_ui_functions(login_signUp_window):
	def buttons(self):
		############# Page toggler buttons (login to sign up)#######################
		self.ui.to_login.clicked.connect(self.login_signup_toggler)
		self.ui.to_sign_up.clicked.connect(self.login_signup_toggler)

		############# Sign Up buttons ##################################
		self.ui.im_a_student.clicked.connect(self.signUp_buttons)
		self.ui.im_a_teacher.clicked.connect(self.signUp_buttons)
		self.ui.student_signUp.clicked.connect(self.signUp_buttons)
		self.ui.teacher_signUp.clicked.connect(self.signUp_buttons)
		#############################################################

		############# Login Buttons ####################################
		self.ui.login_im_a_student.clicked.connect(self.login_buttons)
		self.ui.login_im_a_teacher.clicked.connect(self.login_buttons)
		self.ui.student_login_btn.clicked.connect(self.login_buttons)
		self.ui.teacher_login_btn.clicked.connect(self.login_buttons)
		################################################################

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

		elif category == 'login_error':
			msg.setWindowTitle("ERROR!")
			msg.setText("Wrong password or username")
			msg.setIcon(QMessageBox.Critical)

		elif category == 'password_error':
			msg.setWindowTitle("ERROR!")
			msg.setText("Password does not match")
			msg.setIcon(QMessageBox.Critical)

		elif category == 'add_class_success':
			msg.setWindowTitle("Success!")
			msg.setText("Class Added!")
			msg.setIcon(QMessageBox.Information)

		elif category == 'class_updated':
			msg.setWindowTitle("Success!")
			msg.setText("Class Updated")
			msg.setIcon(QMessageBox.Information)

		elif category == 'class_deleted':
			msg.setWindowTitle("Success!")
			msg.setText("Class Deleted")
			msg.setIcon(QMessageBox.Information)


		x = msg.exec_()

	def student_signup_validations(self):
		
		id_num = self.ui.student_id.text()
		username = self.ui.student_username.text()
		password = self.ui.student_password.text()
		confirm_password = self.ui.student_confirm_pass_signUp.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			login_signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_student_id():
			login_signUp_ui_functions.popups(self, "id")

		elif check_username.check_student_username():
			login_signUp_ui_functions.popups(self, "username")

		elif password != confirm_password:
			login_signUp_ui_functions.popups(self, 'password_error')
			self.ui.student_confirm_pass_signUp.clear()
			self.ui.student_password.clear()

		else:
			login_signUp_ui_functions.addStudent(self)

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

		login_signUp_ui_functions.popups(self, "student_success")

	def teacher_signup_validations(self):
		
		id_num = self.ui.teacher_id.text()
		username = self.ui.teacher_username.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)

		password = self.ui.teacher_password.text()
		confirm_password = self.ui.teacher_confirm_pass_signUp.text()


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			login_signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_teacher_id():
			login_signUp_ui_functions.popups(self, "id")

		elif check_username.check_teacher_username():
			login_signUp_ui_functions.popups(self, "username")

		elif password != confirm_password:
			login_signUp_ui_functions.popups(self, 'password_error')
			self.ui.teacher_confirm_pass_signUp.clear()
			self.ui.teacher_password.clear()

		else:
			login_signUp_ui_functions.addTeacher(self)
			
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

		login_signUp_ui_functions.popups(self, "teacher_success")

	def login_student(self):
		current_user.clear()
		secr = secrets.Secreto()
		username = self.ui.student_login_username.text()
		password = secr.to_process(self.ui.student_login_password.text())

		database = db(username=username)

		user_to_confirm = database.login_student()
		if user_to_confirm:
			if password:
				if secr.check_hash(password, user_to_confirm[6]):
					for item in user_to_confirm:
						current_user.append(item)
					self.to_student_dashboard()
				else:
					login_signUp_ui_functions.popups(self, "login_error")
					self.ui.student_login_password.clear()
		else:
			login_signUp_ui_functions.popups(self, "login_error")
			self.ui.student_login_password.clear()

	def login_teacher(self):
		current_user.clear()
		secr = secrets.Secreto()
		username = self.ui.teacher_login_username.text()
		password = secr.to_process(self.ui.teacher_login_password.text())

		database = db(username=username)


		user_to_confirm = database.login_teacher()
		if user_to_confirm:
			if password:
				if secr.check_hash(password, user_to_confirm[6]):
					for item in user_to_confirm:
						current_user.append(item)
					self.to_teacher_dashboard()
				else:
					login_signUp_ui_functions.popups(self, "login_error")
					self.ui.teacher_login_password.clear()
		else:
			login_signUp_ui_functions.popups(self, "login_error")
			self.ui.teacher_login_password.clear()
		
###########################     STUDENT DASHBOARD      ############################################
class student_dash_ui_functs(student_dashboard):
	def buttons(self):
		self.ui.student_home.clicked.connect(self.student_dash_buttons)
		self.ui.student_view_account.clicked.connect(self.student_dash_buttons)
		self.ui.student_edit.clicked.connect(self.student_dash_buttons)
		self.ui.student_change_pass.clicked.connect(self.student_dash_buttons)
		self.ui.student_logout.clicked.connect(self.student_dash_buttons)

	def view_student_account(self):
		fname = self.ui.student_fname_edit.setText(current_user[2])
		lname = self.ui.student_lname_edit.setText(current_user[3])
		id_num = self.ui.student_id_edit.setText(current_user[1])

		if current_user[4] == 'MALE':
			index = 1
		elif current_user[4] == 'FEMALE':
			index = 2

		gender = self.ui.student_gender_edit.setCurrentIndex(index)
		username = self.ui.student_username_edit.setText(current_user[5])

	def student_edit_validations(self):
		
		id_num = self.ui.student_id_edit.text()
		username = self.ui.student_username_edit.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			login_signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_student_id() and id_num != current_user[1]:
			login_signUp_ui_functions.popups(self, "id")

		elif check_username.check_student_username() and username != current_user[5]:
			login_signUp_ui_functions.popups(self, "username")

		else:
			student_dash_ui_functs.update_student(self)

	def update_student(self):
		fname = self.ui.student_fname_edit.text().upper()
		lname = self.ui.student_lname_edit.text().upper()
		id_num = self.ui.student_id_edit.text()
		gender = self.ui.student_gender_edit.currentText().upper()
		username = self.ui.student_username_edit.text()
		password = self.ui.student_password_edit.text()

		if not password:
			password = current_user[6]

		details = id_num, fname, lname, gender, username, password

		database = db(id_number = id_num, first_name = fname, last_name = lname, gender = gender, username = username, 
					password = password, current_id = current_user[1])

		login_back = db(unique_id = current_user[0])


		database.update_student()
		logged_back = login_back.login_student_back()

		current_user.clear()
		for item in logged_back:
			current_user.append(item)

		login_signUp_ui_functions.popups(self, "update_success")
		print(current_user)

		self.disable_student_edit()

	def student_update_pass(self):
		if self.ui.student_new_pass.text() != self.ui.student_confirm_new_pass.text():
			login_signUp_ui_functions.popups(self, 'password_error')
			self.ui.student_confirm_new_pass.clear()
			self.ui.student_new_pass.clear()
		else:
			database = db(password = self.ui.student_confirm_new_pass.text(), current_id = current_user[1])
			database.update_student_password()

			login_signUp_ui_functions.popups(self, "update_success")

			student_update_password.closeWindow(self)

###########################     TEACHER DASHBOARD      ############################################
class teacher_dash_ui_functs(teacher_dashboard):
	def buttons(self):
		self.ui.teacher_home.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_view_account.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_view_students.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_edit.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_change_pass.clicked.connect(self.teacher_dash_buttons)
		self.ui.teacher_logout.clicked.connect(self.teacher_dash_buttons)
		self.ui.add_class.clicked.connect(self.teacher_dash_buttons)
		
	def view_teacher_account(self):
		fname = self.ui.teacher_fname_edit.setText(current_user[2])
		lname = self.ui.teacher_lname_edit.setText(current_user[3])
		id_num = self.ui.teacher_id_edit.setText(current_user[1])

		if current_user[4] == 'MALE':
			index = 1
		elif current_user[4] == 'FEMALE':
			index = 2

		gender = self.ui.teacher_gender_edit.setCurrentIndex(index)
		username = self.ui.teacher_username_edit.setText(current_user[5])
		
	def teacher_edit_validations(self):
		
		id_num = self.ui.teacher_id_edit.text()
		username = self.ui.teacher_username_edit.text()

		check_username = db(username = username)
		check_id = db(id_number = id_num)


		if not re.match(r'^[0-9]{4}-[0-9]{4}$', id_num):
			login_signUp_ui_functions.popups(self, "id_valid")

		elif check_id.check_teacher_id() and id_num != current_user[1]:
			login_signUp_ui_functions.popups(self, "id")

		elif check_username.check_teacher_username() and username != current_user[5]:
			login_signUp_ui_functions.popups(self, "username")

		else:
			teacher_dash_ui_functs.update_teacher(self)

	def update_teacher(self):
		fname = self.ui.teacher_fname_edit.text().upper()
		lname = self.ui.teacher_lname_edit.text().upper()
		id_num = self.ui.teacher_id_edit.text()
		gender = self.ui.teacher_gender_edit.currentText().upper()
		username = self.ui.teacher_username_edit.text()

		details = id_num, fname, lname, gender, username

		database = db(id_number = id_num, first_name = fname, last_name = lname, gender = gender, username = username, current_id = current_user[1])


		database.update_teacher()

		login_back = db(unique_id = current_user[0])


		database.update_student()
		logged_back = login_back.login_teacher_back()

		current_user.clear()
		for item in logged_back[:6]:
			current_user.append(item)

		login_signUp_ui_functions.popups(self, "update_success")
		self.disable_teacher_edit()

	def teacher_update_pass(self):
		if self.ui.teacher_new_pass.text() != self.ui.teacher_confirm_new_pass.text():
			login_signUp_ui_functions.popups(self, 'password_error')
			self.ui.teacher_confirm_new_pass.clear()
			self.ui.teacher_new_pass.clear()
		else:
			database = db(password = self.ui.teacher_confirm_new_pass.text(), current_id = current_user[1])
			database.update_teacher_password()

			login_signUp_ui_functions.popups(self, "update_success")

			teacher_update_password.closeWindow(self)

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

	def get_selected_student(self):
		getSelected = self.ui.treeWidget.selectedItems()
		database = db()
		display = database.view_all_students()
		if getSelected:
			baseNode = getSelected[0]
			getChildNode = baseNode.text(0)
			for i in display:
				if i[0] == getChildNode:
					self.ui.student_list_fname.setText(str(i[2]))
					self.ui.student_list_lname.setText(str(i[1]))
					self.ui.student_list_id.setText(str(i[0]))
					self.ui.student_list_gender.setText(str(i[3]))

	def add_new_class(self):
		class_name = self.ui.course_name.text()
		class_code = self.ui.course_code.text()
		class_expire_date = self.ui.course_expire_date.date().toString('yyyy-MM-dd')
		class_expire_time = self.ui.course_expire_time.text()


		time = datetime.strptime(class_expire_time, "%I:%M %p")
		new_format_time = datetime.strftime(time, "%H:%M")

		class_expire_datetime = class_expire_date + " " +  new_format_time

		database = db(course_name=class_name, course_code=class_code, expire_date=class_expire_datetime, is_active=True, lecturer=current_user[1])
		database.add_class()

		login_signUp_ui_functions.popups(self, "add_class_success")

	def get_classes(self):
		database = db(id_number=current_user[1])
		display = database.view_all_class()

		return display

	def del_class(self, id_num):
		database = db(id_number = id_num, current_id=current_user[1])
		database.delete_class()

		login_signUp_ui_functions.popups(self, "class_deleted")

	def update_class(self, id_num, status, current_exp_datetime):
		class_name = self.ui.update_course_name.text()
		class_code = self.ui.update_course_code.text()
		class_expire_date = self.ui.update_course_expire_date.date().toString('yyyy-MM-dd')
		class_expire_time = self.ui.update_course_expire_time.text()


		time = datetime.strptime(class_expire_time, "%I:%M %p")
		new_format_time = datetime.strftime(time, "%H:%M")
		class_expire_datetime = class_expire_date + " " +  new_format_time

		if status == 0 and  current_exp_datetime != class_expire_datetime:
			database = db(course_name=class_name, course_code=class_code, expire_date=class_expire_datetime, id_number=id_num, is_active=False)
		else:
			database = db(course_name=class_name, course_code=class_code, expire_date=class_expire_datetime, id_number=id_num)
		
		database.update_class()
		login_signUp_ui_functions.popups(self, "class_updated")


