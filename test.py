'''import sys

from PyQt5 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.menuBar().setCornerWidget(self.dateedit, QtCore.Qt.TopLeftCorner)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())'''



'''import sys

from PyQt5 import QtCore, QtWidgets


class DateEdit(QtWidgets.QDateEdit):
    def __init__(self, parent=None):
        super().__init__(parent, calendarPopup=True)
        self._today_button = QtWidgets.QPushButton(self.tr("Today"))
        self._today_button.clicked.connect(self._update_today)
        self.calendarWidget().layout().addWidget(self._today_button)

    @QtCore.pyqtSlot()
    def _update_today(self):
        self._today_button.clearFocus()
        today = QtCore.QDate.currentDate()
        self.calendarWidget().setSelectedDate(today)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = DateEdit()
    w.show()
    sys.exit(app.exec_())'''





'''from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(QtWidgets.QWidget):
	def setupUi(self, MainWindow):
		MainWindow.resize(422, 255)
		self.centralwidget = QtWidgets.QWidget(MainWindow)

		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28))

		# For displaying confirmation message along with user's info.
		self.label = QtWidgets.QLabel(self.centralwidget)	
		self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))

		# Keeping the text of label empty initially.	
		self.label.setText("")	

		MainWindow.setCentralWidget(self.centralwidget)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Proceed"))
		self.pushButton.clicked.connect(self.takeinputs)
		
	def takeinputs(self):
		name, done1 = QtWidgets.QInputDialog.getText(
			self, 'Input Dialog', 'Enter your name:')

		roll, done2 = QtWidgets.QInputDialog.getInt(
		self, 'Input Dialog', 'Enter your roll:')

		cgpa, done3 = QtWidgets.QInputDialog.getDouble(
			self, 'Input Dialog', 'Enter your CGPA:')

		langs =['C', 'c++', 'Java', 'Python', 'Javascript']
		lang, done4 = QtWidgets.QInputDialog.getItem(
		self, 'Input Dialog', 'Language you know:', langs)

		if done1 and done2 and done3 and done4 :
			# Showing confirmation message along
			# with information provided by user.
			self.label.setText('Information stored Successfully\nName: '
								+str(name)+'('+str(roll)+')'+'\n'+'CGPA: '
								+str(cgpa)+'\nSelected Language: '+str(lang))

			# Hide the pushbutton after inputs provided by the use.
			self.pushButton.hide()	
				
			
			
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show() 

	sys.exit(app.exec_())
'''




'''

 self.scrollArea = QtWidgets.QScrollArea(self.teacher_home_page)
        self.scrollArea.setStyleSheet("*{\n"
"    border:none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 793, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.course_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
                                self.course_frame.setMinimumSize(QtCore.QSize(0, 110))
                                self.course_frame.setMaximumSize(QtCore.QSize(16777215, 110))
                                self.course_frame.setStyleSheet("QFrame{\n"
                        "    border:1px solid black;\n"
                        "}")
                                self.course_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
                                self.course_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                                self.course_frame.setObjectName("course_frame")
                                self.horizontalLayout = QtWidgets.QHBoxLayout(self.course_frame)
                                self.horizontalLayout.setObjectName("horizontalLayout")
                                self.frame_2 = QtWidgets.QFrame(self.course_frame)
                                self.frame_2.setStyleSheet("QFrame{\n"
                        "    border:None;\n"
                        "}")
                                self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
                                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                                self.frame_2.setObjectName("frame_2")
                                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
                                self.verticalLayout_3.setSpacing(0)
                                self.verticalLayout_3.setObjectName("verticalLayout_3")
                                self.course_code_label = QtWidgets.QLabel(self.frame_2)
                                font = QtGui.QFont()
                                font.setFamily("Montserrat")
                                font.setPointSize(22)
                                self.course_code_label.setFont(font)
                                self.course_code_label.setFrameShape(QtWidgets.QFrame.NoFrame)
                                self.course_code_label.setObjectName("course_code_label")
                                self.verticalLayout_3.addWidget(self.course_code_label)
                                self.course_name_label = QtWidgets.QLabel(self.frame_2)
                                self.course_name_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
                                self.course_name_label.setStyleSheet("*{\n"
                        "    margin-left:10px;\n"
                        "}")
                                self.course_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                                self.course_name_label.setIndent(0)
                                self.course_name_label.setObjectName("course_name_label")
                                self.verticalLayout_3.addWidget(self.course_name_label)
                                self.horizontalLayout.addWidget(self.frame_2)
                                self.frame_3 = QtWidgets.QFrame(self.course_frame)
                                self.frame_3.setMaximumSize(QtCore.QSize(150, 16777215))
                                self.frame_3.setStyleSheet("QFrame{\n"
                        "    border:none;\n"
                        "}")
                                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                                self.frame_3.setObjectName("frame_3")
                                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
                                self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
                                self.verticalLayout_4.setSpacing(9)
                                self.verticalLayout_4.setObjectName("verticalLayout_4")
                                self.view_class = QtWidgets.QPushButton(self.frame_3)
                                self.view_class.setMinimumSize(QtCore.QSize(0, 40))
                                self.view_class.setStyleSheet("*{\n"
                        "    background-color: rgb(225, 225, 225);\n"
                        "    border:1px solid rgb(204, 204, 204);\n"
                        "}\n"
                        "\n"
                        "*:hover{\n"
                        "    background-color:rgb(191, 191, 191);\n"
                        "}")
                                self.view_class.setObjectName("view_class")
                                self.verticalLayout_4.addWidget(self.view_class)
                                self.horizontalLayout.addWidget(self.frame_3)
                                self.verticalLayout_2.addWidget(self.course_frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)'''








# NO CLASSS

''' self.noClass_frame = QtWidgets.QFrame(self.teacher_home_page)
                             sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                             sizePolicy.setHorizontalStretch(0)
                             sizePolicy.setVerticalStretch(0)
                             sizePolicy.setHeightForWidth(self.noClass_frame.sizePolicy().hasHeightForWidth())
                             self.noClass_frame.setSizePolicy(sizePolicy)
                             self.noClass_frame.setMinimumSize(QtCore.QSize(0, 300))
                             self.noClass_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
                             self.noClass_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                             self.noClass_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                             self.noClass_frame.setObjectName("noClass_frame")
                             self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.noClass_frame)
                             self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
                             self.verticalLayout_5.setSpacing(0)
                             self.verticalLayout_5.setObjectName("verticalLayout_5")
                             self.label_2 = QtWidgets.QLabel(self.noClass_frame)
                             font = QtGui.QFont()
                             font.setFamily("Montserrat")
                             font.setPointSize(48)
                             self.label_2.setFont(font)
                             self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
                             self.label_2.setObjectName("label_2")
                             self.verticalLayout_5.addWidget(self.label_2)
                             self.label_19 = QtWidgets.QLabel(self.noClass_frame)
                             font = QtGui.QFont()
                             font.setFamily("Montserrat")
                             font.setPointSize(20)
                             self.label_19.setFont(font)
                             self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                             self.label_19.setObjectName("label_19")
                             self.verticalLayout_5.addWidget(self.label_19)
                             self.verticalLayout.addWidget(self.noClass_frame)'''