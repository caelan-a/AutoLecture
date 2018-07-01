from PySide.QtCore import *
from PySide.QtGui import *

from widgets.ConfirmSubjectWidget import confirmSubjectWidget 

from widgets.ShowMoreWidget import ShowMoreWidget 
from widgets.NextButton import NextButton

# class SubjectList

class SubjectConfirmationFrame(QWidget):
	def resizeEvent(self, event):
		self.button_showmore.stopFloatAnimation()
		self.button_showmore.startFloatAnimation()

	def showEvent(self, event):
		print("show widget")
		self.button_showmore.startFloatAnimation()

	def __init__(self, parent, assets):
		QWidget.__init__(self)
		self.setParent(parent)

		self.layout = QVBoxLayout()

		# Initialise widget assets
		self.label_question = QLabel("Choose Subjects")
		self.label_question.setObjectName("question")
		
		self.button_confirm = NextButton("Next")

		self.button_showmore = ShowMoreWidget(self, "showMore", assets.icon_down_icon)
	
		self.label_showmore = QLabel("Show Previous Subjects")
		self.label_showmore.setObjectName("greyText")

		#	Row for current subjects
		self.current_subjects_row = QHBoxLayout()
		self.current_subjects_row.addWidget(confirmSubjectWidget("Linear Algebra", "2", "2017", "MAST10007",assets.icon_subject_icon))
		self.current_subjects_row.addWidget(confirmSubjectWidget("Engineering Systems Design", "2", "2017", "ENGR10003",assets.icon_subject_icon))
		self.current_subjects_row.addWidget(confirmSubjectWidget("Physics", "2", "2017", "PHYC10004",assets.icon_subject_icon))
		self.current_subjects_row.addWidget(confirmSubjectWidget("Linguistics", "2", "2017", "LING2005",assets.icon_subject_icon))
		# self.current_subjects_row.addWidget(confirmSubjectWidget("Linguistics", "2", "2017", "LING2005",assets.icon_subject_icon))

		#	Row for past subjects still available on LMS
		self.past_subjects_row = QHBoxLayout()
		# self.


		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addLayout(self.current_subjects_row)
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.label_showmore, 0, Qt.AlignCenter)
		self.layout.addWidget(self.button_showmore, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addStretch()

		self.layout.addStretch()
		
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)

	def show(self):
		super().show()
		self.parent().title_frame.hide()
