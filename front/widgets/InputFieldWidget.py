from PySide.QtCore import *
from PySide.QtGui import *

class InputField(QWidget):
	def __init__(self, title, value):
		QWidget.__init__(self)
		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		self.heading = QLabel(title)
		self.input = QLineEdit(self)
		self.input.setText(value)
		self.layout.addWidget(self.heading)
		self.layout.addWidget(self.input)
		self.setLayout(self.layout)