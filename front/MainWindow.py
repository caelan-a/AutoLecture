import os, sys
sys.path.append(os.path.dirname(__file__))
from PySide.QtCore import *
from PySide.QtGui import *

from screens.SetupScreen import SetupScreen
from screens.SettingsScreen import SettingsScreen
from screens.MenuScreen import MenuScreen

from Assets import Assets

BUTTON_STYLE_SHEET_PATH = "front/stylesheets/button.stylesheet"

class Window(QWidget):
	def switchScreen(self, next):
		self.active_screen.hide()
		next.show()
		self.active_screen = next

	def setInitialScreen(self,screen):
		self.active_screen = screen
		self.switchScreen(screen)

	def __init__(self, backend_app):
		QWidget.__init__(self)

		self.backend_app = backend_app
		
		# Setup Assets
		assets = Assets()

		sshFile=BUTTON_STYLE_SHEET_PATH
		with open(sshFile,"r") as fh: 
			self.styleSheet = fh.read()

		self.setStyleSheet(self.styleSheet)

		QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        
		self.setMinimumSize(QSize(1600,1000))
		self.setWindowIcon(QIcon('resources/icons/logo_taskbar.png'))  
		self.setWindowTitle(' ') 

		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		
		#	Screens 
		self.screen_setup = SetupScreen(assets)
		self.screen_settings = SettingsScreen(assets)
		self.screen_menu = MenuScreen(assets)
		self.layout.addWidget(self.screen_setup)
		self.layout.addWidget(self.screen_settings)
		self.layout.addWidget(self.screen_menu)
		self.screen_setup.hide()
		self.screen_settings.hide()
		self.screen_menu.hide()

		self.setLayout(self.layout)

	def run(self, qt_app):
        # Show the form
		self.show()
		# Run the qt application
		qt_app.exec_()
		
class ImageFileList(QListWidget):
	def __init__(self, dirpath, parent=None):
		QListWidget.__init__(self, parent)
