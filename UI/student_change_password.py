# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_change_password.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_student_change_pass(object):
    def setupUi(self, student_change_pass):
        student_change_pass.setObjectName("student_change_pass")
        student_change_pass.resize(532, 319)
        student_change_pass.setMinimumSize(QtCore.QSize(532, 319))

        self.centralwidget = QtWidgets.QWidget(student_change_pass)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.student_new_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.student_new_pass.setGeometry(QtCore.QRect(110, 100, 321, 31))
        self.student_new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_new_pass.setObjectName("student_new_pass")
        self.student_confirm_new_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.student_confirm_new_pass.setGeometry(QtCore.QRect(110, 170, 321, 31))
        self.student_confirm_new_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_confirm_new_pass.setObjectName("student_confirm_new_pass")
        self.student_change_pass_btn = QtWidgets.QPushButton(self.centralwidget)
        self.student_change_pass_btn.setGeometry(QtCore.QRect(200, 220, 141, 41))
        self.student_change_pass_btn.setObjectName("student_change_pass_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 150, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 230, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("*{\n"
"    \n"
"    color: rgb(193, 193, 193);\n"
"}")
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.label.raise_()
        self.student_new_pass.raise_()
        self.student_confirm_new_pass.raise_()
        self.student_change_pass_btn.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        student_change_pass.setCentralWidget(self.centralwidget)

        self.retranslateUi(student_change_pass)
        QtCore.QMetaObject.connectSlotsByName(student_change_pass)

    def retranslateUi(self, student_change_pass):
        _translate = QtCore.QCoreApplication.translate
        student_change_pass.setWindowTitle(_translate("student_change_pass", "Student Change Password"))
        self.label.setText(_translate("student_change_pass", "Change Password"))
        self.student_change_pass_btn.setText(_translate("student_change_pass", "Change Password"))
        self.label_2.setText(_translate("student_change_pass", "New Password"))
        self.label_3.setText(_translate("student_change_pass", "Confirm New Password"))
        self.label_9.setText(_translate("student_change_pass", "Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_change_pass = QtWidgets.QMainWindow()
    ui = Ui_student_change_pass()
    ui.setupUi(student_change_pass)
    student_change_pass.show()
    sys.exit(app.exec_())
