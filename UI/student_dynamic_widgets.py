student_widget = []

def has_class():
        has_class_script = """
if 'no_class_frame' in dir(self):
        self.no_class_frame.close()
self.scrollArea = QtWidgets.QScrollArea(self.ui.student_home_page)
self.scrollArea.setStyleSheet("*{border:none;}")
self.scrollArea.setWidgetResizable(True)
self.scrollArea.setObjectName("scrollArea")
self.scrollAreaWidgetContents = QtWidgets.QWidget()
self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 803, 367))
self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
self.verticalLayout_2.setObjectName("verticalLayout_2")
self.scrollArea.setWidget(self.scrollAreaWidgetContents)
self.ui.verticalLayout.addWidget(self.scrollArea)
self.verticalLayout_2.setAlignment(Qt.AlignTop)"""

        return has_class_script


def no_class():
        no_class_script = """
if 'scrollArea' in dir(self):
        self.scrollArea.close()
self.no_class_frame = QtWidgets.QFrame(self.ui.student_home_page)
self.no_class_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
self.no_class_frame.setFrameShadow(QtWidgets.QFrame.Raised)
self.no_class_frame.setObjectName("no_class_frame")
self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.no_class_frame)
self.verticalLayout_2.setObjectName("verticalLayout_2")
self.label_2 = QtWidgets.QLabel(self.no_class_frame)
font = QtGui.QFont()
font.setFamily("Montserrat")
font.setPointSize(60)
self.label_2.setFont(font)
self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
self.label_2.setObjectName("label_2")
self.verticalLayout_2.addWidget(self.label_2)
self.label_14 = QtWidgets.QLabel(self.no_class_frame)
sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
self.label_14.setSizePolicy(sizePolicy)
font = QtGui.QFont()
font.setFamily("Montserrat")
font.setPointSize(24)
self.label_14.setFont(font)
self.label_14.setStyleSheet("")
self.label_14.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
self.label_14.setObjectName("label_14")
self.verticalLayout_2.addWidget(self.label_14)
self.label_13 = QtWidgets.QLabel(self.no_class_frame)
self.label_13.setMinimumSize(QtCore.QSize(0, 0))
font = QtGui.QFont()
font.setFamily("Montserrat")
font.setPointSize(18)
self.label_13.setFont(font)
self.label_13.setStyleSheet("*{margin-bottom:100px;}")
self.label_13.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
self.label_13.setObjectName("label_13")
self.verticalLayout_2.addWidget(self.label_13)
self.ui.verticalLayout.addWidget(self.no_class_frame)

self.label_2.setText("Yeeeyyy!!")
self.label_14.setText("Walay Klase")
self.label_13.setText("Basin Wala si Maam/Sir")

"""
        return no_class_script




def dynamic_class():
        add_widget_script = """
self.course_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
self.course_frame.setMinimumSize(QtCore.QSize(0, 120))
self.course_frame.setMaximumSize(QtCore.QSize(16777215, 110))
self.course_frame.setStyleSheet("QFrame{border:1px solid black;}")
self.course_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
self.course_frame.setFrameShadow(QtWidgets.QFrame.Raised)
self.course_frame.setObjectName("course_frame")
self.horizontalLayout = QtWidgets.QHBoxLayout(self.course_frame)
self.horizontalLayout.setObjectName("horizontalLayout")
self.frame_2 = QtWidgets.QFrame(self.course_frame)
self.frame_2.setStyleSheet("QFrame{border:None;}")
self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
self.frame_2.setObjectName("frame_2")
self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
self.verticalLayout_3.setSpacing(2)
self.verticalLayout_3.setObjectName("verticalLayout_3")
self.course_name_label = QtWidgets.QLabel(self.frame_2)
self.course_name_label.setMinimumSize(QtCore.QSize(0, 30))
font = QtGui.QFont()
font.setFamily("Montserrat")
font.setPointSize(22)
self.course_name_label.setFont(font)
self.course_name_label.setFrameShape(QtWidgets.QFrame.NoFrame)
self.course_name_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
self.course_name_label.setObjectName("course_name_label")
self.verticalLayout_3.addWidget(self.course_name_label)
self.course_code_label = QtWidgets.QLabel(self.frame_2)
self.course_code_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
font = QtGui.QFont()
font.setFamily("Montserrat")
self.course_code_label.setFont(font)
self.course_code_label.setStyleSheet("*{margin-left:10px;}")
self.course_code_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.course_code_label.setIndent(0)
self.course_code_label.setObjectName("course_code_label")
self.verticalLayout_3.addWidget(self.course_code_label)
self.course_lecturer = QtWidgets.QLabel(self.frame_2)
self.course_lecturer.setMaximumSize(QtCore.QSize(16777215, 16777215))
font = QtGui.QFont()
font.setFamily("Montserrat")
font.setBold(True)
font.setWeight(75)
self.course_lecturer.setFont(font)
self.course_lecturer.setStyleSheet("*{margin-left:10px;}")
self.course_lecturer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
self.course_lecturer.setIndent(0)
self.course_lecturer.setObjectName("course_lecturer")
self.verticalLayout_3.addWidget(self.course_lecturer)
self.status_frame = QtWidgets.QFrame(self.frame_2)
self.status_frame.setMinimumSize(QtCore.QSize(0, 0))
self.status_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
self.status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
self.status_frame.setObjectName("status_frame")
self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.status_frame)
self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
self.horizontalLayout_2.setObjectName("horizontalLayout_2")
self.status_icon = QtWidgets.QFrame(self.status_frame)
self.status_icon.setMaximumSize(QtCore.QSize(11, 11))
self.status_icon.setStyleSheet("*{border-radius:5px; background-color:rgb(0, 170, 0);}")
self.status_icon.setFrameShape(QtWidgets.QFrame.StyledPanel)
self.status_icon.setFrameShadow(QtWidgets.QFrame.Raised)
self.status_icon.setObjectName("status_icon")
self.horizontalLayout_2.addWidget(self.status_icon)
self.status_label = QtWidgets.QLabel(self.status_frame)
font = QtGui.QFont()
font.setFamily("Montserrat")
font.setBold(False)
font.setWeight(50)
self.status_label.setFont(font)
self.status_label.setStyleSheet("*{margin-bottom:2px; color:rgb(0, 170, 0)}")
self.status_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
self.status_label.setObjectName("status_label")
self.horizontalLayout_2.addWidget(self.status_label)
self.verticalLayout_3.addWidget(self.status_frame)
self.horizontalLayout.addWidget(self.frame_2)
self.frame_3 = QtWidgets.QFrame(self.course_frame)
self.frame_3.setMaximumSize(QtCore.QSize(150, 16777215))
self.frame_3.setStyleSheet("QFrame{border:none;}")
self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
self.frame_3.setObjectName("frame_3")
self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
self.verticalLayout_4.setContentsMargins(20, -1, 20, -1)
self.verticalLayout_4.setSpacing(9)
self.verticalLayout_4.setObjectName("verticalLayout_4")
self.view_class = QtWidgets.QPushButton(self.frame_3)
self.view_class.setMinimumSize(QtCore.QSize(0, 40))
self.view_class.setStyleSheet('''*{background-color: rgb(225, 225, 225);
        border:1px solid rgb(204, 204, 204);
        }
      *:hover{background-color:rgb(191, 191, 191);}''')
self.view_class.setObjectName('view_class')
if item[7] != 0:
        self.view_class.setObjectName(str(item[0]))
        self.view_class.clicked.connect(self.view_class_buttons)
else:
        self.view_class.setDisabled(True)


self.verticalLayout_4.addWidget(self.view_class)
self.horizontalLayout.addWidget(self.frame_3)
self.verticalLayout_2.addWidget(self.course_frame)
self.course_name_label.setText(item[2])
self.course_code_label.setText(item[1])
self.course_lecturer.setText(f'Teacher: {item[8]} {item[9]}')

if item[7] == 1:
        self.status_label.setText("ACTIVE")
else:
        self.status_label.setText("EXPIRED")
        self.status_label.setStyleSheet("*{margin-bottom:2px; color: rgb(222, 0, 0);}")
        self.status_icon.setStyleSheet("*{border-radius:5px; background-color:rgb(222, 0, 0)}")

self.view_class.setText('View Class')
"""


        return add_widget_script


def clear_scrollArea():
        script = '''
for i in reversed (range(self.verticalLayout_2.count())):
        self.verticalLayout_2.itemAt(i).widget().close()
        self.verticalLayout_2.takeAt(i)
'''

        return script