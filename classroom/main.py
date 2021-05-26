import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from login import Ui_Dialog
from createacc import Ui_Dialog2
import secrets
from database import *

current_user = []



class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class LoginScreen(QDialog, Ui_Dialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.setupUi(self)
        #loadUi("login.ui",self)
        #self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        current_user.clear()
        username = self.username.text()
        password = self.password.text()

        if len(username)==0 or len(password)==0:
            self.error.setText("Please fill in all fields.")

        else:
            data = Database(username=username)
            to_confirm = data.login_student()
            if to_confirm[6] == password:
                for item in to_confirm:
                    current_user.append(item)
                    print('He',item)
                    print('Nge',current_user)
                print("Successfully logged in.")
                self.error.setText("")

                dashboard = DashboardScreen()
                widget.addWidget(dashboard)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                print("F")
                self.error.setText("Invalid username or password")

class CreateAccScreen(QDialog, Ui_Dialog2):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        self.setupUi2(self)
        #loadUi("createacc.ui",self)
        #self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        first_name = self.firstnamefield.text()
        last_name = self.lastnamefield.text()
        id_number = self.idnofield.text()
        gender = self.genderbox.currentText().upper()
        username = self.userfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()
        self.sec = secrets.Secreto()

        if len(first_name) == 0 or len(last_name) == 0 or len(id_number) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.error.setText("Please fill in all fields.")

        elif password != confirmpassword:
            self.error.setText("Password doesn't match!")

        else:
            data = Database(id_number = id_number, first_name = first_name, last_name = last_name, gender = gender, username = username, password=password)

            data.createacc_student()
            print("noice")

            dashboard = DashboardScreen()
            widget.addWidget(dashboard)
            widget.setCurrentIndex(widget.currentIndex()+1)


class DashboardScreen(QDialog):
    def __init__(self):
        super(DashboardScreen, self).__init__()
        loadUi("dashboard.ui",self)
        self.join.clicked.connect(self.joinClassroomFunction)

    def joinClassroomFunction(self):
        Attend = ConfrimJoinScreen()
        widget.addWidget(Attend)
        widget.setCurrentIndex(widget.currentIndex()+1)


class ConfrimJoinScreen(QDialog):
    def __init__(self):
        super(ConfrimJoinScreen, self).__init__()
        loadUi("confirmjoin.ui", self)
        self.join.clicked.connect(self.confirmjoinfun)

    def confirmjoinfun(self):
        first_name = self.firstnamefield.text()
        last_name = self.lastnamefield.text()
        id_number = self.idnofield.text()

        if len(current_user) != 0:
            print('fu',current_user)
            for item in current_user:
                print('oof',item)
                self.firstnamefield.setText(item[2])
                self.lastnamefield.setText(item[3])
                self.idnofield.setText(item[1])
'''
        to_confirm = data.confrimjoin()
        login_back = Database(unique_id = current_user[0])
        logged_back = login_back.login_student_back()

        current_user.clear()
        for item in logged_back:
            current_user.append(item)

        login_signUp_ui_functions.popups(self, "update_success")
        print(current_user)'''


        

class AttendanceScreen(QDialog):
    def __init__(self):
        super(AttendanceScreen, self).__init__()
        loadUi("attendance.ui",self)
        self.tableWidget.setColumnWidth(0,250)
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,350)
        self.loaddata()

    def loaddata(self):

        data = Database()
        attend = data.classroom()
        print("noice!")

        tablerow=0
        self.tableWidget.setRowCount(40)
        for row in attend:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1



# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(463)
widget.setFixedWidth(761)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")