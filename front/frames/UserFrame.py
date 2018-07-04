from PySide.QtCore import *
from PySide.QtGui import *
from FadeWidget import FadeWidget

BUTTON_STYLE_SHEET_PATH = "front/stylesheets/button.stylesheet"

from widgets.InputFieldWidget import InputField


class UserFrame(QWidget):
	def __init__(self, parent):
		super(UserFrame,self).__init__(parent)

		#	Confirmation box for reset
		self.buttonBox = QMessageBox()
		self.buttonBox.addButton(QPushButton("Yes",self),QMessageBox.AcceptRole)
		self.buttonBox.setText("	Are you sure?")
		self.buttonBox.setWindowTitle(' ')
		self.buttonBox.setWindowIcon(QIcon('resources/icons/logo_taskbar.png'))  
		self.buttonBox.setIcon(QMessageBox.NoIcon)

		sshFile=BUTTON_STYLE_SHEET_PATH
		with open(sshFile,"r") as fh:
			self.styleSheet = fh.read()
		self.buttonBox.setStyleSheet(self.styleSheet)
		
		self.layout = QVBoxLayout()
		self.input_username = InputField("Username", "caelana")
		self.input_password = InputField("Password", "cael1998")
		self.input_downloadpath = InputField("Download Path", "C:/Users/caelan/Videos")
		self.button_reset = QPushButton("Reset Account")
		self.button_reset.setObjectName("criticalButton")
		self.button_reset.clicked.connect(self.buttonBox.exec_)


		#self.buttonBox.accepted.connect(self.accept)
		#self.buttonBox.rejected.connect(self.reject)

		self.button_save = QPushButton("Save")


		self.layout.addStretch()
		self.layout.addWidget(self.input_username)
		self.layout.addWidget(self.input_password)
		self.layout.addStretch()
		self.layout.addWidget(self.input_downloadpath)
		self.layout.addStretch()
		self.layout.addWidget(self.button_reset,0,Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addWidget(self.button_save)

		self.setLayout(self.layout)