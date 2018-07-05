from PySide.QtCore import *
from PySide.QtGui import *
from FadeWidget import FadeWidget
from workthreads.GetSubjectInfoThread import GetSubjectInfoThread

FORM_WIDTH = 800

class LoginFrame(QWidget):
	def goToSubjectConfirmation(self):
		print("Going to next frame")
		self.subject_confirmation_frame.populateSubjectsFromInfo(self.backend_app.user.raw_subject_info)
		self.parent().switchSubFrame(self.subject_confirmation_frame)

	@Slot()
	def getLoginInfo(self):
		#	Send login info to backend 
		self.parent().parent().backend_app.setLoginInfo(self.lineedit_login.text(),self.lineedit_password.text())
		self.startGetSubjectInfoThread()
		self.get_subject_info_thread.finished.connect(self.goToSubjectConfirmation, Qt.QueuedConnection)
		self.parent().switchSubFrame(self.loading_frame)

	def startGetSubjectInfoThread(self):
		if not self.get_subject_info_thread.isRunning():
			self.get_subject_info_thread.exiting=False
			self.get_subject_info_thread.start()
	
	def __init__(self, backend_app, loading_frame, subject_confirmation_frame):
		QWidget.__init__(self)
		self.backend_app = backend_app

		self.loading_frame = loading_frame
		self.subject_confirmation_frame = subject_confirmation_frame

		#	Setup get lms subject info thread
		self.get_subject_info_thread = GetSubjectInfoThread(self, backend_app, loading_frame.setLoadingText, subject_confirmation_frame)

		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignHCenter)

		self.vbox_input = QVBoxLayout()

		#	Login form
		self.lineedit_login = QLineEdit()
		self.lineedit_login.setFixedWidth(FORM_WIDTH)
		self.lineedit_login.setPlaceholderText("Username")
		self.lineedit_login.setText("caelana")

		#	Password form
		self.lineedit_password = QLineEdit()
		self.lineedit_password.setFixedWidth(FORM_WIDTH)
		self.lineedit_password.setPlaceholderText("Password")
		self.lineedit_password.setText("cael1998")


		#	Lay widgets out in Login/Password sub layout
		self.vbox_input.addWidget(self.lineedit_login)
		self.vbox_input.addWidget(self.lineedit_password)

		#	Login button
		self.pushbutton_login = QPushButton("Login")
		self.pushbutton_login.clicked.connect(self.getLoginInfo)

		#	Lay widgets out
		self.layout.addLayout(self.vbox_input)
		self.layout.addStretch()
		self.layout.addWidget(self.pushbutton_login, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)