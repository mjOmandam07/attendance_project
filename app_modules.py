import sys

from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

sys.path.append('./UI')
from login_signUp import Ui_MainWindow

from student_dashboard import Ui_student_dash
from teacher_dashboard import Ui_teacher_dash

from teacher_change_password import Ui_teacher_change_pass
from student_change_password import Ui_student_change_pass

from add_class import Ui_create_class
from view_class import Ui_view_class
from student_view_class import Ui_student_view_class
from subj_password import Ui_subject_pass_window

from view_records import Ui_view_records


import teacher_dynamic_widgets as dynamic
import student_dynamic_widgets as student_dynamic


from student_dynamic_widgets import student_widget
from teacher_dynamic_widgets import widgets, expired_class

from class_threads import *

from ui_functions import *

