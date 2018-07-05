from PySide.QtCore import *
from PySide.QtGui import *

from stylesheets.StyleSheets import setStyleSheet
from widgets.FloatingDownArrow import FloatingDownArrow 


class ShowMoreWidget(QWidget):
	def showEvent(self, event):
		self.down_arrow_widget.startFloatAnimation()

	def hideEvent(self, event):
		self.down_arrow_widget.stopFloatAnimation()

	def __init__(self, assets):
		QWidget.__init__(self)
	
		setStyleSheet(self, "subject_tile")

		self.setObjectName("downArrow")

		# Size policy
		self.main_layout = QVBoxLayout()
		self.layout = QVBoxLayout()
		self.frame = QPushButton()
		self.frame.setObjectName("downArrow")
	
		self.down_arrow_widget = FloatingDownArrow(self, "downArrow", assets.icon_down_icon)
		# self.down_arrow_widget.clicked.connect(self.showPastSubjects)
	
		self.label_showmore = QLabel("Show Previous Subjects")
		self.label_showmore.setObjectName("greyText")

		self.layout.addWidget(self.label_showmore, 0, Qt.AlignCenter)
		self.layout.addWidget(self.down_arrow_widget, 0, Qt.AlignCenter)

		self.frame.setLayout(self.layout)
		self.main_layout.addWidget(self.frame)
		self.setLayout(self.main_layout)