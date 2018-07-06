from PySide.QtCore import *
from PySide.QtGui import *

from workthreads.GetOnlineSubjectScheduleInfoThread import GetOnlineSubjectScheduleInfo
from widgets.NextButton import NextButton

class SubjectScheduleFrame(QWidget):
	#	Store subjects to add in backend, then retrieve schedule info from online
	def scheduleSubjects(self, info_subjects_selected):
		self.parent().switchSubFrame(self.loading_frame)
		self.backend_app.fillSubjectsToAdd(info_subjects_selected)
		self.startOnlineSubjectScheduleInfoThread()
		self.get_schedule_info_thread.finished.connect(self.showSelf, Qt.QueuedConnection)

	@Slot()
	def showSelf(self):
		self.parent().switchSubFrame(self)	#	Come back to this frame when info after retrieved
		print("back")

	def startOnlineSubjectScheduleInfoThread(self):
		if not self.get_schedule_info_thread.isRunning():
			self.get_schedule_info_thread.exiting=False
			self.get_schedule_info_thread.start()
	
	def __init__(self, backend_app, loading_frame):
		QWidget.__init__(self)
		self.backend_app = backend_app
		self.loading_frame = loading_frame
		
		#	Initialise thread
		self.get_schedule_info_thread = GetOnlineSubjectScheduleInfo(self, backend_app, self.loading_frame.setLoadingText)

		#	Layouts
		self.layout = QVBoxLayout()

		# Initialise widget assets
		self.label_question = QLabel("Make a Schedule")
		self.label_question.setObjectName("question")
		self.button_confirm = NextButton("Next")
		# self.button_confirm.clicked.connect(self.scheduleSelectedSubjects)

		#	Widget Layout 
		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)	

		self.setLayout(self.layout)