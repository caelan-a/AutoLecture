from PySide.QtCore import *
from PySide.QtGui import *

from widgets.InputFieldWidget import InputField

class SubjectFrame(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.layout = QVBoxLayout()

		self.input_title = InputField("Subject Title", "Engineering")

		self.lecture_dates = ["September 4", "September 6", "September 8"]
		self.label_title_lastwatched = QLabel("Last Lecture Watched")
		self.list_lastwatched = QComboBox(self)
		self.list_lastwatched.addItems(self.lecture_dates)

		self.label_title_lastdownloaded =  QLabel("Last Lecture Downloaded")
		self.list_lastdownloaded = QComboBox(self)
		self.list_lastdownloaded.addItems(self.lecture_dates)

		self.label_title_lecturetimes = QLabel("Lecture Times for the Week")
		self.hbox_times = QHBoxLayout()

		self.vbox_day = QVBoxLayout()
		self.label_title_day = QLabel("Monday")
		self.list_time = QComboBox(self)
		self.list_time.addItems(self.lecture_dates)
		self.vbox_day.addWidget(self.label_title_day)
		self.vbox_day.addWidget(self.list_time)
		self.hbox_times.addLayout(self.vbox_day)


		self.button_save = QPushButton("Save")


		self.layout.addStretch()
		self.layout.addWidget(self.input_title)
		self.layout.addStretch()
		self.layout.addWidget(self.label_title_lastwatched)
		self.layout.addWidget(self.list_lastwatched)
		self.layout.addWidget(self.label_title_lastdownloaded)
		self.layout.addWidget(self.list_lastdownloaded)
		self.layout.addStretch()
		self.layout.addWidget(self.label_title_lecturetimes)
		self.layout.addLayout(self.hbox_times)
		self.layout.addStretch()
		self.layout.addWidget(self.button_save)
		self.setLayout(self.layout)