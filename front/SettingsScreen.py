import sys
from PySide.QtCore import *
from PySide.QtGui import *

class SettingsScreen(QWidget):
	def switchSubFrame(self, next):
		self.active_subframe.hide()
		next.show()
		self.active_subframe = next

	def setInitialSubFrame(self, initial):
		self.active_subframe = initial
		initial.show()

	def __init__(self):
		QWidget.__init__(self)
		self.frame_user = UserFrame(self)
		self.frame_user.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
		self.frame_user.hide()

		self.frame_subject = SubjectFrame()
		self.frame_subject.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
		self.frame_subject.hide()


		self.layout = QHBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)

		self.nav_bar = NavigationBar(self)
		self.nav_bar.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
		self.nav_bar.addStretch()
		self.nav_bar.addItem("My Account", self.switchSubFrame, self.frame_user, selected=True)
		self.nav_bar.addStretch()
		self.nav_bar.addItem("Engineering", self.switchSubFrame,self.frame_subject)
		self.nav_bar.addItem("Linear Algebra",self.switchSubFrame, self.frame_user)
		self.nav_bar.addItem("Linguistics",self.switchSubFrame, self.frame_user)
		self.nav_bar.addItem("Physics",self.switchSubFrame, self.frame_user)
		self.nav_bar.addStretch()
		self.nav_bar.addStretch()
		self.nav_bar.addStretch()
		self.nav_bar.addStretch()
		self.nav_bar.setContentsMargins(0,0,0,0)

		self.setInitialSubFrame(self.frame_user)

		self.layout.addWidget(self.nav_bar)
		self.layout.addWidget(self.frame_subject)
		self.layout.addWidget(self.frame_user)
		self.setLayout(self.layout)
