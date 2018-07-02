from PySide.QtCore import *
from PySide.QtGui import *

from widgets.ConfirmSubjectWidget import confirmSubjectWidget 

from widgets.ShowMoreWidget import ShowMoreWidget 
from widgets.NextButton import NextButton

# class SubjectList

class SubjectTileSet(QWidget):
	def __init__(self, subject_widgets, num_subjects):
		QWidget.__init__(self)
		self.num_subjects = num_subjects
		self.max_subjects_per_row = 5
		self.num_rows = 1 + int(self.max_subjects_per_row/num_subjects)

		self.vert_layout = QVBoxLayout()
		self.row_layouts = []

		self.row = QHBoxLayout()

		for i in range(1, self.num_subjects+1):
			self.row.addWidget(subject_widgets[i-1])
			if i % self.max_subjects_per_row == 0:
				self.row_layouts.append(self.row)
				self.vert_layout.addLayout(self.row)
				self.row = QHBoxLayout()

		if self.num_subjects % self.max_subjects_per_row != 0:
			self.row_layouts.append(self.row)
			self.vert_layout.addLayout(self.row)

		self.setLayout(self.vert_layout)

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

		#	Row for past subjects still available on LMS

		self.past_subjects = []
		for i in range(1, 6):
			self.past_subjects.append(confirmSubjectWidget("Linguistics", str(i), "2017", "LING2005",assets.icon_subject_icon))
		self.past_subject_tile_set = SubjectTileSet(self.past_subjects, len(self.past_subjects))

		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		# self.layout.addLayout(self.current_subjects_row)
		# self.layout.addStretch()
		# self.layout.addStretch()
		# self.layout.addStretch()
		# self.layout.addStretch()
		# self.layout.addWidget(self.label_showmore, 0, Qt.AlignCenter)
		# self.layout.addWidget(self.button_showmore, 0, Qt.AlignCenter)
		self.layout.addWidget(self.past_subject_tile_set)
		self.layout.addStretch()
		self.layout.addStretch()

		self.layout.addStretch()
		
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)

	def show(self):
		super().show()
		self.parent().title_frame.hide()
