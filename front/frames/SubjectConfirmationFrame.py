from PySide.QtCore import *
from PySide.QtGui import *
from FadeWidget import FadeWidget

from stylesheets.StyleSheets import setStyleSheet
from widgets.NextButton import NextButton
from widgets.SubjectTileSet import SubjectTileSet
from widgets.ShowMoreWidget import ShowMoreWidget

class SubjectConfirmationFrame(QWidget):
	@Slot()
	def showPastSubjects(self):
		self.showMoreWidget.hide()
		self.past_subjects_tileset.show()

	# def resizeEvent(self, event):
	# 	self.button_showmore.stopFloatAnimation()
	# 	self.button_showmore.startFloatAnimation()


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

		self.showMoreWidget = ShowMoreWidget(assets)
		self.showMoreWidget.frame.clicked.connect(self.showPastSubjects)

		#	Subject tilesets
		self.current_subjects_tileset = SubjectTileSet(6, assets, "big")
		self.past_subjects_tileset = SubjectTileSet(6, assets, "small")

		self.past_subjects_tileset.hide()

		#	Row for past subjects still available on LMS
		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.current_subjects_tileset)
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.showMoreWidget)
		self.layout.addStretch()
		self.layout.addWidget(self.past_subjects_tileset)
		self.layout.addStretch()
		
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)


	def showEvent(self, event):
		self.parent().title_frame.hide()
