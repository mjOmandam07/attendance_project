import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from login import Ui_Dialog
import secrets
from database import *


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
        username = self.username.text()
        password = self.password.text()

        if len(username)==0 or len(password)==0:
            self.error.setText("Please fill in all fields.")

        else:
            data = Database(username=username)
            to_confirm = data.login_student()
            if to_confirm[6] == password:
                print("Successfully logged in.")
                self.error.setText("")
            else:
                print("F")
                self.error.setText("Invalid username or password")

class CreateAccScreen(QDialog):
    def __init__(self, id_number=None, first_name=None, last_name=None, gender=None, username=None, password=None, current_id=None, unique_id=None):

        self.unique_id = unique_id
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.gender = gender
        self.current_id = current_id

        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        first_name = self.firstnamefield.text()
        last_name = self.lastnamefield.text()
        id_number = self.idnofield.text()
        gender = self.genderbox
        username = self.userfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()
        self.sec = secrets.Secreto()

        if len(first_name) == 0 or len(last_name) == 0 or len(id_number) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.error.setText("Please fill in all fields.")

        elif password != confirmpassword:
            self.error.setText("Password doesn't match!")

        else:
            conn = sqlite3.connect("attendance.db")
            cur = conn.cursor()

            hashed_pass = self.sec.to_hash(self.password)
            student = (self.id_number, self.first_name, self.last_name, self.gender, self.username, hashed_pass,)
            cur.execute('INSERT INTO student(id_number, first_name, last_name, gender, username, password)VALUES(?,?,?,?,?,?)',student)

            conn.commit()
            conn.close()

            fillprofile = DashboardScreen()
            widget.addWidget(fillprofile)
            widget.setCurrentIndex(widget.currentIndex()+1)

class DashboardScreen(QDialog):
    def __init__(self):
        super(FillProfileScreen, self).__init__()
        loadUi("dashboard.ui",self)
        self.image.setPixmap(QPixmap('placeholder.png'))



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