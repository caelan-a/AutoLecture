from PySide.QtCore import *
from PySide.QtGui import *

class NextButton(QPushButton):
	def __init__(self, text, parent=None):
		QPushButton.__init__(self, text, parent)
		self.setObjectName("nextButton")
		self.setMinimumSize(300,70)
		self.setMaximumSize(300,70)