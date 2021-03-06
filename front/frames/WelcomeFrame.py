from PySide.QtCore import *
from PySide.QtGui import *

from FadeWidget import FadeWidget
from widgets.NextButton import NextButton

class WelcomeFrame(FadeWidget):
	@Slot()
	def start(self):
		self.parent().parent().backend_app.setUniversity(self.uni_list.currentText())
		print(self.uni_list.currentText())
		self.parent().switchSubFrame(self.parent().login_frame)
	
	def __init__(self):
		FadeWidget.__init__(self)
		self.layout = QVBoxLayout()

		self.university_names = ['University of Melbourne', 'Monash University']
		self.uni_list = QComboBox(self)
		self.uni_list.setFixedWidth(800)
		self.uni_list.addItems(self.university_names)
		self.layout.addWidget(self.uni_list,0,Qt.AlignCenter)

		self.pushbutton_login = NextButton("Start")
		self.pushbutton_login.clicked.connect(self.start)

		self.layout.addStretch()
		self.layout.addWidget(self.pushbutton_login, 0, Qt.AlignCenter)
		self.setLayout(self.layout)