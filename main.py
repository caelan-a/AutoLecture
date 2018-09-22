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
	window.setInitialScreen(window.screen_menu)
else:
	backend_app.loadUser()
	window.setInitialScreen(window.screen_setup)

window.run(qt_app)

"""

1. Make front screen 2d QScrollArea with all the subject tiles, timetable on main screen, with lectures to watch, assignments to d0, numbers based on colour
2. For documents, have user triggered search that collects all documents, use load frame for elegant load screen in frame.
3. For each subject, 4 tabs -> Lectures, Documents, Assignments
4. Make Documents, Assignments and timetable $3 unlockable
5. Elegant looking website, same style as program, describes key features, and has download
6. Ship with updater
7. Gamify AutoLecture with points and incentives to keep up to date with lectures and even name lectures
8. Mobile app
9. Notes related to each lecture
10. test


"""