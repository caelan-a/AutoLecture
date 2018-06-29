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
window = Window(backend_app) 

# Set initial screen
if(backend_app.isNewUser):
	window.setInitialScreen(window.screen_setup)
else:
	window.setInitialScreen(window.screen_setup)

print(backend_app.user.getCurrentTerm())

window.run(qt_app)

