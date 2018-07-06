from PySide.QtCore import *
from PySide.QtGui import *

from workthreads.GetSubjectInfoThread import GetSubjectInfoThread
from widgets.NextButton import NextButton

class SubjectScheduleFrame(QWidget):
	def scheduleSubjects(self, info_subjects_selected):
		print("hello")

	def __init__(self, backend_app, loading_frame):
		QWidget.__init__(self)
		self.backend_app = backend_app
		self.loading_frame = loading_frame
		
		self.label  = QLabel("Next")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.label)
		self.setLayout(self.layout)