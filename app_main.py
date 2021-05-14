import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from login_signUp import Ui_MainWindow

from student_dashboard import Ui_student_dash
from teacher_dashboard import Ui_teacher_dash

from teacher_change_password import Ui_teacher_change_pass
from student_change_password import Ui_student_change_pass

from logout import Ui_logout

from ui_functions import *

from  logged_user import current_user



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
		self.main = student_dashboard()
		self.main.show()
		self.close()

	def to_teacher_dashboard(self):
		self.main = teacher_dashboard()
		self.main.show()
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
		self.ui.teacher_fname_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_lname_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_id_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_gender_edit.currentIndexChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_username_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		

		self.ui.search_student_lineEdit.textChanged['QString'].connect(lambda:teacher_dash_ui_functs.view_student_list(self))

		self.ui.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
            lambda: teacher_dash_ui_functs.get_selected_student(self))

		self.show()


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









if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = login_signUp_window()
	sys.exit(app.exec())