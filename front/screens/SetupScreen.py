from PySide.QtCore import *
from PySide.QtGui import *

from frames.TitleFrame import TitleFrame
from frames.WelcomeFrame import WelcomeFrame
from frames.LoginFrame import LoginFrame
from frames.LoadingFrame import LoadingFrame
from frames.SubjectConfirmationFrame import SubjectConfirmationFrame

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

	def __init__(self, assets):
		QWidget.__init__(self)

		#	Frames
		self.title_frame = TitleFrame()
		self.login_frame = LoginFrame()
		self.welcome_frame = WelcomeFrame()
		self.loading_frame = LoadingFrame(assets.movie_loading_anim)
		self.subject_confirmation_frame = SubjectConfirmationFrame(self, assets)

		self.login_frame.hide()
		self.welcome_frame.hide()
		self.loading_frame.hide()
		self.subject_confirmation_frame.hide()

		self.active_subframe = self.welcome_frame
		self.switchSubFrame(self.subject_confirmation_frame)

		####

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.title_frame)			# Top frame

		self.layout.addWidget(self.login_frame)		# Bottom frame
		self.layout.addWidget(self.welcome_frame)
		self.layout.addWidget(self.loading_frame)
		self.layout.addWidget(self.subject_confirmation_frame)
		
		self.setLayout(self.layout)