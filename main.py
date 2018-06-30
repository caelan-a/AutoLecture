import os, sys
sys.path.append(os.path.dirname(__file__))

from PySide.QtCore import *
from PySide.QtGui import *

from front.MainWindow import Window  
from back.app import AutoLectureApp 

# Setup backend
backend_app = AutoLectureApp()

# Setup frontend
qt_app = QApplication(sys.argv)
screen_resolution = qt_app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()

window = Window(backend_app, width, height) 

# Set initial screen
if(backend_app.isNewUser):
	window.setInitialScreen(window.screen_setup)
else:
	window.setInitialScreen(window.screen_setup)

print(backend_app.user.getCurrentTerm())

window.run(qt_app)

