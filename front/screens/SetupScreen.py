from PySide.QtCore import *
from PySide.QtGui import *

from frames.TitleFrame import TitleFrame
from frames.WelcomeFrame import WelcomeFrame
from frames.LoginFrame import LoginFrame
from frames.LoadingFrame import LoadingFrame
from frames.SubjectConfirmationFrame import SubjectConfirmationFrame
from frames.SubjectScheduleFrame import SubjectScheduleFrame


class SetupScreen(QWidget):
	def switchSubFrame(self, next):
		self.active_subframe.hide()
		next.show()
		self.active_subframe = next

	def toggleTitle(self):
		if self.title_frame.isHidden():
			self.title_frame.hide()
		else:
			self.title_frame.show()

	def getLoadingFrame(self):
		return self.loading_frame

	def __init__(self,backend_app, assets):
		QWidget.__init__(self)

		#	Frames

		self.title_frame = TitleFrame()
		self.loading_frame = LoadingFrame(assets.movie_loading_anim, self.title_frame)	#	Needs to be at top to pass to frames that use it
		self.subject_schedule_frame = SubjectScheduleFrame(backend_app, self.loading_frame)
		self.subject_confirmation_frame = SubjectConfirmationFrame(self, assets, self.subject_schedule_frame)
		self.login_frame = LoginFrame(backend_app, self.loading_frame, self.subject_confirmation_frame)
		self.welcome_frame = WelcomeFrame()

		self.login_frame.hide()
		self.welcome_frame.hide()
		self.loading_frame.hide()
		self.subject_confirmation_frame.hide()
		self.subject_schedule_frame.hide()

		self.active_subframe = self.welcome_frame
		self.switchSubFrame(self.welcome_frame)

		####
  
		self.layout = QVBoxLayout()

		self.layout.addWidget(self.title_frame)			# Top frame
		self.layout.addWidget(self.login_frame)		# Bottom frame
		self.layout.addWidget(self.subject_confirmation_frame)
		self.layout.addWidget(self.subject_schedule_frame)
		self.layout.addWidget(self.welcome_frame)
		self.layout.addWidget(self.loading_frame)

		self.setLayout(self.layout)