from PySide.QtCore import *
from PySide.QtGui import *

class confirmSubjectWidget(QWidget):
	@staticmethod
	def setIcons(icon_tick_unclicked, icon_tick_clicked):
		confirmSubjectWidget.icon_tick_unclicked = icon_tick_unclicked 
		confirmSubjectWidget.icon_tick_clicked = icon_tick_clicked
		
	@Slot()
	def uncomfirmSubject(self):
		if self.confirm_bool == True:
			self.button_confirm.setIcon(confirmSubjectWidget.icon_tick_clicked)
			self.confirm_bool = False
		else:
			self.button_confirm.setIcon(confirmSubjectWidget.icon_tick_unclicked)
			self.confirm_bool = True

	def __init__(self, title, semester, year, code):
		QWidget.__init__(self)
		self.confirm_bool = False
		self.layout = QHBoxLayout()
		letter_count = len(title +semester + year + code)
		spacing = int((60 - letter_count) / 2)
		if spacing % 2 != 0:
			spacing -= 1
		self.title = QLabel(title + (spacing * " ") + "Semester " + semester + " " + year + (spacing) *  " " + code )
		self.title.setObjectName("rounded")
		#self.semester = QLabel("Semester " + semester)
		#self.semester.setObjectName("rounded")
		#self.year = QLabel(year)
		#self.year.setObjectName("rounded")
		#self.code = QLabel(code)
		#self.code.setObjectName("rounded")

		self.button_confirm = QPushButton()
		self.button_confirm.setObjectName('tickButton')
		self.button_confirm.setIcon(confirmSubjectWidget.icon_tick_clicked)
		self.button_confirm.setIconSize(QSize(100,100));
		self.button_confirm.clicked.connect(self.uncomfirmSubject)

		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.title)
		#self.layout.addWidget(self.code)
		#self.layout.addWidget(self.semester)
		#self.layout.addWidget(self.year)
		self.layout.addWidget(self.button_confirm)
		self.setLayout(self.layout)