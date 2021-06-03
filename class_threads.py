import time
import sys
from datetime import datetime
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

from ui_functions import *



class check_class_expiration_thread(QThread):
    check_class_signal = pyqtSignal(object)
    def run(self):
    	while True:
    		now = datetime.now()
    		current_datetime = now.strftime('%Y-%m-%d %H:%M')
    		print(current_datetime)
    		conn = sqlite3.connect('attendance.db')
    		cursor = conn.cursor()
    		sql = """UPDATE course SET is_active = 0 WHERE expire_date <= julianday('{}') AND is_active = 1""".format(current_datetime)
    		try:
    			cursor.execute(sql)
    			conn.commit()
    			if cursor.rowcount != 1:
    				self.check_class_signal.emit(False)
    			else:
    				self.check_class_signal.emit(True)
    			cursor.close()

    		except Exception as e:
    			print(e)

    		time.sleep(1)