from PySide.QtCore import *
from PySide.QtGui import *

from FadeWidget import FadeWidget

class TitleFrame(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		self.label_title = QLabel("AutoLecture")
		self.label_title.setObjectName("setupScreenTitle")
		self.label_title.setAlignment(Qt.AlignCenter)
		self.label_title.setFixedHeight(400)

		self.layout.addWidget(self.label_title)
		self.setLayout(self.layout)
