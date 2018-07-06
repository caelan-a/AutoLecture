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

	def getSelectedSubjectKeys(self):
		keys = []
		for widget in self.findChildren(ConfirmSubjectWidget):
			if widget.isSelected():
				keys.append(widget.getKey())
		return keys

	def createWidgetFromInfo(self, info_subject):
		icon = self.assets.icon_subject_icon #	implement method to get unique icon
		widget = ConfirmSubjectWidget(info_subject.get('title'), str(info_subject.get('semester')), str(info_subject.get('year')), str(info_subject.get('code')), icon, self.widget_size)
		return widget

	def addSubjectsFromInfo(self, subject_info_list):
		for index, subject in enumerate(subject_info_list):
			self.layout.addWidget(self.createWidgetFromInfo(subject_info_list[subject]))


class SubjectConfirmationFrame(QWidget):
	def getSelectedSubjectKeys(self):
		#	Get keys of selected subjects
		selected_current_subject_keys = self.current_subjects_tileset.getSelectedSubjectKeys()
		selected_past_subject_keys = self.past_subjects_horizontal_list.getSelectedSubjectKeys()

		#	Remove non selected current subjects from info list
		current_subject_keys = list(self.subject_info_list["current"]) 
		for key in current_subject_keys:
			if key not in selected_current_subject_keys:
				del self.subject_info_list["current"][key]

		#	Remove non selected current subjects from info list
		past_subject_keys = list(self.subject_info_list["past"]) 
		for key in past_subject_keys:
			if key not in selected_past_subject_keys:
				del self.subject_info_list["past"][key]

		return self.subject_info_list
		

	@Slot()
	def scheduleSelectedSubjects(self):
		info_subjects_selected = self.getSelectedSubjectKeys()
		self.subject_schedule_frame.scheduleSubjects(info_subjects_selected)
		self.parent().switchSubFrame(self.subject_schedule_frame)

	@Slot()
	def showPastSubjects(self):
		self.showMoreWidget.hide()
		self.past_subjects_tileset.show()

	def populateSubjectsFromInfo(self, subject_info_list):
		self.subject_info_list = subject_info_list

		#	Populate current subjects tileset
		if "current" in subject_info_list.keys():
			self.current_subjects_tileset.addSubjectsFromInfo(subject_info_list["current"])

		#	Populate scrollable past subjects tileset
		if "past" in subject_info_list.keys():
			self.past_subjects_horizontal_list.addSubjectsFromInfo(subject_info_list["past"])
			self.scroll.setMinimumHeight(self.past_subjects_horizontal_list.sizeHint().height())
			self.scroll.setWidget(self.past_subjects_horizontal_list)
			self.scroll.show()

	def __init__(self, parent, assets, subject_schedule_frame):
		QWidget.__init__(self)
		self.setParent(parent)
		self.subject_schedule_frame = subject_schedule_frame

		self.layout = QVBoxLayout()

		setStyleSheet(self, "subject_tile")

		# Initialise widget assets
		self.label_question = QLabel("Choose Subjects to Add")
		self.label_question.setObjectName("question")
		self.button_confirm = NextButton("Next")
		self.button_confirm.clicked.connect(self.scheduleSelectedSubjects)

		self.showMoreWidget = ShowMoreWidget(assets)
		self.showMoreWidget.frame.clicked.connect(self.showPastSubjects)

		#	Subject tilesets
		self.current_subjects_tileset = SubjectTileSet(5, assets, "big")
		self.past_subjects_horizontal_list = HorizontalWidgetList(assets, "small")

		#	Horizontal scroll area for past subjects
		self.scroll = QScrollArea()
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setFrameShape(QFrame.NoFrame)

		#	Widget Layout 
		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addWidget(self.current_subjects_tileset)
		self.layout.addStretch()
		self.layout.addWidget(self.scroll)
		self.layout.addStretch()
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)	
		
		self.setLayout(self.layout)


	def showEvent(self, event):
		self.parent().title_frame.hide()
