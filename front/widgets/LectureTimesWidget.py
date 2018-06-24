from PySide.QtCore import *
from PySide.QtGui import *

class LectureTimesWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.vbox_day = QVBoxLayout()
		self.label_title_day = QLabel("Monday")
		self.list_time = QComboBox(self)
		self.list_time.addItems(self.lecture_dates)
		self.vbox_day.addWidget(self.label_title_day)
		self.vbox_day.addWidget(self.list_time)
		self.hbox_times.addLayout(self.vbox_day)

