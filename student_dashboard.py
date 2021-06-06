# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_student_dash(object):
    def setupUi(self, student_dash):
        student_dash.setObjectName("student_dash")
        student_dash.resize(819, 617)
        self.centralwidget = QtWidgets.QWidget(student_dash)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.current_user_name = QtWidgets.QLabel(self.centralwidget)
        self.current_user_name.setGeometry(QtCore.QRect(180, 30, 631, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.current_user_name.setFont(font)
        self.current_user_name.setScaledContents(True)
        self.current_user_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.current_user_name.setObjectName("current_user_name")
        self.student_view_account = QtWidgets.QPushButton(self.centralwidget)
        self.student_view_account.setGeometry(QtCore.QRect(190, 110, 131, 31))
        self.student_view_account.setObjectName("student_view_account")
        self.student_home = QtWidgets.QPushButton(self.centralwidget)
        self.student_home.setGeometry(QtCore.QRect(40, 110, 121, 31))
        self.student_home.setObjectName("student_home")
        self.student_logout = QtWidgets.QPushButton(self.centralwidget)
        self.student_logout.setGeometry(QtCore.QRect(710, 110, 91, 31))
        self.student_logout.setObjectName("student_logout")
        self.student_view_attendance = QtWidgets.QPushButton(self.centralwidget)
        self.student_view_attendance.setGeometry(QtCore.QRect(360, 110, 131, 31))
        self.student_view_attendance.setObjectName("student_view_attendance")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 150, 801, 451))
        self.stackedWidget.setObjectName("stackedWidget")
        self.student_home_page = QtWidgets.QWidget()
        self.student_home_page.setObjectName("student_home_page")
        self.label_3 = QtWidgets.QLabel(self.student_home_page)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.student_home_page)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 82, 801, 91))
        self.pushButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_5.setStyleSheet("*{\n"
"    Text-align:left;\n"
"    padding-left:2em;\n"
"}")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.student_home_page)
        self.student_account_page = QtWidgets.QWidget()
        self.student_account_page.setObjectName("student_account_page")
        self.label_4 = QtWidgets.QLabel(self.student_account_page)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.student_account_page)
        self.label_5.setGeometry(QtCore.QRect(100, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.student_username_edit = QtWidgets.QLineEdit(self.student_account_page)
        self.student_username_edit.setGeometry(QtCore.QRect(100, 310, 231, 31))
        self.student_username_edit.setObjectName("student_username_edit")
        self.student_id_edit = QtWidgets.QLineEdit(self.student_account_page)
        self.student_id_edit.setGeometry(QtCore.QRect(100, 210, 231, 31))
        self.student_id_edit.setObjectName("student_id_edit")
        self.student_gender_edit = QtWidgets.QComboBox(self.student_account_page)
        self.student_gender_edit.setGeometry(QtCore.QRect(390, 210, 111, 31))
        self.student_gender_edit.setObjectName("student_gender_edit")
        self.student_gender_edit.addItem("")
        self.student_gender_edit.addItem("")
        self.student_gender_edit.addItem("")
        self.student_fname_edit = QtWidgets.QLineEdit(self.student_account_page)
        self.student_fname_edit.setGeometry(QtCore.QRect(100, 130, 231, 31))
        self.student_fname_edit.setObjectName("student_fname_edit")
        self.student_lname_edit = QtWidgets.QLineEdit(self.student_account_page)
        self.student_lname_edit.setGeometry(QtCore.QRect(420, 130, 231, 31))
        self.student_lname_edit.setObjectName("student_lname_edit")
        self.label_8 = QtWidgets.QLabel(self.student_account_page)
        self.label_8.setGeometry(QtCore.QRect(420, 280, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.student_edit = QtWidgets.QPushButton(self.student_account_page)
        self.student_edit.setGeometry(QtCore.QRect(420, 380, 211, 51))
        self.student_edit.setObjectName("student_edit")
        self.label_6 = QtWidgets.QLabel(self.student_account_page)
        self.label_6.setGeometry(QtCore.QRect(420, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.student_account_page)
        self.label_7.setGeometry(QtCore.QRect(390, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.student_account_page)
        self.label_9.setGeometry(QtCore.QRect(100, 280, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.student_account_page)
        self.label_10.setGeometry(QtCore.QRect(100, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.student_change_pass = QtWidgets.QPushButton(self.student_account_page)
        self.student_change_pass.setGeometry(QtCore.QRect(420, 310, 191, 31))
        self.student_change_pass.setObjectName("student_change_pass")
        self.student_section_edit = QtWidgets.QComboBox(self.student_account_page)
        self.student_section_edit.setGeometry(QtCore.QRect(560, 210, 111, 31))
        self.student_section_edit.setObjectName("student_section_edit")
        self.student_section_edit.addItem("")
        self.label_12 = QtWidgets.QLabel(self.student_account_page)
        self.label_12.setGeometry(QtCore.QRect(560, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.student_account_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page)
        student_dash.setCentralWidget(self.centralwidget)

        self.retranslateUi(student_dash)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(student_dash)

    def retranslateUi(self, student_dash):
        _translate = QtCore.QCoreApplication.translate
        student_dash.setWindowTitle(_translate("student_dash", "MainWindow"))
        self.label.setText(_translate("student_dash", "Hello"))
        self.current_user_name.setText(_translate("student_dash", "Firstname"))
        self.student_view_account.setText(_translate("student_dash", "View and Edit Account"))
        self.student_home.setText(_translate("student_dash", "Home"))
        self.student_logout.setText(_translate("student_dash", "Logout"))
        self.student_view_attendance.setText(_translate("student_dash", "View Attendance Record"))
        self.label_3.setText(_translate("student_dash", "Classes"))
        self.pushButton_5.setText(_translate("student_dash", "Class 1"))
        self.label_4.setText(_translate("student_dash", "Account"))
        self.label_5.setText(_translate("student_dash", "I.D Number"))
        self.student_gender_edit.setItemText(0, _translate("student_dash", "Select"))
        self.student_gender_edit.setItemText(1, _translate("student_dash", "Male"))
        self.student_gender_edit.setItemText(2, _translate("student_dash", "Female"))
        self.label_8.setText(_translate("student_dash", "Password"))
        self.student_edit.setText(_translate("student_dash", "Edit"))
        self.label_6.setText(_translate("student_dash", "Last Name"))
        self.label_7.setText(_translate("student_dash", "Gender"))
        self.label_9.setText(_translate("student_dash", "Username"))
        self.label_10.setText(_translate("student_dash", "First Name"))
        self.student_change_pass.setText(_translate("student_dash", "Change Password"))
        self.student_section_edit.setItemText(0, _translate("student_dash", "Select"))
        self.label_12.setText(_translate("student_dash", "Section"))
        self.label_11.setText(_translate("student_dash", "Attendance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_dash = QtWidgets.QMainWindow()
    ui = Ui_student_dash()
    ui.setupUi(student_dash)
    student_dash.show()
    sys.exit(app.exec_())
