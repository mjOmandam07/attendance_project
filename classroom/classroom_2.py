# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classroom_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_classroom1(object):
    def setupUi(self, classroom1):
        classroom1.setObjectName("classroom1")
        classroom1.resize(566, 400)
        self.centralwidget = QtWidgets.QWidget(classroom1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 70, 521, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 521, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        classroom1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(classroom1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        classroom1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(classroom1)
        self.statusbar.setObjectName("statusbar")
        classroom1.setStatusBar(self.statusbar)

        self.retranslateUi(classroom1)
        QtCore.QMetaObject.connectSlotsByName(classroom1)

    def retranslateUi(self, classroom1):
        _translate = QtCore.QCoreApplication.translate
        classroom1.setWindowTitle(_translate("classroom1", "CSC161_CLASSROOM"))
        self.label.setText(_translate("classroom1", "CSC161"))
        self.label_2.setText(_translate("classroom1", "CLASSROOM 2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("classroom1", "ID No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("classroom1", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("classroom1", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("classroom1", "Course"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("classroom1", "Time Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    classroom1 = QtWidgets.QMainWindow()
    ui = Ui_classroom1()
    ui.setupUi(classroom1)
    classroom1.show()
    sys.exit(app.exec_())