from PySide.QtCore import *
from PySide.QtGui import *
from FadeWidget import FadeWidget
from widgets.ConfirmSubjectWidget import confirmSubjectWidget 

from widgets.ShowMoreWidget import ShowMoreWidget 
from widgets.NextButton import NextButton

# class SubjectList
class SubjectTileSet(QWidget):
	def createWidgetFromInfo(self, info_subject):
		icon = self.assets.icon_subject_icon #	implement method to get unique icon
		widget = confirmSubjectWidget(info_subject.get('title'), str(info_subject.get('semester')), str(info_subject.get('year')), icon, self.widget_size)
		return widget

	def addSubjectsFromInfo(self, info_subjects):
		self.num_subjects = len(info_subjects)
		print(info_subjects)
		if self.num_subjects != 0:
			for index, subject in enumerate(info_subjects):
				subject_count = index + 1
				self.row.addWidget(self.createWidgetFromInfo(info_subjects[subject]))

				if subject_count % self.max_subjects_per_row == 0: 
					self.row_layouts.append(self.row)
					self.vert_layout.addLayout(self.row)
					self.row = QHBoxLayout()

			if self.num_subjects % self.max_subjects_per_row != 0:
				self.row_layouts.append(self.row)
				self.vert_layout.addLayout(self.row)
		else:
			label_no_subjects_available = QLabel("Subjects for this semester are yet to be released")
			label_no_subjects_available.setObjectName("greyText")
			self.row.addWidget(label_no_subjects_available)

	def __init__(self, max_subjects_per_row, assets, widget_size):
		QWidget.__init__(self)
		self.max_subjects_per_row = max_subjects_per_row
		self.assets	= assets
		self.widget_size = widget_size

		self.vert_layout = QVBoxLayout()
		self.row_layouts = []
		self.row = QHBoxLayout()

		self.setLayout(self.vert_layout)

class SubjectConfirmationFrame(QWidget):
	def resizeEvent(self, event):
		self.button_showmore.stopFloatAnimation()
		self.button_showmore.startFloatAnimation()

	def showEvent(self, event):
		self.button_showmore.startFloatAnimation()

	def populateSubjectsFromInfo(self, subject_info_list):
		if "current" in subject_info_list.keys():
			self.current_subjects_tileset.addSubjectsFromInfo(subject_info_list["current"])

		if "past" in subject_info_list.keys():
			self.past_subjects_tileset.addSubjectsFromInfo(subject_info_list["past"])

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

		#	Subject tilesets
		self.current_subjects_tileset = SubjectTileSet(6, assets, "big")
		self.past_subjects_tileset = SubjectTileSet(6, assets, "small")

		#	Row for past subjects still available on LMS
		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.current_subjects_tileset)
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.past_subjects_tileset)
		
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)


	def showEvent(self, event):
		self.parent().title_frame.hide()
