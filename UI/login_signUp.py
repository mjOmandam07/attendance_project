# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_signUp.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 614)
        MainWindow.setMinimumSize(QtCore.QSize(715, 614))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.to_sign_up = QtWidgets.QPushButton(self.centralwidget)
        self.to_sign_up.setGeometry(QtCore.QRect(364, 0, 351, 51))
        self.to_sign_up.setObjectName("to_sign_up")
        self.to_login = QtWidgets.QPushButton(self.centralwidget)
        self.to_login.setGeometry(QtCore.QRect(0, 0, 351, 51))
        self.to_login.setObjectName("to_login")
        self.welcome_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.welcome_stackedWidget.setGeometry(QtCore.QRect(0, 50, 711, 561))
        self.welcome_stackedWidget.setObjectName("welcome_stackedWidget")
        self.sign_up_page = QtWidgets.QWidget()
        self.sign_up_page.setObjectName("sign_up_page")
        self.label_2 = QtWidgets.QLabel(self.sign_up_page)
        self.label_2.setGeometry(QtCore.QRect(540, 40, 81, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.im_a_student = QtWidgets.QPushButton(self.sign_up_page)
        self.im_a_student.setGeometry(QtCore.QRect(500, 70, 75, 23))
        self.im_a_student.setObjectName("im_a_student")
        self.im_a_teacher = QtWidgets.QPushButton(self.sign_up_page)
        self.im_a_teacher.setGeometry(QtCore.QRect(590, 70, 75, 23))
        self.im_a_teacher.setObjectName("im_a_teacher")
        self.stackedWidget = QtWidgets.QStackedWidget(self.sign_up_page)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 711, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.student_username = QtWidgets.QLineEdit(self.page_9)
        self.student_username.setGeometry(QtCore.QRect(370, 300, 231, 31))
        self.student_username.setObjectName("student_username")
        self.student_id = QtWidgets.QLineEdit(self.page_9)
        self.student_id.setGeometry(QtCore.QRect(110, 300, 231, 31))
        self.student_id.setObjectName("student_id")
        self.label_31 = QtWidgets.QLabel(self.page_9)
        self.label_31.setGeometry(QtCore.QRect(110, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.page_9)
        self.label_32.setGeometry(QtCore.QRect(370, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.page_9)
        self.label_33.setGeometry(QtCore.QRect(110, 350, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.student_fname = QtWidgets.QLineEdit(self.page_9)
        self.student_fname.setGeometry(QtCore.QRect(110, 170, 231, 31))
        self.student_fname.setObjectName("student_fname")
        self.student_lname = QtWidgets.QLineEdit(self.page_9)
        self.student_lname.setGeometry(QtCore.QRect(370, 170, 231, 31))
        self.student_lname.setObjectName("student_lname")
        self.student_password = QtWidgets.QLineEdit(self.page_9)
        self.student_password.setGeometry(QtCore.QRect(110, 380, 231, 31))
        self.student_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_password.setObjectName("student_password")
        self.label_34 = QtWidgets.QLabel(self.page_9)
        self.label_34.setGeometry(QtCore.QRect(110, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.student_signUp = QtWidgets.QPushButton(self.page_9)
        self.student_signUp.setGeometry(QtCore.QRect(380, 430, 211, 51))
        self.student_signUp.setObjectName("student_signUp")
        self.student_gender = QtWidgets.QComboBox(self.page_9)
        self.student_gender.setGeometry(QtCore.QRect(110, 233, 111, 21))
        self.student_gender.setObjectName("student_gender")
        self.student_gender.addItem("")
        self.student_gender.addItem("")
        self.student_gender.addItem("")
        self.label_35 = QtWidgets.QLabel(self.page_9)
        self.label_35.setGeometry(QtCore.QRect(370, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.page_9)
        self.label_36.setGeometry(QtCore.QRect(110, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.page_9)
        self.label_37.setGeometry(QtCore.QRect(-20, 410, 601, 161))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(100)
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("*{\n"
"    \n"
"    color: rgb(193, 193, 193);\n"
"}")
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_53 = QtWidgets.QLabel(self.page_9)
        self.label_53.setGeometry(QtCore.QRect(370, 350, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.student_confirm_pass_signUp = QtWidgets.QLineEdit(self.page_9)
        self.student_confirm_pass_signUp.setGeometry(QtCore.QRect(370, 380, 231, 31))
        self.student_confirm_pass_signUp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_confirm_pass_signUp.setObjectName("student_confirm_pass_signUp")
        self.label_55 = QtWidgets.QLabel(self.page_9)
        self.label_55.setGeometry(QtCore.QRect(370, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.student_section = QtWidgets.QComboBox(self.page_9)
        self.student_section.setGeometry(QtCore.QRect(370, 233, 111, 21))
        self.student_section.setObjectName("student_section")
        self.student_section.addItem("")
        self.label_37.raise_()
        self.student_username.raise_()
        self.student_id.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.student_fname.raise_()
        self.student_lname.raise_()
        self.student_password.raise_()
        self.label_34.raise_()
        self.student_signUp.raise_()
        self.student_gender.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_53.raise_()
        self.student_confirm_pass_signUp.raise_()
        self.label_55.raise_()
        self.student_section.raise_()
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_38 = QtWidgets.QLabel(self.page_10)
        self.label_38.setGeometry(QtCore.QRect(110, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.teacher_signUp = QtWidgets.QPushButton(self.page_10)
        self.teacher_signUp.setGeometry(QtCore.QRect(380, 430, 211, 51))
        self.teacher_signUp.setObjectName("teacher_signUp")
        self.teacher_lname = QtWidgets.QLineEdit(self.page_10)
        self.teacher_lname.setGeometry(QtCore.QRect(370, 170, 231, 31))
        self.teacher_lname.setObjectName("teacher_lname")
        self.label_39 = QtWidgets.QLabel(self.page_10)
        self.label_39.setGeometry(QtCore.QRect(110, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.teacher_id = QtWidgets.QLineEdit(self.page_10)
        self.teacher_id.setGeometry(QtCore.QRect(110, 300, 231, 31))
        self.teacher_id.setObjectName("teacher_id")
        self.teacher_gender = QtWidgets.QComboBox(self.page_10)
        self.teacher_gender.setGeometry(QtCore.QRect(110, 233, 111, 21))
        self.teacher_gender.setObjectName("teacher_gender")
        self.teacher_gender.addItem("")
        self.teacher_gender.addItem("")
        self.teacher_gender.addItem("")
        self.label_40 = QtWidgets.QLabel(self.page_10)
        self.label_40.setGeometry(QtCore.QRect(370, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.page_10)
        self.label_41.setGeometry(QtCore.QRect(110, 350, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.page_10)
        self.label_42.setGeometry(QtCore.QRect(-30, 410, 601, 161))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(100)
        font.setBold(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("*{\n"
"    \n"
"    color: rgb(193, 193, 193);\n"
"}")
        self.label_42.setScaledContents(True)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.teacher_username = QtWidgets.QLineEdit(self.page_10)
        self.teacher_username.setGeometry(QtCore.QRect(370, 300, 231, 31))
        self.teacher_username.setObjectName("teacher_username")
        self.teacher_password = QtWidgets.QLineEdit(self.page_10)
        self.teacher_password.setGeometry(QtCore.QRect(110, 380, 231, 31))
        self.teacher_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.teacher_password.setObjectName("teacher_password")
        self.label_43 = QtWidgets.QLabel(self.page_10)
        self.label_43.setGeometry(QtCore.QRect(110, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.page_10)
        self.label_44.setGeometry(QtCore.QRect(370, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.teacher_fname = QtWidgets.QLineEdit(self.page_10)
        self.teacher_fname.setGeometry(QtCore.QRect(110, 170, 231, 31))
        self.teacher_fname.setObjectName("teacher_fname")
        self.label_54 = QtWidgets.QLabel(self.page_10)
        self.label_54.setGeometry(QtCore.QRect(370, 350, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.teacher_confirm_pass_signUp = QtWidgets.QLineEdit(self.page_10)
        self.teacher_confirm_pass_signUp.setGeometry(QtCore.QRect(370, 380, 231, 31))
        self.teacher_confirm_pass_signUp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.teacher_confirm_pass_signUp.setObjectName("teacher_confirm_pass_signUp")
        self.label_38.raise_()
        self.teacher_lname.raise_()
        self.label_39.raise_()
        self.teacher_id.raise_()
        self.teacher_gender.raise_()
        self.label_40.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.teacher_username.raise_()
        self.teacher_password.raise_()
        self.label_43.raise_()
        self.label_44.raise_()
        self.teacher_fname.raise_()
        self.teacher_signUp.raise_()
        self.label_54.raise_()
        self.teacher_confirm_pass_signUp.raise_()
        self.stackedWidget.addWidget(self.page_10)
        self.label = QtWidgets.QLabel(self.sign_up_page)
        self.label.setGeometry(QtCore.QRect(30, 10, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget.raise_()
        self.label.raise_()
        self.im_a_student.raise_()
        self.im_a_teacher.raise_()
        self.label_2.raise_()
        self.welcome_stackedWidget.addWidget(self.sign_up_page)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.login_im_a_student = QtWidgets.QPushButton(self.login_page)
        self.login_im_a_student.setGeometry(QtCore.QRect(500, 70, 75, 23))
        self.login_im_a_student.setObjectName("login_im_a_student")
        self.login_im_a_teacher = QtWidgets.QPushButton(self.login_page)
        self.login_im_a_teacher.setGeometry(QtCore.QRect(590, 70, 75, 23))
        self.login_im_a_teacher.setObjectName("login_im_a_teacher")
        self.label_45 = QtWidgets.QLabel(self.login_page)
        self.label_45.setGeometry(QtCore.QRect(540, 40, 81, 31))
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.login_page)
        self.label_46.setGeometry(QtCore.QRect(30, 10, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setScaledContents(True)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.login_stackedWidget = QtWidgets.QStackedWidget(self.login_page)
        self.login_stackedWidget.setGeometry(QtCore.QRect(0, 0, 711, 561))
        self.login_stackedWidget.setObjectName("login_stackedWidget")
        self.login_student_page = QtWidgets.QWidget()
        self.login_student_page.setObjectName("login_student_page")
        self.label_47 = QtWidgets.QLabel(self.login_student_page)
        self.label_47.setGeometry(QtCore.QRect(-20, 410, 601, 161))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(100)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("*{\n"
"    \n"
"    color: rgb(193, 193, 193);\n"
"}")
        self.label_47.setScaledContents(True)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.student_login_btn = QtWidgets.QPushButton(self.login_student_page)
        self.student_login_btn.setGeometry(QtCore.QRect(250, 340, 231, 41))
        self.student_login_btn.setObjectName("student_login_btn")
        self.student_login_username = QtWidgets.QLineEdit(self.login_student_page)
        self.student_login_username.setGeometry(QtCore.QRect(200, 160, 321, 41))
        self.student_login_username.setObjectName("student_login_username")
        self.student_login_password = QtWidgets.QLineEdit(self.login_student_page)
        self.student_login_password.setGeometry(QtCore.QRect(200, 260, 321, 41))
        self.student_login_password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.student_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_login_password.setObjectName("student_login_password")
        self.label_51 = QtWidgets.QLabel(self.login_student_page)
        self.label_51.setGeometry(QtCore.QRect(150, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_51.setFont(font)
        self.label_51.setScaledContents(True)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.login_student_page)
        self.label_52.setGeometry(QtCore.QRect(150, 120, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_52.setFont(font)
        self.label_52.setScaledContents(True)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.login_stackedWidget.addWidget(self.login_student_page)
        self.login_teacher_page = QtWidgets.QWidget()
        self.login_teacher_page.setObjectName("login_teacher_page")
        self.label_48 = QtWidgets.QLabel(self.login_teacher_page)
        self.label_48.setGeometry(QtCore.QRect(-30, 410, 601, 161))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(100)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("*{\n"
"    \n"
"    color: rgb(193, 193, 193);\n"
"}")
        self.label_48.setScaledContents(True)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.login_teacher_page)
        self.label_49.setGeometry(QtCore.QRect(150, 120, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setScaledContents(True)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.teacher_login_username = QtWidgets.QLineEdit(self.login_teacher_page)
        self.teacher_login_username.setGeometry(QtCore.QRect(200, 160, 321, 41))
        self.teacher_login_username.setObjectName("teacher_login_username")
        self.label_50 = QtWidgets.QLabel(self.login_teacher_page)
        self.label_50.setGeometry(QtCore.QRect(150, 220, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_50.setFont(font)
        self.label_50.setScaledContents(True)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.teacher_login_password = QtWidgets.QLineEdit(self.login_teacher_page)
        self.teacher_login_password.setGeometry(QtCore.QRect(200, 260, 321, 41))
        self.teacher_login_password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.teacher_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.teacher_login_password.setObjectName("teacher_login_password")
        self.teacher_login_btn = QtWidgets.QPushButton(self.login_teacher_page)
        self.teacher_login_btn.setGeometry(QtCore.QRect(250, 340, 231, 41))
        self.teacher_login_btn.setObjectName("teacher_login_btn")
        self.login_stackedWidget.addWidget(self.login_teacher_page)
        self.login_stackedWidget.raise_()
        self.label_46.raise_()
        self.label_45.raise_()
        self.login_im_a_student.raise_()
        self.login_im_a_teacher.raise_()
        self.welcome_stackedWidget.addWidget(self.login_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.welcome_stackedWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome | Log in or Sign Up"))
        self.to_sign_up.setText(_translate("MainWindow", "Sign Up"))
        self.to_login.setText(_translate("MainWindow", "Log In"))
        self.label_2.setText(_translate("MainWindow", "Are you a"))
        self.im_a_student.setText(_translate("MainWindow", "Student"))
        self.im_a_teacher.setText(_translate("MainWindow", "Teacher"))
        self.label_31.setText(_translate("MainWindow", "I.D Number"))
        self.label_32.setText(_translate("MainWindow", "Last Name"))
        self.label_33.setText(_translate("MainWindow", "Password"))
        self.label_34.setText(_translate("MainWindow", "First Name"))
        self.student_signUp.setText(_translate("MainWindow", "Sign Up"))
        self.student_gender.setItemText(0, _translate("MainWindow", "Select"))
        self.student_gender.setItemText(1, _translate("MainWindow", "Male"))
        self.student_gender.setItemText(2, _translate("MainWindow", "Female"))
        self.label_35.setText(_translate("MainWindow", "Username"))
        self.label_36.setText(_translate("MainWindow", "Gender"))
        self.label_37.setText(_translate("MainWindow", "Student"))
        self.label_53.setText(_translate("MainWindow", "Confirm Password"))
        self.label_55.setText(_translate("MainWindow", "Section"))
        self.student_section.setItemText(0, _translate("MainWindow", "Select"))
        self.label_38.setText(_translate("MainWindow", "First Name"))
        self.teacher_signUp.setText(_translate("MainWindow", "Sign Up"))
        self.label_39.setText(_translate("MainWindow", "Gender"))
        self.teacher_gender.setItemText(0, _translate("MainWindow", "Select"))
        self.teacher_gender.setItemText(1, _translate("MainWindow", "Male"))
        self.teacher_gender.setItemText(2, _translate("MainWindow", "Female"))
        self.label_40.setText(_translate("MainWindow", "Last Name"))
        self.label_41.setText(_translate("MainWindow", "Password"))
        self.label_42.setText(_translate("MainWindow", "Teacher"))
        self.label_43.setText(_translate("MainWindow", "I.D Number"))
        self.label_44.setText(_translate("MainWindow", "Username"))
        self.label_54.setText(_translate("MainWindow", "Confirm Password"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.login_im_a_student.setText(_translate("MainWindow", "Student"))
        self.login_im_a_teacher.setText(_translate("MainWindow", "Teacher"))
        self.label_45.setText(_translate("MainWindow", "Are you a"))
        self.label_46.setText(_translate("MainWindow", "Log In"))
        self.label_47.setText(_translate("MainWindow", "Student"))
        self.student_login_btn.setText(_translate("MainWindow", "Log In"))
        self.label_51.setText(_translate("MainWindow", "Password"))
        self.label_52.setText(_translate("MainWindow", "Username"))
        self.label_48.setText(_translate("MainWindow", "Teacher"))
        self.label_49.setText(_translate("MainWindow", "Username"))
        self.label_50.setText(_translate("MainWindow", "Password"))
        self.teacher_login_btn.setText(_translate("MainWindow", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
