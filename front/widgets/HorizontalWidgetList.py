from PySide.QtCore import *
from PySide.QtGui import *

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
