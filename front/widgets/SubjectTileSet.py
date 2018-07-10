from PySide.QtCore import *
from PySide.QtGui import *

from widgets.ConfirmSubjectWidget import ConfirmSubjectWidget

# class SubjectList
class SubjectTileSet(QWidget):
	def getSelectedSubjectKeys(self):
		keys = []
		for widget in self.findChildren(ConfirmSubjectWidget):
			if widget.isSelected():
				keys.append(widget.getKey())
		return keys

	def createWidgetFromInfo(self, info_subject):
		icon = self.assets.icon_subject_icon #	implement method to get unique icon
		widget = ConfirmSubjectWidget(info_subject.get('title'), str(info_subject.get('semester')), str(info_subject.get('year')), str(info_subject.get('code')),icon, self.widget_size)
		return widget

	#	List of SubjectTile objects
	def addSubjectTiles(self, subjects_list):
		self.num_subjects = len(subjects_list)
		for index, subject in enumerate(subjects_list):
			subject_count = index + 1
			# index+=1
			self.row.addWidget(subject)

			if subject_count % self.max_subjects_per_row == 0: 
				self.row_layouts.append(self.row)
				self.vert_layout.addLayout(self.row)
				self.row = QHBoxLayout()

		if self.num_subjects % self.max_subjects_per_row != 0:
			self.row_layouts.append(self.row)
			self.vert_layout.addLayout(self.row)

	#	Add subjects from info given by LmsNavigator.getLmsSubjectInfo
	def addSubjectsFromInfo(self, info_subjects):
		self.num_subjects = len(info_subjects)
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
			print("no subjects")
			self.label_no_subjects_available = QLabel("Subjects for this semester are yet to be released")
			self.label_no_subjects_available.setObjectName("noSubjectsText")
			self.row.addWidget(self.label_no_subjects_available, 0, Qt.AlignCenter)
			self.vert_layout.addLayout(self.row)

	def __init__(self, max_subjects_per_row, assets, widget_size):
		QWidget.__init__(self)
		self.max_subjects_per_row = max_subjects_per_row
		self.assets	= assets
		self.widget_size = widget_size

		self.vert_layout = QVBoxLayout()
		self.row_layouts = []
		self.row = QHBoxLayout()

		self.setLayout(self.vert_layout)
