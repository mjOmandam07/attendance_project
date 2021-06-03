import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

from login_signUp import Ui_MainWindow

from student_dashboard import Ui_student_dash
from teacher_dashboard import Ui_teacher_dash

from teacher_change_password import Ui_teacher_change_pass
from student_change_password import Ui_student_change_pass

from add_class import Ui_create_class
from view_class import Ui_view_class


import teacher_dynamic_widgets as dynamic
from teacher_dynamic_widgets import widgets, expired_class

from class_threads import *

from ui_functions import *

from  logged_user import current_user

global main_window




class login_signUp_window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


		login_signUp_ui_functions.buttons(self)

		self.ui.student_signUp.setDisabled(True)
		self.ui.student_fname.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_lname.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_id.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_gender.currentIndexChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_username.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_password.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_confirm_pass_signUp.textChanged['QString'].connect(self.disable_student_SignUp)

		self.ui.teacher_signUp.setDisabled(True)
		self.ui.teacher_fname.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_lname.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_id.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_gender.currentIndexChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_username.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_password.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_confirm_pass_signUp.textChanged['QString'].connect(self.disable_teacher_SignUp)

		self.ui.student_login_btn.setDisabled(True)
		self.ui.student_login_username.textChanged['QString'].connect(self.disable_student_login)
		self.ui.student_login_password.textChanged['QString'].connect(self.disable_student_login)

		self.ui.teacher_login_btn.setDisabled(True)
		self.ui.teacher_login_username.textChanged['QString'].connect(self.disable_teacher_login)
		self.ui.teacher_login_password.textChanged['QString'].connect(self.disable_teacher_login)
		self.show()


	def login_signup_toggler(self):
		btnWidget = self.sender()
		btn_name = btnWidget.objectName()

		if btn_name == 'to_login':
			self.ui.welcome_stackedWidget.setCurrentWidget(self.ui.login_page)
		elif btn_name == 'to_sign_up':
			self.ui.welcome_stackedWidget.setCurrentWidget(self.ui.sign_up_page)

	def login_buttons(self):
		btnWidget = self.sender() # RETURNS THE BUTTON PRESSED
		btn_name = btnWidget.objectName() # RETURNS THE 'NAME' OF THE BUTTON PRESSED
		
		if btn_name == 'login_im_a_teacher':
			self.ui.login_stackedWidget.setCurrentWidget(self.ui.login_teacher_page)
		elif btn_name == 'login_im_a_student':
			self.ui.login_stackedWidget.setCurrentWidget(self.ui.login_student_page)
		elif btn_name == 'student_login_btn':
			login_signUp_ui_functions.login_student(self)
		elif btn_name == 'teacher_login_btn':
			login_signUp_ui_functions.login_teacher(self)


	def disable_student_login(self):
		if self.ui.student_login_username.text() and self.ui.student_login_password.text():
			self.ui.student_login_btn.setDisabled(False)
		else:
			self.ui.student_login_btn.setDisabled(True)

	def disable_teacher_login(self):
		if self.ui.teacher_login_username.text() and self.ui.teacher_login_password.text():
			self.ui.teacher_login_btn.setDisabled(False)
		else:
			self.ui.teacher_login_btn.setDisabled(True)

	def signUp_buttons(self):
		btnWidget = self.sender() # RETURNS THE BUTTON PRESSED
		btn_name = btnWidget.objectName() # RETURNS THE 'NAME' OF THE BUTTON PRESSED

		if btn_name == 'im_a_teacher':
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_10)
		elif btn_name == 'im_a_student':
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_9)
		elif btn_name == 'student_signUp':
			login_signUp_ui_functions.student_signup_validations(self)
		elif btn_name == 'teacher_signUp':
			login_signUp_ui_functions.teacher_signup_validations(self)

	def disable_student_SignUp(self):
		fname = self.ui.student_fname.text()
		lname = self.ui.student_lname.text()
		id_num = self.ui.student_id.text()
		if self.ui.student_gender.currentText() == 'Select':
			gender = None
		else:
			gender = self.ui.student_gender.currentText()

		username = self.ui.student_username.text()
		password = self.ui.student_password.text()
		confirm_password = self.ui.student_confirm_pass_signUp.text()

		if fname and lname and id_num and gender and username and password and confirm_password:
			self.ui.student_signUp.setDisabled(False)
		else:
			self.ui.student_signUp.setDisabled(True)

	def disable_teacher_SignUp(self):
		fname = self.ui.teacher_fname.text()
		lname = self.ui.teacher_lname.text()
		id_num = self.ui.teacher_id.text()
		if self.ui.teacher_gender.currentText() == 'Select':
			gender = None
		else:
			gender = self.ui.teacher_gender.currentText()

		username = self.ui.teacher_username.text()
		password = self.ui.teacher_password.text()
		confirm_password = self.ui.teacher_confirm_pass_signUp.text()

		if fname and lname and id_num and gender and username and password and confirm_password:
			self.ui.teacher_signUp.setDisabled(False)
		else:
			self.ui.teacher_signUp.setDisabled(True)

	def to_student_dashboard(self):
		global main_window
		main_windw = student_dashboard()
		main_window.show()
		self.close()

	def to_teacher_dashboard(self):
		global main_window
		main_window = teacher_dashboard()
		main_window.show()
		self.close()

###########################     STUDENT DASHBOARD      ############################################
class student_dashboard(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_student_dash()
		self.ui.setupUi(self)


		student_dash_ui_functs.buttons(self)

		self.ui.current_user_name.setText(current_user[2])

		self.ui.student_edit.setDisabled(True)
		self.ui.student_fname_edit.textChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_lname_edit.textChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_id_edit.textChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_gender_edit.currentIndexChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_username_edit.textChanged['QString'].connect(self.disable_student_edit)
		
		self.show()


	def student_dash_buttons(self):
		btnWidget = self.sender() # RETURNS THE BUTTON PRESSED
		btn_name = btnWidget.objectName() # RETURNS THE 'NAME' OF THE BUTTON PRESSED


		if btn_name == 'student_home':
			self.ui.stackedWidget.setCurrentWidget(self.ui.student_home_page)
		elif btn_name == 'student_view_account':
			self.ui.stackedWidget.setCurrentWidget(self.ui.student_account_page)
			student_dash_ui_functs.view_student_account(self)
		elif btn_name == 'student_edit':
			student_dash_ui_functs.student_edit_validations(self)
		elif btn_name == 'student_change_pass':
			self.main = student_update_password()
			self.main.show()
		elif btn_name == 'student_logout':
			reply = QMessageBox.question(self, 'Log Out', 'Are you sure you want to logout?',
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

			if reply == QMessageBox.Yes:
				self.main = login_signUp_window()
				self.main.show()
				current_user.clear()
				self.close()
			

	def disable_student_edit(self):
		self.ui.current_user_name.setText(current_user[2])
		fname = self.ui.student_fname_edit.text().upper()
		lname = self.ui.student_lname_edit.text().upper()
		id_num = self.ui.student_id_edit.text()
		if self.ui.student_gender_edit.currentText() == 'Select':
			gender = None
		else:
			gender = self.ui.student_gender_edit.currentText().upper()

		username = self.ui.student_username_edit.text()



		if (fname == current_user[2] and lname == current_user[3] 
				and id_num == current_user[1] and gender == current_user[4]
					and username == current_user[5]):
				self.ui.student_edit.setDisabled(True)

		elif fname and lname and id_num and gender and username:
			self.ui.student_edit.setDisabled(False)

			
		else:
			self.ui.student_edit.setDisabled(True)

###########################     TEACHER DASHBOARD      ############################################
class teacher_dashboard(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_teacher_dash()
		self.ui.setupUi(self)

		self.ui.treeWidgetItem = QtWidgets.QTreeWidgetItem

		teacher_dash_ui_functs.buttons(self)
		teacher_dash_ui_functs.view_student_list(self)

		self.ui.current_user_name.setText(current_user[2])
		self.ui.teacher_edit.setDisabled(True)
		self.ui.top_notify.hide()
		self.ui.teacher_fname_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_lname_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_id_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_gender_edit.currentIndexChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_username_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		
		self.ui.search_student_lineEdit.textChanged['QString'].connect(lambda:teacher_dash_ui_functs.view_student_list(self))

		self.ui.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
            lambda: teacher_dash_ui_functs.get_selected_student(self))


		self.teacher_classes()
		thread_starters.start_check_class(self, 'start')
		self.show()

	def update_class_ui(self, status):
		if status:
			self.ui.top_notify.show()
			#self.teacher_classes()
		elif not status and expired_class:
			self.ui.top_notify.show()
			expired_class.clear()
			#self.teacher_classes()
		elif not status and not expired_class:
			database = db(id_number=current_user[1])
			display = database.view_expired_classes()
			if display:
				for item in display:
					expired_class.append(item)
			else:
				self.ui.top_notify.hide()
				#self.teacher_classes()
		else:
			self.ui.top_notify.close()
			#self.teacher_classes()
		

	def teacher_dash_buttons(self):
		btnWidget = self.sender() # RETURNS THE BUTTON PRESSED
		btn_name = btnWidget.objectName() # RETURNS THE 'NAME' OF THE BUTTON PRESSED

		if btn_name == 'teacher_home':
			self.ui.stackedWidget.setCurrentWidget(self.ui.teacher_home_page)
		elif btn_name == 'teacher_view_account':
			self.ui.stackedWidget.setCurrentWidget(self.ui.teacher_account_page)
			teacher_dash_ui_functs.view_teacher_account(self)
		elif btn_name == 'teacher_view_students':
			self.ui.stackedWidget.setCurrentWidget(self.ui.view_students_page)
		elif btn_name == 'teacher_edit':
			teacher_dash_ui_functs.teacher_edit_validations(self)
		elif btn_name == 'teacher_change_pass':
			self.main = teacher_update_password()
			self.main.show()
		elif btn_name == 'teacher_logout':
			reply = QMessageBox.question(self, 'Log Out', 'Are you sure you want to logout?',
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

			if reply == QMessageBox.Yes:
				self.main = login_signUp_window()
				self.main.show()
				current_user.clear()
				self.close()

		elif btn_name == 'add_class':
			self.main = add_class_window()
			self.main.show()

	def teacher_home_page(self, status):
		if status == 0:
			exec(dynamic.noClass())	
		else:
			exec(dynamic.has_class())

	def teacher_open_view_class(self, id_num):
		self.main = view_class_window()
		self.main.show()
		view_class_window.display_details(self, id_num)

	def teacher_classes(self):
		classes = teacher_dash_ui_functs.get_classes(self)
		if classes and not widgets:
			self.teacher_home_page(1)
			exec(dynamic.clear_scrollArea())
			for item in classes:
				exec(dynamic.add_widget())
			for w in self.ui.teacher_home_page.findChildren(QScrollArea):
				w = w.objectName()
			widgets.append(w)	
		elif classes and widgets:
			exec(dynamic.clear_scrollArea())
			for item in classes:
				exec(dynamic.add_widget())
		else:
			widgets.clear()
			self.teacher_home_page(0)

	def view_class_buttons(self):
		btnWidget = self.sender()
		btn_name = btnWidget.objectName()

		self.teacher_open_view_class(btn_name)
			
	def disable_teacher_edit(self):
		self.ui.current_user_name.setText(current_user[2])
		fname = self.ui.teacher_fname_edit.text().upper()
		lname = self.ui.teacher_lname_edit.text().upper()
		id_num = self.ui.teacher_id_edit.text()
		if self.ui.teacher_gender_edit.currentText() == 'Select':
			gender = None
		else:
			gender = self.ui.teacher_gender_edit.currentText().upper()

		username = self.ui.teacher_username_edit.text()


		if (fname == current_user[2] and lname == current_user[3] 
				and id_num == current_user[1] and gender == current_user[4]
					and username == current_user[5]):
				self.ui.teacher_edit.setDisabled(True)

		elif fname and lname and id_num and gender and username:
			self.ui.teacher_edit.setDisabled(False)

			
		else:
			self.ui.teacher_edit.setDisabled(True)
	
###########################     TEACHER CHANGE PASSWORD WINDOW ####################################
class teacher_update_password(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_teacher_change_pass()
		self.ui.setupUi(self)
		self.modal = self.setWindowModality(QtCore.Qt.ApplicationModal)

		self.ui.teacher_change_pass_btn.setDisabled(True)

		self.ui.teacher_new_pass.textChanged['QString'].connect(self.disable_update_pass_btn)
		self.ui.teacher_confirm_new_pass.textChanged['QString'].connect(self.disable_update_pass_btn)

		self.ui.teacher_change_pass_btn.clicked.connect(lambda: teacher_dash_ui_functs.teacher_update_pass(self))

	def disable_update_pass_btn(self):
		if self.ui.teacher_new_pass.text() and self.ui.teacher_confirm_new_pass.text():
			self.ui.teacher_change_pass_btn.setDisabled(False)

		else:
			self.ui.teacher_change_pass_btn.setDisabled(True)

	def closeWindow(self):
		self.close()

###########################     STUDENT CHANGE PASSWORD WINDOW ####################################
class student_update_password(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_student_change_pass()
		self.ui.setupUi(self)
		self.modal = self.setWindowModality(QtCore.Qt.ApplicationModal)

		self.ui.student_change_pass_btn.setDisabled(True)

		self.ui.student_new_pass.textChanged['QString'].connect(self.disable_update_pass_btn)
		self.ui.student_confirm_new_pass.textChanged['QString'].connect(self.disable_update_pass_btn)

		self.ui.student_change_pass_btn.clicked.connect(lambda: student_dash_ui_functs.student_update_pass(self))

	def disable_update_pass_btn(self):
		if self.ui.student_new_pass.text() and self.ui.student_confirm_new_pass.text():
			self.ui.student_change_pass_btn.setDisabled(False)

		else:
			self.ui.student_change_pass_btn.setDisabled(True)

	def closeWindow(self):
		self.close()

###########################     TEACHER ADD CLASS 	   ############################################
class add_class_window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_create_class()
		self.ui.setupUi(self)
		self.modal = self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.ui.course_expire_date.setDateTime(QtCore.QDateTime.currentDateTime())

		self.ui.course_expire_date.setDisplayFormat("dd MMM yyyy")
		today = QtCore.QDate.currentDate()
		self.ui.course_expire_date.setMinimumDate(today)

		self.ui.add_course.clicked.connect(self.store_data)

		self.ui.course_name.textChanged['QString'].connect(self.disable_add_class)
		self.ui.course_code.textChanged['QString'].connect(self.disable_add_class)
		self.ui.add_course.setDisabled(True)
		self.show()
	
	def store_data(self):
		#thread_starters.start_check_class(self, 'stop')
		teacher_dash_ui_functs.add_new_class(self)
		self.close()
		main_window.teacher_classes()


	def disable_add_class(self):
		course_name = self.ui.course_name.text()
		course_code = self.ui.course_code.text()

		if course_name and course_code:
			self.ui.add_course.setDisabled(False)
		else:
			self.ui.add_course.setDisabled(True)

###########################     TEACHER VIEW CLASS 	   ############################################
class view_class_window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_view_class()
		self.ui.setupUi(self)
		self.modal = self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.ui.update_course_expire_date.setDateTime(QtCore.QDateTime.currentDateTime())

		self.ui.update_course_expire_date.setDisplayFormat("dd MMM yyyy")
		today = QtCore.QDate.currentDate()
		self.ui.update_course_expire_date.setMinimumDate(today)

		self.ui.delete_course.clicked.connect(self.delete_class)

		self.ui.update_course_name.textChanged['QString'].connect(self.disable_update_class)
		self.ui.update_course_code.textChanged['QString'].connect(self.disable_update_class)
		self.ui.update_course_expire_date.dateChanged.connect(self.disable_update_class)
		self.ui.update_course_expire_time.timeChanged.connect(self.disable_update_class)
		self.ui.update_course.setDisabled(True)

		self.ui.update_course.clicked.connect(self.update_class)


		self.show()
		

	def display_details(self, id_num):
		global class_id
		global status
		global current_expire_datetime
		class_id = id_num
		thread_starters.start_check_class(self, 'stop')
		database = db(id_number=int(class_id))
		display = database.view_select_class()
		code = display[2]
		name = display[1]
		date = display[3]
		time = display[4]

		exp_time = datetime.strptime(time, "%H:%M:%S")
		exp_time = datetime.strftime(exp_time, "%H:%M")
		current_expire_datetime = date + " " + exp_time

		create_date = display[6]
		create_time =display[7]
		update_date = display[8]
		update_time = display[9]
		status = display[5]

		if update_time:
			update_datetime = view_class_window.reformat_datetime(self, update_time, update_date, True)
			self.main.ui.course_updated_on.setText(f'{update_datetime[0]} {update_datetime[1]}')
		else:
			self.main.ui.label_10.hide()
			self.main.ui.course_updated_on.hide()
		if status == 1:
			self.main.ui.course_status.setText('ACTIVE')
		else:
			self.main.ui.course_status.setText('EXPIRED')
			self.main.ui.course_status.setStyleSheet("""*{color: rgb(222, 0, 0);}""")

		create_datetime = view_class_window.reformat_datetime(self, create_time, create_date, True)
		expire_datetime = view_class_window.reformat_datetime(self, time, date, False)
		self.main.ui.course_created_on.setText(f'{create_datetime[0]} {create_datetime[1]}')
		self.main.ui.top_course_code.setText(code)
		self.main.ui.top_course_name.setText(name)
		self.main.ui.update_course_name.setText(name)
		self.main.ui.update_course_code.setText(code)
		self.main.ui.update_course_expire_date.setDate(expire_datetime[0])
		self.main.ui.update_course_expire_time.setTime(expire_datetime[1])

	def reformat_datetime(self, time, date, for_top):
		current_date = QDate.fromString(date, 'yyyy-MM-dd')
		current_time = QTime.fromString(time, 'hh:mm:ss')
		if not for_top:
			return current_date, current_time	
		else:
			return current_date.toString('MMM dd, yyyy'), current_time.toString('h:mm AP')

	def delete_class(self):
		global class_id
		reply = QMessageBox.question(self, 'Delete Class', 'Are you sure you want to delete class?',
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			thread_starters.start_check_class(self, 'stop')
			teacher_dash_ui_functs.del_class(self, class_id)

		self.close()
		main_window.teacher_classes()
	
	def disable_update_class(self):
		global class_id
		thread_starters.start_check_class(self, 'stop')
		database = db(id_number=class_id)
		display = database.view_select_class()

		current_name = display[1]
		current_code = display[2]
		current_exp_date = display[3]
		current_exp_time = display[4]
		current_time = datetime.strptime(current_exp_time, "%H:%M:%S")
		current_time = datetime.strftime(current_time, "%H:%M")

		course_name = self.ui.update_course_name.text()
		course_code = self.ui.update_course_code.text()
		class_name = self.ui.update_course_name.text()
		class_code = self.ui.update_course_code.text()
		class_expire_date = self.ui.update_course_expire_date.date().toString('yyyy-MM-dd')
		class_expire_time = self.ui.update_course_expire_time.text()


		time = datetime.strptime(class_expire_time, "%I:%M %p")
		new_format_time = datetime.strftime(time, "%H:%M")

		if (current_name == course_name and current_code == course_code and 
			current_exp_date == class_expire_date and current_time == new_format_time):

			self.ui.update_course.setDisabled(True)
		else:
			self.ui.update_course.setDisabled(False)

	def update_class(self):
		global class_id
		global status
		global current_expire_datetime
		thread_starters.start_check_class(self, 'stop')
		teacher_dash_ui_functs.update_class(self, class_id, status, current_expire_datetime)
		self.close()
		main_window.teacher_classes()
		

class thread_starters:
	def start_check_class(self, opt):
		self.check_class = check_class_expiration_thread()
		if opt == 'start':
			self.check_class.start()
			self.check_class.check_class_signal.connect(self.update_class_ui)
		else:
			self.check_class.quit()













if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = login_signUp_window()
	sys.exit(app.exec())