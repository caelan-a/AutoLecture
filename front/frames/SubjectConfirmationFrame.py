from PySide.QtCore import *
from PySide.QtGui import *
from FadeWidget import FadeWidget

from stylesheets.StyleSheets import setStyleSheet
from widgets.NextButton import NextButton
from widgets.SubjectTileSet import SubjectTileSet
from widgets.ShowMoreWidget import ShowMoreWidget

from widgets.ConfirmSubjectWidget import ConfirmSubjectWidget

class HorizontalWidgetList(QWidget):
	def __init__(self, assets, widget_size):
		QWidget.__init__(self)
		self.assets = assets
		self.widget_size = widget_size

		self.layout = QHBoxLayout(self)
		self.setLayout(self.layout)

	def createWidgetFromInfo(self, info_subject):
		print(info_subject)
		icon = self.assets.icon_subject_icon #	implement method to get unique icon
		widget = ConfirmSubjectWidget(info_subject.get('title'), str(info_subject.get('semester')), str(info_subject.get('year')), icon, self.widget_size)
		return widget

	def addSubjectsFromInfo(self, subject_info_list):
		for index, subject in enumerate(subject_info_list):
			self.layout.addWidget(self.createWidgetFromInfo(subject_info_list[subject]))


class SubjectConfirmationFrame(QWidget):
	@Slot()
	def showPastSubjects(self):
		self.showMoreWidget.hide()
		self.past_subjects_tileset.show()

	def populateSubjectsFromInfo(self, subject_info_list):
		if "current" in subject_info_list.keys():
			self.current_subjects_tileset.addSubjectsFromInfo(subject_info_list["current"])

		if "past" in subject_info_list.keys():
			self.past_subjects_horizontal_list.addSubjectsFromInfo(subject_info_list["past"])
			self.scroll.setMinimumHeight(self.past_subjects_horizontal_list.sizeHint().height())
			self.scroll.setWidget(self.past_subjects_horizontal_list)
			self.scroll.show()

	def __init__(self, parent, assets):
		QWidget.__init__(self)
		self.setParent(parent)

		self.layout = QVBoxLayout()

		setStyleSheet(self, "subject_tile")

		# Initialise widget assets
		self.label_question = QLabel("Choose Subjects to Add")
		self.label_question.setObjectName("question")
		self.button_confirm = NextButton("Next")

		self.showMoreWidget = ShowMoreWidget(assets)
		self.showMoreWidget.frame.clicked.connect(self.showPastSubjects)

		#	Subject tilesets
		self.current_subjects_tileset = SubjectTileSet(5, assets, "big")
		# self.past_subjects_tileset = SubjectTileSet(15, assets, "big")


		#	Row for past subjects still available on LMS
		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		# self.layout.addStretch()
		self.layout.addWidget(self.current_subjects_tileset)
		# self.layout.addStretch()
		# self.layout.addWidget(self.showMoreWidget)
		self.layout.addStretch()
		
		self.past_subjects_horizontal_list = HorizontalWidgetList(assets, "small")

		self.scroll = QScrollArea()
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setFrameShape(QFrame.NoFrame)

		setStyleSheet(self.scroll, "subject_tile")

		# self.scroll.setWidgetResizable(True)
		self.layout.addWidget(self.scroll)

		self.layout.addStretch()
		
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)


	def showEvent(self, event):
		self.parent().title_frame.hide()
