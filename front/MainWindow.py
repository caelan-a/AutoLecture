import os, sys
sys.path.append(os.path.dirname(__file__))
from PySide.QtCore import *
from PySide.QtGui import *

from screens.SetupScreen import SetupScreen
from screens.SettingsScreen import SettingsScreen
from screens.MenuScreen import MenuScreen

from stylesheets.StyleSheets import setStyleSheet

from Assets import Assets

WIDTH_SCALE_FACTOR = 13/14
HEIGHT_SCALE_FACTOR = 3/4

class Window(QWidget):
	def switchScreen(self, next):
		self.active_screen.hide()
		next.show()
		self.active_screen = next

	def setInitialScreen(self,screen):
		self.active_screen = screen
		self.switchScreen(screen)

	def __init__(self, backend_app, width, height):
		QWidget.__init__(self)

		self.backend_app = backend_app

		# Setup Assets
		assets = Assets()

		setStyleSheet(self, "main")

		QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        

		self.setMinimumSize(QSize(WIDTH_SCALE_FACTOR*width,HEIGHT_SCALE_FACTOR*height))
		self.setMaximumSize(QSize(WIDTH_SCALE_FACTOR*width,HEIGHT_SCALE_FACTOR*height))
		self.setWindowIcon(QIcon('resources/icons/logo_taskbar.png'))  
		self.setWindowTitle(' ') 

		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		
		#	Screens 
		self.screen_setup = SetupScreen(backend_app, assets)
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
