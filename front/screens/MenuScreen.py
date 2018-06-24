from PySide.QtCore import *
from PySide.QtGui import *

class MenuScreen(QWidget):
	@Slot()
	def goToSettings(self):
		self.parent().switchScreen(self.parent().screen_settings)

	def __init__(self, assets):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()
		self.hbox = QHBoxLayout()

		self.layout.addStretch()
		self.label_title = QLabel("AutoLecture")
		self.label_title.setObjectName("setupScreenTitle")
		self.label_title.setAlignment(Qt.AlignCenter)
		self.layout.addWidget(self.label_title)

		self.button_lectures = QPushButton("")
		self.button_lectures.setObjectName('menuIcon')
		self.button_lectures.setIcon(assets.icon_play_white)
		self.button_lectures.setIconSize(QSize(150,150));
		self.hbox.addWidget(self.button_lectures)

		self.button_settings = QPushButton("")
		self.button_settings.setObjectName('menuIcon')
		self.button_settings.setIcon(assets.icon_settings_white)
		self.button_settings.setIconSize(QSize(150,150));
		self.button_settings.clicked.connect(self.goToSettings)
		self.hbox.addWidget(self.button_settings)

		self.layout.addStretch()
		self.layout.addLayout(self.hbox)
		self.layout.addStretch()
		self.setLayout(self.layout)