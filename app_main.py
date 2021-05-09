import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from signUp import Ui_MainWindow
from student_dashboard import Ui_student_dash
from teacher_dashboard import Ui_teacher_dash

from ui_functions import *

from  logged_user import current_user




class signUp_window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


		signUp_ui_functions.buttons(self)
		self.ui.student_signUp.setDisabled(True)
		self.ui.student_fname.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_lname.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_id.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_gender.currentIndexChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_username.textChanged['QString'].connect(self.disable_student_SignUp)
		self.ui.student_password.textChanged['QString'].connect(self.disable_student_SignUp)

		self.ui.teacher_signUp.setDisabled(True)
		self.ui.teacher_fname.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_lname.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_id.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_gender.currentIndexChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_username.textChanged['QString'].connect(self.disable_teacher_SignUp)
		self.ui.teacher_password.textChanged['QString'].connect(self.disable_teacher_SignUp)

		self.show()

	def signUp_buttons(self):
		btnWidget = self.sender() # RETURNS THE BUTTON PRESSED
		btn_name = btnWidget.objectName() # RETURNS THE 'NAME' OF THE BUTTON PRESSED


		if btn_name == 'im_a_teacher':
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
		elif btn_name == 'im_a_student':
			self.ui.stackedWidget.setCurrentWidget(self.ui.page)
		elif btn_name == 'student_signUp':
			signUp_ui_functions.student_signup_validations(self)
		elif btn_name == 'teacher_signUp':
			signUp_ui_functions.teacher_signup_validations(self)





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

		if fname and lname and id_num and gender and username and password:
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

		if fname and lname and id_num and gender and username and password:
			self.ui.teacher_signUp.setDisabled(False)
		else:
			self.ui.teacher_signUp.setDisabled(True)

###########################     STUDENT DASHBOARD      ############################################
class student_dashboard(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_student_dash()
		self.ui.setupUi(self)


		student_dash_ui_functs.buttons(self)

		self.ui.current_user_name.setText(current_user[1])



		self.ui.student_edit.setDisabled(True)
		self.ui.student_fname_edit.textChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_lname_edit.textChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_id_edit.textChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_gender_edit.currentIndexChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_username_edit.textChanged['QString'].connect(self.disable_student_edit)
		self.ui.student_password_edit.textChanged['QString'].connect(self.disable_student_edit)

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
		


	def disable_student_edit(self):
		self.ui.current_user_name.setText(current_user[1])
		fname = self.ui.student_fname_edit.text().upper()
		lname = self.ui.student_lname_edit.text().upper()
		id_num = self.ui.student_id_edit.text()
		if self.ui.student_gender_edit.currentText() == 'Select':
			gender = None
		else:
			gender = self.ui.student_gender_edit.currentText().upper()

		username = self.ui.student_username_edit.text()
		password = self.ui.student_password_edit.text()


		if (fname == current_user[1] and lname == current_user[2] 
				and id_num == current_user[0] and gender == current_user[3]
					and username == current_user[4] and password == current_user[5]):
				self.ui.student_edit.setDisabled(True)

		elif fname and lname and id_num and gender and username and password:
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


		
		self.ui.current_user_name.setText(current_user[1])



		self.ui.teacher_edit.setDisabled(True)
		self.ui.teacher_fname_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_lname_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_id_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_gender_edit.currentIndexChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_username_edit.textChanged['QString'].connect(self.disable_teacher_edit)
		self.ui.teacher_password_edit.textChanged['QString'].connect(self.disable_teacher_edit)

		self.ui.search_student_lineEdit.textChanged['QString'].connect(lambda:teacher_dash_ui_functs.view_student_list(self))

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



	def disable_teacher_edit(self):
		self.ui.current_user_name.setText(current_user[1])
		fname = self.ui.teacher_fname_edit.text().upper()
		lname = self.ui.teacher_lname_edit.text().upper()
		id_num = self.ui.teacher_id_edit.text()
		if self.ui.teacher_gender_edit.currentText() == 'Select':
			gender = None
		else:
			gender = self.ui.teacher_gender_edit.currentText().upper()

		username = self.ui.teacher_username_edit.text()
		password = self.ui.teacher_password_edit.text()


		if (fname == current_user[1] and lname == current_user[2] 
				and id_num == current_user[0] and gender == current_user[3]
					and username == current_user[4] and password == current_user[5]):
				self.ui.teacher_edit.setDisabled(True)

		elif fname and lname and id_num and gender and username and password:
			self.ui.teacher_edit.setDisabled(False)

			
		else:
			self.ui.teacher_edit.setDisabled(True)







if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = teacher_dashboard()
	sys.exit(app.exec())