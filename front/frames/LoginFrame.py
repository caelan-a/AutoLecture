from PySide.QtCore import *
from PySide.QtGui import *

class LoginFrame(QWidget):
	@Slot()
	def getLoginInfo(self):
	    print("Username: {}\nPassword: {}".format(self.lineedit_login.text(),self.lineedit_password.text()))
	    self.parent().switchSubFrame(self.parent().loading_frame)
	
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		self.setLayout(self.layout)
		self.layout.setAlignment(Qt.AlignHCenter)

		form_width = 800
		self.vbox_input = QVBoxLayout()
		self.lineedit_login = QLineEdit()
		self.lineedit_password = QLineEdit()
		self.lineedit_login.setPlaceholderText("Username")
		self.lineedit_password.setPlaceholderText("Password")
		self.lineedit_login.setFixedWidth(form_width)
		self.lineedit_password.setFixedWidth(form_width)

		self.vbox_input.addWidget(self.lineedit_login)
		self.vbox_input.addWidget(self.lineedit_password)

		self.pushbutton_login = QPushButton("Login")
		self.pushbutton_login.clicked.connect(self.getLoginInfo)

		self.layout.addLayout(self.vbox_input)
		self.layout.addStretch()
		self.layout.addWidget(self.pushbutton_login, 0, Qt.AlignCenter)