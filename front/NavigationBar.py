import sys
from PySide.QtCore import *
from PySide.QtGui import *

class NavigationBar(QWidget):
	@Slot()
	def goToMenu(self):
		self.parent().parent().switchScreen(self.parent().parent().screen_menu)

	@Slot()
	def onSelection(self, button, action, arg1):
		if button != self.selected_button:
			print("Set style")
			button.setProperty('selected', True)
			button.setStyle(button.style())
			self.selected_button.setProperty('selected', False)
			self.selected_button.setStyle(button.style())
			self.selected_button = button
			action(arg1)

	def addStretch(self):
		self.layout.addStretch()

	def addItem(self, text, action, arg1, selected = False):
		button = QPushButton(text)
		button.setObjectName('listButton')
		button.clicked.connect(lambda: self.onSelection(button, action, arg1))

		if selected:
			self.selected_button = button
			button.setProperty('selected', True)
			button.setStyle(button.style())

		self.layout.addWidget(button)


	def __init__(self):
		QWidget.__init__(self)
		self.layout = QVBoxLayout()

		self.hbox_top = QHBoxLayout()

		self.button_back = QPushButton()
		self.button_back.setObjectName('backButton')
		self.pixmap_back = QPixmap("images/icon_backbutton.png")
		self.icon_back = QIcon(self.pixmap_back)
		self.button_back.setIcon(self.icon_back)
		self.button_back.setIconSize(QSize(80,80));
		self.button_back.clicked.connect(self.goToMenu)
	

		self.label_title = QLabel("Settings")
		self.label_title.setObjectName('settingsTitle')
		self.hbox_top.addWidget(self.button_back)
		self.hbox_top.addWidget(self.label_title)
		self.selected_button = self.button_back

		self.layout.addLayout(self.hbox_top)
		self.setAutoFillBackground(True)
		self.setPalette(QColor('#2F9599'))
		self.setLayout(self.layout)
