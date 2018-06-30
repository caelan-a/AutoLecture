from PySide.QtCore import *
from PySide.QtGui import *

from widgets.ConfirmSubjectWidget import confirmSubjectWidget 

class SubjectConfirmationFrame(QWidget): 
	def __init__(self, parent, assets):
		QWidget.__init__(self)
		self.setParent(parent)

		# Initialise widget assets
		#confirmSubjectWidget.setIcons(assets.icon_tick_grey, assets.icon_tick_green)

		self.label_question = QLabel("Pick subjects you want to ")
		self.label_question.setObjectName("question")
		self.button_confirm = QPushButton("Next")
		#self.button_confirm.setObjectName("nextButton")

		self.layout = QVBoxLayout()
		self.row_layout = QHBoxLayout()
		self.row_layout.addWidget(confirmSubjectWidget("Linear Algebra", "2", "2017", "MAST10007",assets.icon_subject_icon), 0, Qt.AlignCenter)
		self.row_layout.addWidget(confirmSubjectWidget("Engineering Systems Design", "2", "2017", "ENGR10003",assets.icon_subject_icon), 0, Qt.AlignCenter)
		self.row_layout.addWidget(confirmSubjectWidget("Physics", "2", "2017", "PHYC10004",assets.icon_subject_icon), 0, Qt.AlignCenter)
		self.row_layout.addWidget(confirmSubjectWidget("Linguistics", "2", "2017", "LING2005",assets.icon_subject_icon), 0, Qt.AlignCenter)
		
		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addLayout(self.row_layout)
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)

	def show(self):
		super().show()
		self.parent().title_frame.hide()
