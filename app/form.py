# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import models
import secrets


class Ui_Dialog(object):
    # UI that is to be replaced
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(205, 129)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept_data)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erngks")
        msg.setText("You are logged in " + self.lineEdit.text())

        x = msg.exec_()

# takes input and checks if password is correct for a particular username
    def accept_data(self):
        secr = secrets.Secreto()
        mods = models.Student()
        username = self.lineEdit.text()
        password = secr.to_process(self.lineEdit_2.text())

        user_to_confirm = mods.select_student(username)

        if password:
            if secr.check_hash(password, user_to_confirm[5]):
                self.show_popup()
            else:
                print('YOU ARE WRONG')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
